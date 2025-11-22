# def display_info():
#     ## need to design the ui figma check!!!!!


#     return 1

from banner import no_service

with open('./data/metro_data.txt', 'r') as f:
    metro_data = f.readlines()
    metro_data.pop(0) 
colors = {"Red line":"\033[38;2;237;28;36m","Yellow line":"\033[38;2;255;242;0m","Blue line":"\033[38;2;0;112;192m", "Blue line branch":"\033[38;2;0;112;192m", "Green line":"\033[38;2;0;155;72m", "Green line branch":"\033[38;2;0;155;72m", "Violet line":"\033[38;2;111;45;145m","Pink line":"\033[38;2;255;105;180m","Magenta line":"\033[38;2;255;0;255m","Grey line":"\033[38;2;128;128;128m","Airport Express":"\033[38;2;0;153;153m","White line":"\033[38;2;255;255;255m", "Orange line":"\033[38;2;255;128;0m", "Rapid Metro":"\033[0m", "Aqua line": "\033[38;2;0;255;255m", "Gray line": "\033[38;2;128;128;128m"}

# for line in metro_data:
#     # print(dat)
#     dat = line.strip().split(',')
#     # print(dat)
#     print(colors[dat[3]] + ', '.join(dat) + "\033[0m")

# just trying to imagine what the graph might look like:
# for line in metro_data:
#     dat = line.strip().split(',')
#     if dat[3] == "Blue line" or dat[3] == "Blue line branch":
#         color = colors[dat[-2]] if dat[-2] != 'None' else colors[dat[3]] # ok so this wasnt working because it ran both ascii codes not its working when i use variable assignment
#         print(colors[dat[3]] + '==' + "\033[0m" + color + dat[1] + "\033[0m", end="")


def fare_calc(loc1, loc2, day):
    

    return 1

def metro_timings(loc1, loc2, time):
    if time <= 6 or time >= 23:
        no_service()
        return 0
    for i in metro_data:
        if loc1 in i:
            print(i)
        if loc2 in i:
            print(i)
    return 1

# ('gotta make quick suggestions type stuff')

def journey_plan(loc1, loc2, day, time):
    """
    loc1 -> loc2 on day (sunday price low) and time peak or offpeak for calc of time and fare
    """
    
    x, j = "", ""
    for i in metro_data:
        if loc1.lower() in i.lower():
            x = i if x == "" else x
        if loc2.lower() in i.lower():
            j = i if j == "" else j
            # BECAUSE I CANNOT BREAK J WONT BE ASSIGNED BRUV I DONT WANNA RUN 2 LOOPS??
    print(x, j)
    x = x.strip().split(',')
    j = j.strip().split(',') 
    # bruvh metro data was raw???!?!?! i m dumb
    CHANGE = False
    if x[3] != j[3]:
        for k in metro_data:
            # print(j[3].split(' ')[0])
            k = k.strip().split(',') # I KEEP FORGETTING DATA IS RAW BRUUUUUU
            if k[3] == x[3] and k[-2] == j[3].split(' ')[0]:
                print("Change at ", k[1], end=" ")
                CHANGE = True
        if not CHANGE:
            print("No direct route found, try going xyz")
            return 0
    else:
        print("Direct route available on", x[3])
        # now change ke liye need to figure out lat long shit cause easiest? like closest lat on blue line? or like closest lat that connects to xyz 
    print(f"From {loc1} to {loc2} on {day} at {time} hours")
    # basically go from x to (switch till j line change)
    return 1
# journey_plan("Uttam Nagar West", "Nangloi", "sunday", 10)
# print(journey_plan.__doc__)
# metro_timings("Rajiv Chowk", "Dwarka Sector 14", 8)

