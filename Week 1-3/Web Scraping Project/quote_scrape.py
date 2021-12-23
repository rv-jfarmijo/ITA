# imports

from bs4 import BeautifulSoup
import requests
import random
from time import sleep


quote_list = []

url = 'https://quotes.toscrape.com'

def build_quote_source():
    # initial setup
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # define function for building list of quotes
    def build_quote_dict(quotes_raw):
        for quote in quotes_raw:
            text = quote.find('span').get_text()
            author = quote.find('small').get_text()
            bio = quote.find('a')['href']
            quote_list.append({'text': text, 'author': author, 'bio': bio})

    #loop for going through pages and grabbing quotes
    while soup.find(class_ = 'next'):
        quotes = soup.find_all(class_ = 'quote')
        build_quote_dict(quotes)
        next_url = url + soup.find(class_ = 'next').find('a')['href']
        response = requests.get(next_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        sleep(.1)

    #grab final quotes
    quotes = soup.find_all(class_ = 'quote')
    build_quote_dict(quotes)

def play_game():
    build_quote_source()
    remaining_guesses = 4
    random_quote = random.choice(quote_list)
    answer = random_quote['author']
    while guess.lower() != answer.lower() and remaining_guesses > 0:
            guess = input(f'Who said this quuote? Guesses remaining: {remaining_guesses} \n {random_quote['text']}')
            remaining_guesses -= 1
            if remaining_guesses ==3:
                res = requests.get(f'{url}{random_quote["bio"]}')
    print(guess, answer)


play_game()