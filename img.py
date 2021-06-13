import cv2

img = cv2.imread('F:\Computer Vision\opencv-master\samples\data\lena.jpg',0)

print(img)

cv2.imshow('image', img)
cv2.waitKey(5000)
cv2.destroyAllWindows()