import shutil, os, time, keyinp

with open('./data/metro_data.txt', 'r') as f:
    metro_data = f.readlines()
    metro_data.pop(0) 
colors = {"Red line":"\033[38;2;237;28;36m","Yellow line":"\033[38;2;255;242;0m","Blue line":"\033[38;2;0;112;192m", "Blue line branch":"\033[38;2;0;112;192m", "Green line":"\033[38;2;0;155;72m", "Green line branch":"\033[38;2;0;155;72m", "Violet line":"\033[38;2;111;45;145m","Pink line":"\033[38;2;255;105;180m","Magenta line":"\033[38;2;255;0;255m","Grey line":"\033[38;2;128;128;128m","Airport Express":"\033[38;2;0;153;153m","White line":"\033[38;2;255;255;255m", "Orange line":"\033[38;2;255;128;0m", "Rapid Metro":"\033[0m", "Aqua line": "\033[38;2;0;255;255m", "Gray line": "\033[38;2;128;128;128m"}

# stat_blue = ""
# for line in metro_data:
#     dat = line.strip().split(',')
#     if dat[3] == "Blue line" or dat[3] == "Blue line branch":
#         color = colors[dat[-2]] if dat[-2] != 'None' else colors[dat[3]]
#         stat_blue += colors[dat[3]] + '==' + "\033[0m" + color + dat[1] + "\033[0m"

# print(stat_blue)

# width = shutil.get_terminal_size().columns
# # why is width 1/3rd ???????
# # i have no clue
# print(stat_blue[:width*3])

width   = 100
height  = 20
min_lat = 28.3400192
max_lat = 28.7446158
min_lon = 76.9192027
max_lon = 77.5300000
SCALE = 1000

make_dict = {}
# this must must reduce the time complexity by alot when again n again re rendering
def build_dict():
    for i in metro_data:
        data = i.strip().split(',')
        lat = float(data[-5])
        lon = float(data[-4])
        make_dict[abs(int((lat-max_lat)*SCALE)), int((lon-min_lon)*SCALE)] = (data[1], colors[data[3]])
build_dict()
# print(make_dict, len(make_dict), len(metro_data))
reset   = "\033[0m"
ou1, ou2 = 100, 100
c = True
while True:
    os.system('clear')
    
    for x in range(shutil.get_terminal_size().lines - 2):
        y = 0
        print("|", end="")
        while y < (shutil.get_terminal_size().columns -2):
            print(f"{(f"{make_dict[(x+ou1, y+ou2)][1]}◉ {make_dict[(x+ou1, y+ou2)][0] if c else ''}{reset}" if len(make_dict[(x+ou1, y+ou2)][0]) < (shutil.get_terminal_size().columns -2 - y) else " ") if (x+ou1, y+ou2) in make_dict else " "}", end="")
            y+=(len(f"◉ {make_dict[(x+ou1, y+ou2)][0] if c else ''}")-1 if len(make_dict[(x+ou1, y+ou2)][0]) < (shutil.get_terminal_size().columns -2 - y) else 0) if ((x+ou1, y+ou2) in make_dict) else 0
            y+=1
        print("|", end="")
        print()
    print((x+ou1, y+ou2), " ←↑→↓ arrow keys to navigate | q to quit | s to search | c to toggle names | '-/+' to zoom")
    x = keyinp.input_key()
    match x:
        case 'q':
            break
        case 'UP':
            if ou1+10 > 0:
                ou1 -= 10
        case "DOWN":
            if ou1 < ((max_lat - min_lat)*1000 + 2) - height:
                ou1 += 10
            
        case "RIGHT":
            if ou2 < ((max_lon - min_lon)*1000 + 2) - width:
                ou2 += 10

        case "LEFT":
            if ou2+10 > 0:
                ou2 -= 10
        case "s":
            t = False
            station_name = input("Enter station name to search: ")
            for key in make_dict:
                if station_name.lower() in make_dict[key][0].lower():
                    ou1, ou2 = abs(shutil.get_terminal_size().lines//2-key[0]-2), abs(shutil.get_terminal_size().columns//2-key[1]-2)
                    t = True
                    break
            if not t:
                print("[!] Station not found! [!]")
                time.sleep(1)
        case "c":
            c = not c
        case "-":
            SCALE = int(SCALE * 0.8)
            make_dict = {}
            ou1, ou2 = ou1*0.8, ou2*0.8
            build_dict()
        case "+":
            SCALE = int(SCALE * 1.25)
            make_dict = {}
            # ou1, ou2 = ou1*1.25, ou2*1.25
            build_dict()
        case "=":
            SCALE = int(SCALE * 1.25)
            make_dict = {}
            # ou1, ou2 = ou1*1.25, ou2*1.25
            build_dict()
        case _:
            pass
                        
            

    time.sleep(0.1)
    