from pymongo import MongoClient
import cv2
import pyzbar.pyzbar as pyzbar
import numpy
from datetime import date

Date=str(date.today())
# print(Date)
Subject="DCCN"
# Storing Values of QR in MongoDB
client = MongoClient("mongodb://localhost:27017/")
print(client)
# Check DBs
print(client.list_database_names())
# Create DB
db = client.Attendance
collection = db.Lab

def QR_Detect():
    cap = cv2.VideoCapture(0)
    font = cv2.FONT_ITALIC
    while True:
        _, frame = cap.read()
        # QR detection
        decodedobjects = pyzbar.decode(frame)
        #print(decodedobjects)
        for obj in decodedobjects:
            # print("Data",obj.data) ##  print output to console
            cv2.putText(frame, str(obj.data), (50, 50), font, 1, (255, 0, 0), 3)
            Name = obj.data.decode("utf-8")
            # with open("Att.txt", "a") as f:
            #     f.write(obj.data.decode("utf-8"))
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if cv2.waitKey(10) & 0xff == ord('q'):
            break
    
    insertion=collection.insert_one({"Name": Name,"Date":Date,"Subject":Subject})
    
    if insertion.acknowledged:
        print("Document is added and ID is: ", insertion.inserted_id)

    cv2.destroyAllWindows()
    cap.release()
QR_Detect()