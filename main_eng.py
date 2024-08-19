import os
import sys
import serial
import datetime
import cv2

print("Start camera...")
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

if not (cap.isOpened()):
    print("Could not open video device")
    print("Press ENTER to exit")
    input()
    sys.exit()
else:
    print("Camera started successfully")
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    cap.set(cv2.CAP_PROP_FOCUS, 30)
    print("Camera setup completed")

print("Open COM port...")
try:
    s = serial.Serial('COM4', baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
except serial.serialutil.SerialException:
    print("Can't open COM port, check and restart")
    print("Press ENTER to exit")
    input()
    sys.exit()

print("COM started successfully")

print("Create folder...")
folder_name = "Started at " + datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
os.makedirs(folder_name)
os.chdir(folder_name)

img_counter = 1

while True:
    command = s.readline().decode()
    if command.strip() == "SMILE":
        ret, frame = cap.read()
        img_name = f"{img_counter}.jpg"
        cv2.imwrite(img_name, frame)
        print(f"{img_name} is captured")
        img_counter += 1
    if command.strip() == "FINISH":
        s.close()
        cap.release()
        print("Job done successfully")
        print("Press ENTER to exit")
        input()
        break
