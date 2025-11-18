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
