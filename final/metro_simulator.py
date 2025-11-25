import time # using this to delay, animate, reset, take current time and many more time related fns
import os # using this to clear the screen after each load to make it look like an animation
import shutil # this is another amazing module i am using to center text using terminal size to make app responsive
import re # using this to fix the centering issue by removing ascii escape codes from text while centering using .center
import sys # using this for checking os type to make this cross platform

ansi_pattern = re.compile(r'\x1b\[[0-9;]*m') #this is regex pattern that will be matched and removed before centering 
# because when centering text with ANSI escape codes, the codes themselves can affect the calculated length of the text, leading to incorrect centering.

# [!] FIRST THING -> LOAD METRO DATA [!]
with open('./metro_data.txt', 'r') as f:
    metro_data = f.readlines()
    metro_data.pop(0) # REMOVING THE CSV FILE HEADER (first one)


# [!] DEFINING COLORS FOR LINES [!]
colors = {"Red line":"\033[38;2;237;28;36m","Yellow line":"\033[38;2;255;242;0m","Blue line":"\033[38;2;0;112;192m", "Blue line branch":"\033[38;2;0;112;192m", "Green line":"\033[38;2;0;155;72m", "Green line branch":"\033[38;2;0;155;72m", "Violet line":"\033[38;2;111;45;145m","Pink line":"\033[38;2;255;105;180m","Magenta line":"\033[38;2;255;0;255m","Grey line":"\033[38;2;128;128;128m","Airport Express":"\033[38;2;0;153;153m","White line":"\033[38;2;255;255;255m", "Orange line":"\033[38;2;255;128;0m", "Rapid Metro":"\033[0m", "Aqua line": "\033[38;2;0;255;255m", "Gray line": "\033[38;2;128;128;128m"}


# [!] KEY INPUT DETECTION FOR ABSOLUTE CROSS PLATFORM FUNCTIONALITY [!]
if os.name == 'nt':
    import msvcrt # inbuilt module for windows systems

    def input_key():
        ch = msvcrt.getch() # added later on for cross platform same as linux macos i need to test before 
        if ch in (b'\r', b'\n'): return "ENTER"
        if ch == b'\x03': raise KeyboardInterrupt
        if ch in (b'\b', b'\x7f'): return "BACKSPACE"
        if ch == b'\xe0' or ch == b'\x00':
            ch2 = msvcrt.getch()
            if ch2 == b'H': return "UP"
            if ch2 == b'P': return "DOWN"
            if ch2 == b'M': return "RIGHT"
            if ch2 == b'K': return "LEFT"
        return ch.decode(errors="ignore") if isinstance(ch, bytes) else ch
else:
    import termios # inbuilt module for unix based systems (linux and macOS) x1
    import tty # module for unix based systems x2 (linux and macOS) x2

    def input_key():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
            if ch in ('\r', '\n'): return "ENTER"
            if ch == '\x03': raise KeyboardInterrupt 
            if ch == '\b' or ch == '\x7f': return "BACKSPACE"
            if ch == '\x1b': # escape seq for arrow key because its like ^[[A like something this
                ch2 = sys.stdin.read(1)
                ch3 = sys.stdin.read(1)
                if ch2 == '[':
                    if ch3 == 'A': return "UP"
                    if ch3 == 'B': return "DOWN"
                    if ch3 == 'C': return "RIGHT"
                    if ch3 == 'D': return "LEFT"
            return ch # prints any other keyboard inp like abcd for full functionality
                    
            
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return None



# [!] MAIN MENUS FUNCTIONS [!]
def center_ansi(text, width):
    """
    ---
    text: str -> text to be centered
    width: int -> total width to center within
    ---
    returns: str -> centered text
    ---
    simple function to center text
    """
    visible_text = ansi_pattern.sub('', text)
    pad = max(0, (width - len(visible_text)) // 2)
    return ' ' * pad + text

def introduction():
    """
    ---
    no parameters [!]
    ---
    returns: int -> 1/Truthy if success
    ---
    simple function to print the welcome banner
    """
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
    ---
    i: int -> input seconds as int to print specific loading animation frame (out of 3 possible frames)
    ---
    returns: int -> 1/Truthy if success
    ---
    simple function to print ... loading animation
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
    ---
    no parameters [!]
    ---
    returns: None -> no returns because it literally cleans the screen
    ---
    # I am using this because on reading os.system('clear') manual
    # it states it has cls and clear diff for windows and linux and a solution
    # on stackoverflow suggested to use nt so i am going with nt
    """
    if os.name == 'nt':  # again checking for os type before clearing screen
        os.system('cls')
    else:  
        os.system('clear')

def menu():
    """
    ---
    no parameters [!]
    ---
    returns: int 1 -> 1/Truthy if success
             int 0 -> 0/Falsy if failure
             int len(menu_text)-1 -> if "exit"
             Exception as e -> prints ByeBye!
    ---
    Prints an animated menu with arrow key nav functionality and enter to select option
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
    menu_text = ["Display Map", "Metro Timings", "Ride journey planner", "Quick Search", "More Info", "Exit"]
    exit = False
    try:
        while not exit:
            clear_screen()
            width = shutil.get_terminal_size().columns # i am getting width from shutil everytime just in case user resizes
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
                if active == 4:
                    try:
                        more_info()
                    except Exception as e:
                        print(e, "\n[!] Returning to main menu...")
                if active == 3:
                    try:
                        quick_search()
                    except Exception as e:
                        print(e, "\n[!] Returning to main menu...")
                if active == 2:
                    try:
                        journey_plan()
                    except Exception as e:
                        print(e, "\n[!] Returning to main menu...")
                if active == 1:
                    try:
                        metro_timings()
                    except Exception as e:
                        print(e, "\n[!] Returning to main menu...")
                if active == 0:
                    try:
                        metro_map()
                    except Exception as e:
                        print(e, "\n[!] Returning to main menu...")
            
    except:
        print('ByeBye!') 
        return None
        
    return 1

def time_display():
    """
    ---
    no parameters [!]
    ---
    returns: None -> it directly prints the time in a loop every second no return required
    ---
    while loop to print current time every second after sleeping each sec
    # i couldnt figure out how to return this and work similarly so i m just printing for now
    # so i had kept %S for only debugging but it looks nice so ill keep it forever
    """
    while True:
        print("="*len("|| "+ time.strftime("%H:%M:%S", time.localtime()) + " ||"))
        print("|| "+ time.strftime("%H:%M:%S", time.localtime()), end=" ||\n")
        print("="*len("|| "+ time.strftime("%H:%M:%S", time.localtime()) + " ||"))
        time.sleep(1)
        clear_screen()

def no_service():
    """
    ---
    no parameters [!]
    ---
    returns: None -> Nothing because it just prints the no_service banner
    ---
    nothing special, prints the no_service banner when metro is closed/menu not working/some error occurs
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
    print(center_ansi(f"{red}[!] Returning to main menu in 5 seconds...!!! [!]{reset}", width))
    time.sleep(5)
    return 0

def more_info():
    """
    ---
    no parameters [!]
    ---
    returns: None -> Just prints info about project and me
    ---
    info directly printed about project and me
    """
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
[ Video: {blue}https://youtu.be/KqbaZbiuAnA{reset} ]


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
    """
    ---
    no parameters [!]
    ---
    returns: int ->  1/Truthy if success
    ---
    Prints the centered banner for journey planner which is then sent to another function that processed that data and gives us the final outcome of all this
    """
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
    if clean_station_name(x) not in graph or clean_station_name(y) not in graph:
        print(f"\t\t\t{red}[!] One or both of the stations you entered are invalid! Returning to main menu... [!]{reset}")
        time.sleep(2)
        return 1
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
        # time.sleep(10)
        if idk_hrs < '06' or (idk_hrs == '23' and idk_mins > '00') or idk_hrs > '23':
            no_service()
            return 1
        start = clean_station_name(x)
        end = clean_station_name(y)
        top3 = find_paths(graph, start, end, dist_map)
        for d, p in top3:
            colored_path = []
            for st in p:
                colored_path.append(colorize_station(st))
            print("|", " → ".join(colored_path), "|", "\n > Total Travel Distance is:", str(round(d, 2)) + "km", "\n > Total Price of Ticket is ₹" + str(fare_calc(d, day)), f"\n > Total Travel Time is: {round(time_calc(d),0)}mins ", f"\n > Ticket is valid for: {ticket_valid_time(d)}mins ")
            print("-------".center(shutil.get_terminal_size().columns, '-'))
        
    else:
        idk = (input(("\t\t\tEnter time of travel in 24-hour format [HOUR:MINS] : ")))
        if ":" not in idk:
            print(f"\t\t\t{red}[!] Invalid time format! Returning to main menu... [!]{reset}")
            time.sleep(2)
            return 1
        idk_hrs, idk_mins = str(idk).strip().split(":")
        if idk_hrs < '06' or (idk_hrs == '23' and idk_mins > '00') or idk_hrs > '23':
            no_service()
            return 1
        if len(idk_hrs) == 1:
            idk_hrs = '0' + idk_hrs
        if int(idk_hrs) > 23 or int(idk_mins) > 59:
            print(f"\t\t\t{red}[!] [!] Invalid time format! Returning to main menu... [!]{reset}")
            time.sleep(2)
            return 1
        print(f"\t\t\t:D Planning journey from {x} to {y} on a {'sunday' if day.lower() == 'y' else 'weekday'} at {idk_hrs}:{idk_mins}...")
        
        # time.sleep(10)
        start = clean_station_name(x)
        end = clean_station_name(y)
        top3 = find_paths(graph, start, end, dist_map)
        for d, p in top3:
            colored_path = []
            for st in p:
                colored_path.append(colorize_station(st))
            print("|", " → ".join(colored_path), "|", "\n > Total Travel Distance is:", str(round(d, 2)) + "km", "\n > Total Price of Ticket is ₹" + str(fare_calc(d, day)), f"\n > Total Travel Time is: {round(time_calc(d),0)}mins ", f"\n > Ticket is valid for: {ticket_valid_time(d)}mins ")
            print("-------".center(shutil.get_terminal_size().columns, '-'))
    print("\t\t\t-> Most Recommended Route is at the very top <-")
    print()
    print("\t\t\t[!] Press any key twice to return to main menu...")
    time.sleep(2)
    input_key()
    return input_key()

def metro_timings():
    """
    ---
    no parameters [!]
    ---
    returns: int -> 1/Truthy if success
    ---
    Just prints the timings banner, takes required inputs and then sends to another function that calculates timings and stuff 
    """
    saffron = "\033[38;2;255;153;51m"
    white   = "\033[38;2;255;255;255m"
    green   = "\033[38;2;19;136;10m"
    reset   = "\033[0m"
    blue = "\033[38;2;50;50;255m"
    red = "\033[38;2;237;28;36m"
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
    if clean_station_name(y) not in graph:
        print(f"\t\t\t{red}[!] station name or line name you entered is invalid! Returning to main menu... [!]{reset}")
        time.sleep(2)
        return 1
    tike = input(("\t\t\tEnter time of travel in 24-hour format [HOUR:MINS] or type 'now' to use current time: "))
    if tike.lower() != 'now':
        if ":" not in tike:
            print(f"\t\t\t{red}[!] Invalid time format! Returning to main menu... [!]{reset}")
            time.sleep(2)
            return 1
        idk_hrs, idk_mins = str(tike).strip().split(":")
        if len(idk_hrs) == 1:
            idk_hrs = '0' + idk_hrs
        if int(idk_hrs) > 23 or int(idk_mins) > 59:
            print(f"\t\t\t{red}[!] Invalid time format! Returning to main menu... [!]{reset}")
            time.sleep(2)
            return 1
        print(f"\t\t\tUsing provided Time {idk_hrs}:{idk_mins} to find {x} line {y} metro timings...")
        # time.sleep(0.5)
        for i in metro_timings_real(y, x, f"{idk_hrs}:{idk_mins}").split("\n"):
            print(f"\t\t{i}")
            time.sleep(1)
        print("\t\t\tPress any key to return to main menu...")
        return input_key()
    idk_hrs = (time.strftime("%H", time.localtime()))
    idk_mins = (time.strftime("%M", time.localtime()))
    print(f"\t\t\tUsing current Time {idk_hrs}:{idk_mins} to find {x} line {y} metro timings...")
    # time.sleep(0.5)
    for i in metro_timings_real(y, x, f"{idk_hrs}:{idk_mins}").split("\n"):
        print(f"\t\t{i}")
        time.sleep(1)
    print("\t\t\tPress any key to return to main menu...")
    return input_key()
    # print(center_ansi(x, shutil.get_terminal_size().columns))
               
def metro_map():
    """
    ---
    no parameters [!]
    ---
    returns: int -> 1/Truthy if success
    ---
    This is just a placeholder before the actual map is printed!!!
    Just prints the metro map banner and then calls the graph rendering function for displaying the actual functional metro map
    """
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

def quick_search():
    """
    ---
    no parameters [!]
    ---
    returns: int -> 1/Truthy if success
    ---
    Just prints the quick search banner, takes required inputs and then sends to another function that processes that data and gives us the final outcome of all this
    """
    # same as suggestions but with a banner
    saffron = "\033[38;2;255;153;51m"
    white   = "\033[38;2;255;255;255m"
    green   = "\033[38;2;19;136;10m"
    reset   = "\033[0m"
    blue = "\033[38;2;50;50;255m"
    red = "\033[38;2;237;28;36m"
    banner = f"""
{saffron}███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║{reset}
{white}███████╗█████╗  ███████║██████╔╝██║     ███████║{reset}
{green}╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝{reset}
    """
    text1 = f"{saffron}[!] Station Name :{reset}"
    idk = ''
    jjj = []
    while True:
        clear_screen()
        print()
        print()
        for i in banner.split("\n"):
            print(center_ansi(i, shutil.get_terminal_size().columns))
        print()
        print(f"{text1} : {idk}", end="\n")
        print()
        print("Suggestions: ")
        kkkk = jjj[:10] if len(jjj) > 10 else jjj
        print(" | " + ", ".join(i for i in kkkk) + " | ")
        
        x = input_key()
        if x == "BACKSPACE":
            idk = idk[:-1]
        elif x == "ENTER":
            print(colorize_station(jjj[0]) if len(jjj) > 0 else f"{red}[!] No station found with that name! [!]{reset}")
            for i in metro_data:
                if jjj[0].lower() == i.strip().split(',')[1].lower():
                    print()
                    print("-------")
                    print(f"Full Station Name: {colorize_station(clean_station_name(i.strip().split(',')[1]))}")
                    print(f"Station Code: {i[4].split(" ")[0]}-{i.strip().split(',')[0]}")
                    print(f"Line Name: {i.strip().split(',')[3]}")
                    print(f"Latitude: {i.strip().split(',')[-6]}")
                    print(f"Longitude: {i.strip().split(',')[-5]}")
                    print(f"Layout: {i.strip().split(',')[5]}")
                    print(f"Est. Year: {i.strip().split(',')[4]}")
                    print("-------")
                    break
            time.sleep(1)
            print(f"{saffron}[!] Press any key to exit [!]{reset}")
            # input_key()
            return input_key()
        else:
            idk += x
        
        jjj = []
        
        for i in metro_data:
            if idk.lower() in i.lower():
                jjj.append(i.strip().split(',')[1])



# [!] SOME GLOBAL VAR FOR THE GRAPH FUNCTION!! [!]
# THESE ARE JUST HERE IN CASE I NEED THEM LATER ON WHEN DEBUGGING OR CHANGING SOME STUFF
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
    """
    ---
    SCALE: int -> scale factor for lat lon to x y conversion
    ---
    returns: dict -> mapping of (x, y) coordinates to (station name, color)
    ---
    simple function to build a dictionary for the metro map
    """
    make_dict = {}
    for i in metro_data:
        data = i.strip().split(',')
        lat = float(data[-6])
        lon = float(data[-5])
        make_dict[abs(int((lat-max_lat)*SCALE)), int((lon-min_lon)*SCALE)] = (data[1], colors[data[3]])
    return make_dict

def graph_renderer():
    """
    ---
    no parameters [!]
    ---
    returns: None -> no returns prints directly to buffer
    ---
    Renders the metro map in terminal using ascii characters and ANSI escape codes for colors
    [!] Simple to use i have all keys listed q,c,+,-,=,s all of them work amazingly [!]
    [!] Arrow keys to navigate the map up, down, left, right [!]
    """
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
                print(f"{(f"{make_dict[(x+ou1, y+ou2)][1]}* {make_dict[(x+ou1, y+ou2)][0] if c else ''}{reset}" if len(make_dict[(x+ou1, y+ou2)][0]) < (shutil.get_terminal_size().columns -2 - y) else " ") if (x+ou1, y+ou2) in make_dict else " "}", end="")
                y+=(len(f"* {make_dict[(x+ou1, y+ou2)][0] if c else ''}")-1 if len(make_dict[(x+ou1, y+ou2)][0]) < (shutil.get_terminal_size().columns -2 - y) else 0) if ((x+ou1, y+ou2) in make_dict) else 0
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
        

# [!] ACTUAL CALULATION FUNCTIONS ARE BELOW [!]
def fare_calc(distance, day):
    """
    ---
    distance: int -> distance in km
    day: str -> 'y' for sunday and 'n' for weekday
    ---
    returns: int -> fare in rupees
    ---
    fare calculation based on dmrc fare chart
    minimum -> 11rupees 
    maximum -> 64rupees
    """
    # all of this is from the dmrc data i found online and also mentioned in report, so its official
    # i have added it in the readme too (add in production release)
    if distance <= 2:
        return 11

    if day.lower() == 'y':
        if distance <= 5:
            return 11
        elif distance <= 12:
            return 21
        elif distance <= 21:
            return 32
        elif distance <= 32:
            return 43
        else:
            return 54
    else:
        if distance <= 5:
            return 21
        elif distance <= 12:
            return 32
        elif distance <= 21:
            return 43
        elif distance <= 32:
            return 54
        else:
            return 64

def time_calc(distance_km):
    """
    ---
    distance_km: int -> distance in km
    ---
    returns: int -> time in minutes
    ---
    function to calculate time taken for a journey
    assuming the avg speed of metro is 34.3 km/h
    34.3 km in 60 mins
    1 km in 60/34.3 mins
    distance_km in distance_km * (60/34.3) mins
    """
    return distance_km * (60 / 34.3)

def ticket_valid_time(distance_km):
    """
    ---
    distance_km: int -> distance in km
    ---
    returns: int -> validity time in minutes
    ---
    function to return ticket valid time based on distance
    """
    
    if distance_km <= 2:
        return 65
    elif distance_km <= 21:
        return 100
    elif distance_km <= 32:
        return 180
    return 'Forever'

def time_converter(time):
    """
    ---
    time: int -> time in minutes
    ---
    returns: str -> in HH:MM [PEAK/OFF-PEAK] format
    ---
    just divmod to convert min to HH:MM and fstring to format it nicely
    08:00-10:00 and 17:00-19:00 are peak hours
    00:00-08:00, 10:00-17:00 and 19:00-24:00 are off-peak hours
    360 mins = 6:00 AM
    1380 mins = 11:00 PM
    """
    x,y = divmod(time, 60)
    return f"{x:02}:{y:02} {'[PEAK]' if 8<=x<10 or 17<=x<19 else '[OFF-PEAK]'}" #02 zero padded fstring

def suggestions(text1):
    """
    ---
    no parameters [!]
    ---
    returns: None -> just prints suggestions when typing input
    ---
    Quick function to give suggestions when typing station names
    - takes input char by char
    - matches with metro_data
    - prints suggestions
    - loops until enter is pressed
    """
    idk = ''
    jjj = []
    while True:
        clear_screen()
        print()
        print()
        
        print(f"{text1} : {idk}", end="\n")
        print()
        print("Suggestions: ")
        kkkk = jjj[:10] if len(jjj) > 10 else jjj
        print(" | " + ", ".join(i for i in kkkk) + " | ")
        
        x = input_key()
        if x == "BACKSPACE":
            idk = idk[:-1]
        elif x == "ENTER":
            return jjj[0] if jjj else idk
        else:
            idk += x
        
        jjj = []
        
        for i in metro_data:
            if idk.lower() in i.lower():
                jjj.append(i.strip().split(',')[1])
        
        # time.sleep(0.1)
# suggestions("enter station 1 name")
def metro_timings_real(loc, line, time):
    """
    ---
    loc: str -> station name
    line: str -> metro line
    time: int -> time in HH:MM format
    ---
    returns: str -> outcome of the computations 
    ---
    simple function to center text
    """
    line = line + " line" if "line" not in line.lower() else line

    # time is in HH:MM format so just splitting
    x, y = map(int, time.split(':'))
    if y > 59 or y < 0:
        return f'\033[38;2;237;28;36m[!] Invalid minutes value: {y}. It should be between 0 and 59.\033[0m'

    mins = x * 60 + y
    if mins < 360 or mins > 1380:
        no_service()
        return 0
    def is_peak(t):
        return (480 <= t < 600) or (1020 <= t < 1140)


    def interval(t):
        return 4 if is_peak(t) else 8

    for row in metro_data:
        cols = row.strip().split(',')
        station = cols[1].lower()
        metro_line = cols[3].lower()
        first_time = int(cols[-2])

        if loc.lower() in station and line.lower() in metro_line:
            tym = first_time  # ffffff

            # need to hold previous state so now we are using 3 tym (time) variables
            if mins < tym:
                tym1 = tym + interval(tym)
                tym2 = tym1 + interval(tym1)
                tym3 = tym2 + interval(tym2)
                return f"""
                \033[38;2;237;28;36mThe first metro from {loc} on {line} line is at {time_converter(tym)}.\033[0m
                Subsequent trains are available at -> {time_converter(tym1)}, {time_converter(tym2)}, {time_converter(tym3)}.
                """
            o = tym
            while o < mins:
                o += interval(o)

            tym = o
            tym1 = tym + interval(tym)
            tym2 = tym1 + interval(tym1)
            tym3 = tym2 + interval(tym2)

            return f"""
            \033[38;2;237;28;36mThe Metro from {loc} on {line} line is at {time_converter(tym)}.\033[0m
            Subsequent trains are available at -> {time_converter(tym1)}, {time_converter(tym2)}, {time_converter(tym3)}.
            """

    return f'\033[38;2;237;28;36m[!] No station has/contains the name {loc} on {line} line.\033[0m'

def journey_plan_idk(loc1, loc2, day, time):
    """
    ---
    loc1: str -> station name
    loc2: str -> destination name
    day: str -> day of the week
    time: str -> time in HH:MM format
    ---
    returns: 1/Truthy -> if program ran successfully
    ---
    journey_plan calculator 
    """
    
    x, j = "", ""
    for i in metro_data:
        if loc1.lower() in i.lower():
            x = i if x == "" else x
        if loc2.lower() in i.lower():
            j = i if j == "" else j
            
    print(x, j)
    x = x.strip().split(',')
    j = j.strip().split(',') 
    
    changes = []
    if x[3] != j[3]:
        for k in metro_data:
            
            k = k.strip().split(',') 
            if k[3] == x[3] and k[-2] == j[3].split(' ')[0]:
                print("Change at ", k[1])
                changes.append(k)
        if not changes:
            print("No direct route found, try going xyz")
            return 0
    else:
        print("Direct route available on", x[3])

    print(f"From {loc1} to {loc2} on {day} at {time} hours")
    return 1

# [!] SETTING UP DATA FOR DFS SEARCH - **took AI assistance for DFS** [!]
data123 = []
for i in metro_data:
    data123.append(i.strip().split(','))

def clean_station_name(s):
    """
    ---
    s: str -> station name
    ---
    returns: None -> if input is None or "none"
             str -> cleaned station name
    ---
    cleans all the station names by removing using regex to remove brackets and their contents
    """
    if s is None:
        return None
    s = s.strip()
    if s.lower() == "none":
        return None
    s = re.sub(r"\s*\[.*?\]", "", s)
    return s.strip()

def is_line_name(x):
    """
    ---
    x: str -> metro line name
    ---
    returns: bool -> x in dict of line colors True/False
    ---
    returns True if x is a line name based on color names
    """
    if x is None:
        return False
    x = x.strip().lower()
    return x in ["blue","yellow","pink","red","green","violet","magenta","orange","aqua","gray"]

def build_station_graph(data123):
    """
    ---
    data123: list -> list of metro station data
    ---
    returns: graph, dist_map -> dictionary of station connections and distance map
    ---
    builds a graph of metro stations and their connections
    - creates adjacency list for stations
    - creates distance map for stations
    - groups stations by line for direct connections
    - adds connections based on line groups
    """
    graph = {}
    dist_map = {}
    line_groups = {}

    for row in data123:
        station = clean_station_name(row[1])
        line = row[3].strip()
        dist = float(row[2])

        if station not in graph:
            graph[station] = set()

        dist_map[station] = dist

        if line not in line_groups:
            line_groups[line] = []
        line_groups[line].append(station)

        con2 = clean_station_name(row[-4])
        con1 = clean_station_name(row[-3])

        for c in (con1, con2):
            if c is None:
                continue
            if is_line_name(c):
                continue
            if c not in graph:
                graph[c] = set()
            graph[station].add(c)
            graph[c].add(station)

    for line, stations in line_groups.items():
        for i in range(len(stations) - 1):
            a, b = stations[i], stations[i+1]
            graph[a].add(b)
            graph[b].add(a)

    return graph, dist_map

def path_distance(path, dist_map):
    """
    ---
    path: int -> scale factor for lat lon to x y conversion
    ---
    returns: dict -> mapping of (x, y) coordinates to (station name, color)
    ---
    simple function to build a dictionary for the metro map
    """
    d = 0
    for i in range(len(path)-1):
        d += abs(dist_map[path[i+1]] - dist_map[path[i]])
    return d

def find_paths(graph, start, end, dist_map, max_len=30):
    """
    ---
    graph: dict -> adjacency list of metro stations
    start: str -> starting station
    end: str -> ending station
    dist_map: dict -> distance map of stations
    max_len: int -> maximum path length to explore (to prevent timeouts)
    ---
    returns: top3: nested list -> top 3 shortest paths with distances
    ---
    finds all paths from start to end using DFS and returns top 3 shortest paths
    """
    all_paths = []

    def dfs(cur, end, visited, path):
        """
        ---
        cur: int -> current station
        end: int -> ending station
        visited: set -> set of visited stations
        path: list -> current path being explored
        ---
        returns: None -> just appends found paths to all_paths
        ---
        recursive dfs function to explore all paths from cur to end
        """
        if len(path) > max_len:
            return
        if cur == end:
            all_paths.append(path[:])
            return
        for nxt in graph[cur]:
            if nxt not in visited:
                visited.add(nxt)
                path.append(nxt)

                dfs(nxt, end, visited, path)
                
                path.pop()
                visited.remove(nxt)

    dfs(start, end, {start}, [start])

    scored = []
    for p in all_paths:
        scored.append((path_distance(p, dist_map), p))

    for i in range(len(scored)):
        for j in range(i + 1, len(scored)):
            if scored[i][0] > scored[j][0]:
                scored[i], scored[j] = scored[j], scored[i]

    return scored[:3] # only going to print top 3 paths

# [!] BUILDING THE GRAPH FOR JOURNEY PLANNER (only need to build once) [!]
graph, dist_map = build_station_graph(data123)

# start = clean_station_name("Uttam Nagar West")
# end = clean_station_name("Harkesh Nagar Okhla")

# top3 = find_paths(graph, start, end, dist_map)


# [!] mapping station name to line color for using in colorize_station fn [!]
station_to_line = {}

for row in data123:
    st = clean_station_name(row[1])
    ln = row[3].strip()
    station_to_line[st] = ln

def colorize_station(station):
    """
    ---
    station: str -> station name
    ---
    returns: station: str -> colored station name
    ---
    maps station and line from station_to_line and colors dict to return colored station name
    """
    line = station_to_line.get(station, None)
    if line in colors:
        return f"{colors[line]}{station}\033[0m"
    return station

# for d, p in top3:
#     colored_path = []
#     for st in p:
#         colored_path.append(colorize_station(st))
#     print(" → ".join(colored_path), "|", round(d, 2), "km", "₹" + str(fare_calc(d, "saturday")))


if __name__ == "__main__":
    clear_screen() 
    clear_screen() # x2 twice because running only once leads to the dir path still being printed in terminal
    (introduction()) # printing banner
    time.sleep(1)
    clear_screen() # clearing after the banner
    # this loop prints the dot ... loading . .. ...
    for i in range(3):
        print(loading(i))
        time.sleep(0.5)
        clear_screen()

    menu() # prints full main menu 
