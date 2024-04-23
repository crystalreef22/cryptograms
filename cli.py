#!/Users/etn/Programming/py-venv/bin/python3
import signal, sys
import time
import quoteGenerator as qg
import txtEncoder as te


qg.init() #Ideally, I should make this a class

aristocrat = te.AristocratEncoder()
kg = te.keyWordGenerator("storage/commonWordList.txt")

while True:
    q = qg.getNextQuote()
    plaintext = q['q']
    author = q['a']
    del q

    key = kg.next()
    ciphertext = aristocrat.encrypt(plaintext)

    print(ciphertext)
    print("\t--", author)
    input("\n")
    print(plaintext)
    print("Key:", kg.current)
    print('\n'*4)
