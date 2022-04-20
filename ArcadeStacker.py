import curses
from curses import wrapper
import time
import keyboard

def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_RED)
    REDSQUARE = curses.color_pair(1)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLACK)
    BLACKSQUARE = curses.color_pair(2)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    YELLOW = curses.color_pair(3)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLUE)
    BLUESQUARE = curses.color_pair(4)
          
    stdscr.clear()
    
    score = 0
    stdscr.addstr("Score: ", curses.A_BOLD)
    stdscr.addstr(0, 7, str(score), YELLOW)
    stdscr.addstr(0, 22, "@benmcca", curses.A_BOLD)
    stdscr.addstr(1, 0, "------------------------------")
    stdscr.addstr(2, 14, "  ", REDSQUARE)
    
    i = 2    
    row = 3
    back = False
    speed = 0.15
    increase = 0.9                
    play = True

    while play:

        while back == False:
            if i == 30:
                back = True
                break 

            stdscr.addstr(row, i, "  ", REDSQUARE)
            stdscr.refresh()
            stdscr.addstr(row, i - 2, "  ", BLACKSQUARE)
            stdscr.refresh()
            time.sleep(speed)
            i += 2

            if keyboard.is_pressed(' '):
                if i == 16:
                    score += 1
                    stdscr.addstr(0, 7, str(score), YELLOW)
                    time.sleep(0.1)
                    speed *= increase
                    row += 1
                else:
                    stdscr.addstr(row, i - 2, "  ", BLUESQUARE)
                    stdscr.addstr(row + 1, 14, str(score), YELLOW)
                    stdscr.addstr(row + 2, 10, "PLAY AGAIN")
                    stdscr.refresh()
                    play = False 
                    time.sleep(1.5)
                    wrapper(main)                                                        
   
                  
        while back == True:
            if i == 2:
                back = False
                break                       

            i -= 2
            stdscr.addstr(row, i - 2, "  ", REDSQUARE)
            stdscr.refresh()
            stdscr.addstr(row, i, "  ", BLACKSQUARE)
            stdscr.refresh()
            time.sleep(speed)

            if keyboard.is_pressed(' '): 
                if i == 16:
                    score += 1
                    stdscr.addstr(0, 7, str(score), YELLOW)               
                    time.sleep(0.1)
                    speed *= increase
                    row += 1       
                else:
                    stdscr.addstr(row, i - 2, "  ", BLUESQUARE)
                    stdscr.addstr(row + 1, 14, str(score), YELLOW)
                    stdscr.addstr(row + 2, 10, "PLAY AGAIN")
                    stdscr.refresh()
                    play = False 
                    time.sleep(1.5)
                    wrapper(main)
                    
    stdscr.getch()              
     
wrapper(main)          