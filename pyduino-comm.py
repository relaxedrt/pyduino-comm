#pip install pyserial
import serial
import time

#Describimos cual sera el puerto en el que estara conectado el arduino
arduino = serial.Serial(port = "COM4", baudrate = 115200, timeout = .1)

def write_read(x):
    #Escribimos por el puerto serie al arduino
    arduino.write(bytes(x, "utf-8"))
    time.sleep(0.05)
    #leemos la ultima linea de la comunicacion serie
    data = arduino.readline()
    return data

while True:
    num = input(f"Introduce un numero: ")
    value = write_read(num)
    print(value)