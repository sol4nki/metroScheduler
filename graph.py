import shutil, os, time

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

make_dict = {}
# this must must reduce the time complexity by alot when again n again re rendering
for i in metro_data:
    data = i.strip().split(',')
    lat = float(data[-4])
    lon = float(data[-3])
    make_dict[int((lat-min_lat)*1000), int((lon-min_lon)*1000)] = (data[1], colors[data[3]])

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
    