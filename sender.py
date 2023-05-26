import socket

from os import path
from math import ceil
from bytes import *
from consts import *

# Packet structure:

# HEADER (8 bytes)
# [0:4] - Sequence number
# [4:8] - CRC

# DATA (300 bytes)
# message


socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def read_block(file_name, seq_number):
    with open(file_name, 'rb') as file:
        file.seek(BLOCK_SIZE * seq_number)
        data = file.read(BLOCK_SIZE)
        return data
        

def header(seq_number, block):
    seq_number = bytes_from_int(seq_number)
    block_crc = crc(block)
    return seq_number + block_crc


def send(message):
    message = message.encode(FORMAT)
    socket.sendto(message, (IP, PORT))


def send_file(file_name):    
    file_size = path.getsize('file.txt')
    blocks = int(ceil(file_size / BLOCK_SIZE))

    send(str(file_size))

    for seq_number in range(blocks):
        data = read_block(file_name, seq_number)

        if len(data) < BLOCK_SIZE:
            data = pad(data, BLOCK_SIZE)

        data = header(seq_number, data) + data
        socket.sendto(data, (IP, PORT))


while True:
    message = input('--> ')
    send(message)

    if message == SEND_FILE:
        send_file('file.txt')
