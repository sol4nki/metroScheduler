# this file only contains the "big" chunks of text that ill 
# use to make it aesthetically pleasing nothing mych

import time # i m using this for almost everything this is the best module ever
import os # using this to clear the screen after each load to make it look like an nimation
import shutil # this is another amazing module ill use it rn to fix the loading centering issue
import re # using this to fix the cenrtering issue
ansi_pattern = re.compile(r'\x1b\[[0-9;]*m')

def center_ansi(text, width):
    visible_text = ansi_pattern.sub('', text)
    pad = max(0, (width - len(visible_text)) // 2)
    return ' ' * pad + text

def introduction():
    saffron = "\033[38;2;255;153;51m"
    white   = "\033[38;2;255;255;255m"
    green   = "\033[38;2;19;136;8m"
    reset   = "\033[0m"
    blue = "\033[38;2;50;50;255m"

    x = f"""
{saffron}
        ██████╗ ███████╗██╗     ██╗  ██╗██╗    ███╗   ███╗███████╗████████╗██████╗  ██████╗          
        ██╔══██╗██╔════╝██║     ██║  ██║██║    ████╗ ████║██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗         
        ██║  ██║█████╗  ██║     ███████║██║    ██╔████╔██║█████╗     ██║   ██████╔╝██║   ██║         
{white}        ██║  ██║██╔══╝  ██║     ██╔══██║██║    ██║╚██╔╝██║██╔══╝     ██║   ██╔══██╗██║   ██║         
        ██████╔╝███████╗███████╗██║  █{blue}█║██║    ██║ ╚═╝ ██{white}║███████╗   ██║   ██║  ██║╚██████╔╝         
        ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚{blue}═╝╚═╝    ╚═╝     ╚═{white}╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝          
                                                                                                     

██╗    ██╗███████╗██╗      ██████╗ ███{blue}███╗ ███╗   ███╗███{white}████╗███████╗    ██╗   ██╗ ██████╗ ██╗   ██╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝██╔════╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║
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
    green   = "\033[38;2;19;136;8m"
    reset   = "\033[0m"
    blue = "\033[38;2;0;0;255m"
    
    dot1 = f"""     
{saffron}██  {reset}
"""
    dot2 = f"""     
{saffron}██ {white}██{reset}
 
"""
    dot3 = f"""     
{saffron}██ {white}██ {green}██{reset}
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
    green   = "\033[38;2;19;136;8m"
    reset   = "\033[0m"
    blue = "\033[38;2;50;50;255m" 
    width = shutil.get_terminal_size().columns

    x = f"""
{saffron}███╗   ███╗███████╗███╗   ██╗██╗   ██╗
████╗ ████║██╔════╝████╗  ██║██║   ██║
{white}██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
{green}██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ {reset}
    """
    

    
    active = 0
    menu_text = ["Display Map", "Metro Timings", "Ride journey planner", "More Info", "Exit"]
    while True:
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
        time.sleep(0.1)
        active = active+1 if active < len(menu_text) else active-1
        clear_screen()
        # clear_screen()
        
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
    green   = "\033[38;2;19;136;8m"
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

if __name__ == "__main__":
    clear_screen() # just using this because i want a clear canvas using python functional notation name_xyz not javascript nameXyz
    clear_screen() # twice because running only once leads to the dir path still being printed
    print(introduction())
    time.sleep(1)
    clear_screen()
    for i in range(3):
        print(loading(i))
        time.sleep(0.5)
        clear_screen()

# menu()
# time_display()

no_service()