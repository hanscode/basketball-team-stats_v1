import copy


def clean_data(data):
    """
    Cleans and standardizes the player data.

    This function performs the following actions on player data:
    - Converts the 'height' from a string to an integer.
    - Converts the 'experience' field to a boolean.
    - Splits 'guardians' into a list of individual names.

    Args:
        data (list of dict): The original list of player dictionaries.

    Returns:
        list of dict: A deep-copied list of player dictionaries with cleaned
        data.
    """
    players_copy = copy.deepcopy(data)
    for player in players_copy:
        player.update({
            'height': int(player['height'].split()[0]),
            'experience': True if player['experience'] == 'YES' else False,
            'guardians': [
                guardian for guardian in player['guardians'].split(" and ")
            ]
        })
    return players_copy
