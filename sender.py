import socket
from bytes import *
from os import path
from math import ceil
from consts import *


socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def send(message):
    message = message.encode(FORMAT)
    socket.sendto(message, (IP, PORT))


def send_file(file_name):    
    file_size = path.getsize('file.txt')
    blocks = int(ceil(file_size / BLOCK_SIZE))

    send(str(file_size))

    with open(file_name, 'rb') as file:
        for _ in range(blocks):
            data = file.read(BLOCK_SIZE)

            if len(data) < BLOCK_SIZE:
                data = pad(data, BLOCK_SIZE)

            socket.sendto(data, (IP, PORT))


while True:
    message = input('--> ')
    send(message)

    if message == SEND_FILE:
        send_file('file.txt')
