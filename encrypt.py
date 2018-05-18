
def encrypt(word,key):
	st = ''
	key_list = [int(x) for x in str(key)]
	count = 0
	for char in word:
		int_form = ord(char)
		if 65 <= int_form <= 90:
			st += chr(wrap(65, 90, int_form + key_list[count % len(key_list)]))
			count += 1
		elif 97 <= int_form <= 122:
			st += chr(wrap(97, 122, int_form + key_list[count % len(key_list)]))
			count += 1
		else:
			st += chr(int_form)
		
	return st

# helper function to wrap numbers into range
def wrap(lo,hi,val):
	return ((val - lo) % (hi - lo + 1)) + lo

message = "-Your friend, Alice"
encryption = "-Atvt hrqgse, Cnikg"
msg1 = "Bjj rwkcs dwpyp fwz ovors wxjs vje tcez fqg"
key = "8251220"
#print(encrypt(message,2512208))

# io = input()
# key = int(input())
# print("'{0}' ---[ENCRYPTION]---> '{1}'".format(io,encrypt(io,key)))

def decrypt(encrypted_message):
	decrypted_msg = ''
	count = 0
	for char in encrypted_message:
		int_form = ord(char)
		if 65 <= int_form <= 90:
			decrypted_msg += chr(wrap(65, 90, int_form - int(key[count % len(key)])))
			count += 1
		elif 97 <= int_form <= 122:
			decrypted_msg += chr(wrap(97, 122, int_form - int(key[count % len(key)])))
			count += 1
		else:
			decrypted_msg += chr(int_form)
		
	return decrypted_msg

print(decrypt(msg1))
	

