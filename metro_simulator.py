# def display_info():
#     ## need to design the ui figma check!!!!!


#     return 1

with open('./data/metro_data.txt', 'r') as f:
    metro_data = f.readlines()
colors = {"Red line":"\033[38;2;237;28;36m","Yellow line":"\033[38;2;255;242;0m","Blue line":"\033[38;2;0;112;192m", "Blue line branch":"\033[38;2;0;112;192m", "Green line":"\033[38;2;0;155;72m", "Green line branch":"\033[38;2;0;155;72m", "Violet line":"\033[38;2;111;45;145m","Pink line":"\033[38;2;255;105;180m","Magenta line":"\033[38;2;255;0;255m","Grey line":"\033[38;2;128;128;128m","Airport Express":"\033[38;2;0;153;153m","White line":"\033[38;2;255;255;255m", "Orange line":"\033[38;2;255;128;0m", "Rapid Metro":"\033[0m", "Aqua line": "\033[38;2;0;255;255m", "Gray line": "\033[38;2;128;128;128m"}

metro_data.pop(0)
for line in metro_data:
    # print(dat)
    dat = line.strip().split(',')
    # print(dat)
    print(colors[dat[3]] + ', '.join(dat) + "\033[0m")
