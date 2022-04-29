import cv2 as cv
import numpy as np

haystack_img = cv.imread('images/haystack.jpg', cv.IMREAD_UNCHANGED)
needle_img = cv.imread('images/needle.jpg', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)

cv.imshow('Result', result)
cv.waitKey()