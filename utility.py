# utils.py
# The Committee Will Look Into It
# This file contains all the functions resued in the actual notebooks 1-5.


import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns


# ---------------------------------------
# THEME
# ---------------------------------------

def set_style():
    sns.set_theme(style="whitegrid")
    plt.rcParams.update({
        "figure.figsize":        (20,7),
        "figure.facecolor":      "#f9f6f1",
        "axes.facecolor":        "#f9f6f1",
        "axes.edgecolor":        "#cccccc",
        "axes.spines.top":       False,
        "axes.spines.right":     False,
        "axes.titlepad":         15,
        "axes.labelpad":         11,
        "font.family":           "sans-serif",
        "xtick.color":           "#555555",
        "ytick.color":           "#555555",
        "grid.color":            "#e0e0e0",
        "grid.linestyle":        "--",
        "grid.alpha":            0.6
    })

