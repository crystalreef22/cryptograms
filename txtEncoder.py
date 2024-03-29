import random

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


class Encoded:
    def __init__(self, plaintext, encoder):
        self.plaintext = plaintext
        self.encoder = encoder
        self.formattedPlaintext = self.encoder.format(plaintext)
        self.ciphertext = self.encoder.encrypt(ciphertext)

    def reencode(self):
        '''Runs the encoder on the plaintext again'''

        self.formattedPlaintext = self.encoder.format(plaintext)
        self.ciphertext = self.encoder.encrypt(ciphertext)



class Encoder:
    # List used for all letters
    LETTERS = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def format(self, plaintext):
        return plaintext

    def encrypt(self, plaintext):
        raise NotImplementedError("Please implement encryption in child class of Encoder")

class AristocratEncoder(Encoder):
    def format(self, plaintext):
        return plaintext.lower()

    def encrypt(self,plaintext, keyword = None, K = 1):
        if keyword == None:
            key = random.sample(self.LETTERS, len(self.LETTERS))
        else:
            raise NotImplementedError("TODO: Implement keywords and K123 for monoalphabetic substitution")
        
        plaintextL = list(plaintext.upper())
        ciphertextL = plaintextL
        for i in range(len(ciphertextL)):
            for j in range(len(letters)):
                if plaintextL[i] == letters[j]:
                    ciphertextL[i] = key[j]
                    break
        return "".join(ciphertextL)

class PatristocratEncoder(Encoder):

    def __init__(self, seperator = " ", groupLength = 5):
        super().__init__()
        self.seperator = seperator
        self.groupLength = groupLength


    def format(self, plaintext):
        s = plaintext.lower()
        s = [ch for ch in s if ch.upper() in self.LETTERS] # Discard non-alpha characters
        
        if self.groupLength == 0:
            return ''.join(s)

        p = []
        for i in range(len(s)):
            if i > 0 and i % self.groupLength == 0:
                p.append(self.seperator)
            p.append(s[i])

        return ''.join(p)
    
    def encrypt(self, plaintext, keyword = None, K = 1):
        if keyword == None:
            key = random.sample(self.LETTERS, len(self.LETTERS))
        else:
            raise NotImplementedError("TODO: Implement keywords and K123 for monoalphabetic substitution")

        key = random.sample(self.LETTERS, len(self.LETTERS))
        plaintextL = list(self.format(plaintext).upper())
        ciphertextL = plaintextL
        for i in range(len(ciphertextL)):
            for j in range(len(letters)):
                if plaintextL[i] == letters[j]:
                    ciphertextL[i] = key[j]
                    break
        return "".join(ciphertextL)

class BaconianEncoder(Encoder):

    def format(self, plaintext):
        s = plaintext.lower()
        return ''.join(ch for ch in s if ch.upper() in self.LETTERS)

    def encrypt(self, plaintext, possibleAs = ['a'], possibleBs = ['b']):
        aVal = lambda: random.choice(possibleAs)
        bVal = lambda: random.choice(possibleBs)
        plaintextL = list(self.format(plaintext).upper())
        ciphertext = []
        for ch in plaintextL:
            x = self.LETTERS.index(ch)
            if x > 20:
                x -= 2
            elif x > 8:
                x-= 1

            x = format(x, '05b')
            y = []
            for i in range(len(x)):
                y.append(x[i].replace('0', aVal()).replace('1', bVal()))
            ciphertext.append(''.join(y))
        return ' '.join(ciphertext)
        # Such unreadable bodgecode...




if __name__ == "__main__":
    a = AristocratEncoder()
    p = PatristocratEncoder()
    print("\n" * 2 + p.format(input("")))
    print("\n" * 2 + p.encrypt(input("")))
