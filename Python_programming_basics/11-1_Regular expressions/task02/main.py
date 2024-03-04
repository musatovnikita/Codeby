import re

with open('proxy.txt', 'r') as file:
    content = file.read()
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    ip_addresses = re.findall(ip_pattern, content)
    for ip in ip_addresses:
        print(ip)