import socket
import pyaudio

#Inicijalizacija za PyAudio

CHUNK = 1024
KANALI = 2
RATE = 44100
OUTPUT = True
FORMAT = pyaudio.paInt16

#Inicijalizacija Socketa
HOST = "127.0.0.1"
PORT = 953
BACKLOG = 1
SIZE = 4096

if __name__ == '__main__':
    p = pyaudio.PyAudio()
    strujanje = p.open(
        format=FORMAT,
        channels = KANALI,
        rate = RATE,
        output = OUTPUT)
    veza = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    veza.bind((HOST,PORT))
    while True:
        podaci,adresaKlijenta = veza.recvfrom(SIZE)
        if podaci:
            strujanje.write(podaci)
    
    veza.close()
    strujanje.stop_stream()
    strujanje.close()
    p.terminate()