import cv2

path = "cat.jpg"
# read img
img = cv2.imread(path)
print(img.shape)

# image resize
# dsize = (width, height)
imgResize = cv2.resize(img, dsize=(500, 300))
print(imgResize.shape)  # (width,height,RGB)

# image cropped
# imgCropped = img[height,width]
imgCropped = imgResize[0:300, 80:600]

# show image
cv2.imshow("Image", img)
cv2.imshow("Image resize", imgResize)
cv2.imshow("Image cropeed", imgCropped)
cv2.waitKey(0)
