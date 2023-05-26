import socket
from bytes import *
from math import *
from consts import *


socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind((IP, PORT))


def write_file(file_name, data):
    with open(file_name, 'wb') as file:
        file.write(data)


def receive_file():
    file_size, address = socket.recvfrom(1024)
    file_size = int(file_size.decode(FORMAT))

    num_blocks = int(ceil(file_size / BLOCK_SIZE))
    blocks = [b'' for _ in range(num_blocks)]
    padding = file_size % BLOCK_SIZE

    for i in range(blocks):
        data, address = socket.recvfrom(BLOCK_SIZE)

        if i == blocks - 1:
            data = unpad(data, padding)
        

print('Waiting for messages...')
while True:

    message, address = socket.recvfrom(1024)
    message = message.decode(FORMAT)

    if message == SEND_FILE:
        receive_file()
        print(f'File received from {address}')
    else:
        print(f'{address}: {message}')
    