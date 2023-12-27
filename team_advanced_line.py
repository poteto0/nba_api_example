import matplotlib.pyplot as plt

import teams as tm
import stats as st
import calc

def scan_data(letter = "what?"):
  print(letter)
  return input()

def prepare(logs):
  logs = logs.iloc[::-1].reset_index()
  logs = calc.calc_and_assign_rating(
            df=logs, 
            rating_type='OFF')
  logs = calc.calc_and_assign_rating(
            df=logs, 
            rating_type='DEF')
  logs = calc.calc_and_assign_rating(
            df=logs, 
            rating_type='NET')

  return logs

arrow_dict = dict(arrowstyle="->", color="saddlebrown")

# テキストボックスのプロパティ
# fc:facecolor, ec:edgecolor
text_dict = dict(boxstyle="round",
                 fc="silver", ec="mediumblue")

def main():
  fig = plt.figure()
  ax = [fig.add_subplot(3, 1, 1), fig.add_subplot(3, 1, 2), fig.add_subplot(3, 1, 3)]
  ax[0].set_ylabel('OFF_RTG')
  ax[1].set_ylabel('DEF_RTG')
  ax[2].set_ylabel('NET_RTG')
  
  teams = tm.get_teams()

  i = 1
  for team in teams:
    print(f"=== {i}/30===")
    logs = st.get_game_logs(team['id'])
    logs = prepare(logs)

    rolled_offense = calc.rollings(logs, target_column='OFF_RTG', ws=7)
    rolled_defense = calc.rollings(logs, target_column='DEF_RTG', ws=7)
    rolled_net     = calc.rollings(logs, target_column='NET_RTG', ws=7)
    
    if not team['city'] == 'Portland':
      ax[0].plot(logs.index, rolled_offense, color='lightgray', alpha=0.5)
      ax[1].plot(logs.index, rolled_defense, color='lightgray', alpha=0.5)
      ax[2].plot(logs.index, rolled_net, color='lightgray', alpha=0.5)
    i +=1

  team = tm.get_team_by_city('Portland')
  logs = st.get_game_logs(team['id'])
  logs = prepare(logs)
  
  rolled_offense = calc.rollings(logs, target_column='OFF_RTG', ws=7)
  rolled_defense = calc.rollings(logs, target_column='DEF_RTG', ws=7)
  rolled_net     = calc.rollings(logs, target_column='NET_RTG', ws=7)
    
  ax[0].plot(logs.index, rolled_offense, color='#ff6347', alpha=1.0)
  ax[1].plot(logs.index, rolled_defense, color='#ff6347', alpha=1.0)
  ax[2].plot(logs.index, rolled_net, color='#ff6347', alpha=1.0)

  ax[2].axhline(y=0, xmin=0, xmax=len(logs), color="black", ls="--", lw=1)

  is_event = scan_data('Do you want annotate event? [y/n]')
  if is_event == 'y':
    events_name = scan_data('what event? ex) A out,A in').split(',')
    events_game = scan_data('when event occur? event game number ex) 2,3').split(',')
    
    j = 0
    for en, eg in zip(events_name, events_game):
      eg = int(eg)
      ax[2].annotate(
          en, size=10, color = "black",
          xy=(eg, rolled_net[eg]), xytext=(eg+1, rolled_net[eg]+0.1),
          bbox=text_dict, arrowprops=arrow_dict)
      
      j += 1
  plt.show()

if __name__ == "__main__":
  main()