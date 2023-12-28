from nba_api.stats.endpoints import teamgamelogs as tgls
from nba_api.stats.endpoints import playergamelogs as pgls

def get_team_game_logs(
      team_id,
      season = '2023-24',
    ):
  return tgls.TeamGameLogs(
          team_id_nullable = team_id,
          season_nullable = season,
        ).get_data_frames()[0]

def get_player_game_logs(
      player_id,
      season = '2023-24',
    ):
  return pgls.PlayerGameLogs(
          player_id_nullable = player_id,
          season_nullable = season,
        ).get_data_frames()[0]