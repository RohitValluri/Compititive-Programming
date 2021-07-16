# A Caesar Cipher is a simple cipher that works by shifting each letter in 
# the given message by a certain number. For example, if we shift the message 
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given 
# message by shift letters. You are guaranteed that message is a string, and 
# that shift is an integer between -25 and 25. Capital letters should stay capital 
# and lowercase letters should stay lowercase, and non-letter characters should not be changed. 
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")


def fun_applycaesarcipher(msg, shift):
	string = ""
	for i in range(len(msg)):
		if(msg[i].isupper()):
			string+=chr((ord(msg[i]) + shift - ord('A')) % 26 + ord('A'))
		elif(msg[i].islower()):
			string+=chr((ord(msg[i]) + shift - ord('a')) % 26 + ord('a'))
		elif(msg[i]==" "):
			string+=(" ")
	return string					

# print(fun_applycaesarcipher("We Attack At Dawn", 1))
# print(fun_applycaesarcipher("zodiac", -2))
# print(fun_applycaesarcipher("ABCDXYZ", -3))
# print(fun_applycaesarcipher("ABCDXYZ", 3))
# print(fun_applycaesarcipher("abcdxyz", -3))
# print(fun_applycaesarcipher("abcdxyz", 3))


