# this file only contains the "big" chunks of text that ill 
# use to make it aesthetically pleasing nothing mych

import time # i m using this for almost everything this is the best module ever
import os # using this to clear the screen after each load to make it look like an nimation
import shutil # this is another amazing module ill use it rn to fix the loading centering issue
import re # using this to fix the cenrtering issue
import sys
ansi_pattern = re.compile(r'\x1b\[[0-9;]*m')
import keyinp


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
{white} ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║{reset}  
{green} ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║  
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
            key = keyinp.input_key()
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
    except:
        print("byebye")
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
    x = keyinp.input_key()
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
        day = input(("\t\t\tAre you travelling on a weekday? (y/n): "))
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
        print(f"\t\t\tPlanning journey from {x} to {y} on a {'weekday' if day.lower() == 'y' else 'weekend'} at {idk_hrs}:{idk_mins}...")
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
        print(f"\t\t\t:D Planning journey from {x} to {y} on a {'weekday' if day.lower() == 'y' else 'weekend'} at {idk_hrs}:{idk_mins}...")
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
{white}██╔████╔██║███████║██████╔╝{reset}  
{green}██║╚██╔╝██║██╔══██║██╔═══╝  
██║ ╚═╝ ██║██║  ██║██║     
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝ {reset}    
                           
    """

    print(center_ansi(x, shutil.get_terminal_size().columns))
    return 1

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

    no_service()