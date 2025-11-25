# metroScheduler
This project supports all the metro lines in Delhi and Delhi NCR region!!!
You can check metro timings, fare calculations, a metro map displayer and quick metro journey planner.


youtube video in case the provided video doesnt work: 
https://www.youtube.com/watch?v=KqbaZbiuAnA

devlog is in the provided github repository in the info section it contains the entire journey of creating this code

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


Make sure you have all the files in the same folder


I have added proper doc strings for all functions 


and also added comments and full detail next to modules

### Inbuilt modules used:
i didnt use any external libraries but i did use interal already available python libraries that are on every python installation but still ill recommend python 3.8+ but in theory it should work on every python version that supports f-strings 

below mentioned is indetail explanation of how i used all the libraries i imported:


- time # using this to delay, animate, reset, take current time
- os # using this to clear the screen after each load to make it look like an animation
- shutil # this is another amazing module i am using to center text using terminal size to make app responsive
- re # using this to fix the centering issue by removing ascii escape codes from text while centering using .center
- sys # using this for checking os type to make this cross platform

---


### Features ->

Below Listed are the features in this code:

- Live station name suggestions

- Full Delhi NCR metro coverage

- Fare calculation (DMRC accurate)

- Peak/Off-peak timing logic (4mins and 8mins)

- Graph-based journey planning

- ASCII Metro Map renderer

- Cross-platform key input handling

- Loading animations & clean UI with rendered header text

- DFS for calculating shortest path (only ai assisted thing in code)

### Data flow ->
How data is interpreted in what format is listed below:


Opens data, reads it using readlines -> gets 2x nested list -> (then when required can loop through list and split each nested list by ',' to get 3x nested list with proper data in each line)

---

### Miscellaneous ->

defined a colors dictionary to color inside the terminal

defined a function named input_key() to take inputs for all 3 platforms windows, linux, macos

defined suggestion function to suggest metro station names when typing input

(all these are in detail in the other readme file which contains the misc functions in detail)

### Functional Flow -> 

All the functions have their own doc strings for detailed explanation `print(fn_name.__doc__)' 

first i clear the screen twice for empty canvas then run an introduction function, then another clear screenfn then a loading animation with 3 dots then i proceed to print the entire menu

menu has 4 options -> 1. graph 2. timings 3. journey planner 4. info 5. exit

i did implement proper edge case handling using try except blocks for all the calculative functions to prevent crashing of program but u can crash it using ctrl + C in case you are stuck in somewhere, this can be easily prevented by just ignoring the input_key() function's give error i delibrately added it to the code for easy and quick exit.


### Assumptions -> 

Taking metro speed as `33km/hr` (accounting for stops and minor delays too)
But metro speed for ONLY orange line is `100kmph`



### Data online -> 

I got the data from Kaggle but had to modify most of it, changed the lattitude, longitude of almost all metro lines except magenta and blue, added few more columns for time. (all links are at the very bottom)

```
ID (Station ID),Station Names,Dist. From First Station(km),Metro Line,Opened(Year),Layout,Latitude,Longitude,Connection1,Connection2,First Time,Travel Time
```

This is the header for the txt file which i am popping when reading to prevent errors

for the fare calculation i used dmrc data i.e. this data list provided: 


```
For DMRC fare calculation:

Distance       | Mon–Sat Fare | Sun/Holiday Fare | Time Limit
--------------------------------------------------------------
0 – 2 km       | Rs 11         | Rs 11            | 65 mins
2 – 5 km       | Rs 21         | Rs 11
5 – 12 km      | Rs 32         | Rs 21
12 – 21 km     | Rs 43         | Rs 32            | 100 mins
21 – 32 km     | Rs 54         | Rs 43            | 180 mins
> 32 km        | Rs 64         | Rs 54
```



## NOTE:

More Details are inside the code itself i have added docstrings and comments to support the functions you can print the docstrings (`fn_name.__doc__`)

if we enter and exit the same station we do get a deduction of rupees 11 so i didnt implement the station1 == station2 logic as it is incorrect! in real life scenario if i enter station1 and exit without boarding metro money is deducted from my ticket/card so it was deliberate

I also used ai assistance to code the dfs search algorithm other than that, entire code, the graph, suggestion and everything is made by me, for the graph i used the same logic used in old 2d video games of coordinate rendering and rerendering at fixed intervals or rerendering on input or change in positions of elements.


### Reference links:

https://delhimetrorail.com/map
https://delhimetrorail.com/fare
https://web.iitd.ac.in/~tobiastoll/Metro.pdf
https://www.kaggle.com/datasets/arunjangir245/delhi-metro-dataset
https://otd.delhi.gov.in/data/staticDMRC/
https://delhimetrorail.com/


[!] README_extra_misc.md contains all the other miscellaneous data!!! [!]