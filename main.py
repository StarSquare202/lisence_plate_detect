import os
import sys
import logging
from logging import handlers
from PySide6.QtCore import Qt, QThread, Signal, Slot
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog, QFrame
from PySide6.QtGui import QFontDatabase, QFont
from ui.mainWindow import Ui_MainWindow
from ui.loadingWindow import Ui_Loading
from extractor import Extractor

# 절대경로 명시
basedir = os.path.abspath(os.path.dirname(__file__))

# OCR 초기화
extractor = Extractor()

class MainWindow(QMainWindow):
    def __init__(self, file_logger):
        super().__init__()
        self.file_logger = file_logger
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self)

        # 폰트 설정
        fontDB = QFontDatabase()
        fontDB.addApplicationFont(os.path.join(basedir, "ui", "NanumSquareR.ttf"))
        app.setFont(QFont("NanumSquare"))

        self.ui_main.image_add_btn.clicked.connect(self.add_images)
        self.ui_main.image_delete_btn.clicked.connect(self.delete_selected_images)
        self.ui_main.image_reset_btn.clicked.connect(self.delete_all_images)
        self.ui_main.run_ocr_btn.clicked.connect(self.run_ocr)

        self.extract_worker = ExtractWorker()
        self.extract_worker.complete_signal.connect(self.result_complete)

        self.loading = LoadingWindow()
        self.loading.setParent(self)
        self.loading.hide()

        dlg_rect = self.loading.frameGeometry()
        dlg_rect.moveCenter(self.frameGeometry().center())

    def add_images(self):
        """
        이미지 추가 버튼 클릭 이벤트
        """
        images = QFileDialog.getOpenFileNames(self,'이미지 추가','추출 대상 이미지를 선택해주세요',filter='All Files(*);; Images(*.jpg *.jpeg *.png)')
        if len(images[0]) > 0:
            for image in [x for x in images[0] if str(x).lower().endswith(('.jpg','.jpeg','.png'))]:
                self.ui_main.image_list.addItem(image)
        else:
            pass

    def delete_selected_images(self):
        """
        이미지 삭제 버튼 클릭 이벤트
        """
        selected_items = self.ui_main.image_list.selectedItems()
        if len(selected_items) <= 0:
            self.show_message_box(icon=QMessageBox.Icon.Warning, title='경고', text='선택 된 이미지가 없습니다.')
        else:
            if self.show_confirm_box(icon=QMessageBox.Icon.Warning, title='경고', text='선택 된 이미지를 삭제 하시겠습니까?'):
                for item in selected_items:
                    self.ui_main.image_list.takeItem(self.ui_main.image_list.row(item))
            else:
                pass

    def delete_all_images(self):
        """
        초기화 버튼 클릭 이벤트
        """
        if self.ui_main.image_list.count() <= 0:
            self.show_message_box(icon=QMessageBox.Icon.Warning, title='경고', text='이미지가 없습니다.')
        else:
            if self.show_confirm_box(icon=QMessageBox.Icon.Warning, title='경고', text='모든 이미지들을 삭제 하시겠습니까?'):
                for i in range(self.ui_main.image_list.count()):
                    self.ui_main.image_list.clear()
            else:
                pass

    def run_ocr(self):
        """
        텍스트 추출 버튼 클릭 이벤트
        """
        try:
            if self.ui_main.image_list.count() > 0:
                self.loading.show()
                QApplication.processEvents() # GUI 프리징 현상 해소
                self.extract_worker.run(self.ui_main.image_list.get_items())
            else:
                self.show_message_box(icon=QMessageBox.Icon.Warning, title='경고', text='추출 대상 이미지가 없습니다.')
        except Exception as ex:
            file_logger.error(ex)

    @Slot(name='complete')
    def result_complete(self):
        """
        파일 생성 완료 슬롯 이벤트
        """
        self.show_message_box(icon=QMessageBox.Icon.Warning, title='알림', text='추출 결과가 생성되었습니다.')
        self.loading.hide()

    def show_message_box(self, icon:QMessageBox.Icon, title:str, text:str):
        msgBox = QMessageBox()
        msgBox.setIcon(icon)
        msgBox.setWindowTitle(title)
        msgBox.setText(text)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        msgBox.exec()

    def show_confirm_box(self, icon:QMessageBox.Icon, title:str, text:str):
        msgBox = QMessageBox()
        msgBox.setIcon(icon)
        msgBox.setWindowTitle(title)
        msgBox.setText(text)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        result = msgBox.exec()
        if result == QMessageBox.StandardButton.Ok:
            return True
        else:
            return False

class LoadingWindow(QFrame):
     def __init__(self):
        super().__init__()
        self.ui_loading = Ui_Loading()
        self.ui_loading.setupUi(self)

class ExtractWorker(QThread):

    complete_signal = Signal(name="complete")

    def run(self, images):
        extractor.extract_text(images)
        self.complete_signal.emit()
     
    def stop(self):
        self.quit()

if __name__ == "__main__":

    log_path = os.path.abspath(
        os.path.join(basedir, os.pardir, "log")
    )
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    # for debug
    file_logger = logging.getLogger("license_plate_detect")
    file_logger.setLevel(logging.INFO)

    file_handler = handlers.RotatingFileHandler(
        os.path.join(
            log_path,
            "detector.log",
        ),
        maxBytes=(1024 * 1024 * 2),
        backupCount=5,
    )
    formatter = logging.Formatter(
        "%(asctime)s %(name)s %(levelname)s [%(module)s.%(funcName)s] : %(message)s"
    )
    file_handler.setFormatter(formatter)
    file_logger.addHandler(file_handler)

    app = QApplication(sys.argv)
    main_window = MainWindow(file_logger)
    main_window.show()
    sys.exit(app.exec())