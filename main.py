import random
import json
from colorama import Fore, Style, init
import pyfiglet

# Initialize colorama
init()

# Load words from JSON file
with open('words.json', 'r') as file:
    data = json.load(file)
    words = data['words']

# Display welcome message in ASCII art
ascii_banner = pyfiglet.figlet_format("Word Guessing Game")
print(Fore.CYAN + ascii_banner + Style.RESET_ALL)

# Select a random word
word = random.choice(words)
guessed_letters = set()
max_attempts = 6
attempts = 0

# Display the current progress
def display_progress():
    progress = [letter if letter in guessed_letters else "_" for letter in word]
    print(" ".join(progress))

print(Fore.GREEN + "Welcome to the Word Guessing Game!" + Style.RESET_ALL)
display_progress()

# Main game loop
while attempts < max_attempts:
    guess = input(Fore.YELLOW + "Guess a letter: " + Style.RESET_ALL).lower()
    
    if guess in guessed_letters:
        print(Fore.RED + "You've already guessed that letter." + Style.RESET_ALL)
    elif guess in word:
        guessed_letters.add(guess)
        print(Fore.GREEN + "Good guess!" + Style.RESET_ALL)
    else:
        attempts += 1
        print(Fore.RED + "Incorrect guess. Attempts left:" + Style.RESET_ALL, max_attempts - attempts)
    
    display_progress()
    
    if all(letter in guessed_letters for letter in word):
        print(Fore.GREEN + "Congratulations! You've guessed the word:" + Style.RESET_ALL, word)
        break
else:
    print(Fore.RED + "Sorry, you've run out of attempts. The word was:" + Style.RESET_ALL, word)
