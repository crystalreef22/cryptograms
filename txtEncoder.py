import random



class Encoded:
    def __init__(self, plaintext, encoder):
        self.plaintext = plaintext
        self.encoder = encoder
        self.formattedPlaintext = self.encoder.format(plaintext)
        self.ciphertext = self.encoder.encrypt(plaintext)

    def reencode(self):
        '''Runs the encoder on the plaintext again'''

        self.formattedPlaintext = self.encoder.format(self.plaintext)
        self.ciphertext = self.encoder.encrypt(self.plaintext)



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

    def encrypt(self,plaintext, key = None, keyType = 'K1'):
        if key == None:
            key = random.sample(self.LETTERS, len(self.LETTERS))
        else:
            if keyType == 'K1':
                pass
            else:
                raise NotImplementedError("Only K1 is supported at this moment")
        
        plaintextL = list(plaintext.upper())
        ciphertextL = plaintextL
        for i in range(len(ciphertextL)):
            for j in range(len(self.LETTERS)):
                if plaintextL[i] == self.LETTERS[j]:
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
    
    def encrypt(self, plaintext, key = None, keyType = "K1"):
        if key == None:
            key = random.sample(self.LETTERS, len(self.LETTERS))
        else:
            if keyType == 'K1':
                pass
            else:
                raise NotImplementedError("Only K1 is supported at this moment")

        key = random.sample(self.LETTERS, len(self.LETTERS))
        plaintextL = list(self.format(plaintext).upper())
        ciphertextL = plaintextL
        for i in range(len(ciphertextL)):
            for j in range(len(self.LETTERS)):
                if plaintextL[i] == self.LETTERS[j]:
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
            x = self.LETTERS.index(ch) # letters to numbers
            if x > 20: # u = v; i = j
                x -= 2
            elif x > 8:
                x-= 1

            x = format(x, '05b') # Convert all letters to binary
            y = []
            for i in range(len(x)):
                y.append(x[i].replace('0', aVal()).replace('1', bVal())) # replace 0 with random a and 1 with random b
            ciphertext.append(''.join(y))
        return ' '.join(ciphertext)
        # Such unreadable bodgecode...


class keyWordGenerator:
    # List used for all letters
    LETTERS = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def __init__(self, wordListFile):
        with open(wordListFile, 'r') as f:
            self.wordList = f.read().splitlines()

        self.current = random.choice(self.wordList)

    def nextWord(self):
        return random.choice(self.wordList)

    def next(self):
        self.current = "A"*30
        while len(self.current) > 26:
            self.current = random.choice(self.wordList).upper()

        key = list(self.LETTERS)
        currentWord = []
        for ch in self.current:
            try:
                del key[key.index(ch)]
            except ValueError:
                pass
            else:
                currentWord.append(ch)
        
        insertionIndex = random.randint(0, len(key) - 1)
        key[insertionIndex:insertionIndex] = currentWord
        return key
    


if __name__ == "__main__":
    a = AristocratEncoder()
    p = PatristocratEncoder()
    print("\n" * 2 + p.format(input("")))
    print("\n" * 2 + p.encrypt(input("")))
