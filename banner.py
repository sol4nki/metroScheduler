# this file only contains the "big" chunks of text that ill 
# use to make it aesthetically pleasing nothing mych

import time # i m using this for almost everything this is the best module ever
import os # using this to clear the screen after each load to make it look like an nimation

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
    dot1 = """     
██╗
╚═╝     
"""
    dot2 = """     
██╗ ██╗
╚═╝ ╚═╝
"""
    dot3 = """     
██╗ ██╗ ██╗
╚═╝ ╚═╝ ╚═╝
"""
    match i%3: 
        
        case 0:
            return '\t\t\t' + dot1
        case 1:
            return '\t\t\t' + dot2
        case 2:
            return '\t\t\t' + dot3

def clearScreen():
    """
    # I am using this because on reading os.system('clear') manual
    # it states it has cls and clear diff for windows and linux and a solution
    # on stackoverflow suggested to use nt so i am going with nt
    """
    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')


if __name__ == "__main__":
    clearScreen() # just using this because i want a clear canvas
    clearScreen() # twice because running only once leads to the dir path still being printed
    print(introduction())
    time.sleep(1)
    for i in range(10):
        print(loading(i))
        time.sleep(0.5)
        clearScreen()