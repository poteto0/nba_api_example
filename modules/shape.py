import numpy as np
import math

def shape_to_zorn_scatter(
    x_array,
    y_array,
    width = 6, 
    height = 2,
    max_columns = 6,
  ):
  if len(x_array) != len(y_array):
    print("array size is not equal")
    return [[]]
  
  val = np.zeros((max_columns, max_columns))
  for x, y in zip(x_array, y_array):
    x_idx = round_max(int((int(x)) / width), max_columns-1)
    y_idx = round_max(int((int(y)) / height), max_columns-1)

    val[x_idx][y_idx] += 1
  
  return val

def round_max(v, m):
  return m if v > m else v