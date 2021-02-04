from pymongo import MongoClient
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import sys
import datetime


# starting the webcam using opencv
cap = cv2.VideoCapture(0)
names = []

# function for writing the data into Mongo DB
# Mongo Initialization
client = MongoClient("mongodb://localhost:27017/")
database = client.Attendance
collection = database.Lab


def enterData(Name, Date, Subject):
    if Name in names:
        pass
    else:
        names.append(Name)
        print(names)
        Name = ''.join(str(Name))

        insertion = collection.insert_one(
            {"Name": Name, "Date": Date, "Subject": Subject})
        if insertion.acknowledged:
            print("Document is added and ID is: ", insertion.inserted_id)
    return names


def QR_attendance():

    print("<------------------------->")
    Subject = str(input("Enter Name of Subject : "))
    Date = datetime.datetime.today()
    print('<------ Reading ---------->')

    # function for check the data is present or not
    def checkData(data):
        data = str(data)
        if data in names:
            print(data + ' is already present')
        else:
            print('\n'+str(len(names)+1)+'\n'+data)
            enterData(data, Date, Subject)

    while True:
        _, frame = cap.read()
        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:
            Name = obj.data.decode("utf-8")
            checkData(Name)

        cv2.imshow("Frame", frame)

        # closing the program when s is pressed
        if cv2.waitKey(1) & 0xFF == ord('c'):
            cv2.destroyAllWindows()
            break


QR_attendance()
