# 13CSI Math Game
## Research
Strengthen - Easyish
Stetch - Hard


## Todo:
- Accelerators for all buttons 
  - https://stackoverflow.com/questions/42797709/tkinter-menu-bindings-and-accelerators
- Menu bar popups ✔️
- Error explaining for text inputs e.g. name ✔️
- Question system
    - JSON file for dynamically loading quesitons
    E.g. easy, med, hard from one file ✔️
    - Support for Multi choice questions?
    - https://www.w3schools.com/python/python_json.asp
- Excesive Documentation
- Radial Gradient bgs to draw attention
- Consistent fonts / colors / branding
  - use ttk for pretteirness
- Interface for making different questions
  - Done via help menu
  - Change question set via help menu
- LaTeX support for math equations?
  - Similar effect with matplotlib https://www.tutorialspoint.com/how-to-display-latex-in-real-time-in-a-text-box-in-tkinter

## Files
### data.json
Formated question data with difficulties implemented

### icon.gif / .ico
Image for the GUI's interface

### stolen.py
ChatGPT generated code for use as refernce for making json files. No code has been copied line for line from said file.

### ...quiz_v1.py
Fully error checked name input as well as setup for the rest of the program
#### Known Bugs:
- Menu bar is non functional
- relx results in non-centred elements
- Code is unoptimized
- Logo doesn't work cross platform due to discrepencies in CWD. (Returns ./../ on windows vs. ./ on unix)

### ...quiz_v2.py
Verbose documentation for end user  
*N.b.* Tutorial is unfinished, and whole system is untested on windows

### ...quiz_v3.py
Get the data from a json file, seperates into the difficulties.  
Fixed an issue where the boxes weren't aligned, used relx=0.45, relwidth=0.1

### ...quiz_v4.py
Lets the user choose their level, calls the question into a dictionary called ```question_set```

### ...quiz_v5.py
Shows and iterates through the questions. Goes blank after all questions have been asked.
#### Known Bugs:
- Throws Index error after questions
- Doesnt keep track of score
### ...quiz_v6.py
Results screen. question_set[current_question][2] holds the user input if its wrong. Allows the user to start again from the start or quit
#### Known Bugs:
Upon restarting, pressing next will show result screen.
### ...quiz_v7.py
Coversion to ttk + proper feedback for answers ~ln 125
#### Known Bugs:
Uses ttk but none of the features, feedback is unaligned.
### ...quiz_v8.py
JSON maker + choose alternate question set. When choosing new questions, checks for the json being valid, if it isnt, revert.
### json_maker.py
In house solution to dynamically creating question lists for my program. Made to be dynamic with a GUI, not made to be user friendly as it is intented as a developer tool. Saves to the dir the program is ran from.
json_maker works as intended, Could be slightly more clear, but fine enough for me. 
#### Known Bugs:
After creating a file from the dropdown, the menubar is bugged (possibly a compiler issue)