import cv2

frameWidth = 600
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
while True:
    success, img = cap.read()
    imgBlur = cv2.GaussianBlur(img, (7, 7), 1)

    cv2.imshow("Results", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyWindow()
