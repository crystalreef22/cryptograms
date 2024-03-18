#!/Users/etn/Programming/py-venv/bin/python3
import signal, sys
import time
import quoteGenerator as qg
import txtEncoder


qg.init() #Ideally, I should make this a class

while True:
    q = qg.getNextQuote()
    plaintext = q['q']
    author = q['a']
    del q

    ciphertext = txtEncoder.aristocrat(plaintext)

    print(ciphertext)
    print("\t--", author)
    input("\n")
    print(plaintext)
    print('\n'*4)
