import cv2
import pyzbar.pyzbar as pyzbar
import numpy



cap= cv2.VideoCapture(0)
font = cv2.FONT_ITALIC
while True:
    _,frame = cap.read()
    ### QR detection
    decodedobjects = pyzbar.decode(frame)
    for obj in decodedobjects:
        #print("Data",obj.data) ##  print output to console
        cv2.putText(frame,str(obj.data),(50,50),font,0.5,(255,0,0),3)
        with open("Att.txt","a") as f:
            f.write(obj.data.decode("utf-8"))
    cv2.imshow("Frame",frame)
    key = cv2.waitKey(1)
    if  cv2.waitKey(10)  &  0xff  == ord('q') :
        break
cv2.destroyAllWindows()
cap.release()

