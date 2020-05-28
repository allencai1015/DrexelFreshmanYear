''' Took tips from https://www.youtube.com/watch?v=y7AKtWGOPAE to try to program the hard AI and
https://www.youtube.com/watch?v=UYgyRArKDEs to make the basic game
Wrote my own code to let the player choose between playing against another human or an AI
Wrote my own code to check for ties and to program simplistic AI to play against.  ''' 
import numpy as np
import random
import time

ROW_COUNT = 6
COL_COUNT = 7
board = np.zeros((ROW_COUNT, COL_COUNT)) # board is a numpy array full of zeroes

def drop_piece(board, row, col, piece) :
    """Replaces the zero at that row and column of the array with the player's piece."""
    board[row][col] = piece
    
def is_valid_location(board, col) :
    """Checks that column isn't full yet. if full, not allowed to put in a piece."""
    return board[ROW_COUNT-1][col] == 0      

def get_next_open_row(board, col):
    """Finds the lowest row in the column that isn't already filled."""
    for r in range(ROW_COUNT) :
        if board[r][col] == 0:
            return r
        
def winning_move(board, piece) :
    """Checks if placing a piece somewhere would make a connect 4 horizontally, vertically, or diagonally."""
    # Horizontal
    for c in range(COL_COUNT - 3) : # minus 3 makes it so you can't start a "4 in a row" outside of the board
        for r in range(ROW_COUNT) :
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece :
                return True
    # Vertical
    for c in range(COL_COUNT) :
        for r in range(ROW_COUNT - 3) : # minus 3 makes it so you can't start a "4 in a row" outside of the board
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece :
                return True
    # Diagonal Postive Slope
    for c in range(COL_COUNT - 3) :
        for r in range(ROW_COUNT - 3) : # minus 3 makes it so you can't start a "4 in a row" outside of the board
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece :
                return True
    # Diagonal Negative Slope
    for c in range(COL_COUNT - 3) :
        for r in range(3, ROW_COUNT) : # minus 3 makes it so you can't start a "4 in a row" outside of the board
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece :
                return True
            
def is_tie(board) :
    """Checks every space on the board to see if any are still 0 (empty).
    If not, board is full and the game ends in a tie."""
    if np.any(board[:, :] == 0) == False:   # found on https://stackoverflow.com/questions/7088625/what-is-the-most-efficient-way-to-check-if-a-value-exists-in-a-numpy-array
        return True

def print_board(board):
    """ prints out the board flipped so the pieces stack from bottom to top."""
    print(np.flip(board, 0))
    
print_board(board)
game_over = False
turn = 0

# Code allows player to select whether the game will be played with 2 humans or 1 human and an AI.
human_VS_human = False
human_VS_AI = False
easyAI = False
hardAI = False

opponent_type = input("\n Welcome! Above is the Connect 4 board. Would you like to play with 2 humans, or with 1 human against an AI? Type human for human or AI for an AI.")
if opponent_type.upper() == "HUMAN":
    human_VS_human = True
elif opponent_type.upper() == "AI":
    human_VS_AI = True
else :
    print("Invalid command. Refresh to try again!")
    
if human_VS_AI == True :
    difficulty = input("Okay, do you want to play against an easy or hard AI? Type easy for easy or hard for hard.")
    if difficulty.upper() == "EASY":
        easyAI = True
    elif difficulty.upper() == "HARD":
        hardAI = True
    else :
        print("Invalid command. Refresh to try again!")

# handles human_VS_human games
while human_VS_human and (not game_over) :
    while turn == 0 and (not game_over) : # while loop ensures the game doesn't move on until a valid move is inputted
        col = int(input("\nPlayer 1, choose a column by inputting an integer from 0 to 6:"))
        if 0 <= col <= 6 :
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 1)
                turn += 1
                turn %= 2
                print_board(board)
                if winning_move(board,1) :
                    print("Player 1 wins!")
                    game_over = True
                if is_tie(board) :
                    print("Tie game. Board was filled before either player won.")
                    game_over = True
        else :
            print("\n Invalid command. Column may be already full, or you may have mistyped.\n")
    while turn == 1 and (not game_over) : # while loop ensures the game doesn't move on until a valid move is inputted
        col = int(input("\nPlayer 2, choose a column by inputting an integer from 0 to 6:"))
        if 0 <= col <= 6 :
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 2)
                turn += 1
                turn %= 2
                print_board(board)
                if winning_move(board,2) :
                    print("Player 2 wins!")
                    game_over = True
                if is_tie(board) :
                    print("Tie game. Board was filled before either player won.")
                    game_over = True
            else :
                print("\n Invalid command. Column may be already full, or you may have mistyped.\n")
                
#handles human VS easyAI game, where the AI just selects a random column each turn
columns = [0, 1, 2, 3, 4, 5, 6] 
while easyAI and (not game_over):
    if turn == 0 : # handles player turns
        col = int(input("\nPlayer 1, choose a column by inputting an integer from 0 to 6:"))
        if 0 <= col <= 6 :
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 1)
                turn += 1
                turn %= 2
                print_board(board)
                if winning_move(board,1) :
                    print("Player 1 wins!")
                    game_over = True
                if is_tie(board) :
                    print("Tie game. Board was filled before either player won.")
                    game_over = True
            else :
                col = int(input("\n Invalid command. Column may be already full, or you may have mistyped. Player 1, choose a column by inputting an integer from 0 to 6:\n"))
    while turn == 1 and (not game_over) : # handles computer turns
        time.sleep(2)
        col = int(random.choice(columns)) # randomly selects from a list, removes from list and tries again if column is full
        print()
        if is_valid_location(board,col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
            print("The computer selected column {}\n".format(col))
            turn += 1
            turn %= 2
            print_board(board)
            if winning_move(board,2) :
                print("Player 2 wins!")
                game_over = True
            if is_tie(board) :
                print("Tie game. Board was filled before either player won.")
                game_over = True
        else :
            print("Column {} is full. Computer will no longer drop into that column.".format(col))
            columns.remove(col)
            new_col = int(random.choice(columns))
            if is_valid_location(board, new_col):
                row = get_next_open_row(board, new_col)
                drop_piece(board, row, new_col, 2)
                turn += 1
                turn %= 2
                print_board(board)
                print("The computer selected column {}\n".format(new_col)) 
                if winning_move(board,2) :
                    print("Player 2 wins!")
                    game_over = True
                if is_tie(board) :
                    print("Tie game. Board was filled before either player won.")
                    game_over = True
    
if hardAI and (not game_over):
    print("Sorry, Allen wasn't able to finish the hard AI just yet. Refresh to play again.")
    
''' EVERYTHING BELOW HERE HANDLES THE HARD AI, WHICH I COULD NOT IMPLEMENT SUCCESSFULLY
BEFORE THE DUE DATE. STILL LEFT IT IN TO SHOW MY PROGRESS AND THAT I MADE MY OWN FUNCTIONS
column_scores = [0, 10, 20, 30, 20, 10, 0]
def check_possible_win():
    """ AI makes 7 copies of the board and drops its piece into a different column
    in each copy. Then, if winning_move would evaluate to true for any of them, it
    will change that column's score in the column_scores list to 100, guaranteeing
    that the AI will choose to drop into that column.
    """
    for col in column_scores :
        board_ai_test_copy = np.copy(board) # creates a copy of the board at each step for the AI to test moves on
        col_index = column_scores.index(col)
        row = get_next_open_row(board, col_index)
        if is_valid_location(board, col_index) :
            drop_piece(board_ai_test_copy, row, col_index, 2)
            if winning_move(board_ai_test_copy, 2) == True :
                column_scores[col_index] = 1000
                print("I can win if I drop my piece in column {}!".format(col_index))
        
def check_possible_loss():
    """ AI makes 7 copies of the board and drops the player's piece into a different column
    in each copy. Then, if winning_move would evaluate to true for any of them, it
    will change that column's score in the column_scores list to 90 """
    for col in column_scores :
        board_ai_test_copy = np.copy(board) # creates a copy of the board at each step for the AI to test moves on
        col_index = column_scores.index(col)
        row = get_next_open_row(board, col_index)
        if is_valid_location(board, col_index) :
            drop_piece(board_ai_test_copy, row, col_index, 1)
            if winning_move(board_ai_test_copy, 1) == True :
                column_scores[col_index] = column_scores[col_index] + 900
                print("I can prevent the human from winning if I drop my piece in column {}!".format(col_index))

def specific_scenarios(board, piece):
    if board[0][3] == 1 or board[0][3] == 2 :
        column_scores[4] = 60
    for c in range(COL_COUNT-1) :
        for r in range(ROW_COUNT-1) :
            if board[r][c-1] == piece or board[r][c+1] == piece :
                column_scores[r] = 40
            if board[r-1][c] == piece or board[r+1][c] == piece :
                column_scores[r] = 40
            if board[r-1][c-1] == piece or board[r+1][c+1] == piece :
                column_scores[r] = column_scores[r] + 20

def invalid_selection():
    for col in column_scores :
        board_ai_test_copy = np.copy(board) # creates a copy of the board at each step for the AI to test moves on
        col_index = column_scores.index(col)
        if is_valid_location(board, col_index) == False :
            column_scores[col_index] = column_scores[col_index] - 1000

def highest_column_score(column_scores) :
    highest_score = max(column_scores)
    viable_moves = []
    for score in column_scores:
        if score == highest_score:
            viable_moves.append(score)
    chosen_move = random.choice(viable_moves)
    move_index = column_scores.index(chosen_move)
    return move_index

# handles the human vs hardAI, where the AI is coded to pick better moves
while hardAI and (not game_over) :
    while turn == 0 and (not game_over) : # while loop ensures the game doesn't move on until a valid move is inputted
        col = int(input("\nPlayer 1, choose a column by inputting an integer from 0 to 6:"))
        if 0 <= col <= 6 :
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 1)
                turn += 1
                turn %= 2
                print_board(board)
                if winning_move(board,1) :
                    print("Player 1 wins!")
                    game_over = True
                if is_tie(board) :
                    print("Tie game. Board was filled before either player won.")
                    game_over = True
            else :
                print("\n Invalid command. Column may be already full, or you may have mistyped.\n")
    while turn == 1 and (not game_over) :
        time.sleep(2)
        column_scores = [0, 10, 20, 30, 20, 10, 0]
        check_possible_win()
        check_possible_loss()
        invalid_selection()
        specific_scenarios(board, 2)
        col = highest_column_score(column_scores)
        print(column_scores) 
        print()
        if is_valid_location(board,col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
            print("The computer selected column {}\n".format(col))  
            turn += 1
            turn %= 2
            print_board(board)
            if winning_move(board,2) :
                print("Player 2 wins!")
                game_over = True
            if is_tie(board) :
                print("Tie game. Board was filled before either player won.")
                game_over = True
        else :
            col = int(random.randint(0, 6))
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 2)
                print("The computer selected column {}\n".format(col)) 
                if winning_move(board,2) :
                    print("Player 2 wins!")
                    game_over = True
                if is_tie(board) :
                    print("Tie game. Board was filled before either player won.")
                    game_over = True
'''