from os import urandom
from binascii import hexlify, crc32


def string_from_bytes(bytes):
    return hexlify(bytes).decode('utf-8').upper()


def bytes_from_int(int):
    return int.to_bytes(4, 'big')


def bytes_from_string(string):
    return bytes.fromhex(string)


def random_bytes(size):
    return urandom(size)


def pad(bytes, size):
    return bytes + b'\0' * (size - len(bytes))


def unpad(bytes, size):
    return bytes[:size]


def crc(bytes):
    return bytes_from_int(crc32(bytes))
    