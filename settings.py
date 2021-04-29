# suppress warnings
import warnings


warnings.filterwarnings("ignore")

# common imports
import matplotlib
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import re
import glob
import os
import sys
import json
import random
import logging
import seaborn as sns
import regex as re
import shutil
import urllib.request 
#import bamboolib as bam
from datetime import datetime
#from tqdm.auto import tqdm

# register `pandas.progress_apply` and `pandas.Series.map_apply` with `tqdm`
#tqdm.pandas()

# pandas display options
# https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html#available-options
#pd.options.display.max_columns = 30  # default 20
#pd.options.display.max_rows = 999  # default 60
pd.options.display.float_format = "{:.2f}".format
# pd.options.display.precision = 2
pd.options.display.max_colwidth = 200  # default 50; -1 = all
# otherwise text between $ signs will be interpreted as formula and printed in italic
#pd.set_option("display.html.use_mathjax", False)


#pd.set_option('display.max_rows', 500)
#pd.set_option('display.max_columns', 500)
#pd.set_option('display.width', 1000)

# np.set_printoptions(edgeitems=3) # default 3


plot_params = {
    "figure.figsize": (10, 6),
    "axes.labelsize": "large",
    "axes.titlesize": "large",
    "xtick.labelsize": "large",
    "ytick.labelsize": "large",
    "figure.dpi": 100,
}
# adjust matplotlib defaults
matplotlib.rcParams.update(plot_params)


sns.set_style("darkgrid")

# additional imports by Jay
#from wordcloud import WordCloud
#from PIL import Image
#from collections import Counter

print(f"Imports and display options set...")
