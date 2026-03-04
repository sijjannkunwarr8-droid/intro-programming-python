from noughtsandcrosses_2551483 import *

    
def main():
    board = [[' ']*3 for _ in range(3)] 
    
    welcome(board)
    user_total_score = 0
    comp_total_score = 0

    while True:
        choice = menu()

        if choice == '1':
            user_score, comp_score = play_game(board)
            user_total_score += user_score
            comp_total_score += comp_score
            print('Your current score is:', user_total_score)
            print('Computer\'s score is:', comp_total_score)

        elif choice == '2':
            save_score(user_total_score)

        elif choice == '3':
            leader_board = load_scores()
            display_leaderboard(leader_board)

        elif choice == 'q':
            print('Thank you for playing the "Unbeatable Noughts and Crosses" game.')
            print('Goodbye!')
            break

# Program execution begins here
if __name__ == '__main__':
    main()
