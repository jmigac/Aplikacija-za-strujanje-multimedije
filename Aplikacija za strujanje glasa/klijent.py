import socket
import pyaudio
import wave

#Inicijalizacija za PyAudio

CHUNK = 1024
KANALI = 2
RATE = 44100
INPUT = True
FORMAT = pyaudio.paInt16

#Inicijalizacija Socketa
HOST = "127.0.0.1"
PORT = 953
SIZE = 1024

if __name__ == '__main__':
    p = pyaudio.PyAudio()
    strujanje = p.open(
        format = FORMAT,
        channels = KANALI,
        rate = RATE,
        input = INPUT,
        frames_per_buffer = CHUNK)
    veza = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while 1:
        podaci = strujanje.read(CHUNK)
        veza.sendto(podaci,(HOST,PORT))
    
    veza.close()
    strujanje.stop_stream()
    strujanje.close()
    p.terminate()
