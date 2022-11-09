import cv2
cam = cv2.VideoCapture(0)
cv2.namedWindow("test camera")
imgCont = 0
while True:
    ret, frame = cam.read()
    if not ret:
        print("error")
        

    cv2.imshow("test", frame)


cam.release()
cam.destroyAllWindows()
