import json


try:
    import requests
except ImportError:
    print("The requests module is not installed. Run:\n\n\tpython3 -m pip install requests\n\nand restart the program")
    exit

quotes = []

def fetchQuotes():
    global quotes
    global quoteI
    if not quotes:
        try:
            with open("quotes.json", "r") as file:
                quotes = json.load(file)
        except 
    
    if quoteI < len(quotes):
        return quotes[quoteI]
        quoteI += 1
    else:
        # Make the API request to fetch quotes
        response = requests.get("https://zenquotes.io/api/quotes")
        response.raise_for_status()        
        # Parse the JSON response
        quotes = response.json()

        # Save quotes to a file
        with open("quotes.json", 'w') as file:
            json.dump(quotes, file, indent=2)

        print(f"New quotes downloaded!")


# except requests.RequestException

def retrieveLastIndex():
    try:
        with open("index.txt", 'r') as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

def writeIndex(index):
    with open("index.txt", 'w') as file:
        file.write(str(index))


quoteI = retrieveLastIndex()
