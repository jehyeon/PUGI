import cv2

# Easy width height
# Using cv2
class ESwh:
    def __init__(self, src):
        self._src = src
        self._origin_image = cv2.imread(src)
        self._gray = cv2.cvtColor(self._origin_image, cv2.COLOR_BGR2GRAY)
        self._blur = cv2.GaussianBlur(self._gray, (3,3), 0)         # 임시적으로 (5,5) 가우시안 블러 적용

        self._h, self._w, _ = self._origin_image.shape

    def save_all(self, _src):
        # to be update
        # _src 마지막에 유동적으로 '/' 추가 및 제거
        # jpg 이외 다양한 포맷 지원
        cv2.imwrite(_src + 'origin.jpg', self._origin_image)
        cv2.imwrite(_src + 'gray.jpg', self._gray)
        cv2.imwrite(_src + 'blur.jpg', self._blur)