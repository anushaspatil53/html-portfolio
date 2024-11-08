
def encryption(plain,key):
	cipher_text = ''
	for char in plain:
		if 'A'<=char<='Z': 
			new_char = chr(((ord(char)-ord('A')+key)%26)+ord('A'))
			cipher_text += new_char
		elif 'a'<=char <= 'z':
                        new_char = chr(((ord(char)-ord('a')+key)%26)+ord('a'))
                        cipher_text += new_char
		else:
			cipher_text += char
	return cipher_text



plain = input("enter the plain text:")
key = int(input("enter the shift:"))
cipher = encryption(plain,key)
print(f"The cipher is {cipher}")

def decryption(cipher,shift):
        decrypted_text = ''
        for char in cipher:
                if 'A'<=char<='Z': 
                        new_char = chr(((ord(char)-ord('A')-shift)%26)+ord('A'))
                        decrypted_text += new_char
                elif 'a'<=char <= 'z':
                        new_char = chr(((ord(char)-ord('a')-shift)%26)+ord('a'))
                        decrypted_text += new_char
                else:
                        decrypted_text += char
        return decrypted_text


cipher = input("enter the cipher text:")
shift = int(input("enter the shift:"))
decrypt = decryption(cipher,shift)
print(f"The decrypted text is {decrypt}:")
