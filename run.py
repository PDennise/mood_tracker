from colorama import init, Fore, Back, Style
import os   # Operating System
import json
import datetime
import sys

# Start Colorama
init(autoreset=True)

MOODS = {
    "happy": (Back.WHITE, Fore.GREEN),
    "sad": (Back.BLUE, Fore.BLACK),
    "angry": (Back.BLACK, Fore.RED),
    "calm": (Back.GREEN, Fore.WHITE),
    "anxious": (Back.YELLOW, Fore.LIGHTRED_EX)
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
            "calm, anxious): ").strip().lower()
        if mood in MOODS:
            return mood
        print(Fore.RED + "Invalid mood. Please try again." + Style.RESET_ALL)


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
                return input(
                    Fore.LIGHTWHITE_EX + "Enter your note: \n").strip()
            elif add_note == "no":
                return ""
            else:
                raise ValueError(
                    "Invalid input for note option. Expected 'yes' or 'no'.")
        except ValueError as e:
            print(Fore.RED + str(e) + Style.RESET_ALL)


def save_data(data):
    """
    Save data dict to JSON file. "w" for writing on the file,
    encoding is for special characters on json file
    """
    with open(MOOD_FILE, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def show_history(data):
    """
    Display mood history with colors, sorted by datetime ascending.
    """
    history_sorted = sorted(
        data.get("history", []),
        key=lambda x: x.get("datetime", ""),
        reverse=True  # <- Newest entries on top
    )

    for entry in history_sorted:
        dt = entry.get("datetime", "Unknown date")
        m = entry.get("mood", "Unknown mood")
        note = entry.get("note", "")
        bg, fg = MOODS.get(m, (Back.RESET, Fore.RESET))
        print(bg + fg + f"{dt} - Mood: {m}" + Style.RESET_ALL)
        if note:
            print(Fore.LIGHTWHITE_EX + f"  Note: {note}" + Style.RESET_ALL)


def ask_history(data):
    # Ask to show history
    while True:
        try:
            show = input(
                Fore.MAGENTA + "Would you like to see the mood history? "
                "(yes/no): "
                ).strip().lower()
            if show == "yes":
                show_history(data)
                break
            elif show == "no":
                return ""
            else:
                raise ValueError(
                    "Invalid input for history option. Expected "
                    "'yes' or 'no'.")
        except ValueError as e:
            print(Fore.RED + str(e) + Style.RESET_ALL)


def save_note(data, note_text, mood):
    """
    Get the current date and time formatted as a string,
    Create a new dictionary entry with the datetime and mood,
    If a note was provided (non-empty), add it to the entry dictionary
    """
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = {"datetime": now, "mood": mood}

    if note_text:
        entry["note"] = note_text

    # Append the new entry to the mood history list
    data["history"].append(entry)
    save_data(data)

    # Show confirmation
    bg, fg = MOODS[mood]
    # Print a confirmation message with the appropriate colors,
    # then reset style
    print(bg + fg + f"Logged mood '{mood}' at {now}" + Style.RESET_ALL)


def exit_program():
    """
    Prompt the user to confirm if they want to exit the program
    """
    while True:
        try:
            # Ask to exit
            user_input = input(
                Fore.MAGENTA + "Would you like to exit the program? (yes/no): "
                ).strip().lower()

            if user_input == "yes":
                # User chose to exit, print goodbye message and terminate program
                print(
                    Fore.GREEN + "Goodbye! Have a nice day!" + Style.RESET_ALL)
                sys.exit() # Safe exit from the program

            elif user_input == "no":
                print(
                    Fore.CYAN + "Continuing the program..." + Style.RESET_ALL)
                return  # Exit the loop and continue program

            else:
                 # Input was invalid, raise an error to be caught below
                raise ValueError(
                    "Invalid input for exit option. Expected 'yes' or 'no'.")

        except ValueError as e:
            # Print the error message in red if input is invalid
            print(Fore.RED + str(e) + Style.RESET_ALL)


def main():
    data = read_file()
    data = ensure_history(data)

    while True:  # Main loop: keeps the program running until user chooses to exit
        # Ask the user about their current mood
        mood = enter_mood()
        # Ask if they want to add a note
        note_text = enter_note()
        # Ask if they want to see the mood history
        ask_history(data)
        # Save the mood and optional note
        save_note(data, note_text, mood)
        # Exit program prompt
        # If user selects "no", the loop continues (program restarts)
        # If user selects "yes", sys.exit() terminates the program
        exit_program()


if __name__ == "__main__":
    main()
