import socket
import wave

#Inicijalizacija Klijenta
HOST = "localhost"
PORT = 13132

veza = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
veza.connect((HOST,PORT))

wf = wave.open("pjesma.wav", "rb")
rate = wf.getframerate()

while 1:
    podaci = wf.readframes(rate*2)
    veza.sendall(podaci)

veza.close()