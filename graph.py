import shutil

with open('./data/metro_data.csv', 'r') as f:
    metro_data = f.readlines()
    metro_data.pop(0) 
colors = {"Red line":"\033[38;2;237;28;36m","Yellow line":"\033[38;2;255;242;0m","Blue line":"\033[38;2;0;112;192m", "Blue line branch":"\033[38;2;0;112;192m", "Green line":"\033[38;2;0;155;72m", "Green line branch":"\033[38;2;0;155;72m", "Violet line":"\033[38;2;111;45;145m","Pink line":"\033[38;2;255;105;180m","Magenta line":"\033[38;2;255;0;255m","Grey line":"\033[38;2;128;128;128m","Airport Express":"\033[38;2;0;153;153m","White line":"\033[38;2;255;255;255m", "Orange line":"\033[38;2;255;128;0m", "Rapid Metro":"\033[0m", "Aqua line": "\033[38;2;0;255;255m", "Gray line": "\033[38;2;128;128;128m"}

stat_blue = ""
for line in metro_data:
    dat = line.strip().split(',')
    if dat[3] == "Blue line" or dat[3] == "Blue line branch":
        color = colors[dat[-2]] if dat[-2] != 'None' else colors[dat[3]]
        stat_blue += colors[dat[3]] + '==' + "\033[0m" + color + dat[1] + "\033[0m"

# print(stat_blue)

width = shutil.get_terminal_size().columns
# why is width 1/3rd ???????
# i have no clue
print(stat_blue[:width*3])