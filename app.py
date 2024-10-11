# Import the constants file that contains teams and players data
from constants import PLAYERS, TEAMS

import clean
import balance
import menu

if __name__ == "__main__":
    # clean the data
    players_copy = clean.clean_data(PLAYERS)
    
    # Balance the teams
    balanced_teams = balance.balance_teams(players_copy, TEAMS)

    # Call the main menu
    menu.main_menu(balanced_teams)