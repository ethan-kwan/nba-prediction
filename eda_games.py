"""
Name: Ethan Kwan
CSE 163 - Autumn 2026
NBA Prediction Project

Exploratory data analysis of NBA game results.
"""

import pandas as pd
import matplotlib.pyplot as plt


def plot_home_win_percentage(games):
    """
    Creates a bar chart comparing home and away win percentages
    in NBA regular-season games.
    """

    home_win_pct, away_win_pct = home_win_percentage(games)

    plt.figure(figsize=(7, 5))
    plt.bar(
        ['Home Team', 'Away Team'],
        [home_win_pct, away_win_pct],
        color=['steelblue', 'orange']
    )

    plt.title('NBA Regular Season Win Percentage by Location')
    plt.xlabel('Team Location')
    plt.ylabel('Win Percentage (%)')
    plt.ylim(0, 100)

    plt.savefig('home_win_percentage.png')
    #plt.show()

    # print('Home win percentage:', round(home_win_pct, 2))
    # print('Away win percentage:', round(away_win_pct, 2))


def home_win_percentage(games):
    """
    Calculates the home win percentage for NBA regular-season games.
    """

    # Filter for regular-season games
    regular_games = games[games['gameType'] == 'Regular Season']

    # Check if winner is the home team
    # Winner is the home team if the winner is the home team id
    home_wins = regular_games['winner'] == regular_games['hometeamId']

    # Get the total number of games
    total_games = len(regular_games)

    # Get the number of home wins
    home_wins = home_wins.sum()

    # Get the number of away wins
    away_wins = total_games - home_wins

    # Get the home win percentage
    home_win_pct = home_wins / total_games * 100
    away_win_pct = away_wins / total_games * 100

    return home_win_pct, away_win_pct

def main():
    games = pd.read_csv('data/Games.csv')
    home_pct, away_pct = home_win_percentage(games)
    print('Home win percentage:', round(home_pct, 2))
    print('Away win percentage:', round(away_pct, 2))
    plot_home_win_percentage(games)


if __name__ == '__main__':
    main()