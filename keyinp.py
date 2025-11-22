# because macos, linux && windows have diff clear screen + input methods and modules 
# i m making a specific file for the up down side side key input detection

import sys, os

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

# x = """1,Yamuna Bank,0,Blue line branch,10-05-2009,At-Grade,28.62331,77.26792,None,None,0
# 2,Laxmi Nagar,1.3,Blue line branch,06-01-2010,Elevated,28.63064,77.27749,None,None,8
# 3,Nirman Vihar,2.4,Blue line branch,06-01-2010,Elevated,28.63663,77.28683,None,None,16
# 4,Preet Vihar,3.4,Blue line branch,06-01-2010,Elevated,28.64171,77.29543,None,None,24
# 5,Karkar Duma [Conn: Pink],4.6,Blue line branch,06-01-2010,Elevated,28.64849,77.30558,Pink,None,32
# 6,Anand Vihar [Conn: Pink],5.7,Blue line branch,06-01-2010,Elevated,28.64695,77.31603,Pink,None,40
# 7,Kaushambi,6.5,Blue line branch,14-07-2011,Elevated,28.64544,77.32432,None,None,48
# 8,Vaishali,8.1,Blue line branch,14-07-2011,Elevated,28.64997,77.33974,None,None,56
# """

# x = x.strip().split('\n')
# for i in x:
#     i = i.strip().split(',')
#     # print(i)
#     print(i[0] + ',' + i[1])