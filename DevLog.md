# Data Collection (Mandatory Before Coding)

used -> https://otd.delhi.gov.in/data/staticDMRC/ for data zip got 7 files 
```
pr4njal@Macbook-Air DMRC_GTFS % tree
.
├── agency.txt
├── calendar.txt
├── routes.txt
├── shapes.txt
├── stop_times.txt
├── stops.txt
└── trips.txt

1 directory, 7 files
```

using these i can map the lat long or i can just directly use kaggle data which is sorted and completely in csv form so ill go w it
kaggle data link -> https://www.kaggle.com/datasets/arunjangir245/delhi-metro-dataset


# day 1 (mon nov 17)

no idea, so working with banners as its the simplest and thinking of ideas 
1. idea - adding graph to display metro properly (like use game logic refresh using os the terminal and display metro graph and active also switched similarly)
2. using ANSI Shadow font for delhi metro text and making it look india themed too haha using color codes so like it looks like the flag -> https://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=Delhi%20METRO&x=none website used 
3. figured out the biggest headache, how to work with terminal uis so -> ill be using an amazing inbuilt module named shutil :D


Updates -> loading works finally centered shadow wasnt working so i removed the shadow, banner looks nice indian flag and colorful
also added clock for the main graph display ill have it right at the top in the middle like loading screen :DD

Plans -> keep ascii look, make graph functional its just an idea rn sketched out, time on top && graph ui design in figma
         ## Metro Timings
            ● Start time: 06:00 AM
            ● End time: 11:00 PM
            ● Frequency:
            ○ Off-peak hours: every 8 minutes
            ○ Peak hours (8–10 AM and 5–7 PM): every 4 minutes
            print all of this data on the top banner (where i kept the time and all)
            ill need to somehow calculate the css "flexbox flex:1" logic to make it look good but thats not mandatory


        Phase 2: Program Functionality
            In this phase you will implement two functionalities:
            1. Metro Timings Module: In this part, you will load your station and travel-time data to
            calculate when the next train will arrive at any station based on the current time.
            2. Ride journey planner: Here, you will build a program that finds the best route between
            two stations, showing total travel time, interchange points, and when the rider can catch
            the next train.

        change the csv into some other format like split('\n') and list_item.split(',') or any key i like

# day 2 (tue nov 18)

cant do alot today so ill be working with menus for now, in short, whatll come after the "loading" screen so yeah
also need to sort the data in magenta and blue line only and remove other lines? or keep the other lines for the graphs cause itll look good

-> -> -> also need to make an option or something to reset colors in case someone's terminal cant render 24bit color escape codes properly, where tho thats the ques