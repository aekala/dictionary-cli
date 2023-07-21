import requests
from string import Template

DICTIONARY_URL = Template("https://www.dictionaryapi.com/api/v3/references/collegiate/json/$word?key=$key")
THESAURUS_URL = Template("https://www.dictionaryapi.com/api/v3/references/thesaurus/json/$word?key=$key")
ERROR_MSG = Template("Error: $error")
SEPARATOR = "------------"
DICTIONARY_API_KEY = "" #Enter dictionary API key from Merriam-Webster's developer center (https://dictionaryapi.com/)
THESAURAUS_API_KEY = "" #Enter thesaurus API key from Merriam-Webster's developer center (https://dictionaryapi.com/)

def handle_error(err):
    print(ERROR_MSG.substitute(error = err))
    print(SEPARATOR)

while True:

    word = input("Enter a word to look up: ")
    definitionRes = requests.get(DICTIONARY_URL.substitute(word = word, key = DICTIONARY_API_KEY)).json()
    try:
        definitions = definitionRes[0]["shortdef"]
        print("\nDefinitions of " + word + ":")
        for d in definitions:
            print(d)
        print()
    except Exception as err:
        handle_error(err)
        continue

    try: 
        thesaurusRes = requests.get(THESAURUS_URL.substitute(word = word, key = THESAURAUS_API_KEY)).json()
        synonyms = thesaurusRes[0]["meta"]["syns"]
        print("Synonyms for " + word + ":")
        for s in synonyms[0]:
            print(s)
        print("\n" + SEPARATOR)
    except Exception as err:
        handle_error(err)
        continue







