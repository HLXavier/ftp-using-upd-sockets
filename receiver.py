import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 34754

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

print("UDP target IP: %s" % UDP_IP)

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received message: %s" % data)