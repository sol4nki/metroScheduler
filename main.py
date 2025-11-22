# this file only contains the "big" chunks of text that ill 
# use to make it aesthetically pleasing nothing mych

import time # i m using this for almost everything this is the best module ever
import os # using this to clear the screen after each load to make it look like an nimation
import shutil # this is another amazing module ill use it rn to fix the loading centering issue
import re # using this to fix the cenrtering issue
import sys
ansi_pattern = re.compile(r'\x1b\[[0-9;]*m')

# SABSE PHELE DATA 
with open('./data/metro_data.txt', 'r+') as f:
    metro_data = f.readlines()
    metro_data.pop(0)
    
colors = {"Red line":"\033[38;2;237;28;36m","Yellow line":"\033[38;2;255;242;0m","Blue line":"\033[38;2;0;112;192m", "Blue line branch":"\033[38;2;0;112;192m", "Green line":"\033[38;2;0;155;72m", "Green line branch":"\033[38;2;0;155;72m", "Violet line":"\033[38;2;111;45;145m","Pink line":"\033[38;2;255;105;180m","Magenta line":"\033[38;2;255;0;255m","Grey line":"\033[38;2;128;128;128m","Airport Express":"\033[38;2;0;153;153m","White line":"\033[38;2;255;255;255m", "Orange line":"\033[38;2;255;128;0m", "Rapid Metro":"\033[0m", "Aqua line": "\033[38;2;0;255;255m", "Gray line": "\033[38;2;128;128;128m"}


# [!] MAIN MENUS FUNCTIONS [!]

def center_ansi(text, width):
    visible_text = ansi_pattern.sub('', text)
    pad = max(0, (width - len(visible_text)) // 2)
    return ' ' * pad + text

def introduction():
    saffron = "\033[38;2;255;153;51m"
    white   = "\033[38;2;255;255;255m"
    green   = "\033[38;2;19;136;10m"
    reset   = "\033[0m"
    blue = "\033[38;2;50;50;255m"

    x = f"""
{saffron}
        ██████╗ ███████╗██╗     ██╗  ██╗██╗    ███╗   ███╗███████╗████████╗██████╗  ██████╗          
        ██╔══██╗██╔════╝██║     ██║  ██║██║    ████╗ ████║██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗         
        ██║  ██║█████╗  ██║     ███████║██║    ██╔████╔██║█████╗     ██║   ██████╔╝██║   ██║  {reset}       
{white}        ██║  ██║██╔══╝  ██║     ██╔══██║██║    ██║╚██╔╝██║██╔══╝     ██║   ██╔══██╗██║   ██║         
        ██████╔╝███████╗███████╗██║  █{reset}{blue}█║██║    ██║ ╚═╝ ██{reset}{white}║███████╗   ██║   ██║  ██║╚██████╔╝         
        ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚{reset}{blue}═╝╚═╝    ╚═╝     ╚═{reset}{white}╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝          
                                                                                                     

██╗    ██╗███████╗██╗      ██████╗ ███{reset}{blue}███╗ ███╗   ███╗███{reset}{white}████╗███████╗    ██╗   ██╗ ██████╗ ██╗   ██╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝██╔════╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║{reset}
{green}██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  ███████╗     ╚████╔╝ ██║   ██║██║   ██║
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  ╚════██║      ╚██╔╝  ██║   ██║██║   ██║
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗███████║       ██║   ╚██████╔╝╚██████╔╝
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ 
{reset}
    """
    for i in x.split("\n"):
        print(center_ansi(i, shutil.get_terminal_size().columns))
    return 1

def loading(i):
    """
    # using match so i can use time later on and then
    # just print the dots (i couldnt figure out how to work with \n sequences in these)
    """
    saffron = "\033[38;2;255;153;51m"
    white   = "\033[38;2;255;255;255m"
    green   = "\033[38;2;19;136;10m"
    reset   = "\033[0m"
    blue = "\033[38;2;0;0;255m"
    
    dot1 = f"""     
{saffron}██  {reset}
"""
    dot2 = f"""     
{saffron}██{reset}  {white}██{reset}
 
"""
    dot3 = f"""     
{saffron}██{reset}  {white}██{reset}  {green}██{reset}
"""
    width = shutil.get_terminal_size().columns
    match i%3: 
        
        case 0:
            for i in dot1.split("\n"):
                print(center_ansi(i, shutil.get_terminal_size().columns))
            # return "\n\n\n".join(line.center(width) for line in dot1.split("\n"))
        case 1:
            for i in dot2.split("\n"):
                print(center_ansi(i, shutil.get_terminal_size().columns))
            # return "\n\n\n".join(line.center(width) for line in dot2.split("\n"))
        case 2:
            for i in dot3.split("\n"):
                print(center_ansi(i, shutil.get_terminal_size().columns))
            # return "\n\n\n".join(line.center(width) for line in dot3.split("\n"))
    return 1

def clear_screen():
    """
    # I am using this because on reading os.system('clear') manual
    # it states it has cls and clear diff for windows and linux and a solution
    # on stackoverflow suggested to use nt so i am going with nt
    """
    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')

def menu():
    """
    this just prints the menu, couldnt figure out shutil center with ascii escape color codes so
    going with plain stuff and color
    """
    saffron = "\033[38;2;255;153;51m"
    white   = "\033[38;2;255;255;255m"
    green   = "\033[38;2;19;136;10m"
    reset   = "\033[0m"
    blue = "\033[38;2;50;50;255m" 
    width = shutil.get_terminal_size().columns

    x = f"""
{saffron}███╗   ███╗███████╗███╗   ██╗██╗   ██╗
████╗ ████║██╔════╝████╗  ██║██║   ██║{reset}
{white}  ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║{reset}  
{green}  ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║  
██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ {reset}
    """
    

    
    active = 0
    menu_text = ["Display Map", "Metro Timings", "Ride journey planner", "More Info", "Exit"]
    exit = False
    try:
        while not exit:
            clear_screen()
            width = shutil.get_terminal_size().columns # i am getting it everytime just in case user resizes
            print(("═"*len("███╗   ███╗███████╗███╗   ██╗██╗   ██╗ ")).center(width))
            for line in x.split("\n"):
                print(center_ansi(line, width))
            for i in range(len(menu_text)):
                if i == active:
                    print(center_ansi((f"{saffron}>> " + menu_text[i] + f" <<{reset}"), width))
                    continue
                print(menu_text[i].center(width))
                
            print(("═"*len("███╗   ███╗███████╗███╗   ██╗██╗   ██╗ ")).center(width))
            print("\n")
            print("[!]* use the arrow keys to move ↑ ↓ and enter to select an option *[!]".center(width))
            print("\n\n")
            key = input_key()
            if key == "UP":
                active = (active - 1) % len(menu_text)
            elif key == "DOWN":
                active = (active + 1) % len(menu_text)
            elif key == "ENTER":
                clear_screen()
                if active == len(menu_text)-1:
                    exit = True
                    return active
                if active == 3:
                    more_info()
                if active == 2:
                    journey_plan()
                if active == 1:
                    metro_timings()
                if active == 0:
                    metro_map()
                
                
            # time.sleep()
            # active = active+1 if active < len(menu_text) else active-1
            # clear_screen()
    except Exception as e:
        print(e)
        return None
        
    return 1

def time_display():
    """
    i couldnt figure out how to return this and work similarly so i m just printing for now
    so i had kept %S for only debugging but it looks nice so ill keep it forever
    """
    while True:
        print("="*len("|| "+ time.strftime("%H:%M:%S", time.localtime()) + " ||"))
        print("|| "+ time.strftime("%H:%M:%S", time.localtime()), end=" ||\n")
        print("="*len("|| "+ time.strftime("%H:%M:%S", time.localtime()) + " ||"))
        time.sleep(1)
        clear_screen()

def no_service():
    """
    nothing special only a banner
    """
    saffron = "\033[38;2;255;153;51m"
    white   = "\033[38;2;255;255;255m"
    green   = "\033[38;2;19;136;10m"
    reset   = "\033[0m"
    blue = "\033[38;2;50;50;255m"
    red = "\033[38;2;237;28;36m"

    width = shutil.get_terminal_size().columns
    x = f"""
{red}███╗   ██╗ ██████╗     ███████╗███████╗██████╗ ██╗   ██╗██╗ ██████╗███████╗    ██╗██╗
████╗  ██║██╔═══██╗    ██╔════╝██╔════╝██╔══██╗██║   ██║██║██╔════╝██╔════╝    ██║██║
██╔██╗ ██║██║   ██║    ███████╗█████╗  ██████╔╝██║   ██║██║██║     █████╗      ██║██║
██║╚██╗██║██║   ██║    ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██║██║     ██╔══╝      ╚═╝╚═╝
██║ ╚████║╚██████╔╝    ███████║███████╗██║  ██║ ╚████╔╝ ██║╚██████╗███████╗    ██╗██╗
╚═╝  ╚═══╝ ╚═════╝     ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚═╝ ╚═════╝╚══════╝    ╚═╝╚═╝{reset}
                                                                           
    """
    for line in x.split("\n"):
            print(center_ansi(line, width))
    print(center_ansi(f"{red}[!] Metro only operates from 6:00AM to 11:00PM [!]{reset}", width))
    print(center_ansi(f"{red}[!] Sorry for the inconvinence [!]{reset}", width))

def more_info():
    saffron = "\033[38;2;255;153;51m"
    white   = "\033[38;2;255;255;255m"
    green   = "\033[38;2;19;136;10m"
    reset   = "\033[0m"
    blue = "\033[38;2;50;50;255m"
    red = "\033[38;2;237;28;36m"

    """
    just info about project and me -> pranjal yes :D
    """
    banner = f"""
{saffron}███╗    ██╗███╗   ██╗███████╗ ██████╗     ███╗
██╔╝    ██║████╗  ██║██╔════╝██╔═══██╗    ╚██║
{white}██║     ██║██╔██╗ ██║█████╗  ██║   ██║     ██║
{green}██║     ██║██║╚██╗██║██╔══╝  ██║   ██║     ██║
███╗    ██║██║ ╚████║██║     ╚██████╔╝    ███║
╚══╝    ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝     ╚══╝{reset}
                                              
"""
    x = f"""
This project supports all the metro lines in Delhi and Delhi NCR region!!!
You can check metro timings, fare calculations, a metro map displayer and quick metro journey planner :D
{green}[ Metro Scheduler v1.00 ]{reset}
{saffron}[ Pranjal Solanki | 2025386 ]{reset}
[ GitHub: {blue}https://github.com/sol4nki/metroScheduler{reset} ]
[ Video: {blue}ill create yt video baadmein{reset} ]


[!] press any key to go back to menu [!]{reset}
"""

    width = shutil.get_terminal_size().columns
    for line in banner.split("\n"):
            print(center_ansi(line, width))
    for line in x.split("\n"):
            print(center_ansi(line, width))
    x = input_key()
    print(x)

def journey_plan():
    saffron = "\033[38;2;255;153;51m"
    white   = "\033[38;2;255;255;255m"
    green   = "\033[38;2;19;136;10m"
    reset   = "\033[0m"
    blue = "\033[38;2;50;50;255m"
    red = "\033[38;2;237;28;36m"

    x = f"""
\t\t\t{saffron}██████╗ ██╗      █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
\t\t\t██╔══██╗██║     ██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗{reset}
\t\t\t{white}██████╔╝██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝{reset}  
\t\t\t{green}██╔═══╝ ██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
\t\t\t██║     ███████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
\t\t\t╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝{reset}
                                                            
    """

    print(center_ansi(x, shutil.get_terminal_size().columns))
    x = input(("\t\t\tWhich station are you closest to right now?: "))
    y = input(("\t\t\tWhat is your final destination?: "))
    day = ''
    use_current_time = ''
    lup = True
    while lup:
        day = input(("\t\t\tAre you travelling on sunday? (y/n): "))
        if day.lower() == 'y' or day.lower() == 'n':
            lup = False
        else:
            print(f"\t\t\t{red}[!] Please input either y or n [!!]{reset}")
    lup = True
    while lup:
        use_current_time = input(("\t\t\tDo you want to use current time? (y/n): "))
        if use_current_time.lower() == 'y' or use_current_time.lower() == 'n':
            lup = False
        else:
            print(f"\t\t\t{red}[!] Please input either y or n [!!]{reset}")
    if use_current_time.lower() == 'y':
        idk_hrs = (time.strftime("%H", time.localtime()))
        idk_mins = (time.strftime("%M", time.localtime()))
        print(f"\t\t\tPlanning journey from {x} to {y} on a {'sunday' if day.lower() == 'y' else 'weekday'} at {idk_hrs}:{idk_mins}...")
        time.sleep(10)
    else:
        idk = (input(("\t\t\tEnter time of travel in 24-hour format [HOUR:MINS] : ")))
        if ":" not in idk:
            print(f"\t\t\t{red}[!] Invalid time format! Returning to main menu... [!]{reset}")
            time.sleep(2)
            return 1
        idk_hrs, idk_mins = str(idk).strip().split(":")
        if len(idk_hrs) == 1:
            idk_hrs = '0' + idk_hrs
        if int(idk_hrs) > 23 or int(idk_mins) > 59:
            print(f"\t\t\t{red}[!] [!] Invalid time format! Returning to main menu... [!]{reset}")
            time.sleep(2)
            return 1
        print(f"\t\t\t:D Planning journey from {x} to {y} on a {'sunday' if day.lower() == 'y' else 'weekday'} at {idk_hrs}:{idk_mins}...")
        time.sleep(10)
    return 1
                
def metro_timings():
    saffron = "\033[38;2;255;153;51m"
    white   = "\033[38;2;255;255;255m"
    green   = "\033[38;2;19;136;10m"
    reset   = "\033[0m"
    blue = "\033[38;2;50;50;255m"
    x = f"""
\t\t\t{saffron}████████╗██╗███╗   ███╗██╗███╗   ██╗ ██████╗ ███████╗
\t\t\t╚══██╔══╝██║████╗ ████║██║████╗  ██║██╔════╝ ██╔════╝{reset}  
\t\t\t{white}   ██║   ██║██╔████╔██║██║██╔██╗ ██║██║  ███╗███████╗{reset}  
\t\t\t{green}   ██║   ██║██║╚██╔╝██║██║██║╚██╗██║██║   ██║╚════██║ 
\t\t\t   ██║   ██║██║ ╚═╝ ██║██║██║ ╚████║╚██████╔╝███████║
\t\t\t   ╚═╝   ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝{reset}
                                                     
    """

    print(center_ansi(x, shutil.get_terminal_size().columns))
    x = input(("\t\t\tWhich Metro line are you on?: "))
    y = input(("\t\t\tWhat is the name of your Station? : "))
    idk_hrs = (time.strftime("%H", time.localtime()))
    idk_mins = (time.strftime("%M", time.localtime()))
    print(f"\t\t\tUsing current Time {idk_hrs}:{idk_mins} to find {x} line {y} metro timings...")
    time.sleep(2)
    print(center_ansi(x, shutil.get_terminal_size().columns))

    # gotta call that function i forgot its name but yeah wtv calculates timing and stuff also i need to generate qr code
    return 1
               
def metro_map():
    saffron = "\033[38;2;255;153;51m"
    white   = "\033[38;2;255;255;255m"
    green   = "\033[38;2;19;136;10m"
    reset   = "\033[0m"
    blue = "\033[38;2;50;50;255m"
    x = f"""
{saffron}███╗   ███╗ █████╗ ██████╗ 
 ████╗ ████║██╔══██╗██╔══██╗{reset}  
{white} ██╔████╔██║███████║██████╔╝{reset}  
{green} ██║╚██╔╝██║██╔══██║██╔═══╝  
██║ ╚═╝ ██║██║  ██║██║     
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝ {reset}    
                           
    """
    for i in x.split("\n"):
        print(center_ansi(i, shutil.get_terminal_size().columns))
    
    print(center_ansi(f"{saffron}[!] Loading Metro Map Display Module... [!]{reset}", shutil.get_terminal_size().columns))
    time.sleep(1)
    graph_renderer()
    return 1


# KEY INPUT WALA FUNCTION


if os.name == 'nt':
    import msvcrt

    def input_key():
        return msvcrt.getch()

else:
    import sys
    import termios
    import tty

    def input_key():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
            if ch in ('\r', '\n'): return "ENTER"
            if ch == '\x03': raise KeyboardInterrupt # i need to add many more input options
            if ch == '\x1b': # arrow key ka escape sequence
                ch2 = sys.stdin.read(1)
                ch3 = sys.stdin.read(1)
                if ch2 == '[':
                    if ch3 == 'A': return "UP"
                    if ch3 == 'B': return "DOWN"
                    if ch3 == 'C': return "RIGHT"
                    if ch3 == 'D': return "LEFT"
            return ch
                    
            
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return None



# GRAPH WALA FUNCTION

width   = 100
height  = 20
min_lat = 28.3400192
max_lat = 28.7446158
min_lon = 76.9192027
max_lon = 77.5300000
SCALE = 1000

make_dict = {}
# this must must reduce the time complexity by alot when again n again re rendering
def build_dict(SCALE):
    make_dict = {}
    for i in metro_data:
        data = i.strip().split(',')
        lat = float(data[-5])
        lon = float(data[-4])
        make_dict[abs(int((lat-max_lat)*SCALE)), int((lon-min_lon)*SCALE)] = (data[1], colors[data[3]])
    return make_dict
# build_dict()
# print(make_dict, len(make_dict), len(metro_data))
# reset   = "\033[0m"
# ou1, ou2 = 100, 100
# c = True
def graph_renderer():
    width   = 100
    height  = 20
    min_lat = 28.3400192
    max_lat = 28.7446158
    min_lon = 76.9192027
    max_lon = 77.5300000
    SCALE = 1000

    saffron = "\033[38;2;255;153;51m"
    white   = "\033[38;2;255;255;255m"
    green   = "\033[38;2;19;136;10m"
    reset   = "\033[0m"
    blue = "\033[38;2;50;50;255m"

    make_dict = build_dict(SCALE)
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
        print(f"{saffron}[!] {(x+ou1, y+ou2)} | ←↑→↓ arrow keys to navigate | q to quit | s to search | c to toggle names | '-/+' to zoom{reset}")
        x = input_key()
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
                
                # ou1, ou2 = ou1*0.8, ou2*0.8
                make_dict = build_dict(SCALE)
            case "+":
                SCALE = int(SCALE * 1.25)
                
                # ou1, ou2 = ou1*1.25, ou2*1.25
                make_dict = build_dict(SCALE)
            case "=":
                SCALE = int(SCALE * 1.25)
                
                # ou1, ou2 = ou1*1.25, ou2*1.25
                make_dict = build_dict(SCALE)
            case _:
                pass
                            
                

        time.sleep(0.1)
        

# METRO SIM WALEY FUNCTIONS

def fare_calc(loc1, loc2, day):
    

    return 1
def time_converter(time):
    """
    converts mins to hh:mm format
    """
    x,y = divmod(time, 60)
    return f"{x:02}:{y:02} {'[PEAK]' if 8<=x<=10 or 17<=x<=19 else '[OFF-PEAK]'}" #02 zero padded fstring

def metro_timings(loc, line, time):
    """
    doc string placehodler ill add later on
    """
    line = line + " line" if "line" not in line.lower() else line
            
    x,y = map(int, time.split(':'))
    if y > 60 or y < 0:
        return f'\033[38;2;237;28;36m[!] Invalid minutes value: {y}. It should be between 0 and 59.\033[0m'
    mins = x*60 + y
    if mins < 360 or mins > 1380:
        no_service()
        return 0

    for i in metro_data:
        if loc.lower() in i.lower() and line.lower() in i.lower():
            tym = int(i.strip().split(',')[-1]) + 360 # ffffff
            # previous state holde karni padegi cause phele error tha prev state hold nhi hori thi now it works amazingly
            tym1 = (tym) + 4 if ((tym + 4) < 600 and (tym + 4) > 480) or ((tym + 4) > 1020 and (tym + 4) < 1380) else tym+8
            tym2 = (tym1) + 4 if ((tym1 + 4) < 600 and (tym1 + 4) > 480) or ((tym1 + 4) > 1020 and (tym1 + 4) < 1380) else tym1+8
            tym3 = (tym2) + 4 if ((tym2 + 4) < 600 and (tym2 + 4) > 480) or ((tym2 + 4) > 1020 and (tym2 + 4) < 1380) else tym2+8
            if mins < (tym):
                return f"""
                \033[38;2;237;28;36mThe first metro from {loc} on {line} line is at {time_converter((tym))}.\033[0m
                Subsequent trains are available at -> {time_converter(tym1)}, {time_converter(tym2)}, {time_converter(tym3)}.
                """
            else:
                o = 360
                while o < mins:
                    if (o < 600 and o > 480) or (o > 1020 and o < 1380):
                        o+=4
                    else:
                        o+=8
                tym = o
                tym1 = (tym) + 4 if ((tym + 4) < 600 and (tym + 4) > 480) or ((tym + 4) > 1020 and (tym + 4) < 1380) else tym+8
                tym2 = (tym1) + 4 if ((tym1 + 4) < 600 and (tym1 + 4) > 480) or ((tym1 + 4) > 1020 and (tym1 + 4) < 1380) else tym1+8
                tym3 = (tym2) + 4 if ((tym2 + 4) < 600 and (tym2 + 4) > 480) or ((tym2 + 4) > 1020 and (tym2 + 4) < 1380) else tym2+8

                return f"""
                \033[38;2;237;28;36mThe Metro from {loc} on {line} line is at {time_converter((tym))}.\033[0m
                Subsequent trains are available at -> {time_converter(tym1)}, {time_converter(tym2)}, {time_converter(tym3)}.
                """
            return i
    return f'\033[38;2;237;28;36m[!] No station has/contains the name {loc} on {line} line.\033[0m'


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
    changes = []
    if x[3] != j[3]:
        for k in metro_data:
            # print(j[3].split(' ')[0])
            k = k.strip().split(',') # I KEEP FORGETTING DATA IS RAW BRUUUUUU
            if k[3] == x[3] and k[-2] == j[3].split(' ')[0]:
                print("Change at ", k[1])
                changes.append(k)
        if not changes:
            print("No direct route found, try going xyz")
            return 0
    else:
        print("Direct route available on", x[3])
        # now change ke liye need to figure out lat long shit cause easiest? like closest lat on blue line? or like closest lat that connects to xyz 
    print(f"From {loc1} to {loc2} on {day} at {time} hours")
    # basically go from x to (switch till j line change)
    return 1
# journey_plan("Uttam Nagar West", "Govindpuri", "sunday", 10)
# print(journey_plan.__doc__)
# print(metro_timings("janakpuri west", "blue", "16:40"))



if __name__ == "__main__":
    clear_screen() # just using this because i want a clear canvas using python functional notation name_xyz not javascript nameXyz
    clear_screen() # twice because running only once leads to the dir path still being printed
    (introduction())
    time.sleep(1)
    clear_screen()
    for i in range(3):
        print(loading(i))
        time.sleep(0.5)
        clear_screen()

    x = menu()
    # print(x)
    # (more_info())
    # time_display()

    # no_service()