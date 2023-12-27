from nba_api.stats.endpoints import teamgamelogs as tgls

def get_game_logs(
      team_id,
      season = '2023-24',
    ):
  return tgls.TeamGameLogs(
          team_id_nullable = team_id,
          season_nullable = season,
        ).get_data_frames()[0]