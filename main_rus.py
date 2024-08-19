import os
import sys
import serial
import datetime
import cv2

print("Запуск камеры...")
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

if not (cap.isOpened()):
    print("Не удалось открыть видеоустройство")
    print("Нажмите ENTER для выхода")
    input()
    sys.exit()
else:
    print("Камера успешно запущена")
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    cap.set(cv2.CAP_PROP_FOCUS, 30)
    print("Настройка камеры завершена")

print("Открытие COM порта...")
try:
    s = serial.Serial('COM4', baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
except serial.serialutil.SerialException:
    print("Не удается открыть COM порт, проверьте настройки и перезапустите")
    print("Нажмите ENTER для выхода")
    input()
    sys.exit()

print("COM порт успешно открыт")

print("Создание папки...")
folder_name = "Начато " + datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
os.makedirs(folder_name)
os.chdir(folder_name)

img_counter = 1

while True:
    command = s.readline().decode()
    if command.strip() == "SMILE":
        ret, frame = cap.read()
        img_name = f"{img_counter}.jpg"
        cv2.imwrite(img_name, frame)
        print(f"{img_name} сохранено")
        img_counter += 1
    if command.strip() == "FINISH":
        s.close()
        cap.release()
        print("Работа завершена успешно")
        print("Нажмите ENTER для выхода")
        input()
        break
