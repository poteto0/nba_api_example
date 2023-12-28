from nba_api.stats.static import players

def get_players():
  return players.get_players()

def get_player_by_name(name):
  all_players = get_players()
  return [p for p in all_players if p['full_name'] == name][0]