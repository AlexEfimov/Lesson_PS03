from bs4 import BeautifulSoup
from googletrans import Translator

import requests


def get_english_word():
    url = 'https://randomword.com/'
    translator = Translator()
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        english_words = soup.find('div', id='random_word').text.strip()
        word_definition = soup.find('div', id='random_word_definition').text.strip()
        russian_words = translator.translate(english_words, dest='ru').text.strip()
        russian_definition = translator.translate(word_definition, dest='ru').text.strip()
        return {
            'russian_words': russian_words,
            'russian_definition': russian_definition}
    except:
        print('Произошла ошибка')

def word_game():
    print("Добро пожаловать в игру")

    while True:
        word_dict = get_english_word()
        word = word_dict.get('russian_words')
        word_definition = word_dict.get('russian_definition')

        print(f"Значение слова: {word_definition}")
        user = input ("Что это за слово?: ")
        if user in word:
            print("все верно")
        else:
            print(f"Ответ неверный! Было загадано слово - {word}")

        play_again = input("Хотите сыграть еще раз? y/n")
        if play_again != 'y':
            print("Спасибо за игру")
            break

word_game()


