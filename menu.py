def display_team_stats(team_name, team_players):
    """
    Displays detailed statistics for a specified team.

    This function calculates and prints the following information:
    - Total number of players
    - Number of experienced and inexperienced players
    - Average player height
    - List of player names
    - List of guardian names

    Args:
        team_name (str): The name of the team.
        team_players (list of dict): A list of player dictionaries assigned to the team.

    Returns:
        None
    """
    print(f"\nTeam: {team_name} Stats")
    print("--------------------")
    print(f"Total players: {len(team_players)}")

    # Calculate experienced and inexperienced players
    experienced_players = [player for player in team_players if player['experience']]
    inexperienced_players = [player for player in team_players if not player['experience']]
    print(f"Total experienced players: {len(experienced_players)}")
    print(f"Total inexperienced players: {len(inexperienced_players)}")

    # Calculate average height
    total_height = sum([player['height'] for player in team_players])
    average_height = total_height / len(team_players)
    print(f"Average height: {average_height:.1f}\n")

    # Print player names and guardians
    print("Players on Team:")
    print(", ".join([player['name'] for player in team_players]))

    print("\nGuardians:")
    print(", ".join([", ".join(player['guardians']) for player in team_players]))

    input("\nPress ENTER to continue...")

def main_menu(balanced_teams):
    """
    Displays the main menu and processes user choices.

    Provides options to display team statistics or quit the program. If 'Display Team Stats'
    is selected, prompts the user to choose a team and displays relevant statistics.

    Args:
        balanced_teams (dict): A dictionary of teams with lists of player dictionaries.

    Returns:
        None
    """
    while True:
        print("\nBASKETBALL TEAM STATS TOOL\n")
        print("---- MENU ----\n")
        print("Here are your choices:")
        print("1) Display Team Stats")
        print("2) Quit\n")
        
        try:
            option = input("Enter an option:  ")
            if option == '1':
                print("\nSelect a Team:")
                for i, team_name in enumerate(balanced_teams, start=1):
                    print(f"{i}) {team_name}")
                choice = input("\nEnter an option > ")

                # Convert choice to integer and validate range
                team_index = int(choice) - 1
                if 0 <= team_index < len(balanced_teams):
                    team_name = list(balanced_teams.keys())[team_index]
                    # Call display_team_stats for the selected team
                    display_team_stats(team_name, balanced_teams[team_name])
                else:
                    print("\nInvalid option. Please choose a valid team number.\n")
            elif option == '2':
                print("Thank you for using the Basketball Team Stats Tool!")
                break
            else:
                print("\nInvalid option. Please enter 1 or 2.\n")
        except ValueError:
            print("\nInvalid input. Please enter a number.\n")

