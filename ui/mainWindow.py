# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
from ui.customListWidget import CustomListWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(522, 472)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(500, 20))
        font = QFont()
        font.setFamilies([u"\ub098\ub214\uc2a4\ud018\uc5b4 Bold"])
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(170, 0, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.image_list = CustomListWidget(self.horizontalLayout)
        self.image_list.setObjectName(u"image_list")
        self.image_list.setMinimumSize(QSize(500, 350))
        font1 = QFont()
        font1.setFamilies([u"\ub098\ub214\uc2a4\ud018\uc5b4"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.image_list.setFont(font1)
        self.image_list.setStyleSheet(u"border: 1px solid rgb(170, 0, 255);")
        self.image_list.setFrameShape(QFrame.StyledPanel)
        self.image_list.setDragDropOverwriteMode(True)
        self.image_list.setDragDropMode(QAbstractItemView.DropOnly)
        self.image_list.setSelectionMode(QAbstractItemView.SingleSelection)

        self.verticalLayout_2.addWidget(self.image_list)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.image_add_btn = QPushButton(self.centralwidget)
        self.image_add_btn.setObjectName(u"image_add_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.image_add_btn.sizePolicy().hasHeightForWidth())
        self.image_add_btn.setSizePolicy(sizePolicy1)
        self.image_add_btn.setMinimumSize(QSize(30, 30))
        self.image_add_btn.setFont(font)
        self.image_add_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color:  rgb(170, 0, 255);\n"
"border: 1px solid rgb(170, 0, 255);\n"
"border-radius: 5px;\n"
"padding 5px;\n"
"")

        self.horizontalLayout_3.addWidget(self.image_add_btn)

        self.image_delete_btn = QPushButton(self.centralwidget)
        self.image_delete_btn.setObjectName(u"image_delete_btn")
        sizePolicy1.setHeightForWidth(self.image_delete_btn.sizePolicy().hasHeightForWidth())
        self.image_delete_btn.setSizePolicy(sizePolicy1)
        self.image_delete_btn.setMinimumSize(QSize(30, 30))
        self.image_delete_btn.setFont(font)
        self.image_delete_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color:  rgb(170, 0, 255);\n"
"border: 1px solid rgb(170, 0, 255);\n"
"border-radius: 5px;\n"
"padding 5px;\n"
"")

        self.horizontalLayout_3.addWidget(self.image_delete_btn)

        self.image_reset_btn = QPushButton(self.centralwidget)
        self.image_reset_btn.setObjectName(u"image_reset_btn")
        sizePolicy1.setHeightForWidth(self.image_reset_btn.sizePolicy().hasHeightForWidth())
        self.image_reset_btn.setSizePolicy(sizePolicy1)
        self.image_reset_btn.setMinimumSize(QSize(30, 30))
        self.image_reset_btn.setFont(font)
        self.image_reset_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color:  rgb(170, 0, 255);\n"
"border: 1px solid rgb(170, 0, 255);\n"
"border-radius: 5px;\n"
"padding 5px;\n"
"")

        self.horizontalLayout_3.addWidget(self.image_reset_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.run_ocr_btn = QPushButton(self.centralwidget)
        self.run_ocr_btn.setObjectName(u"run_ocr_btn")
        sizePolicy1.setHeightForWidth(self.run_ocr_btn.sizePolicy().hasHeightForWidth())
        self.run_ocr_btn.setSizePolicy(sizePolicy1)
        self.run_ocr_btn.setMinimumSize(QSize(500, 30))
        self.run_ocr_btn.setFont(font)
        self.run_ocr_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color:  rgb(170, 0, 255);\n"
"border: 1px solid rgb(170, 0, 255);\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"")

        self.verticalLayout_2.addWidget(self.run_ocr_btn)

        self.verticalLayout_2.setStretch(1, 6)

        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"OCR(\ud14d\uc2a4\ud2b8\uc778\uc2dd)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\ucd94\ucd9c \ub300\uc0c1 \uc774\ubbf8\uc9c0", None))
        self.image_add_btn.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 \ucd94\uac00", None))
        self.image_delete_btn.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 \uc0ad\uc81c", None))
        self.image_reset_btn.setText(QCoreApplication.translate("MainWindow", u"\ucd08\uae30\ud654", None))
        self.run_ocr_btn.setText(QCoreApplication.translate("MainWindow", u"\ud14d\uc2a4\ud2b8 \ucd94\ucd9c", None))
    # retranslateUi

