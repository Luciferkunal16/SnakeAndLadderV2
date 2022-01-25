import logging
import random


class SnakeAndLadderMain:
    def __init__(self):
        self.position_of_player = {"a": 0, "b": 0}
        self.NO_PLAY = 1
        self.SNAKE = 2
        self.LADDER = 3
        self.MAX_POSITION = 100

    def dice(self):
        return random.randint(1, 6)

    def game_option(self, player_type):
        dice_value = self.dice()
        print("Dice Value For Player is {}".format(dice_value))
        check_play = random.randint(1, 3)
        if check_play == self.NO_PLAY:
            print("Same Position")

        elif check_play == self.LADDER:
            if self.position_of_player[player_type] + dice_value > self.MAX_POSITION:
                return
            else:
                self.position_of_player[player_type] += dice_value
        elif check_play == self.SNAKE:
            self.position_of_player[player_type] -= dice_value
            if self.position_of_player[player_type] < 0:
                self.position_of_player[player_type] = 0

    def main_game(self):
        try:
            while self.position_of_player["a"] < self.MAX_POSITION and self.position_of_player["b"] < self.MAX_POSITION:
                print("Turn of Player A")
                self.game_option("a")
                print("position of player A is {}".format(self.position_of_player["a"]))
                print("Turn of Player B")
                self.game_option("b")
                print("position of player B is {}".format(self.position_of_player["b"]))
            if self.position_of_player["a"]>self.position_of_player["b"]:
                print("Player A is Winner")
                return "Player A"
            else:
                print("Player B is Winner")
                return "Player B"
        except Exception as e:
            print(e)
            logging.ERROR(e)



if __name__ == "__main__":
    obj = SnakeAndLadderMain()
    obj.main_game()
