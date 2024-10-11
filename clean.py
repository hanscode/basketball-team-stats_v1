import copy

# clean the data, converting height to integer, experience to boolean and guardians to a list.
def clean_data(data):
    players_copy = copy.deepcopy(data)
    for player in players_copy:
        player.update({
            'height': int(player['height'].split()[0]),
            'experience': True if player['experience'] == 'YES' else False,
            'guardians': [guardian for guardian in player['guardians'].split(" and ")]
        })
    return players_copy
