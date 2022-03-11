import logging
import random

logging.basicConfig(filename='snake_an_ladder_log.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')
logging.info("Logger Running")


class SnakeAndLadder:

    def __init__(self):
        self.snake_dict = {
            99: 5,
            45: 10,
            32: 12,
            20: 1
        }
        self.ladder_dict = {
            21: 7,
            42: 32,
            94: 2,
            13: 22
        }
        self.count = 0

    def dice(self):
        """
        dice rolls and give value between 1 to 6
        :return: number from 1 to 6
        """
        self.count += 1
        return random.randint(1, 6)

    def snake(self, position):
        """

        :param position:player current position
        :return: player position after beaten  by Snake
        """

        if position in self.snake_dict:
            position = position - self.snake_dict.get(position)
        return position

    def ladder(self, position):
        """

        :param position:player current position
        :return: player position after taking ladder
        """
        if position in self.ladder_dict and (position + self.ladder_dict.get(position)) < 100:
            position = position + self.ladder_dict.get(position)
            return position
        else:
            return


if __name__ == "__main__":
    try:
        print("welcome to Snake And Ladder Problem")
        WINNER_POS = 100
        player_position = 0
        print("player initial position : {}".format(player_position))
        snake_and_ladder_obj = SnakeAndLadder()

        while player_position < WINNER_POS:
            dice = snake_and_ladder_obj.dice()
            print("dice value after roll: {}".format(dice))
            if player_position + dice <= 100:
                player_position = player_position + dice
            print(player_position)
            snake_and_ladder_obj.snake(player_position)
            snake_and_ladder_obj.ladder(player_position)
        print("Player Won the Game")
        print("Number of Times Dice Rolled= {} ".format(snake_and_ladder_obj.count))
    except Exception as err:
        print("Error Occured {}".format(err))
        logging.ERROR(err)
