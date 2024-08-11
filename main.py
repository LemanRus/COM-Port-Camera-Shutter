import sys
import serial
import datetime
import cv2

print("Start camera...")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not (cap.isOpened()):
    print("Could not open video device")
else:
    print("Camera started succesfully")

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
cap.set(cv2.CAP_PROP_FOCUS, 255)

try:
    s = serial.Serial('COM4', baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
except serial.serialutil.SerialException:
    print("Can't open COM port, check and restart")
    sys.exit()

while True:
    command = s.readline().decode("Ascii")
    if command.strip() == "SMILE":
        ret, frame = cap.read()
        img_name = datetime.datetime.now().strftime("%Y_%m_%d__%H_%M_%S") + ".jpg"
        cv2.imwrite(img_name, frame)
        print("{} is captured".format(img_name))