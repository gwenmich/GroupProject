from unittest import TestCase
from unittest.mock import patch
import requests
from world.high_scores_screen import HighScoreScreen, NoScoresFoundException, NoResponseException, APINotReachedException

class TestTop10Scores(TestCase):
    # In this test we won't be testing the actual API, instead we are using the decorator patch to mock the api request
    # passing mock_get which is the object that replaces the requests.get
    @patch("requests.get")
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

        # this is creating the path to replace the requests with the mock call which retrieves the mock_api_response list
        mock_get.return_value.json.return_value = mock_api_response

        result = scores.get_top10_scores_front_end()

        # when the test is run and get_top_ten_scores function is called as the mock_get was passed as an argument, it replaces the
        # the api call and it should get the mock api response. If it does the test is a success
        self.assertEqual(result, mock_api_response)


    # test to raise an exception if the score list is coming back empty
    @patch("requests.get")
    def test_get_top10_empty_scores(self, mock_get):

        scores = HighScoreScreen()

        # this time the mock api response is empty
        mock_api_response = []

        mock_get.return_value.json.return_value = mock_api_response

        # Looking for NoScoresFoundException to be raised on the empty list
        with self.assertRaises(NoScoresFoundException):
            scores.get_top10_scores_front_end()


    # test to raise an exception if the response comes back as none
    @patch("requests.get")
    def test_get_top10_no_response(self, mock_get):
        scores = HighScoreScreen()

        # this time the mock api response is empty
        mock_api_response = None

        mock_get.return_value.json.return_value = mock_api_response

        # Looking for NoResponseException to be raised if the result comes back as None
        with self.assertRaises(NoResponseException):
            scores.get_top10_scores_front_end()

    @patch("requests.get")
    def test_get_top10_API_no_reached(self, mock_get):
        scores = HighScoreScreen()

        # using side_effect to create a custom behaviour which allows to simulate the DB not reached exception
        mock_get.side_effect = requests.exceptions.RequestException

        # Ao now we pass the APINotReached exception we want to assert
        with self.assertRaises(APINotReachedException):
            scores.get_top10_scores_front_end()




