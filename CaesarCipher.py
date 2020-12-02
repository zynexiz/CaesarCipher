'''
Simple implementation of Caesar cipher
Author: Michael Rydén

@package CaesarCipher
'''

# Main class for working with the cipher
#
# Public functions:
#   string encrypt( string, shiftCounter)
#   string decrypt( string, shiftCounter)
#   dictionary analyze( string )
#
class CaesarCipher():
    def __init__(self):
        self.chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
    # Private function to shift the chars string n positions
    def __shiftString(self, n):
        i = n % len(self.chars)
        return self.chars[i:] + self.chars[:i]
    
    def encrypt(self, str, n):
        cipher = self.__shiftString(n)
        result = ""
        for s in str:
            try:
                idx = self.chars.index(s)
                result += cipher[idx]
            except:
                result += s
        return result

    def decrypt(self, str, n):
        cipher = self.__shiftString(n)
        result = ""
        for s in str:
            try:
                idx = cipher.index(s)
                result += self.chars[idx]
            except:
                result += s
        return result
    
    def analyze(self, str):
        dic = {}
        # Initialize dictionary with zeros
        for i in range(0, len(self.chars)): dic[self.chars[i]] = 0
        for char in str:
            try:
                idx = self.chars.index(char)
                dic[char] += 1
            except:
                continue
        return dic




# Init CaesarCipher class and set the shift shift counter
cc = CaesarCipher()
shift = 30

# Open file and encrypt it
rf = open('clearText.txt')
nf = open('encryptedFile.txt','w')

print('-'*60+'\nEncrypted text:\n'+'-'*60)
for line in rf:
    enc = cc.encrypt(line,shift)
    nf.write(enc)
    print(enc, end="")

rf.close()
nf.close()

# Try open the encrypted file and decrypt it
rf = open('encryptedFile.txt')

print('\n\n'+'-'*60+'\nDecrypted file from encryptedFile.txt\n'+'-'*60)
for line in rf:
    dec = cc.decrypt(line, shift)
    print(dec, end="")

rf.close()

# Open the encrypted file and do a frequency analysis on it
rf = open('encryptedFile.txt')
test = sorted(cc.analyze(rf.read()).items(), key=lambda x: x[1], reverse=True)

print('\n\n'+'-'*60+'\nFrequency analysis\n'+'-'*60)
for i in test:
    if i[1] == 0: break
    print(i[0],'occurs', i[1], 'times in encrypted text')
