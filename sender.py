import socket

IP = '127.0.0.1'
PORT = 34754
FORMAT = 'utf-8'

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send(message):
    message = message.encode(FORMAT)
    socket.sendto(message, (IP, PORT))

while True:
    message = input('--> ')
    send(message) 
