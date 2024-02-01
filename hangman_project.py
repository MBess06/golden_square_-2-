#Hangman_game_project
import random

def Players_name():
    name = input("Players name: ")
    print(f"Welcome, {name}!")

def choose_word(words):
    words = ["raspberry", "garlic bread", "kangeroo", "octopus"]
    chosen_word = random.choice(words)
    return chosen_word

def guessing_letters():
    pass