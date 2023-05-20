import socket

IP = '127.0.0.1'
PORT = 34754
FORMAT = 'utf-8'

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind((IP, PORT))

while True:
    message, address = socket.recvfrom(1024)
    message = message.decode(FORMAT)

    print(f'{address}: {message}')
    