#

def next_turn():
    if turn == "X":
        turn = "O"
        not_turn = "X"
    else:
        turn = "X"
        not_turn = "O"

# Defining some variables
                                

# Design ASCII version of board (Appearance of game)
"""
Should look like this!
1   |   2   |   3
 _______________
4   |   5   |   6
 _______________
7   |   8   |   9
"""

# Checking for Wins.
"""
Possible wins would include:
123
456
789
147
258
369
159
753

"""


def check_win():

    if pos_1 == "X" and pos_2 == "X" and pos_3 == "X":
        Winner_X ()
    elif pos_4 == "X" and pos_5 == "X" and pos_6 == "X":
        Winner_X()
    elif pos_7 == "X" and pos_8 == "X" and pos_9 == "X":
        Winner_X()
    elif pos_1 == "X" and pos_4 == "X" and pos_7 =="X":
        Winner_X()
    elif pos_2 == "X" and pos_5 == "X" and pos_8 == "X":
        Winner_X()
    elif pos_3 == "X" and pos_6 == "X" and pos_9 =="X":
        Winner_X()
    elif pos_1 == "X" and pos_5 == "X" and pos_9 == "X":
        Winner_X()
    elif pos_3 == "X" and pos_5 == "X" and pos_7 == "X":
        Winner_X()
    elif pos_1 == "O" and pos_2 == "O" and pos_3 == "O":
        Winner_O()
    elif pos_4 == "O" and pos_5 == "O" and pos_6 == "O":
        Winner_O()
    elif pos_7 == "O" and pos_8 == "O" and pos_9 == "O":
        Winner_0()
    elif pos_1  == "O" and pos_4 == "O" and pos_7 == "O":
        Winner_O()
    elif pos_2 == "O" and pos_5 == "O" and pos_8 == "O":
        Winner_O()
    elif pos_3 == "O" and pos_6 == "O" and pos_9 == "O":
        Winner_O()
    elif pos_1 == "O" and pos_5 == "O" and pos_9 == "O":
        Winner_O()
    elif pos_3 == "O" and pos_5 == "O" and pos_7 == "O":
        Winner_0()

def Winner_O():
    print("************************************")
    print("|        CONGRADULATIONS!!         |")
    print("|           X WINS!!               |")
    print("************************************")


def Winner_X():
    print("************************************")
    print("|        CONGRADULATIONS!!         |")
    print("|           O WINS!!               |")
    print("************************************")















print("**************************************************************************")
print("**************************************************************************")
print("***      The numbers on the screen represent empty spaces.             ***")
print("***To play the game, enter the number to replace with an 'X' or an 'O'.***")
print("**************************************************************************")
print("**************************************************************************")










class position_board():
    def __init__(self, one, two, three, four, five, six, seven, eight, nine):
        position_board.one = one
        position_board.two = two
        position_board.three = three
        position_board.four = four
        position_board.five = five
        position_board.six = six
        position_board.seven = seven
        position_board.eight = eight
        position_board.nine = nine

position_board1 = position_board(1, 2, 3, 4, 5, 6, 7, 8, 9)



def display_board():
    print(position_board1.one, "  |  ", position_board1.two, "  |  ", position_board1.three)
    print(" _______________ ")
    print(position_board1.four, "  |  ", position_board1.five, "  |  ", position_board1.six)
    print(" _______________")
    print(position_board1.seven, "  |  ", position_board1.eight, "  |  ", position_board1.nine)



#Display Initial Board


def play_game():
    display_board()
    turn = "X"
    not_turn = "O"
    position = input("'Position your 'X' or 'O': (Using numbers 1-9): ")
    if position == "1" and pos_1 != not_turn:
        position_board1.one = turn
        next_turn()
        display_board()
        pos_1 =  turn
        position = input("'Position your 'X' or 'O': (Using numbers 1-9): ")
    elif position == 2 and pos_1 != not_turn:
         position_board1.two = turn
         next_turn()
         display_board()
         pos_2 =  turn
         position = input("'Position your 'X' or 'O': (Using numbers 1-9): ")
    elif position == 3 and pos_2 != not_turn:
         position_board1.three = turn
         next_turn()
         display_board()
         pos_3 =  turn
         position = input("'Position your 'X' or 'O': (Using numbers 1-9): ")
    elif position == 4 and pos_4 and pos_3 != not_turn:
         position_board1.four = turn
         next_turn()
         display_board()
         pos_4 =  turn
         position = input("'Position your 'X' or 'O': (Using numbers 1-9): ")
    elif position == 5 and pos_5 != not_turn:
         position_board1.five = turn
         next_turn()
         display_board()
         pos_5 =  turn
         position = input("'Position your 'X' or 'O': (Using numbers 1-9): ")
    elif position == 6 and pos_6 != not_turn:
         position_board1.six = turn
         next_turn()
         display_board()
         pos_6 =  turn
         position = input("'Position your 'X' or 'O': (Using numbers 1-9): ")
    elif position == 7 and pos_7 != not_turn:
         position_board1.seven = turn
         next_turn()
         display_board()
         pos_7 =  turn
         position = input("'Position your 'X' or 'O': (Using numbers 1-9): ")
    elif position == 8 and pos_8 != not_turn:
         position_board1.eight = turn
         next_turn()
         display_board()
         pos_8 =  turn
         position = input("'Position your 'X' or 'O': (Using numbers 1-9): ")
    elif position == 9 and pos_9 != not_turn:
         position_board1.nine = turn
         next_turn()
         display_board()
         pos_0 =  turn
         position = input("'Position your 'X' or 'O': (Using numbers 1-9): ")

def reset():
    position_board1.one = 1
    position_board1.two = 2
    position_board1.three = 3
    position_board1.four = 4
    position_board1.five = 5
    position_board1.six = 6
    position_board1.seven = 7
    position_board1.eight = 8
    position_board1.nine = 9
    pos_1 = 1
    pos_2 = 2
    pos_3 = 3
    pos_4 = 4
    pos_5 = 5
    pos_6 = 6
    pos_7 = 7
    pos_8 = 8
    pos_9 = 9


reset()
play_game()








