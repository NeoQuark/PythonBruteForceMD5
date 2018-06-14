import sys, hashlib, time, inquirer

def getShadow():
	global users
	users = {}
	#with open(raw_input('Where is shadow ?\n'), 'r') as shadow:
	with open('shadow', 'r') as shadow:
			for l in shadow:
				if len(l.split(':')[1].split('$')) > 1:
					if l.split(':')[1].split('$')[1] == '1':
						users[l.split(':')[0]] = l.split(':')[1]

def write(user, password, time):
	line = user + " : " + password + " in " + str(t_time) + "s\n"
	with open('passwords', 'a') as pwdsFile:
		pwdsFile.write(line)

def crack():
	global user
	global pwd
	try:
		pwds = open('dico_mini_fr')
	except:
		while True:
			dico = raw_input('File not found. Where is dictionary ?\n')
			try:
				pwds = open(dico)
			except:
				continue
			else:
				break
	while True:
		choices = []
		for user, hashdpwd in users.iteritems():
			print(user + " : " + hashdpwd)
			choices.append(user)
		# user = raw_input("\nWhose password do you want to find ?\n")
		question = [inquirer.List('action', message='Whose password do you want to find ?', choices=choices)]
		user = inquirer.prompt(question)['action']
		try:
			fileHash = users[user].split('$')[2]
		except:
			print("User not found.\n")
		else:
			break

	start = time.time()
	for pwd in pwds:
		hashMD5 = hashlib.md5(pwd.strip()).hexdigest()
		print("Trying password " + str(pwd.strip()) + " for user " + str(user))

		end = time.time()
		global t_time 
		t_time = end - start

		if fileHash == hashMD5:
			print("\nPassword Found. \nPassword for user " + user + " is : " + pwd)
			print("Total runtime was : " + str(t_time) + " seconds\n")
			write(user, pwd.strip(), t_time)
			break
	else:
		print("\nPassword not Found.")
		print(fileHash)

def main():
	getShadow()
	crack()

if __name__ == "__main__":
	main()
	sys.exit(0)