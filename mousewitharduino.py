import pyautogui
import serial
ser = serial.Serial(
    port='COM4',
    baudrate=9600,
)
while True:
    if ser.readable():
        res = ser.readline()
        a= res.decode()[:len(res)-1].split()
        pyautogui.moveRel(-0.1*(520-int(a[0])), 0.1*(515-int(a[1])))
        if int(a[2])==0:
            pyautogui.click()
