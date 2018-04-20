# Barbara King
# H8-4: readint.py
#
#   Starting code H8-4
#

def read_int():
	'''
	read int from user and return;
	handle exceptions to defend against invalid ints
	:return:
	'''
	while True:
		# read str from user
		try:
			instr = input("Enter an integer: ")
			value = int(instr)
			break # instead of setting true/false statements, can use break
		except:
			print("Bad input, try again. Enter an integer: ")

	return value

print(read_int())





