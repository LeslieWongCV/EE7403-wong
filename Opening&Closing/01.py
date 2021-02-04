# -*- coding: utf-8 -*-
# @Time    : 2021/2/4 1:29 下午
# @Author  : Yushuo Wang
# @FileName: 01.py
# @Software: PyCharm
# @Blog    ：https://lesliewongcv.github.io/

import cv2
import numpy as np


img = cv2.imread('fingerprint.png', 0)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
img_01 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
img_02 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

img_O_C = cv2.morphologyEx(img_01, cv2.MORPH_CLOSE, kernel)
img_C_O = cv2.morphologyEx(img_02, cv2.MORPH_OPEN, kernel)

cv2.imwrite("img_O_C.png", img_O_C)
cv2.imwrite("img_C_O.png", img_C_O)
