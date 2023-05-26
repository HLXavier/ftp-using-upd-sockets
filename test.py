from bytes import *
from os import path
from math import ceil

# bytes = random_bytes(10)
# print(string_from_bytes(bytes))

# bytes_crc = crc(bytes)
# print(string_from_bytes(bytes_crc))

# _bytes = random_bytes(10)
# print(string_from_bytes(_bytes))

# _bytes_crc = crc(_bytes)
# print(string_from_bytes(_bytes_crc))

BLOCK_SIZE = 300

def get_block(block):
    with open('file.txt', 'rb') as file:
        file.seek(BLOCK_SIZE * block)
        data = file.read(BLOCK_SIZE)
        return data

def copy_file():    
    file_size = path.getsize('file.txt')
    blocks = int(ceil(file_size / BLOCK_SIZE))

    copy = b''

    for i in range(blocks):
        data = get_block(i)

        copy += data

    with open('file.copy.txt', 'wb') as file:
        file.write(copy)

copy_file()
