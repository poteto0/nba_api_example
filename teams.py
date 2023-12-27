from nba_api.stats.static import teams

def get_teams():
  return teams.get_teams()

def get_team_by_city(city):
  all_team = get_teams()
  return [t for t in all_team if t['city'] == city][0]