# PlottingSuite-python-


* Dependencies: scipy, numpy, seaborn, matplotlib, pandas, json, statsmodels

## Format of input
The majority of these functions take a list of lists (LOL) as the input. Most functions want an LOL and its associated labels, which could easily be taken from a dictionary or pandas DataFrame.

Here's an example input:

values = [
  np.random.random(200)*4. + 50,
  np.random.random(200)*4.1 + 50,
  np.random.random(200)*5.6 + 50,
  np.random.random(100)*3.6 + 40,
  np.random.random(100)*4.1 + 55,
  np.random.random(100)*3.1 + 45,
  ]
labels = [
  'Pyramidal',
  'Pyramidal',
  'Pyramidal',
  'PV+ interneuron',
  'PV+ interneuron',
  'PV+ interneuron',
  ]

Passing this to, say, *hori_scatter* produces a 1x6 array of subplots.

## What are these even good for?
This plotting suite was made for highly variable data, and so robust measures were needed in addition to intuitive plots. Medians are shown as often as means, and generally every sample has its own subplot. The data can be easily normalized and put on a log scale, and the groups are color coded based on set(labels), so the example above would have two colors. Colors can be easily changed.

Many of these plots display inter-quartile range, either as shading or with simple whiskers. The internal workings of many plots are similar, so if you can decipher one you'll have a good idea of what's going on in the others. See below for some examples.

## Common flags
Most plots have several of the following:
* title (str), axes (list of str, i.e.: ['','Length'] if no x-label is desired)
* bounds/rrange ([maxY, minY] or bool) - if outliers make data in a ragion-of-interest difficult to see, setting bonds will force outliers to sit on the boundary so the ROI can be examined
* showmean / showboth (bool) - show the mean +/- median, usually as a purple line (median: dashed/dotted)
* switch (bool)    - move dataset[0] to the back
* llog (bool)      - plot on a log scale
* counts (bool)    - show the number of data points in a list above the subgraph (helpful for small, non-uniform values)
* xcnt (bool)      - (for histograms and violins) show the max histogram value; since histograms/violins are normalized, one looses sight of the amount of data, and sometimes we're interested in when 1000 vs 40000 values contributes to the distribution
* bench (double/list) - plot a benchmark as a light purple line at the value; if a list, can be different for each plot
* forcebins (int/list) - for histograms/violins, can force a max number of bins (or specify exact bins). If the number of filled (len>=1) bins is less than forcebins/2, new bins are calculated and len(filled_bins)*2 is used for the number of bins
* showleg (bool, str) - if True, 'best' is used for the legend position, otherwise can be specified; False means legend is hidden
* shade (bool)     - (deprecated) IQRs used to be shown as large transparent blocks; some of this code is still hanging around though it doens't do anything in most cases
* eps (bool)       - (deprecated) PyPlot has difficulty saving alpha values to *.eps files, so a different hue of the color was used previously for shading; now, this color ("altcolor") is used for IQRs for all plots


## Examples

* *pretty_3d* 3-D feature plot with shadows
Three features (_v1_, _v2_, _v3_) and their associated labels (_labelsin_ -- used for color and legend) as plotted in 3-D. _shadows_ drops a line to the plane where _shadows_ = 0 (i.e.: shadows='z' drops a line from the point to the XY-plane). _ellipses_ shows the standard deviation in the XY-plane on the XY-plane; without much work, this could be changed from ellipses to 2-D crosshairs or whiskers.

![alt tag](https://raw.githubusercontent.com/acsutt0n/PlottingSuite-python-/master/\/subtrees_3d_scatter.png)

* *pretty_2d* 2-D feature plot
Similar to 3-D but ellipses now show all relevant information (no z-dimension to ignore).

![alt tag](https://raw.githubusercontent.com/acsutt0n/PlottingSuite-python-/master/paths_2d_scatter.png)

* *violin_spline* Modified boxplot
This is obviously based on the beautiful Seaborn package that everyone should be using (https://stanford.edu/~mwaskom/software/seaborn/). A main difference (as of this writing, 4/2016) is that the IQR is differentiated by another hue of the same color. _stepfilled_ (bool) shows the underlying histogram used to generate the data.

![alt tag](https://raw.githubusercontent.com/acsutt0n/PlottingSuite-python-/master/violin_example.png)

* *hori_scatter* Horizontal scatter plot
This allows for a _bench_ to be set (see above), and can indicate the IQR with simple lines. Simple is good.

![alt tag](https://raw.githubusercontent.com/acsutt0n/PlottingSuite-python-/master/scatter_bench_crosshairs.png)
