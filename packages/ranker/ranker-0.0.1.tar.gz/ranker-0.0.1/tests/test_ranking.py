import unittest
import os

from ranker.modules.main import get_input
from ranker.modules.ranker import Ranker, SameTeam


# To run all the tests, use the following command from project root directory:
# python -m unittest

class TestRanker(unittest.TestCase):
    
    files_path = 'tests/test_files/'
    files_names = os.listdir(files_path + 'input/')

    def test_base_case(self):
        name = self.files_names[0]
        path = self.files_path + 'input/' + name
        league = Ranker(get_input(path))
        with open(self.files_path + 'output/' + name, 'r') as f : output = f.read()

        self.assertEqual(league.process_data(), output)


    def test_score_multiple_digits(self):
        name = self.files_names[1]
        path = self.files_path + 'input/' + name
        league = Ranker(get_input(path))
        with open(self.files_path + 'output/' + name, 'r') as f : output = f.read()

        self.assertEqual(league.process_data(), output)


    def test_points_tie(self):
        name = self.files_names[2]
        path = self.files_path + 'input/' + name
        league = Ranker(get_input(path))
        with open(self.files_path + 'output/' + name, 'r') as f : output = f.read()

        self.assertEqual(league.process_data(), output)


    def test_multiple_games(self):
        name = self.files_names[3]
        path = self.files_path + 'input/' + name
        league = Ranker(get_input(path))
        with open(self.files_path + 'output/' + name, 'r') as f : output = f.read()

        self.assertEqual(league.process_data(), output)


    def test_same_team(self):
        name = self.files_names[4]
        path = self.files_path + 'input/' + name
        league = Ranker(get_input(path))

        with self.assertRaises(SameTeam):
            league.process_data()
