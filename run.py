from colorama import init, Fore, Back, Style
import os   # Operating System
import json
import datetime

# Start Colorama
init(autoreset=True)

MOODS = {
    "happy": (Back.WHITE, Fore.GREEN),
    "sad": (Back.BLUE, Fore.BLACK),
    "angry": (Back.BLACK, Fore.RED),
    "calm": (Back.GREEN, Fore.WHITE),
    "anxius": (Back.YELLOW, Fore.LIGHTRED_EX)
}

# Filename of the JSON file used to read and write mood data
MOOD_FILE = 'mood-history.json'


def read_file():
    """
    Read mood data from JSON file, return as dict.
    """
    if not os.path.exists(MOOD_FILE):
        with open(MOOD_FILE, 'w', encoding='utf-8') as file:
            json.dump({}, file)

# To read the file
# 'r' is for reading the file, encoding is for special characters on json file
# Read mood history from file with error handling
    try:
        with open(MOOD_FILE, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    return data


def ensure_history(data):
    """
    Ensure the data dict has a 'history' key.
    """
    if "history" not in data:
        data["history"] = []
    return data


def enter_mood():
    """
    Prompt user for mood until valid input is given.
    """
    while True:
        mood = input(
            Fore.CYAN + "How are you feeling? (happy, sad, angry, "
            "calm, anxius): ").strip().lower()
        if mood in MOODS:
            return mood
        print(Fore.RED + "Invalid mood. Please try again." + Style.RESET_ALL)

# To write to the file
# 'r' is for writing on the json file,
# ensure_ascii= is for using ascii characters on json file
with open(MOOD_FILE, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)


def enter_note():
    """
    Prompt the user if they want to add a note, 
    input shown in yellow text
    """
    while True:
        try:
            add_note = input(
                Fore.YELLOW + "Would you like to add a note? "
                "(yes/no): ").strip().lower()
            if add_note == "yes":
                return input(Fore.LIGHTWHITE_EX + "Enter your note: \n").strip()
            elif add_note == "no":
                return ""
            else:
                raise ValueError(
                    "Invalid input for note option. Expected 'yes' or 'no'.")
        except ValueError as e:
            print(Fore.RED + str(e) + Style.RESET_ALL)


def save_data(data):
    """Save data dict to JSON file."""
    with open(MOOD_FILE, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def show_history(data):
    """
    Display mood history with colors.
    """
    for entry in data.get("history", []):
        dt = entry.get("datetime", "Unknown date")
        m = entry.get("mood", "Unknown mood")
        note = entry.get("note", "")
        bg, fg = MOODS.get(m, (Back.RESET, Fore.RESET))
        print(bg + fg + f"{dt} - Mood: {m}" + Style.RESET_ALL)
        if note:
            print(Fore.LIGHTWHITE_EX + f"  Note: {note}" + Style.RESET_ALL)

# Get the current date and time formatted as a string
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create a new dictionary entry with the datetime and mood
entry = {"datetime": now, "mood": mood}

# If a note was provided (non-empty), add it to the entry dictionary
if note_text:
    entry["note"] = note_text

# If there is no "history" key in the data, initialize it as an empty list
if "history" not in data:
    data["history"] = []

# Get the current date and time in the format YYYY-MM-DD HH:MM:SS
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create a new entry containing the timestamp and the entered mood
entry = {"datetime": now, "mood": mood, "note": note_text}

# Append the new entry to the mood history list
data["history"].append(entry)

# Save the updated data back to the JSON file with UTF-8 encoding
try:
    with open(MOOD_FILE, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
except OSError as e:
    print(Fore.RED + f"Error saving mood data: {e}" + Style.RESET_ALL)

# Retrieve background and foreground colors for the mood
bg, fg = moods[mood]
# Print a confirmation message with the appropriate colors,
# then reset style
print(bg + fg + f"Logged mood '{mood}' at {now}" + Style.RESET_ALL)

# After completing mood and note recording
# Ask the user if they want to view the mood history data
show_history = input(
    Fore.MAGENTA + "Would you like to see the mood history data? "
    "(yes/no): "
    ).strip().lower()

# If the user agrees, iterate through the history list and
# display each entry with colors
# Showing date, mood, and note if available
            

# Prompt the user to confirm if they want to exit the program
exit_program = input(
    Fore.MAGENTA + "Would you like to exit the program? (yes/no): "
    ).strip().lower()

if exit_program == "yes":
    # If yes, print a goodbye message in green and terminate the program
    print(Fore.GREEN + "Goodbye! Have a nice day!" + Style.RESET_ALL)
    exit()
elif exit_program != "no":
    raise ValueError("Invalid input for exit option. Expected 'yes' or 'no'.")
else:
    print(Fore.CYAN + "Continuing the program..." + Style.RESET_ALL)


def main():
    data = read_file()
    data = ensure_history(data)


if __name__ == "__main__":
    main()