#!/usr/bin/python3
import txtEncoder
try:
    import requests
except ModuleNotFoundError:
    print('Please install the "requests" library.\n Run the following code:\n\n\tpython3 -m pip install requests')
    exit(1)

def getQuote():
    response = requests.get("https://zenquotes.io/api/random")
    response.raise_for_status()

    quote_data = response.json()
    quote = quote_data[0]['q']
    author = quote_data[0]['a']
    return quote, author

while True:
    q = getQuote()
    print(q[1])
    print("\t" + txtEncoder.aristocrat(q[0]))
    input()
    print(q[0]+"\n\n\n\n")

