def analyse_nba_game(play_by_play_moves):
    """
    Processes an array of NBA play-by-play moves and returns a dictionary summarizing the game.

    Args:
        play_by_play_moves: An array of strings, each representing a play in the format:
            PERIOD|REMAINING_SEC|RELEVANT_TEAM|AWAY_TEAM|HOME_TEAM|AWAY_SCORE|HOME_SCORE|DESCRIPTION

    Returns:
        A dictionary with the following structure:
        {"home_team": {"name": TEAM_NAME, "players_data": DATA}, "away_team": {"name": TEAM_NAME, "players_data": DATA}}
        DATA is an array of dictionaries with the following format:
        {"player_name": XXX, "FG": XXX, "FGA": XXX, "FG%": XXX, "3P": XXX, "3PA": XXX, "3P%": XXX, "FT": XXX, "FTA": XXX, "FT%": XXX, "ORB": XXX, "DRB": XXX, "TRB": XXX, "AST": XXX, "STL": XXX, "BLK": XXX, "TOV": XXX, "PF": XXX, "PTS": XXX}
        Percent are on 100.
        Player is a string everything else are integers.
    """
    home_team = {}
    away_team = {}

    # Initialize teams and players
    home_team["name"] = play_by_play_moves[0].split("|")[4]
    home_team["players_data"] = []
    away_team["name"] = play_by_play_moves[0].split("|")[3]
    away_team["players_data"] = []

    # Process each play
    for play in play_by_play_moves:
        period, remaining_sec, relevant_team, away_team_name, home_team_name, away_score, home_score, description = play.split("|")

        # Extract player and relevant actions
        player = description.split(" ")[1]
        actions = description.split(" ")[2:]

        # Update player stats based on actions
        if relevant_team == home_team_name:
            player_stats = get_player_stats(home_team["players_data"], player)
            update_stats(player_stats, actions)
        elif relevant_team == away_team_name:
            player_stats = get_player_stats(away_team["players_data"], player)
            update_stats(player_stats, actions)

    # Calculate percentages
    for team in [home_team, away_team]:
        for player_stats in team["players_data"]:
            if player_stats["FGA"] > 0:
                player_stats["FG%"] = int(100 * player_stats["FG"] / player_stats["FGA"])
            if player_stats["3PA"] > 0:
                player_stats["3P%"] = int(100 * player_stats["3P"] / player_stats["3PA"])
            if player_stats["FTA"] > 0:
                player_stats["FT%"] = int(100 * player_stats["FT"] / player_stats["FTA"])

    return {"home_team": home_team, "away_team": away_team}

def get_player_stats(players_data, player):
    """
    Finds the stats of a player in the given list, or creates a new entry for the player if not found.

    Args:
        players_data: The list of player stats dictionaries.
        player: The name of the player to find.

    Returns:
        The player's stats dictionary, or a new empty dictionary if the player wasn't found.
    """
    for stats in players_data:
        if stats["player_name"] == player:
            return stats
    # Player not found, create a new entry
    new_stats = {"player_name": player, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0,
                "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0}
    players_data.append(new_stats)
    return new_stats

def update_stats(player_stats, actions):
    """
    Updates player stats based on the given actions.

    Args:
        player_stats: The player's stats dictionary.
        actions: A list of strings representing the actions in the play.
    """
    for action in actions:
        if action.startswith("makes"):
            if "3-pt" in action:
                player_stats["3P"] += 1
                player_stats["3PA"] += 1
                player_stats["PTS"] += 3
            else:
                player_stats["FG"] += 1
                player_stats["FGA"] += 1
                player_stats["PTS"] += 2
        elif action.startswith("misses"):
            if "3-pt" in action:
                player_stats["3PA"] += 1
            else:
                player_stats["FGA"] += 1
        elif action.startswith("free"):
            player_stats["FT"] += 1
            player_stats["FTA"] += 1
            player_stats["PTS"] += 1
        elif "offensive" in action:
            player_stats["ORB"] += 1
        elif "defensive" in action:
            player_stats["DRB"] += 1
        elif "assist" in action:
            player_stats["AST"] += 1
        elif "steal" in action:
            player_stats["STL"] += 1
        elif "block" in action:
            player_stats["BLK"] += 1
        elif "turnover" in action:
            player_stats["TOV"] += 1
        elif "foul" in action:
            player_stats["PF"] += 1
        # Add other actions as needed

def print_nba_game_stats(team_dict):
    """
    Prints the statistics for the given game in a table format.

    Args:
        team_dict: A dictionary containing the game statistics, as returned by analyse_nba_game.
    """
    print("Players\tFG\tFGA\tFG%\t3P\t3PA\t3P%\tFT\tFTA\tFT%\tORB\tDRB\tTRB\tAST\tSTL\tBLK\tTOV\tPF\tPTS")
    for team in ["home_team", "away_team"]:
        for player_stats in team_dict[team]["players_data"]:
            print(f"{player_stats['player_name']}\t{player_stats['FG']}\t{player_stats['FGA']}\t.{player_stats['FG%']:03}\t{player_stats['3P']}\t{player_stats['3PA']}\t.{player_stats['3P%']:03}\t{player_stats['FT']}\t{player_stats['FTA']}\t.{player_stats['FT%']:03}\t{player_stats['ORB']}\t{player_stats['DRB']}\t{player_stats['TRB']}\t{player_stats['AST']}\t{player_stats['STL']}\t{player_stats['BLK']}\t{player_stats['TOV']}\t{player_stats['PF']}\t{player_stats['PTS']}")
        # Team Totals
        team_totals = {"FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0,
                       "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0}
        for player_stats in team_dict[team]["players_data"]:
            for key in team_totals:
                team_totals[key] += player_stats[key]
        if team_totals["FGA"] > 0:
            team_totals["FG%"] = int(100 * team_totals["FG"] / team_totals["FGA"])
        if team_totals["3PA"] > 0:
            team_totals["3P%"] = int(100 * team_totals["3P"] / team_totals["3PA"])
        if team_totals["FTA"] > 0:
            team_totals["FT%"] = int(100 * team_totals["FT"] / team_totals["FTA"])
        print(f"Team Totals\t{team_totals['FG']}\t{team_totals['FGA']}\t.{team_totals['FG%']:03}\t{team_totals['3P']}\t{team_totals['3PA']}\t.{team_totals['3P%']:03}\t{team_totals['FT']}\t{team_totals['FTA']}\t.{team_totals['FT%']:03}\t{team_totals['ORB']}\t{team_totals['DRB']}\t{team_totals['TRB']}\t{team_totals['AST']}\t{team_totals['STL']}\t{team_totals['BLK']}\t{team_totals['TOV']}\t{team_totals['PF']}\t{team_totals['PTS']}")
        print()

# Example Usage
play_by_play_data = [
    "1|708.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|0|Turnover by K. Thompson (bad pass; steal by S. Adams)",
    "1|703.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|0|Turnover by P. George (bad pass)",
    "1|691.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|3|S. Curry makes 3-pt jump shot from 24 ft (assist by K. Durant)",
    "1|673.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|3|S. Adams misses 2-pt jump shot from 12 ft",
    "1|671.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|3|Offensive rebound by D. Schröder",
    "1|667.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|3|P. George misses 3-pt jump shot from 26 ft",
    "1|665.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|3|Defensive rebound by K. Durant",
    "1|657.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|5|K. Durant makes 2-pt layup from 2 ft",
    "1|638.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|5|D. Schröder misses 2-pt jump shot from 14 ft",
    "1|636.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|5|Offensive rebound by D. Schröder",
    "1|623.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|5|S. Adams misses 2-pt layup from 3 ft (block by K. Durant)",
    "1|621.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|5|Defensive rebound by D. Green",
    "1|618.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|5|Turnover by D. Green (out of bounds lost ball)",
    "1|608.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|2|5|P. Patterson makes 2-pt layup from 2 ft (assist by S. Adams)",
    "1|608.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|2|5|Shooting foul by D. Green (drawn by P. Patterson)",
    "1|608.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|3|5|P. Patterson makes free throw 1 of 1",
    "1|598.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|3|7|D. Jones makes 2-pt dunk from 1 ft (assist by D. Green)",
    "1|581.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|3|7|P. Patterson misses 2-pt hook shot from 8 ft",
    "1|580.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|3|7|Offensive rebound by P. Patterson",
    "1|580.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|3|7|Shooting foul by K. Thompson (drawn by P. Patterson)",
    "1|580.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|7|P. Patterson makes free throw 1 of 2",
    "1|580.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|7|P. Patterson misses free throw 2 of 2",
    "1|580.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|7|Defensive rebound by D. Green",
    "1|569.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|7|D. Green misses 3-pt jump shot from 28 ft",
    "1|567.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|7|Defensive rebound by D. Schröder",
    "1|552.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|7|P. Patterson misses 2-pt jump shot from 16 ft",
    "1|551.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|7|Defensive rebound by S. Curry",
    "1|547.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|7|Turnover by S. Curry (bad pass; steal by P. George)",
    "1|542.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|7|Turnover by S. Adams (bad pass; steal by K. Durant)",
    "1|533.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|10|K. Thompson makes 3-pt jump shot from 26 ft (assist by D. Green)"
]

game_stats = analyse_nba_game(play_by_play_data)
print_nba_game_stats(game_stats)

