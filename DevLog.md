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

updates -> 
1. made menu need to animate and add keys working 2. need to google how to make footer work have an basic idea use shutil to get column size and yeah !!!! ALSO USE SHUTIL TO TELL USER TO KEEP TERMINAL SIZE LARGE

2. !!! need to figure out how to take both windows, linux and MacOS inputs 

3. dmrc fare rates found 
```
For DMRC
Distance (in KMs)	FARE	Time Limit (in Mins.)
Monday to Saturday	Sunday & National Holidays
0-2	Rs 11/-	Rs 11/-	65
2-5	Rs 21/-	Rs. 11/-
5-12	Rs 32/-	Rs 21/-
12-21	Rs. 43/-	Rs. 32/-	100
21-32	Rs 54/-	Rs 43/-	180
More than 32	Rs 64/-	Rs 54/-

```

3. changed the data a little added connection1 and connection2

4. added color dictionary which took alot of time to make
5. trying to figure out the footer now [not_required]
6. i used chatgpt to fix the colored menus and other options not visible so now ill use re regular expression matching to edit it with a custom centering function
7. write a small algorithm to calc shortest route?? 
8. start taking inputs [done]


# day 3 (wed nov 19)

ill be working on "qr code" because maps are almost impossible to make man FF too hard

-> !!! map idea -> do one thing map will basically contain xyz line and uska poora map and current metro (from current time)
-> try to add metro animation somehow, wont be hard just use time(1) refresh every sec and yeah update it 

-> figured out the biggest headache. "green   = "\033[38;2;19;136;10m" yes literally the issue was "saturation in b/w the contrast basically same as terminal bg hence not visible on b/w terminals lol

-> also graph idea -> USE LAT LONG TO MAP THEM?? LIKE BEST RIGHT? but need to figure out how but yeah might just work
^^^^ took inspiration from mapscii braille maps in terminal so yeah gotta figure it out now 

# day 4 (wed nov 19)

need to do:
-> braille maps 
-> first actually map the coordinates on some graph or something or write py script to visualize and create bounding boxes
-> [!!!!] just figured out that many of the coordinate pairs are wrong in this dataset even tho its a nice dataset i have to fix it myself F

-> almsot entire day spend fixing the map bruh

memo -> find the largest lat and long (also the minimum too just iterate over the code once simple python script)
```py
tempmin = 10000000
tempmax = 0

for i in metro_data:
    data = i.strip().split(',')
    if float(data[-2]) >= tempmax:
        name1 = data[1]
        tempmax = float(data[-2])
    if float(data[-2]) <= tempmin:
        name2 = data[1]
        tempmin = float(data[-2])
```
```
pr4njal@Macbook-Air metroScheduler % python3 metro_simulator.py
max lat Samaypur Badli(First Station)  +  28.7446158
min lat Raja Nahar Singh  +  28.3400192
pr4njal@Macbook-Air metroScheduler % python3 metro_simulator.py
max long Pari Chowk Greater Noida  +  77.53
min long Brigadier Hoshiar Singh  +  76.9192027
```
ill double confirm from the `delhi_metro_map.html` file generated using plotly.py
[image attachment placeholder]

so we know box size is width -> [28.3400192, 28.7446158] and height -> [76.9192027, 77.53]

like might need difference too? smallest difference? 
n^2 time complexity 
```py
temp = 1000
count=0
for l in metro_data:
    dat = l.strip().split(',')
    for l in metro_data:
        count+=1
        idk = l.strip().split(',')
        # print(dat[-4], idk[-4], count)
        if abs(float(dat[-4]) - float(idk[-4])) < temp and abs(float(dat[-4]) - float(idk[-4])) != 0:
            temp = abs(float(dat[-4]) - float(idk[-4]))

print(f"smallest distance to scale is {temp} lat units")
```

lol this is crazy so we can just take it accurately to like idk
```
pr4njal@Macbook-Air metroScheduler % python3 metro_simulator.py
smallest distance to scale is 2.500000000793534e-06 lat units
```

so this aint gon work, ill just make a list sort it and print least 10 values to get a viable so called "limit" to lat long on the graph ill make

```py
temp = 1000
count=0
x = []
for l in metro_data:
    dat = l.strip().split(',')
    for l in metro_data:
        count+=1
        idk = l.strip().split(',')
        # print(dat[-4], idk[-4], count)
        x.append(abs(float(dat[-4]) - float(idk[-4])) if dat[-4] != idk[-4] else 1000)
x.sort()
print("smallest 10 lat distances are :")
for i in range(10):
    print(f"{i+1}th -> {x[i]}")
```



i dont even know what to say atp
```
pr4njal@Macbook-Air metroScheduler % python3 metro_simulator.py
smallest 10 lat distances are :
1th -> 2.500000000793534e-06
2th -> 2.500000000793534e-06
3th -> 3.899999999390502e-06
4th -> 3.899999999390502e-06
5th -> 5.39999999915608e-06
6th -> 5.39999999915608e-06
7th -> 6.100000000230921e-06
8th -> 6.100000000230921e-06
9th -> 9.999999999621423e-06
10th -> 9.999999999621423e-06
```

ill just take 9.999999999621423e-06 as the metric because def these are stations i overlooked when updating lats and longs

so unit is -> `0.000010`. now well 

### graph?!?!

```py
width = 100
height = 20

for i in range(height):
    for x in range(width):
        print("*", end="")
    print()
```

so basically prints a grid same as the logic of a game now i just need to implement quick checks to check (x,i) coord and leading to ill change i to y so (x,y) leading to easy grid rendering [i can also use current terminal size using shutil btw ill try dat]


```py
width = 100
height = 20
while True:
    os.system('clear')
    for i in range(shutil.get_terminal_size().lines - 2):
        print("|", end="")
        for x in range(shutil.get_terminal_size().columns -2):
            print("*", end="")
        print("|", end="")
        print()
    time.sleep(1)

```

works beautifully i dont think i can find any solution better than this :pray: just dec sleep time to 0.1 for qucik response ill keep it 1sec for easy debugging :D


now ill work on getting the data and printing on the screen


welp another sad day to be programming i might have some clue why output is 269 and 283 cause floating point div is messed up in py or its just overlapping closeby stations (ill love to consider the latter) ill take "268 283" by taking 1000 like it was before
```py
width   = 100
height  = 20
min_lat = 28.3400192
max_lat = 28.7446158
min_lon = 76.9192027
max_lon = 77.5300000

make_dict = {}
# this must must reduce the time complexity by alot when again n again re rendering
for i in metro_data:
    data = i.strip().split(',')
    lat = float(data[-4])
    lon = float(data[-3])
    make_dict[int((lat-min_lat)*10000000000), int((lon-min_lon)*10000000000)] = (data[1])

print(make_dict, len(make_dict), len(metro_data))

```

ALSO I M NOT TAKING "10000000000" ITS JUST FOR DEBUGGING WHY DICT LEN != LEN OF INIT LIST

this absolute beauty works now, my eyes are blessed 

```py
print(make_dict, len(make_dict), len(metro_data))
reset   = "\033[0m"
while True:
    os.system('clear')
    for i in range(shutil.get_terminal_size().lines - 2):
        
        print("|", end="")
        for x in range(shutil.get_terminal_size().columns -2):
            print(f"{f"{make_dict[(x+200, i+200)][1]}*{reset}" if (x+200, i+200) in make_dict else "_"}", end="")
        print("|", end="")
        print()
    print((x+100, i+100))
    time.sleep(0.1)

```

just gotta work w/ the joining of these chars now somehow hmm using \\ - | or sum better chars "mapscii braille if it works"



