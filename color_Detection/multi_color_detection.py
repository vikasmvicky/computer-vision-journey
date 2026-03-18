import cv2

img = cv2.imread("image.jpg", 0)

cv2.imshow("Gray Image", img)

cv2.imwrite("gray_output.jpg", img)

cv2.waitKey(0)

cv2.destroyAllWindows()