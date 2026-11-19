
"""
Name: Ethan Kwan, Gabriel Kan
CSE 163 - Autumn 2026
NBA Prediction Project - Exploratory Data Analysis

Explores the structure and missing values of NBA game datasets.
"""

import pandas as pd


GAMES_PATH = 'data/Games.csv'
TEAM_STATS_PATH = 'data/TeamStatistics.csv'


def explore_dataset(data, name):
    """
    Prints basic information about an NBA dataset.
    """
    print(f'\n--- {name} ---')

    print(f'Rows: {data.shape[0]}')
    print(f'Columns: {data.shape[1]}')

    print('\nFirst 5 rows:')
    print(data.head())

    print('\nMissing values by column:')
    print(data.isna().sum().sort_values(ascending=False))

    print('\nData types:')
    print(data.dtypes)


def main():
    games = pd.read_csv(GAMES_PATH)
    team_stats = pd.read_csv(TEAM_STATS_PATH)

    explore_dataset(games, 'Games')
    explore_dataset(team_stats, 'Team Statistics')


if __name__ == '__main__':
    main()
