from colorama import init, Fore, Back, Style
import os   # Operating System
import json
import datetime

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

if not os.path.exists(MOOD_FILE):
    with open(MOOD_FILE, 'w', encoding='utf-8') as file:
        json.dump({}, file)

# To read the file
# 'r' is for reading the file, encoding is for special characters on json file
with open(MOOD_FILE, 'r', encoding='utf-8') as file:
    data = json.load(file)

# To write to the file
# 'r' is for writing on the json file,
# ensure_ascii= is for using ascii characters on json file
with open(MOOD_FILE, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

# Get user input for mood
mood = input(Fore.CYAN + "How are you feeling? (happy, sad, angry, calm, anxius): ").strip().lower()

# Check if the entered mood is in the predefined moods dictionary
if mood in moods:
    # If there is no "history" key in the data, initialize it as an empty list
    if "history" not in data:
        data["history"] = []

    # Get the current date and time in the format YYYY-MM-DD HH:MM:SS
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create a new entry containing the timestamp and the entered mood
    entry = {"datetime": now, "mood": mood}

    # Append the new entry to the mood history list
    data["history"].append(entry)

    # Save the updated data back to the JSON file with UTF-8 encoding
    with open(MOOD_FILE, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    # Retrieve background and foreground colors for the mood
    bg, fg = moods[mood]
    # Print a confirmation message with the appropriate colors, then reset style
    print(bg + fg + f"Logged mood '{mood}' at {now}" + Style.RESET_ALL)
else:
    # Print an error message in red if the entered mood is invalid
    print(Fore.RED + "Invalid mood entered." + Style.RESET_ALL)