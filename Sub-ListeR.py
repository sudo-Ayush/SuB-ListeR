from requests.models import Response
from os import system, name
from colorama import Fore
import colorama
import time
import requests

colorama.init(autoreset=True)

if name == 'nt':
	_ = system('cls')

else:
	_ = system('clear')

print(f'{Fore.YELLOW} STARTING SubLister....')
time.sleep(2)

if name == 'nt':
	_ = system('cls')

else:
	_ = system('clear')

print(f"""{Fore.RED} _______________
< !!SuB-ListeR!! >
 ---------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----w |
                ||     ||\n""")


print(f'{Fore.YELLOW} [-] Usage: Enter the domain name without <http> or <https>')
print(f'{Fore.YELLOW} [-] Example: google.com')
print(f'{Fore.YELLOW} [-] Enter the domain name :\n')
domain = input(f">").lower()

if name == 'nt':
	_ = system('cls')

else:
	_ = system('clear')

file = open('sub-list.txt','r')

name = file.read()
subs = name.splitlines()
discovered_subdomains = []
for sub in subs:
    url = f"https://{sub}.{domain}"
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print(f"{Fore.GREEN}[+] Discovered subdomain:", url)
        discovered_subdomains.append(url)

print(f'{Fore.YELLOW} Finished...!')
