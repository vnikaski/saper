from mouse import *
from create_board import create_board
from random import randint
from initate_graphics import  ini_graphics
from click import click
from you_won import check_flags
from flag import update_flagged





num_of_bombs = randint(5,20)
game_on = True
window_width = 300
window_height = 300

def main():
    global num_of_bombs, game_on
    ini_myszki()
    board = create_board(10, 10, num_of_bombs, window_height, window_width)
    ini_graphics(board, window_width, window_height, num_of_bombs)
    while game_on:
        click(board, window_width, window_height, game_on, num_of_bombs)
        check_flags(board, update_flagged(board), num_of_bombs, window_height, window_width, game_on)
main()
