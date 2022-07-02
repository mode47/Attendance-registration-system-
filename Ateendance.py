import face_recognition
import  cv2
import os

import numpy as np
import time
path='photots'
img=[]
imgname=[]

myList=os.listdir(path)
for i in myList:
    imgpath=cv2.imread(f'{path}/{i}')
    img.append(imgpath)
    imgname.append(os.path.splitext(i)[0])
print(imgname)
name_data=[]
def findEnquding(img):
    encoding=[]
    for i in img:
        img=cv2.cvtColor(i,cv2.COLOR_BGR2RGB)
        face_encidung = face_recognition.face_encodings(img)[0]
        encoding.append(face_encidung)

    return encoding
from datetime import datetime
def markaddtend(name):
    with open('sheet.csv','r+') as f:
        datatimelist=f.readlines()
        names=[]
        for Line in datatimelist:
            entry=Line.split(',')
            names.append(entry[0])
            if name not in names:

                currunt=datetime.now()
                datastring=currunt.strftime('%H:%M:%S')

                #name_data.append([name,datastring])
                f.writelines(f'{name},{datastring}\n')
                #time.sleep(1)


        #print(name_data)
encodingListKnown=findEnquding(img)
cap=cv2.VideoCapture(0)
while True:
    success, img = cap.read()

# img = captureScreen()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame,facesCurFrame):
             matches = face_recognition.compare_faces(encodingListKnown, encodeFace)
             faceDis = face_recognition.face_distance(encodingListKnown, encodeFace)
# print(faceDis)
             matchIndex = np.argmin(faceDis)
             #print(matches)
             if matches[matchIndex]:

                 name = imgname[matchIndex].upper()
                 y1, x2, y2, x1 = faceLoc
                 y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                 cv2.rectangle(img,(faceLoc[3]*4,faceLoc[0]*4),(faceLoc[1]*4,faceLoc[2]*4),(255,0,0),1)
                # cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                 cv2.putText(img,name,(x1 +6,y2 -6),cv2.FONT_HERSHEY_SIMPLEX,1,(255, 255, 255),2)
                 markaddtend(name)
    cv2.imshow('Webcam', img)

    cv2.waitKey(1)
