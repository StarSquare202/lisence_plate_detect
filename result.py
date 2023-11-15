import logging
file_logger = logging.getLogger("license_plate_detect")

class Result:
    """
    번호판 추출 결과 저장 객체
    """
    def __init__(self, file_name:str, ocr_result:list):
        self.file_name = file_name
        self.boxes = [ocr_result[i][0] for i in range(len(ocr_result))]
        self.texts = [str(ocr_result[i][1][0]) for i in range(len(ocr_result))]
        self.scores = [float(ocr_result[i][1][1]) for i in range(len(ocr_result))]

        file_logger.info(f'file_name : {self.file_name}')
        file_logger.info(f'boxes : {self.boxes}')
        file_logger.info(f'texts : {self.texts}')
        file_logger.info(f'scores : {self.scores}')
