import cv2

image=cv2.imread('Cfd.png')
rgb_img=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
cv2.imshow('rgb',rgb_img)
cv2.imshow('image',image)
cv2.waitKey(0)