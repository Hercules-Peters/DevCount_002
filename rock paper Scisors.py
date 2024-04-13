import random

class RockPaperScissors:
    def __init__(self):
        self.player = None
        self.choices = ['rock', 'paper', 'scissors']

    def play_game(self):
        while self.player not in self.choices:
            self.player = input('Select rock, paper, or scissors: ').lower()
        computer = random.choice(self.choices)
        print(f'Computer: {computer}')

        if self.player == computer:
            print("Draw")
        elif self.player == 'rock':
            if computer == "scissors":
                print("Player wins!")
            elif computer == "paper":
                print("Computer wins!")
        elif self.player == "paper":
            if computer == "scissors":
                print("Computer wins!")
            elif computer == 'rock':
                print("Player wins!")
        elif self.player == "scissors":
            if computer == "paper":
                print("Player wins!")
            elif computer == "rock":
                print("Computer wins!")


if __name__ == "__main__":
    while True:
        game = RockPaperScissors()
        game.play_game()
        play_again = input("Do you want to play again? (Yes/No): ").lower()
        if play_again != "yes":
            break
