#!/bin/python
import socket
import sys
host = sys.argv[1]

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((host,21))

print("Connectando ao servidor...")
banner = tcp.recv(1024)
print(banner)

print("Enviando User...")
tcp.send(b"USER ftp\r\n")
user = tcp.recv(1024)
print(user)

print("Enviando Pass...")
tcp.send(b"PASS ftp\r\n")
pw = tcp.recv(1024)
print(pw)

print("Enviando comando Help....")
tcp.send(b"HELP \r\n")
cmd = tcp.recv(2048)
print(cmd.decode())
