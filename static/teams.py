from nba_api.stats.static import teams

def get_teams():
  return teams.get_teams()

def get_team_by_city(city):
  all_teams = get_teams()
  return [t for t in all_teams if t['city'] == city][0]