# metroScheduler
This project supports all the metro lines in Delhi and Delhi NCR region!!!
You can check metro timings, fare calculations, a metro map displayer and quick metro journey planner.

---


### How to use:

Project structure :
```
.
├── metro_data.txt
├── metro_simulator.py
└── README.md
```

Run `python3 metro_simulator.py` in your terminal

I have added proper doc strings for all functions 


and also added comments and full detail next to modules

### Inbuilt modules used:
- time # using this to delay, animate, reset, take current time
- os # using this to clear the screen after each load to make it look like an animation
- shutil # this is another amazing module i am using to center text using terminal size to make app responsive
- re # using this to fix the centering issue by removing ascii escape codes from text while centering using .center
- sys # using this for checking os type to make this cross platform

---

### Data flow ->

Opens data, reads it using readlines -> gets 2x nested list -> (then when required can loop through list and split each nested list by ',' to get 3x nested list with proper data)

---

### Miscellaneous ->

defined a colors dictionary to color inside the terminal

defined a function named input_key() to take inputs for all 3 platforms windows, linux, macos

defined suggestion function to suggest metro station names when typing input

### Functional Flow -> 

All the functions have their own doc strings for detailed explanation `print(fn_name.__doc__)' 

first i clear the screen twice for empty canvas then run an introduction function, then another clear screenfn then a loading animation with 3 dots then i proceed to print the entire menu

menu has 4 options 1. graph 2. timings 3. journey planner 4. info 5. exit

i did implement proper edge case handling using try except blocks.


### Assumptions -> 

Taking metro speed as 33km/hr (accounting for stops and minor delays too)
But metro speed for ONLY orange line is 100kmph

### Data online -> 

I got the data from Kaggle but had to modify most of it, changed the lattitude, longitude of almost all metro lines except magenta and blue, added few more columns for time.

```
ID (Station ID),Station Names,Dist. From First Station(km),Metro Line,Opened(Year),Layout,Latitude,Longitude,Connection1,Connection2,First Time,Travel Time
```

This is the header for the txt file which i am popping when reading to prevent errors

## NOTE:

if we enter and exit the same station we do get a deduction of rupees 11 so i didnt implement the station1 == station2 logic as it is incorrect if fare isnt deducted for same station travel

I also used ai assistance to code the dfs search algorithm other than that entire code the graph and everything is made by me, for the graph i used the same logic used in old 2d video games of coordinate rendering and rerendering at fixed intervals or rerendering on input or change in positions of elements


