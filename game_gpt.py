import requests
from bs4 import BeautifulSoup

def get_english_word():
    url = 'https://randomword.com/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Will raise an HTTPError for bad responses
        soup = BeautifulSoup(response.content, 'html.parser')
        english_word = soup.find('div', id='random_word').text.strip()
        word_definition = soup.find('div', id='random_word_definition').text.strip()
        return {
            'english_word': english_word,
            'word_definition': word_definition}
    except requests.RequestException as e:
        print(f'An error occurred: {e}')
        return None

def word_game():
    print("Welcome to the word game!")

    while True:
        word_dict = get_english_word()
        if word_dict is None:
            print("Could not retrieve a word. Exiting the game.")
            break

        word = word_dict.get('english_word')
        word_definition = word_dict.get('word_definition')

        print(f"Word definition: {word_definition}")
        user_guess = input("What is the word?: ")

        if user_guess.lower() == word.lower():
            print("Correct!")
        else:
            print(f"Incorrect! The word was - {word}")

        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    word_game()
