import cv2
from playsound import playsound
import time
import threading
def sounds():
    start_time = time.time()
    while time.time() - start_time < 11:
          playsound('audio.mp3')


cam = cv2.VideoCapture(1)
fair_ca = cv2.CascadeClassifier('fire_detection.xml')

alarm_start = False
last_time = 0
while True:
    ret , frame = cam.read()
    if not ret :
        break
    fire = fair_ca.detectMultiScale(frame,1.2,5)
    if len(fire) > 0 and not alarm_start:
        print('fire detected')
        threading.Thread(target=sounds).start()
        alarm_start = True
        last_time = time.time()

    if alarm_start and time.time() - last_time > 11:
        alarm_start = False

    for (x,y,w,h) in fire:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)



    cv2.imshow('fire',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break



