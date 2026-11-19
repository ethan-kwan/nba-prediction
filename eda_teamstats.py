"""
Name: Ethan Kwan
CSE 163 - Autumn 2026
NBA Prediction Project

Exploratory data analysis of NBA team statistics.
"""

import os

import pandas as pd
import matplotlib.pyplot as plt


def average_score_by_location(team_stats):
    """
    Calculates average team score for home and away rows.
    """
    # Filter for regular-season games
    regular_games = team_stats[team_stats['gameType'] == 'Regular Season']

    # Filter for Warriors games
    warriors_games = regular_games[regular_games['teamName'] == 'Warriors']

    # home == 1 means home team row, home == 0 means away team row
    home_rows = warriors_games[warriors_games['home'] == 1]
    away_rows = warriors_games[warriors_games['home'] == 0]

    home_avg = home_rows['teamScore'].mean()
    away_avg = away_rows['teamScore'].mean()

    return home_avg, away_avg


def plot_average_score_by_location(team_stats):
    """
    Creates a bar chart of average points scored at home vs away.
    """
    home_avg, away_avg = average_score_by_location(team_stats)

    plt.figure(figsize=(7, 5))
    plt.bar(
        ['Home Team', 'Away Team'],
        [home_avg, away_avg],
        color=['steelblue', 'orange']
    )

    plt.title('Warriors Regular Season Average Points by Location')
    plt.xlabel('Game Location')
    plt.ylabel('Average Points Scored')

    os.makedirs('figures', exist_ok=True)
    plt.savefig('figures/avg_score_by_location.png')
    # plt.show()


def main():
    team_stats = pd.read_csv('data/TeamStatistics.csv')

    print('Team Statistics shape:', team_stats.shape)
    print('home value counts:')
    print(team_stats['home'].value_counts())
    print('win value counts:')
    print(team_stats['win'].value_counts(dropna=False))

    home_avg, away_avg = average_score_by_location(team_stats)
    print('Home average score:', round(home_avg, 2))
    print('Away average score:', round(away_avg, 2))

    plot_average_score_by_location(team_stats)


if __name__ == '__main__':
    main()
