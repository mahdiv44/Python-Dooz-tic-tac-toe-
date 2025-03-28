from termcolor import colored
print(colored("-----------------Welcome to Tic Tac Toe Game --------------", "yellow"))
board = list(range(1, 10))
winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
moves = ((1, 7, 3, 9), (5,), (2, 4, 6, 8))


def print_board():
    j = 1
    for i in board:
        end = " "
        if j % 3 == 0:
            end = "\n\n"
        if i == "X":
            print(colored(f"[{i}]", "red"), end=end)  
        elif i == "O":
            print(colored(f"[{i}]", "blue"), end=end)
        else:
            print(f"[{i}]", end=end)
        j += 1

def computer_move(pc, player):
    mv = -1
    for i in range(1, 10):
        if make_move(board, pc, i, True)[1]:
            mv = i 
            break   

    if mv == -1:
        for j in range(1, 10):
            if make_move(board, player, j, True)[1]:
                mv = j
                break

    if mv == -1:
        for tup in moves:
            for m in tup:
                if mv == -1 and can_move(board, m):
                    mv = m
                    break
    return make_move(board, pc, mv)                 

def make_move(brd, plyr, mve, undo=False):
    if can_move(brd, mve): 
        brd[mve-1] = plyr
        win = is_winner(brd, plyr)
        if undo: 
            brd[mve-1] = mve
        return True, win
    return False, False

def can_move(brd, mve):
    if mve in range(1, 10) and isinstance(brd[mve-1], int):
        return True
    return False

def is_winner(brd, plyr):
    for tup in winners:
        win = True
        for j in tup:
            if brd[j] != plyr:
                win = False
                break
        if win:
            return True  
    return False  

def empty_space():
    return board.count("X") + board.count("O") != 9

def play_game():
    player = "O"
    pc = "X"
    
    while empty_space():
        print_board()
        try:
            move = int(input(colored("Enter your choice (1-9) : ", "white")))
        except ValueError:
            print(colored("Invalid input! Please enter a number between 1 and 9.", "red"))
            continue
        
        moved, won = make_move(board, player, move)
        if not moved:
            print(colored("Invalid number!!!", "red"))
            continue
        if won:
            print_board()  
            print(colored("YOU WON!!", "green"))
            break
        
        moved, won = computer_move(pc, player)
        if won:
            print_board()  
            print(colored("Game Over!!! Computer Won!", "red"))
            break
        
        if not empty_space(): 
            print_board()
            print(colored("It's a Tie!!!", "yellow"))
            break


play_game()