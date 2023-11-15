import logging
from paddleocr import PaddleOCR
from result import Result
from datetime import datetime

file_logger = logging.getLogger("license_plate_detect")

class Extractor():
    def __init__(self):
        self.ocr_model = PaddleOCR(use_angle_cls=True, lang='korean', use_gpu=False)
        self.result_list = []

    def extract_text(self, images:list[str]):
        """
        이미지->텍스트 추출 실행
        """
        try:
            for image in images:
                self.result_list.append(Result(file_name=image, ocr_result=self.ocr_model.ocr(image)[0]))
            self.save_to_text()
            self.result_list.clear()
        except Exception as ex:
            file_logger.error(ex)
    
    def save_to_text(self):
        try:
            text_file_path = f"{datetime.now().strftime('%Y-%m-%d %H_%M_%S')}.txt"
            with open(text_file_path, "w") as f:
                f.write(
                        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} OCR 실행 결과\n순번\t\t이미지 경로\t\t\t차량번호\n------------------------------------------------------------------------\n"
                    )
                for i in range(len(self.result_list)):
                    f.write(f"{str(i+1)}\t\t")
                    f.write(f"{str(self.result_list[i].file_name)}\t\t\t")
                    f.write(f"{str(''.join(self.result_list[i].texts))}\n")
        except Exception as ex:
            file_logger.error(ex)