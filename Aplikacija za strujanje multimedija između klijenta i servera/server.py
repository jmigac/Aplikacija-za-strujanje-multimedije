import socket 
import pyaudio

#Konfiguracija pjesme
BUFFER = 512
CHUNK = 9000
FORMAT = pyaudio.paInt32
KANALI = 2
RATE = 44100
WIDTH = 2
p = pyaudio.PyAudio()

#Konfiguracija socketa
HOST = "localhost"
PORT = 13132
