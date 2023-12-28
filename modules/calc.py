import pandas as pd

def calc_and_assign_rating(
      df,
      # OFF | DEF | NET
      rating_type = 'OFF',
    ):

    df = calc_and_assign_possession(df=df)

    if rating_type == 'OFF':
      target_column = 'PTS'

    if rating_type == 'DEF':
      if 'OPP_PTS' not in df.columns:
        df['OPP_PTS'] = df['PTS'] - df['PLUS_MINUS']
      target_column = 'OPP_PTS'

    if rating_type == 'NET':
      target_column = 'PLUS_MINUS'
    
    df[f'{rating_type}_RTG'] = df[target_column] / df['POSS'] * 100
    return df

def calc_and_assign_possession(df):
  if 'POSS' in df.columns:
    return df

  df['POSS'] = df['FGA'] + df['TOV'] + df['FTA'] * 0.436 - df['OREB'] 
  return df

def rollings(df, target_column, ws=5):
  return df[target_column].rolling(ws).mean()