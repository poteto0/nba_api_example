import matplotlib.pyplot as plt
import numpy as np

import static.players as ply
import stats.stats as st
from modules import calc, helper, shape
import my_plot.plot_parts as pp
import my_plot.color_picker as cp
import my_plot.plot_setting as ps

def plot_label(ax, max_columns, width, height, s=2, space=1):
  for i in range(max_columns):
    start, end = i * width, (i+1) * width - 1
    text = f'{start} to {end}'
    ax.text(
          x=s*0.5+i*(s+space), y=-1, 
          s=text,
          weight='extra bold',
          family='monospace',
          size=8,
          ha='center',
          va='center'
      )
  ax.axhline(y=-0.5, xmin=-1, xmax=(max_columns-1)*(s+space), color='black')
  ax.text(
          x=max_columns*0.5*(s+space), y=-2, 
          s="PTS",
          weight='extra bold',
          family='monospace',
          size=10,
          ha='center',
          va='center'
        )
  
  for i in range(max_columns):
    start, end = i * height, (i+1) * height - 1
    text = f'{start}\nto\n{end}'
    ax.text(
          x=-1, y=s*0.5+i*(s+space),
          s=text,
          weight='extra bold',
          family='monospace',
          size=8,
          ha='center',
          va='center'
      )
  ax.axvline(x=-0.5, ymin=-1, ymax=(max_columns-1)*(s+space), color='black')
  ax.text(
          x=-2, y=max_columns*0.5*(s+space), 
          s="A\nS\nT",
          weight='extra bold',
          family='monospace',
          size=10,
          ha='center',
          va='center'
        )

def plot_box_scatter(ax, val, color_picker, s=2, space=1):
  max_val = val.max()
  (h, w) = val.shape

  for i in range(h):
    for j in range(w):
      box = pp.FancyBboxPatch(
              bottom = i*s+i*space, left = j*s+j*space,
              width = s, height = s,
              color=color_picker.pick((val[i][j]/max_val) * 100)
            )
      ax.add_patch(box)
      ax.text(
          x=s*0.5+i*(s+space), y=s*0.5+j*(s+space), 
          s=str(int(val[i][j])),
          weight='extra bold',
          family='monospace',
          size=15,
          ha='center',
          va='center'
        )

def main():
  max_columns = 6
  fig = plt.figure(figsize=(12,6))
  ax = [fig.add_subplot(1, 2, 1), fig.add_subplot(1, 2, 2)]

  full_name = 'Jabari Walker'
  player = ply.get_player_by_name(name=full_name)
  seasons = ['2022-23', '2023-24']
  
  i = 0
  for season in seasons:
    logs = st.get_player_game_logs(player_id=player['id'], season=season)
    val = shape.shape_to_zorn_scatter(
            x_array = logs['PTS'],
            y_array = logs['AST'],
            max_columns = max_columns
          )
    cp1 = cp.ColorPicker()
    cp1.prepare()

    plot_box_scatter(ax[i], val, cp1)
    plot_label(ax[i], width=6, height=2, max_columns=max_columns)
    ax[i].set_title(f'{season}')

    i+=1
  
  size, space = 2, 1
  ax[0].set_xlim(-2,max_columns*(size+space))
  ax[0].set_ylim(-2,max_columns*(size+space))
  ax[1].set_xlim(-2,max_columns*(size+space))
  ax[1].set_ylim(-2,max_columns*(size+space))

  for axi in ax:
    ps.box_off(axi)

  fig.suptitle(f'{full_name} box scatter')
  plt.show()

if __name__ == "__main__":
  main()