import numpy as np
import matplotlib.colors as clr
from sklearn import preprocessing

class ColorPicker:
  def __init__(self, colors = np.array([[0, '#1e90ff'], [50, '#ffffff'], [100, '#ff0000']])):
    self.colors = colors

  def prepare(self):
    colorindex = self.colors[:, 0].astype(np.float32)
    colorindex = preprocessing.minmax_scale(colorindex)

    colornorm = []
    for no, norm in enumerate(colorindex):
      colornorm.append([norm, self.colors[no, 1]])
    
    self.color_map = clr.LinearSegmentedColormap.from_list('a', colornorm, N=100)

  def pick(self, val):
    r,g,b,a = np.array(self.color_map(int(val)))
    return (r, g, b)

  def get_color_map(self):
    self.prepare()
    return self.color_map