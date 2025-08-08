from colorama import init, Fore, Back, Style
import os   # Operating System
import json

# Start Colorama
init(autoreset=True)

moods = {
    "happy": (Back.WHITE, Fore.GREEN),
    "sad": (Back.BLUE, Fore.BLACK),
    "angry": (Back.BLACK, Fore.RED),
    "calm": (Back.GREEN, Fore.WHITE),
    "anxius": (Back.YELLOW, Fore.LIGHTRED_EX)
}

# Filename of the JSON file used to read and write mood data
MOOD_FILE = 'mood-history.json'

# Reading the file
# 'r' is for reading the file, encoding is for special caracters on json file
with open('mood-history.json', 'r', encoding='utf-8') as file:
    data = json.load(file)