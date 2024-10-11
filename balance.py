
def balance_teams(players, teams):
    """
    Balances players across teams to ensure equal numbers and experience
    distribution.

    This function separates players into experienced and inexperienced groups,
    then evenly distributes them across the specified teams.

    Args:
        players (list of dict): The list of cleaned player dictionaries.
        teams (list of str): The list of team names.

    Returns:
        dict: A dictionary with team names as keys and lists of assigned
        players as values.
    """

    def distribute(players_list):
        for i, player in enumerate(players_list):
            team_index = i % len(teams)
            if len(balanced_teams[teams[team_index]]) < num_players_team:
                balanced_teams[teams[team_index]].append(player)

    # Separate players by experience
    experienced_players = [
        player for player in players if player['experience']
    ]
    inexperienced_players = [
        player for player in players if not player['experience']
    ]

    # Calculate number of players per team
    num_players_team = len(players) // len(teams)

    # Initialize empty teams
    balanced_teams = {team: [] for team in teams}

    # Distribute experienced players
    distribute(experienced_players)
    # Distribute inexperienced players
    distribute(inexperienced_players)

    return balanced_teams
