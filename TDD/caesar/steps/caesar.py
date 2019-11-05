# 
# Python class to implement Caesar Cipher
#
class caesar():
	
	#
	# Constructor
	#
	def __init__(self,offset):
		if offset < -26 or offset > 25:
			raise ValueError("Invalid offset value: "+str(offset))
		self.offset = offset
		
	#
	# Check text is alpha chars only else raise exception
	#
	def isAlpha(self,string):
		if not string.isalpha():
			raise ValueError("Text must be alpha characters only :"+string)
		return self

	#
	# Shift the character by the required positions and rotate around the alphabet as needed
	#
	def shiftChar(self,char,shift):
		base = 65 if char.isupper() else 97
		return chr(base+((ord(char)+shift)-base) % 26)
			
			
	#
	# function returns the encrypted text generated using the character offset provided
	#
	def cipherText(self,text): 
		return "".join([self.shiftChar(text[i],self.offset) for i in range(len(text))])

		
	# 
	# function decrypts the cipher text and returns in the clear
	#
	def originalText(self,cipher_text): 
		return "".join([self.shiftChar(cipher_text[i],-self.offset) for i in range(len(cipher_text))])
		

#
# If run as main then perform interactive test
#
if __name__ == "__main__": 
    while True:
	
		#
		# Loop requesting character offset and then the text to encrypt
		#
        mystr = input("Offset: ")
        if not len(mystr):
            break

        try:
            offset = int(mystr)
            engine = caesar(offset)
        except:
            print("Invalid offset - "+mystr)
            continue

        while True:	
            string = input("Text to encrypt: ")
            if not len(string):
                break		
			
			#
			# Check text is alpha chars only and then encrypt, then decrypt and display strings
			#
            cipher_text = engine.isAlpha(string).cipherText(string) 
            print("Cipher:", cipher_text) 
            print("Plain :", engine.originalText(cipher_text)) 
