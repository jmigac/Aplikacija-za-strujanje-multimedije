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