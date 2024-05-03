# 13CSI Math Game
https://github.com/AltraMage/3.7_maths_quiz
## Research
Strengthen - Easyish  
Stretch - Hard


## Todo:
- Accelerators for all buttons 
  - https://stackoverflow.com/questions/42797709/tkinter-menu-bindings-and-accelerators
- Menu bar popups ✔️
- Error explaining for text inputs e.g. name ✔️
- Question system
    - JSON file for dynamically loading questions
    E.g. easy, med, hard from one file ✔️
    - Support for Multichoice questions?
    - https://www.w3schools.com/python/python_json.asp
- Excesive Documentation
- Radial Gradient bgs to draw attention
- Consistent fonts/colors / branding
  - use ttk for pretteirness ✔️
- Interface for making different questions ✔️
  - Done via the help menu ✔️
  - Change the question set via the help menu ✔️
- LaTeX support for math equations?
  - Similar effect with matplotlib https://www.tutorialspoint.com/how-to-display-latex-in-real-time-in-a-text-box-in-tkinter

## Files
### data.json
Formated question data with difficulties implemented

### icon.gif / .ico
Image for the GUI's interface

### stolen.py
ChatGPT generated code for use as a reference for making JSON files. No code has been copied line for line from said file.

### ...quiz_v1.py
Fully error-checked name input as well as set up for the rest of the program
#### Known Bugs:
- Menu bar is nonfunctional
- relx results in non-centred elements
- Code is unoptimized
- The logo doesn't work cross-platform due to discrepancies in CWD. (Returns ./../ on windows vs. ./ on UNIX)

### ...quiz_v2.py
Verbose documentation for the end user  
*N.b.* The Tutorial is unfinished, and the whole system is untested on Windows

### ...quiz_v3.py
Get the data from a JSON file, and separate it into the difficulties.  
Fixed an issue where the boxes weren't aligned, used relx=0.45, relwidth=0.1

### ...quiz_v4.py
Lets the user choose their level, and calls the question into a dictionary called ```question_set```

### ...quiz_v5.py
Shows and iterates through the questions. Goes blank after all questions have been asked.
#### Known Bugs:
- Throws Index error after questions
- Doesn't keep track of the score
### ...quiz_v6.py
Results screen. question_set[current_question][2] holds the user input if its wrong. Allows the user to start again from the start or quit
#### Known Bugs:
Upon restarting, pressing next will show the result screen.
### ...quiz_v7.py
Conversion to ttk + proper feedback for answers ~ln 125
#### Known Bugs:
Uses ttk but none of the features, and feedback are unaligned.
### ...quiz_v8.py
JSON maker + choose alternate question set. When choosing new questions, check for the JSON being valid, if it isn't, revert.
#### Known Bugs:
After creating a file from the dropdown, the menubar is bugged (possibly a compiler issue)
### json_maker.py
In-house solution to dynamically creating question lists for my program. Made to be dynamic with a GUI, not made to be user friendly as it is intended as a developer tool. Saves to the dir the program is ran from.
json_maker works as intended, Could be slightly more clear, but good enough for me.
### ...quiz_v9.py
Pep8 approved. More theming???? *N.b.* MacOS auto centers text, and uses a dark theme. Gonna be a pain to make consistent.
Did A & M testing on this version. Technically the version to submit, but yeah.  
Uses rdbende's azure theme for cross platformisms, havent actually checked windows though. 
Some minor refactoring as well. (We ❤️ Spagetti code!) 
#### Known bugs:
- There is now a cut off to the amount of levels. 
- azure.tcl, and ./theme/* have to be included in the download, (Watch this space(filestealer.py))
- A lot is slightly off centre due to python things.
### ...quiz_v10.py
Tried adding a font via `option_add()`, doesnt work. 
Added light / dark mode switcher
Added verbose error catchingc to serveral situations
### json_maker_ux.py
Successor to json_maker. Verbosifying errors