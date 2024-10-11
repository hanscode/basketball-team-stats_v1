# Import the constants file that contains teams and players data
from constants import PLAYERS, TEAMS

import clean
import balance

if __name__ == "__main__":
    # clean the data
    players_copy = clean.clean_data(PLAYERS)
    
    # Balance the teams
    balanced_teams = balance.balance_teams(players_copy, TEAMS)
    
    # Print balanced teams to verify
    for team, members in balanced_teams.items():
        print(f"{team} has {len(members)} players:")
        for member in members:
            print(f"  - {member['name']}, Experienced: {member['experience']}, Height: {member['height']} inches")
        print("\n")
