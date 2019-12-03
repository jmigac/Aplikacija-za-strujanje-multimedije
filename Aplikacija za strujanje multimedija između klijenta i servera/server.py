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

strujanje = p.open(
    format = p.get_format_from_width(WIDTH),
    channels = KANALI,
    rate = RATE,
    output = TRUE,
    frame_per_buffer = CHUNK
)

veza = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
veza.bind((HOST,PORT))
veza.listen(1)

while 1:
    vezaSocket, adresaKlijenta = veza.accept()
    data = veza.recv(BUFFER*2)
    while data != '':
        strujanje.write(data)
        data = vezaSocket.recv(BUFFER*2)

vezaSocket.close()
strujanje.stop_stream()
strujanje.close()
p.terminate()
veza.close()