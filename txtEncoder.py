import random

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def aristocrat(plaintext):

    key = random.sample(letters, len(letters))
    plaintextL = list(plaintext.upper())
    ciphertextL = plaintextL
    for i in range(len(ciphertextL)):
        for j in range(len(letters)):
            if plaintextL[i] == letters[j]:
                ciphertextL[i] = key[j]
                break
    return "".join(ciphertextL)



if __name__ == "__main__":
    print("\n" * 5 + aristocrat(input("")))
