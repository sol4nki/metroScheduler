# this file only contains the "big" chunks of text that ill 
# use to make it aesthetically pleasing nothing mych

import time # i m using this for almost everything this is the best module ever
import os # using this to clear the screen after each load to make it look like an nimation
import shutil # this is another amazing module ill use it rn to fix the loading centering issue




def introduction():
    saffron = "\033[38;2;255;153;51m"
    white   = "\033[38;2;255;255;255m"
    green   = "\033[38;2;19;136;8m"
    reset   = "\033[0m"
    blue = "\033[38;2;0;0;255m"

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
    return x

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
    
    dot1 = """     
██  
"""
    dot2 = """     
██ ██
 
"""
    dot3 = """     
██ ██ ██
"""
    width = shutil.get_terminal_size().columns
    match i%3: 
        
        case 0:
            return "\n\n\n".join(line.center(width) for line in dot1.split("\n"))
        case 1:
            return "\n\n\n".join(line.center(width) for line in dot2.split("\n"))
        case 2:
            return "\n\n\n".join(line.center(width) for line in dot3.split("\n"))


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


if __name__ == "__main__":
    clear_screen() # just using this because i want a clear canvas using python functional notation name_xyz not javascript nameXyz
    clear_screen() # twice because running only once leads to the dir path still being printed
    print(introduction())
    time.sleep(1)
    clear_screen()
    for i in range(10):
        print(loading(i))
        time.sleep(0.5)
        clear_screen()
# while True:
#     print("="*len("|| "+ time.strftime("%H:%M:%S", time.localtime()) + " ||"))
#     print("|| "+ time.strftime("%H:%M:%S", time.localtime()), end=" ||\n")
#     print("="*len("|| "+ time.strftime("%H:%M:%S", time.localtime()) + " ||"))
#     time.sleep(1)
#     clear_screen()
time_display()