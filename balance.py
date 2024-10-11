
def balance_teams(players, teams):

    # Calculate number of players per team
    num_players_team = len(players) / len(teams)

    # Initialize empty teams
    balanced_teams = { team: [] for team in teams } # {'Panthers': [], 'Bandits': [], 'Warriors': []}

    # Distribute all players in one loop
    for i, player in enumerate(players):
        team_index = i % len(teams)
        if len(balanced_teams[teams[team_index]]) < num_players_team:
            balanced_teams[teams[team_index]].append(player)
    
    return balanced_teams
        
    
