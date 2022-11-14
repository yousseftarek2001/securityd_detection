import cv2
live = cv2.VideoCapture(0)
imgcount= 0
while True:
    ret, frame = live.read()
    if not ret:
        print("error")
        break

    
    if cv2.waitKey(20) & 0xFF == ord('d'):
        print("close app")
        break
    elif cv2.waitKey(32) & 0xFF == ord('s'):
        cv2.imwrite("screenShot{}.png".format(imgcount),frame)
        print("screenshot was taken")
        imgcount+=1

    cv2.imshow("take ScreenShot",frame)


live.release()
live.destroyAllWindows()