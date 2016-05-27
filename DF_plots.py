# DF_plots.py -- some more complex plots that take DFs as input,
#                rather than lists of lists


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt




# Cohort plot
# -- this actually requires a data frame

def cohort(df, cntCol, startCol, endCol, as_date=True, title=None,
           axes=None):
  """
  Based on beautiful work by Panos Ipeirotis @ 
  http://www.behind-the-enemy-lines.com/2016/02/a-cohort-analysis-of-mechanical-turk.html
  - cntCol is the count -- (str) number of users, preps, etc.
  - startCol -- (str) firstSeen; endCol -- (str) lastSeen
  - as_date -- (bool) forces start/end to dates, else uses floats
  """
  # Check inputs; if a DF, need strings to identify column inputs
  if type(df) is pd.DataFrame:
    if type(cntCol) != type(startCol) != type(endCol) != str:
      print('If passing a DF, pass the column titles (as strings) \n for counts, start and end')
  elif type(df) is None: # If DF is none, then cntCol, start, endCol are lists/arrays
    try:
      mat = np.array([[startCol[i], endCol[i], cntCol[i]] for i in range(len(cntCol))])
      df = pd.DataFrame(mat, columns=['firstSeen', 'lastSeen', 'cnt'])
      cntCol, startCol, endCol = 'cnt', 'firstSeen', 'lastSeen'
    except:
      print('Could not load lists/arrays; make sure they are same length?')
  
  # Pivot and clean the tables
  pivot = pd.pivot_table(df, values=cntCol, index=[endCol], 
                         columns=[startCol])
  # Order by cumulative row-wise sums
  pc = pivot.cumsum()
  # Max value for column [c] (sum for that time point), 
  pc2 = pd.DataFrame(pivot) # then subtract for each subsequent time point
  for c in pc.columns.values:
    pc2[c] = np.amax(pc, axis=0)[c] - pc[c].shift()
  for c in pc.columns.values: # Fill in diagonal (currently NaNs, but should be max cnt)
    pc2.at[c,c] = np.amax(pc, axis=0)[c]
  
  # Create the plot
  f = plt.figure(edgecolor='k')
  ax = f.gca()
  pc2.plot(kind='area', stacked=True, legend=True, figsize=(16,8), 
           cmap='Paired', grid=True, ax=ax)
  if title is not None:
    plt.title(title)
  plt.legend(loc='lower center', ncol=9, bbox_to_anchor=[0.5, -0.25])
  if axes is not None:
    ax.set_xlabel(axes[0])
    ax.set_ylabel(axes[1])
  plt.show(); return







#######################################################################

if __name__ == "__main__":
  print('Module must be used interactively')



  
