from SnakeAndLadderGame.snake_game_v2 import SnakeAndLadderMain


def test_dice():
    dice_obj = SnakeAndLadderMain()
    assert dice_obj.dice() in [1, 2, 3, 4, 5, 6]


def test_main_game_method():
    test_obj = SnakeAndLadderMain()
    test_player = test_obj.main_game()
    assert test_player == "Player A " or "Player B"
