import logging
import random

logging.basicConfig(filename='snake_an_ladder_log.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')
logging.info("Logger Running")


class SnakeAndLadderMain:
    def __init__(self):
        self.position_of_player = {"a": 0, "b": 0}
        self.NO_PLAY = 1
        self.SNAKE = 2
        self.LADDER = 3
        self.MAX_POSITION = 100

    def dice(self):
        """
        for simulating dice
        :return: random Number Between 1 to 6
        """
        return random.randint(1, 6)

    def game_option(self, player_type):
        """

        :param player_type: Player A OR Player B
        :return: Player move after rolling dice
        """
        dice_value = self.dice()
        print("Dice Value For Player is {}".format(dice_value))
        check_play = random.randint(1, 3)
        dict_check_play = {self.NO_PLAY:print,self.LADDER: self.ladder, self.SNAKE: self.snake}
        if check_play == self.NO_PLAY:
            print("no play")
        else:
            dict_check_play.get(check_play)(player_type, dice_value)

    def ladder(self, player_type, dice_value):
        """
        logi for Ladder Move
        :param player_type: which player A or B
        :param dice_value:
        :return:
        """
        if self.position_of_player[player_type] + dice_value > self.MAX_POSITION:
            return
        else:
            self.position_of_player[player_type] += dice_value

    def snake(self, player_type, dice_value):
        """
        For snake Move
        :param player_type: Type of Player A or B
        :param dice_value: Dice value
        :return:
        """
        self.position_of_player[player_type] -= dice_value
        if self.position_of_player[player_type] < 0:
            self.position_of_player[player_type] = 0

    def main_game(self):
        """
        for simmulating the main game

        :return: String -Player A or B Who is Winner
        """
        try:
            while self.position_of_player["a"] < self.MAX_POSITION and self.position_of_player["b"] < self.MAX_POSITION:
                print("Turn of Player A")
                self.game_option("a")
                print("position of player A is {}".format(self.position_of_player["a"]))
                print("Turn of Player B")
                self.game_option("b")
                print("position of player B is {}".format(self.position_of_player["b"]))
                print("================================================================")
            if self.position_of_player["a"] > self.position_of_player["b"]:
                print("Player A is Winner")
                return "Player A"
            else:
                print("Player B is Winner")
                return "Player B"
        except Exception as e:
            print(e)



if __name__ == "__main__":
    try:
        obj = SnakeAndLadderMain()
        obj.main_game()
    except Exception as e:
        print(e)
