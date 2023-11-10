# profilometer
import numpy as np
import pandas as pd
from .misc import *
__all__ = ['parse_tabular']

def read_files(input_path, csv_path, plot_path, interactive=False, linear_regression=False, wide=False, subplots=False, reference=False, logy=False, zero_intercept=True, xrd=False):
    df = pd_read_csv( 
        filename=input_path, encoding="utf-8", sep=",", header_count=0,
        rename_columns=False,
    )
    df.to_csv(csv_path, index=False)
    p = Plot(df, interactive=interactive, linear_regression=linear_regression, wide=wide, subplots=subplots, reference=reference, logy=logy, zero_intercept=zero_intercept, xrd=xrd)
    p.plot(plot_path)

def parse_tabular(**kwargs):
    interactive = kwargs["interactive"] if "interactive" in kwargs.keys() else False
    linear_regression = kwargs["linear_regression"] if "linear_regression" in kwargs.keys() else False
    wide = kwargs["wide"] if "wide" in kwargs.keys() else False
    subplots = kwargs["subplots"] if "subplots" in kwargs.keys() else False
    reference = kwargs["reference"] if "reference" in kwargs.keys() else False
    logy = kwargs["logy"] if "logy" in kwargs.keys() else False
    xrd = kwargs["xrd"] if "xrd" in kwargs.keys() else False
    zero_intercept = kwargs["zero_intercept"] if "zero_intercept" in kwargs.keys() else False
    read_files(kwargs["input_path"], kwargs["csv_path"], kwargs["plot_path"], interactive=interactive, linear_regression=linear_regression, wide=wide, subplots=subplots, reference=reference, logy=logy, zero_intercept=zero_intercept, xrd=xrd)
