# suppress warnings
import warnings
warnings.filterwarnings("ignore")


# common python imports
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
from datetime import datetime

from tqdm.auto import tqdm

# register `pandas.progress_apply` and `pandas.Series.map_apply` with `tqdm`
tqdm.pandas()

# pandas display options
# https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html#available-options
pd.options.display.float_format = "{:.2f}".format
pd.options.display.max_colwidth = 200  # default 50; -1 = all

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


RIVANA = False

if RIVANA != True:
    import findspark
    findspark.init()

from pyspark.ml import Pipeline
from pyspark.sql import SparkSession
from pyspark import SparkConf
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.types import IntegerType
from pyspark.sql.functions import udf
from pyspark.sql.functions import col

from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator
from pyspark.ml.evaluation import ClusteringEvaluator

from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import OneHotEncoder, StringIndexer
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.classification import LinearSVC

from sklearn.metrics import accuracy_score
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# setting seed to be used across all model's consistently
SEED = 42 
print(f"SEED variable set to {SEED}")
print(f"Imports and display options set...")
