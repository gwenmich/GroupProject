from unittest import TestCase
from unittest.mock import patch
from world.high_scores_screen import HighScoreScreen

class TestTop10Scores(TestCase):
    # In this test we won't be testing the actual API, instead we are using the decorator patch to mock the api request
    @patch("requests.get")
    # passing mock_get which is the object that replaces the requests.get
    def test_get_top10_scores_front_end(self, mock_get):
        # instantiating the Class high scores that contains the method we are testing
        scores = HighScoreScreen()

        # this is the mock api response displaying the high scores
        mock_api_response = [
            {'Final Time': '03:50', 'Stars': '5 Stars', 'Player': 'Arianne_40K'},
            {'Final Time': '06:22', 'Stars': '5 Stars', 'Player': 'SuperGM'},
            {'Final Time': '08:45', 'Stars': '5 Stars', 'Player': 'Arianne_40K'},
            {'Final Time': '10:10', 'Stars': '4 Stars', 'Player': 'jedi_LUKE'},
            {'Final Time': '12:26', 'Stars': '4 Stars', 'Player': 'Fatihah'},
            {'Final Time': '13:40', 'Stars': '4 Stars', 'Player': 'wizard_HAMED'},
            {'Final Time': '14:55', 'Stars': '4 Stars', 'Player': 'JMG'},
            {'Final Time': '18:10', 'Stars': '3 Stars', 'Player': 'just_GRACE'},
            {'Final Time': '21:50', 'Stars': '3 Stars', 'Player': 'Arianne_40K'},
            {'Final Time': '22:45', 'Stars': '3 Stars', 'Player': 'SuperGM'}
        ]


        mock_get.return_value.json.return_value = mock_api_response

        result = scores.get_top10_scores_front_end()

        self.assertEqual(result, mock_api_response)
