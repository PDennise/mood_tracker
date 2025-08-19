**MOOD TRACKER**

![test_1](images/test_1.png)

Simple Python Mood Logging Application

1. Description
2. Installation
3. Usage
4. Features
5. Error Handling
6. Deployment
7. Flowchart
8. Testing

---

## 1. Description
Mood Tracker is a simple Python application that allows users to record their mood along with optional notes and timestamps. 

Users can view their mood history with color-coded output for easy tracking of emotional patterns.

## 2. Installation
    1. Make sure you have Python 3.6+ installed.

    2. Clone the repository:

        git clone https://github.com/yourusername/mood-tracker.git

    3. Navigate into the project directory:

        cd mood-tracker

    4. Install dependencies using pip:

        pip install -r requirements.txt

 Note: After cloning the repository, run pip install -r requirements.txt to install all necessary dependencies before running the program.

## 3. Usage
Run the program using:

    python run.py

Follow the prompts to:

    Enter your current mood (happy, sad, angry, calm, anxius)

    Optionally add a note
    
    View mood history
    
    Exit the program

![test_1](images/test_1.png)
![test_2](images/test_2.png)
![test_3](images/test_3.png)

## 4. Features
- Mood input validation with user-friendly prompts
- Optional note addition for detailed mood tracking
- Timestamped mood entries stored in a JSON file
- Color-coded mood history display (Colorama Library)
- Error handling for file operations and invalid inputs

## 5. Error Handling
- Handles missing or corrupted mood history files by creating/resetting them
- Validates all user inputs, prompting the user again on invalid responses
- Catches file write errors and informs the user
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


## 6. Deployment
This project can be deployed easily on platforms like Heroku.

    Steps include:

    - Set up a Python environment

    - Push the project repository to Heroku

    - Use a requirements.txt file to manage dependencies

    - Configure Procfile if needed

## 7. Flowchart

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
6. **End Program:** The program terminates. 
    - If Yes, the program continues and asks moods again.
    - If No, the program ends.

This flowchart provides a visual guide to the program's logic and user input handling.

If you would like to see the image of flowchart:
![Flowchart](images/flowchart-mood_tracker.png)

## 8. Testing

I have manually tested this project by doing the following:

- Passed the code through a PEP8 linter and confirmed there are no problems
- Tested in my local terminal and on my Heroku terminal

**Validator Testing**
- PEP8 
    No errors were returned from PEP8online.com