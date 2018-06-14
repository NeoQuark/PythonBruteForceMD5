import sys, hashlib, time, string, itertools, inquirer

def getShadow():
	global users
	users = {}
	#with open(raw_input('Where is shadow ?\n'), 'r') as shadow:
	with open('shadow', 'r') as shadow:
			for l in shadow:
				if len(l.split(':')[1].split('$')) > 1:
					if l.split(':')[1].split('$')[1] == '1':
						users[l.split(':')[0]] = l.split(':')[1]

def brut(target, size=1):
	start = time.time()
	for char in itertools.product(string.printable, repeat=size):
		pwd = ''.join(char)
		print("Trying password " + str(pwd.strip()) + " for user " + str(user))
		
		end = time.time()
		global t_time 
		t_time = end - start

		if hashlib.md5(pwd).hexdigest() == target:
			print("\nPassword Found. \nPassword for user " + user + " is : " + pwd)
			print("Total runtime was : " + str(t_time) + " seconds\n")
			write(user, pwd.strip(), t_time)
			return pwd
			break

	return brut(target, size+1)

def write(user, password, time):
	line = user + " : " + password + " in " + str(t_time) + "s\n"
	with open('passwords', 'a') as pwdsFile:
		pwdsFile.write(line)

def crack():
	global user
	global pwd
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

	brut(fileHash)

def main():
	getShadow()
	crack()

if __name__ == "__main__":
	main()
	sys.exit(0)