import requests 
import time 
import os 
import ctypes from colorama import init, Fore; init()

with open('token.txt', 'r', encoding='UTF-8') as f: token = f.read()
num = 0

words = ['Testing', 'Something', 'Interesting']
emoji_id = '795820417717501993'
emoji_name = 'teehee'

headers = {
    'Authorization': token,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Content-Type': 'application/json',
    'Accept': '*/*'
}

while True:
    for x in range(3):
        try:
            data = {'custom_status':{'text':words[x],'emoji_id':emoji_id,'emoji_name':emoji_name}}
            r = requests.patch('https://discordapp.com/api/v6/users/@me/settings', headers=headers, json=data)
            if "'code': 0" in r.text: print(f'{Fore.RED}Invalid/outdated token{Fore.WHITE}.'); time.sleep(600); os._exit(0)
            else: print(f'{Fore.GREEN}Edited status to{Fore.WHITE}: {words[x]}'); num += 1; ctypes.windll.kernel32.SetConsoleTitleW(f'Edited: {num} times'); time.sleep(1)
        except:
            pass
