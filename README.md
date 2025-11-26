<div align="center">
  <h4> MOOD TRACKER </h4>
</div>

![starting](/images/starting.png)

[Mood Tracker](https://mood-tracker-bc9acc8bde14.herokuapp.com/) is a simple yet powerful Python application designed to help users record and explore their emotions over time. Instead of just logging moods, it allows users to capture the subtle context of each feeling through optional notes and timestamps. The core feature is a color-coded interactive history, which makes it easy to visually track emotional patterns and identify trends.

The goal of Mood Tracker is not merely to store data, but to create awareness and insight into one’s emotional landscape, turning daily reflections into a meaningful habit. A minimal and clear interface has been maintained, presenting only the necessary prompts and outputs to keep the focus on the moods and notes.

By combining intuitive input validation, optional note-taking, and visual feedback through color-coded output, Mood Tracker offers a coherent, interactive experience that encourages mindful self-reflection, rather than just acting as a static log of feelings.

## Table of Contents
1. [Installation](#1-installation)
2. [Usage](#2-usage)
3. [Features](#3-features)
4. [Error Handling](#4-error-handling)
5. [Deployment](#5-deployment)
6. [Flowchart](#6-flowchart)
7. [Testing](#7-testing)
8. [Bug Fixes](£8-bug-fixes)
9. [Libraries](#9-libraries)
10. [Credits](#10-credits)

---

## 1. Installation

Follow these steps to set up Mood Tracker on your local machine:

1. Install Python 3.6+
    
    Make sure Python 3.6 or higher is installed on your system. You can check with:
    
        python3 --version

2. Clone the repository:

        git clone https://github.com/yourusername/mood-tracker.git

3. Navigate into the project directory:

        cd mood-tracker
    
4. Set up a virtual environment (optional but recommended)

        python3 -m venv venv
        source venv/bin/activate  # Mac/Linux
        venv\Scripts\activate     # Windows

5. Install dependencies using pip:

        pip install -r requirements.txt

6. Run the program:

        python3 run.py

---

## 2. Usage

Run the program using:

    python run.py

Follow the prompts to:

   - Enter your current mood:

        Choose from: happy, sad, angry, calm, anxious.

   - Optionally add a note:

        You can write a short note about your mood to capture context or details.
    
   - View mood history:

        The program will ask if you want to see past entries, showing color-coded output.
    
   - Exit the program:

        You can exit at any time. If you choose to continue, the program will loop back to the mood input.

💡 Note: All moods are timestamped and saved in mood-history.json. New entries are appended at the top of the history for easy review.

----

## 3. Features

- **Mood Input Validation**

    Only accepts predefined moods (happy, sad, angry, calm, anxious) to ensure accurate data.

- **Optional Note Addition**

    Users can add context or details for each mood entry.

- **Timestamped Entries**

    Each mood is saved with a date and time for accurate tracking.

- **Color-coded Mood History** 

    Easily identify mood patterns at a glance with visually distinct colors (using Colorama).

- **Interactive History Display** 

    Users can view past entries on demand, with the newest entries shown first.

- **Robust Error Handling** 

    Handles missing or corrupted JSON files, invalid inputs, and file write errors gracefully.

- **Safe Program Exit** 

    Replaces quit() with exit_program() for controlled termination.


💡 Note: All features are designed to provide a minimal, focused, and user-friendly experience, keeping the attention on moods and notes rather than extra clutter.

----

## 4. Error Handling

Mood Tracker includes robust error handling to ensure smooth operation:

- **Missing or Corrupted JSON File**

        - If mood-history.json does not exist or is corrupted, the program automatically creates a new, empty file.
        
        - This prevents crashes and ensures the user can continue logging moods.
- **Invalid Mood Input**

        - Users are prompted until a valid mood is entered.

        - Invalid entries (typos, unsupported moods) trigger clear, colored error messages.
- **Invalid Note Input**

        - Only accepts yes or no when asking whether to add a note.

        - Prompts again on invalid input, preventing program interruption.
- **File Write Errors**

        - Catches exceptions during saving and informs the user if data cannot be written.
- **Safe Program Exit**

        - Replaces quit() with exit_program() function.
        
        - Confirms with the user before terminating the program to avoid accidental exits.


Example snippets:
------------------------------------------------------------------------------------------
#### Read mood history from file with error handling

```python
 try:
        with open(MOOD_FILE, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    return data
```

#### Save mood data to file with error handling
```python
 def ask_history(data):
    """Prompt user to view mood history with error handling"""
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
```

----

## 5. Deployment
This project can be deployed easily on platforms like Heroku.

Steps for Heroku deployment:

1. Create a Heroku app:
    
    heroku create your-app-name

2. Push the repository to Heroku:

    git push heroku main

3. Ensure requirements.txt and Procfile are included for dependencies and entry point.

💡 Note: Once deployed, you can access the live app via https://your-app-name.herokuapp.com/.

----

## 6. Flowchart

The flowchart illustrates the user interaction flow of the Mood Tracker application:

1. **Start Program:** The program begins execution.
2. **Mood Selection:** The user is prompted to select their current mood from predefined options: Happy, Sad, Angry, Calm, or Anxious.
3. **Add Note Decision:** The user is asked whether they want to add a note related to their mood.
    - If Yes, the user writes a note.
    - If No, the program skips to saving the mood.
4. **Save Mood:** The mood (and note if provided) is saved to a file.
5. **View Mood History Decision:** The user is asked if they want to view their past mood entries.
    - If Yes, the program displays the mood history.
    - If No, the program ends.
6. **Repeat or End Program:** The user is asked whether to continue logging moods. 
    - If Yes, the program loops back to **Mood Selection**.
    - If No, the program terminates.

This flowchart provides a visual guide to the program's logic and user input handling.

If you would like to see the image of flowchart:
![Flowchart](images/flowchart-mood_tracker.png)

----

## 7. Testing

The application has been manually tested as follows:

1. Terminal tests (local):
    - Ran the program in the local terminal
    - Entered valid and invalid moods
    - Added notes and checked JSON file updates
    - Verified color-coded output and history display

2. PEP8 compliance:
    - Ran code through a PEP8 validator
    - Fixed all warnings (line length, trailing whitespaces, indentation)
    - Confirmed no remaining style issues

3. JSON file creation:
    - Deleted mood-history.json
    - Ran the program
    - Verified that the file was automatically created and new entries appended correctly

4. Heroku deployment test:
    - Deployed to Heroku
    - Ran program in the Heroku terminal
    - Verified that mood input, notes, and history display work as expected

5. Screenshots
    - Screenshots of valid and invalid inputs can be found in the images:
    
    [local test valid yes](/images/terminal-valid-test-yes.png)
    [local test valid no](/images/terminal-test-no.png)
    [local test invalid](/images/terminal-test-invalid.png)
    [pep8 test](/images/pep8-test.png)
    [pep8 test 2](/images/pep8-test-2.png)
    [pep8 test 3](/images/pep8-test-3.png)
    [heroku valid yes](/images/heroku-valid-yes.png)
    [heroku valid no](/images/heroku-valid-no.png)
    [heroku invalid](/images/heroku-invalid.png)
    [no.json](/images/no-json.png)
    [jason file](/images/json-file.png)
----

## 8. Bug Fixes

During development, several issues were identified and resolved to improve stability, usability, and code quality.

1. Incorrect mood spelling

    Bug: Mood option "anxius" was misspelled.

    Fix: Corrected to "anxious" in all validation checks.


2. Program terminated using quit()

    Bug: Using quit() can behave inconsistently and is not recommended in production code.

    Fix: Replaced with a custom exit_program() function for a controlled and safe exit.


3. Mood history order incorrect

    Bug: New entries appeared at the bottom of the list.

    Fix: History is now reversed, showing the newest mood at the top.


4. PEP8 style violations

    Bug: Long lines, trailing whitespaces, and indentation issues detected via PEP8 linter.

    Fix: All formatting errors were corrected; code now passes PEP8 validation.


5. JSON file handling issues

    Bug: When mood-history.json was missing or corrupted, the program would crash.

    Fix: Added error handling to automatically create or reset the JSON file.
    

6. Input validation feedback

    Bug: Invalid mood or history inputs did not show helpful error messages.

    Fix: Added descriptive error messages and looped prompts using try/except.

