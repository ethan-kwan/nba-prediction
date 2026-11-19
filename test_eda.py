"""
Name: Ethan Kwan
CSE 163 - Autumn 2026
NBA Prediction Project

Simple tests for Games and TeamStatistics EDA helpers.
"""

import unittest

import pandas as pd

from eda_games import home_win_percentage
from eda_teamstats import average_score_by_location


class TestGamesEDA(unittest.TestCase):
    """Tests for Games.csv home/away win percentage helpers."""

    def test_home_win_percentage_regular_season_only(self):
        # 3 Regular Season games: 2 home wins, 1 away win
        # 1 Playoffs game should be ignored
        games = pd.DataFrame({
            'gameType': [
                'Regular Season',
                'Regular Season',
                'Regular Season',
                'Playoffs'
            ],
            'hometeamId': [1, 1, 2, 1],
            'winner': [1, 2, 2, 1]
        })

        home_pct, away_pct = home_win_percentage(games)

        self.assertAlmostEqual(home_pct, 2 / 3 * 100)
        self.assertAlmostEqual(away_pct, 1 / 3 * 100)
        self.assertAlmostEqual(home_pct + away_pct, 100)


class TestTeamStatsEDA(unittest.TestCase):
    """Tests for TeamStatistics Warriors home/away scoring helpers."""

    def test_average_score_by_location_warriors_regular_season(self):
        # Only Warriors + Regular Season rows should be used
        team_stats = pd.DataFrame({
            'gameType': [
                'Regular Season',
                'Regular Season',
                'Regular Season',
                'Playoffs',
                'Regular Season'
            ],
            'teamName': [
                'Warriors',
                'Warriors',
                'Warriors',
                'Warriors',
                'Lakers'
            ],
            'home': [1, 1, 0, 1, 1],
            'teamScore': [110, 120, 100, 130, 140]
        })

        home_avg, away_avg = average_score_by_location(team_stats)

        # Warriors regular-season home scores: 110, 120 -> 115
        # Warriors regular-season away scores: 100 -> 100
        self.assertAlmostEqual(home_avg, 115.0)
        self.assertAlmostEqual(away_avg, 100.0)


if __name__ == '__main__':
    unittest.main()
