import random
import os.path
import json
random.seed()

def draw_board(board):
    for i in range(3):
        row_str = ""
        for j in range(3):
            if board[i][j] == 'X' or board[i][j] == 'O':
                row_str += f" {board[i][j]} "
            else:
                row_str += f" {i * 3 + j + 1} "
            if j < 2:
                row_str += '|'
        print(row_str)
        if i < 2:
            print("-" * 11) 

def welcome(board):
    print("Welcome to the 'Unbeatable Noughts and Crosses' game.")
    print("The board layout is shown below:\n")
    draw_board(board)

def initialise_board(board):
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
    return board

def get_player_move(board):
    print("Choose your square (1-9): ")
    while True:
        try:
            choice = int(input(""))
            if 1 <= choice <= 9:
                row = (choice - 1) // 3
                col = (choice - 1) % 3

                if board[row][col] not in ['X', 'O']:
                    board[row][col] = 'X'
                    print("Player's move:")
                    return row, col
                else:
                    print("Invalid move. The chosen square is already occupied. Try again.")
            else:
                print("Invalid choice. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def choose_computer_move(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)

        if board[row][col] == ' ':
            board[row][col] = 'O'
            return row, col

    draw_board(board)
    return row, col

def check_for_win(board, mark):
    for i in range(3):
        if all(board[i][j] == mark for j in range(3)) or all(board[j][i] == mark for j in range(3)):
            return True

    if all(board[i][i] == mark for i in range(3)) or all(board[i][2 - i] == mark for i in range(3)):
        return True

    return False

def check_for_draw(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def play_game(board):
    user_score = 0
    comp_score = 0
    
    # Reset the board for each new game 
    initialise_board(board)

    while True:
        # Player's turn
        player_row, player_col = get_player_move(board)
        draw_board(board)

        if check_for_win(board, 'X'):
            print("Congratulations! You win!")
            user_score += 1
            return user_score, comp_score
        elif check_for_draw(board):
            print("It's a draw!")
            return user_score, comp_score

        # Computer's turn
        comp_row, comp_col = choose_computer_move(board)
        print("Computer's move:")
        draw_board(board)

        if check_for_win(board, 'O'):
            print("Computer wins! Better luck next time.")
            comp_score += 1
            return user_score, comp_score
        elif check_for_draw(board):
            print("It's a draw!")
            return user_score, comp_score

def menu():
    while True:
        try:
            user_input = input("Enter one of the following options:\n"
                               "1 - Play the game\n"
                               "2 - Save Your score in the leaderboard\n"
                               "3 - Load and display the leaderboard\n"
                               "q - End the program.\n\n"
                               "1, 2, 3 or q? ").lower()
            if user_input == '1' or user_input == '2' or user_input == '3' or user_input == 'q':
                return user_input
            else:
                print("Invalid input. Please enter 1, 2, 3, or q.")
        except ValueError:
            print("Invalid input. Please enter 1, 2, 3, or q.")

def load_scores():
    try:
        with open('leaderboard.txt', 'r') as file:
            leaders = json.load(file)
            return leaders
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_score(score):
    name = input("Enter your name: ")
    scores = load_scores()
    scores[name] = score           

    with open('leaderboard.txt', 'w') as file:
        json.dump(scores, file)

def display_leaderboard(leaders):
    print("Leaderboard:")
    for name, score in leaders.items():
        print(f"{name}: {score}")

