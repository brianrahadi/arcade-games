from turtle import Turtle, Screen
from ponggame.main import play_pong
from snakegame.main import play_snake
from crossinggame.main import play_crossing

title = 'Menu'
text = '\nEnter 1 to play pong (Use AWSD and arrow key). \nEnter 2 to play snake (Use arrow key). \nEnter 3 to play crossing game (Use arrow key). \nEnter 4 to quit'

screen = Screen()
screen.setup(0, 0)


def main_screen():
  while True:
    answer = screen.numinput(title=title, prompt=text, minval=1, maxval=4)
    screen.clearscreen()
    if answer == 1:
      play_pong(main_screen)
      
    elif answer == 2:
      play_snake(main_screen)
    elif answer == 3:
      play_crossing(main_screen)
    elif answer == 4:
      screen.clearscreen()
      screen.bye()

main_screen()
