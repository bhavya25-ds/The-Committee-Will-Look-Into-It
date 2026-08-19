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




# ---------------------------------------
# DATA INPUT
# ---------------------------------------

def load_data(path, encoding="utf-8", sheet=0, **kwargs):
    ext = str(path).split(".")[-1].lower()
    if ext in ("xlsx", "xls"):
        return pd.read_excel(path, sheet_name=sheet, **kwargs)
    try:
        return pd.read_csv(path, encoding=encoding, **kwargs)
    except UnicodeDecodeError:
        return pd.read_csv(path, encoding="latin1", **kwargs)


def save_clean(df, path):
    df.to_csv(path, index= False)
    print(f"Saved | shape- {df.shape}")




# ---------------------------------------
# EDA
# ---------------------------------------

def eda(df, name="DataFrame"):
    print(f"  {name}")
    print(f"Shape       : {df.shape[0]} rows × {df.shape[1]} cols")
    print(f"\nDtypes:\n{df.dtypes.to_string()}")
    print(f"\nNull counts:\n{df.isnull().sum().to_string()}")
    print(f"\nNull %:\n{(df.isnull().mean() * 100).round(2).to_string()}")
    print(f"\nSample:\n{df.head(3).to_string()}")




# ---------------------------------------
# DATA CLEANING
# ---------------------------------------

def parse_dates(df, col, fmt="mixed"):
    df[col]= pd.to_datetime(df[col], format= fmt, dayfirst=True, errors= "coerce")
    df["year"]    = df[col].dt.year
    df["month"]   = df[col].dt.month
    df["quarter"] = df[col].dt.quarter
    return df



def clean_state_names(df, col):
    replacements = {
            "ANDAMAN & NICOBAR ISLANDS": "Andaman & Nicobar Islands",
            "JAMMU & KASHMIR":           "Jammu & Kashmir",
            "D & N HAVELI":              "Dadra & Nagar Haveli",
            "A & N ISLANDS":             "Andaman & Nicobar Islands",
            "D&NH AND DD":               "Dadra & Nagar Haveli and Daman & Diu",
        }
    df[col] = (
            df[col]
            .str.strip()
            .str.title()
            .replace(replacements)
    )
    return df


def fill_numeric_nulls(df, cols, fill_value=0):
    for col in cols:
        if col in df.columns:
            df[col]= df[col].fillna(fill_value)
    return df


def drop_totals(df, col, keywords= ("total", "all india", "india total")):
    mask= df[col].str.lower().str.strip().isin([k.lower() for k in keywords])
    dropped= mask.sum()
    df= df[~mask].reset_index(drop=True)
    print(f"Dropped {dropped} aggregate rows from '{col}'")
    return df


def clean_amount(series):
    "convert indian currency strings like '1,00,00,000' or '₹10 cr to plain intergers" 
    return(
        series.astype(str)
        .str.replace()
        .str.replace(r"[₹,\s]", "", regex=True)
        .str.replace(r"[Cc][Rr]", "0000000", regex=True)
        .str.replace(r"[Ll][Aa][Kk][Hh]", "00000", regex=True)
        .pipe(pd.to_numeric, errors="coerce")         
    )




# ---------------------------------------
# GRAPHS PLOTTING
# ---------------------------------------

