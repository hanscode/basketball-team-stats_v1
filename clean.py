import copy


def clean_data(data):
    players_copy = copy.deepcopy(data)
    for player in players_copy:
        player.update({
            'height': int(player['height'].split()[0]),
            'experience': True if player['experience'] == 'YES' else False
        })
    return players_copy
