from requests.models import Response
import requests
import os

color = 'color 04'
os.system(color)
print(""" _______________
< !!SuB-ListeR!! >
 ---------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----w |
                ||     ||""")


print('Usage: Enter the domain name without <http> or <https>')
print('Example: google.com')
domain = input('Enter the domain name : ')

clear = 'cls'
os.system(clear)

file = open('domains.txt','r')

name = file.read()
subs = name.splitlines()
colour = 'color 02'
os.system(colour)
discovered_subdomains = []
for sub in subs:
    url = f"http://{sub}.{domain}"
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print("[+] Discovered subdomain:", url)
        discovered_subdomains.append(url)
