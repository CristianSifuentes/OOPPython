"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
import random


<<<<<<< HEAD
def run_game():
    scores = [0, 0]
=======
def run_game(num_players=2):
    scores = [0 for _ in range(num_players)]
>>>>>>> c556b7242cc3db179e61b0759834bb98c098481e

    while True:
        for i, score in enumerate(scores):
            player_num = i + 1
            roll = random.randint(1, 6)
            score += roll
            scores[i] = score
            print(f'Player {player_num} rolled a {roll} ({score})')
            if score >= 100:
<<<<<<< HEAD
                print(f'Player {player_num} wins!')
=======
                print(f"Player {player_num} wins!")
>>>>>>> c556b7242cc3db179e61b0759834bb98c098481e
                return


if __name__ == '__main__':
<<<<<<< HEAD
    run_game()
=======
    print("------ GAME 1 --------")
    run_game(4)
    print("------ GAME 2 --------")
    run_game(3)
>>>>>>> c556b7242cc3db179e61b0759834bb98c098481e
