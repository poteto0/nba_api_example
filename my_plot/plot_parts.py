from matplotlib import patches

def FancyBboxPatch(
    bottom, left,
    width, height,
    color,
    edgecolor='black',
    lw=1,
    bs='round'
  ):
  return patches.FancyBboxPatch( 
            (bottom, left) , 
            width, height, 
            fc=color,
            ec=edgecolor,
            lw=lw,
            boxstyle=bs,
          )