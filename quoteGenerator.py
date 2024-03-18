import requests
import json
import signal, sys

QUOTE_FILE = "quoteList.json"
CURRENT_QUOTE_FILE = "currentQuote"

currentQuoteIndex = -1
quotes = []

def downloadQuotes():
    '''Download a bunch of quotes from zenquotes and write to QUOTE_FILE'''

    response = requests.get("https://zenquotes.io/api/quotes")
    response.raise_for_status()

    quote_data = response.text


    with open(QUOTE_FILE, 'w') as f:
        f.write(quote_data)

    global currentQuoteIndex

def readQuotes() -> list:
    '''Returns json from the downloaded quotes'''

    with open(QUOTE_FILE, 'r') as f:
        x = json.load(f)
    return x

def readCurrentQuoteIndex() -> int:
    with open(CURRENT_QUOTE_FILE, 'r') as f:
        x=int(f.read())
    return x

def writeCurrentQuoteIndex(x: int):
    with open(CURRENT_QUOTE_FILE, 'w') as f:
        f.write(str(x))

def getCurrentQuote() -> str:
    x = quotes[currentQuoteIndex]
    return x

def getNextQuote(lastIndex:int = -10) -> str:
    '''increments the index, then returns the quote (start with -1); if reached the last index, then download new ones
            lastIndex negative means download new ones if near end of list'''

    global currentQuoteIndex
    currentQuoteIndex += 1
    
    # Download new quotes if current quote is bad
    if lastIndex < 0:
        lastIndex += len(quotes)

    if currentQuoteIndex > lastIndex:
        try:
            downloadQuotes()
            currentQuoteIndex -= 1
        except requests.exceptions.RequestException as ex:
            print("New quotes could not be generated. Cache left: ", len(quotes) - currentQuoteIndex)

    # Now, all quotes should be safe. Get current quote
    x = getCurrentQuote()

    return x

def init():
    '''Sets up the generator- must run before using module'''

    global quotes
    global currentQuoteIndex

    quotes = readQuotes()
    currentQuoteIndex = readCurrentQuoteIndex()

def closeHandler(*args):
    '''automatically runs before quitting program- clean up stuff'''
    print("\nWriting quote index:", currentQuoteIndex)
    print("Bye!")
    writeCurrentQuoteIndex(currentQuoteIndex)
    sys.exit()

if __name__ == "__main__":
    init()
    print('i:', currentQuoteIndex)
    x = getNextQuote()
    print(x['q'])
    print("\t-- " + x['a'])
    print(sum(c.isalpha() for c in x['q']))
    close()

# todo: class Quote(quote, author="Unknown", characters=sum, etc.)

# try:
#     downloadQuotes()
# except requests.exceptions.RequestException as x: 
#     print("Exception: ", x) 



signal.signal(signal.SIGTERM, closeHandler)
signal.signal(signal.SIGINT, closeHandler)
