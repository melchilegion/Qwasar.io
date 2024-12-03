# Welcome to My Nba Game Analysis
***

## Task
- What is the problem? And where is the challenge?
- This Python script provides a simple tool for analyzing NBA game data. Given a list of play-by-play moves, it generates a summary of the game statistics.

## Description
- How have you solved the problem?
- Input:
- The script expects a list of play-by-play moves in the following format:
PERIOD|REMAINING_SEC|RELEVANT_TEAM|AWAY_TEAM|HOME_TEAM|AWAY_SCORE|HOME_SCORE|DESCRIPTION
Period: The game period (e.g., 1, 2, 3, 4).
Remaining Sec: Seconds remaining in the period.
Relevant Team: The team directly involved in the action (e.g., the team scoring, committing a turnover, etc.).
Away Team: Name of the away team.
Home Team: Name of the home team.
Away Score: Away team score at the time of the play.
Home Score: Home team score at the time of the play.
Description: A detailed description of the play, including the player and the action.
Output:
The script returns a dictionary containing the game statistics for both teams (home and away).
The dictionary has the following structure:
{
  "home_team": {
    "name": "TEAM_NAME",
    "players_data": [
      {
        "player_name": "PLAYER_NAME",
        "FG": 10,
        "FGA": 20,
        "FG%": 50, 
        "3P": 3,
        "3PA": 8,
        "3P%": 37,
        "FT": 5,
        "FTA": 7,
        "FT%": 71,
        "ORB": 2,
        "DRB": 6,
        "TRB": 8,
        "AST": 4,
        "STL": 2,
        "BLK": 1,
        "TOV": 3,
        "PF": 4,
        "PTS": 28
      },
      ...
    ]
  },
  "away_team": {
    "name": "TEAM_NAME",
    "players_data": [
      ...
    ]
  }
}
name: The team's name.
players_data: A list of dictionaries containing individual player statistics.
player_name: Player's name.
FG: Field goals made.
FGA: Field goals attempted.
FG%: Field goal percentage.
3P: Three-point field goals made.
3PA: Three-point field goals attempted.
3P%: Three-point field goal percentage.
FT: Free throws made.
FTA: Free throws attempted.
FT%: Free throw percentage.
ORB

## Installation
- How to install your project? npm install? make? make re?
- It works exactly as i said it would work.

## Usage
- How does it work?
- Input:
- The script expects a list of play-by-play moves in the following format:
PERIOD|REMAINING_SEC|RELEVANT_TEAM|AWAY_TEAM|HOME_TEAM|AWAY_SCORE|HOME_SCORE|DESCRIPTION
Period: The game period (e.g., 1, 2, 3, 4).
Remaining Sec: Seconds remaining in the period.
Relevant Team: The team directly involved in the action (e.g., the team scoring, committing a turnover, etc.).
Away Team: Name of the away team.
Home Team: Name of the home team.
Away Score: Away team score at the time of the play.
Home Score: Home team score at the time of the play.
Description: A detailed description of the play, including the player and the action.
Output:
The script returns a dictionary containing the game statistics for both teams (home and away).
The dictionary has the following structure:
{
  "home_team": {
    "name": "TEAM_NAME",
    "players_data": [
      {
        "player_name": "PLAYER_NAME",
        "FG": 10,
        "FGA": 20,
        "FG%": 50, 
        "3P": 3,
        "3PA": 8,
        "3P%": 37,
        "FT": 5,
        "FTA": 7,
        "FT%": 71,
        "ORB": 2,
        "DRB": 6,
        "TRB": 8,
        "AST": 4,
        "STL": 2,
        "BLK": 1,
        "TOV": 3,
        "PF": 4,
        "PTS": 28
      },
      ...
    ]
  },
  "away_team": {
    "name": "TEAM_NAME",
    "players_data": [
      ...
    ]
  }
}
name: The team's name.
players_data: A list of dictionaries containing individual player statistics.
player_name: Player's name.
FG: Field goals made.
FGA: Field goals attempted.
FG%: Field goal percentage.
3P: Three-point field goals made.
3PA: Three-point field goals attempted.
3P%: Three-point field goal percentage.
FT: Free throws made.
FTA: Free throws attempted.
FT%: Free throw percentage.
ORB


### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
