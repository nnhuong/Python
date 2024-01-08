import unittest
from unittest.mock import patch
from io import StringIO
from dambuakeo import main

class TestGame(unittest.TestCase):

    @patch('builtins.input', side_effect=["R", "Q"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_game_quit(self, mock_output, mock_input):
        main()
        expected_output = (
            "Welcome to our game\n[R] = Rock, [P] = Paper, [S]= Scissor and [Q] = Quit Game\n"
            "Game #1. Please enter your choice:\nThanks for joining. Have a nice day"
        )
        self.assertEqual(mock_output.getvalue().strip(), expected_output)

    @patch('builtins.input', side_effect=["R"])
    @patch('random.randint', return_value=0)
    @patch('sys.stdout', new_callable=StringIO)
    def test_game_win(self, mock_output, mock_random, mock_input):
        main()
        expected_output = "You win"
        self.assertIn(expected_output, mock_output.getvalue().strip())

    @patch('builtins.input', side_effect=["R"])
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=StringIO)
    def test_game_loss(self, mock_output, mock_random, mock_input):
        main()
        expected_output = "Sorry, you're lose"
        self.assertIn(expected_output, mock_output.getvalue().strip())

    @patch('builtins.input', side_effect=["R"])
    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=StringIO)
    def test_game_draw(self, mock_output, mock_random, mock_input):
        main()
        expected_output = "wow, it's a Draw"  # Kiểm tra giá trị mong đợi trong chương trình của bạn
        self.assertIn(expected_output, mock_output.getvalue().strip())

if __name__ == '__main__':
    unittest.main()
