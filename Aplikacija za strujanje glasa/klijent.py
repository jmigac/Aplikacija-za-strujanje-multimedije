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