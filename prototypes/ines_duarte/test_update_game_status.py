from unittest import TestCase
from main.game_class import Game

# the update_game_status is a vital part of blocking re-entry into building that have already been won

class TestUpdateGameStatus(TestCase):

    def test_updating_Won(self):

        game = Game()

        game.games_won = {
        "library": "Not won",
        "cafeteria": "Not won",
        "counselling_office": "Not won",
        "classroom": "Not won",
        "it_dept": "Not won"
    }

        game.library.victory_status = "Won"

        expected = {
        "library": "Won",
        "cafeteria": "Not won",
        "counselling_office": "Not won",
        "classroom": "Not won",
        "it_dept": "Not won"
    }
        game.update_game_status("library")

        self.assertEqual(game.games_won, expected)




