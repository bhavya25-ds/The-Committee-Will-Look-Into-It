# utils.py
# The Committee Will Look Into It
# This file contains all the functions resued in the actual notebooks 1-5.


import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
from sqlalchemy import create_engine



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


def wide_to_long(df, id_cols, value_name="crime_count", var_name="year"):
    id_vars = [id_cols] if isinstance(id_cols, str) else id_cols
    
    long_df = df.melt(
        id_vars=id_vars,
        var_name=var_name,
        value_name=value_name
    )
    return long_df




# ---------------------------------------
# GRAPHS PLOTTING
# ---------------------------------------

def save_fig(fig, folder, filename, dpi=175):
    os.makedirs(folder, exist_ok=True)
    path= os.path.join(folder,filename)
    fig.savefig(path, bbox_inches= "tight", dpi= dpi, facecolor= "#f9f6f1")
    print(f"Chart saved- {path}")
    return path


def label_bars(ax, fmt= "{:.0f}", pad=2, fontsize=10, color= "#333333"):
    for p in ax.patches:
        h= p.get_height()
        if pd.notna(h) and h != 0:
            ax.annotate(
                fmt.format(h),
                xy= (p.get_x() + p.get_wight / 2, h),
                xytext=(0, pad),
                textcoords="offset points",
                ha="center",
                va="bottom",
                fontsize=fontsize,
                color=color,
            )


def add_source(ax, text, fontsize=8, color= "#888888"):
    ax.annotate(
        f"Source: {text}",
        xy=(0, -0.15),
        xycoords="axes fraction",
        fontsize=fontsize,
        color=color,
    )


def crore_formatter(x, pos):
    "For money"
    if x >= 1e7:
        return f"₹{x/1e7:.0f} Cr"
    elif x >= 1e5:
        return f"₹{x/1e5:.0f} L"
    return f"₹{x:.0f}"


def lakh_formatter(x, pos):
    "For data values"
    return f"{x/1e5:.1f}L" if x >= 1e5 else f"{x:.0f}"




# ---------------------------------------
# THREAD LOADERS
# ---------------------------------------

def load_thread(thread_num, filename, **kwargs):
    thread_dirs = {
        1: "01_Exam_Frauds",
        2: "02_Gender_Injustice",
        3: "03_MP_Performance",
        4: "04_Suppression_of_Dissent",
        5: "05_Corruption_Electoral_Bonds",
        }
    base = thread_dirs.get(thread_num, f"thread_{thread_num}")
    path = os.path.join(base, filename)
    return load_data(path, **kwargs)




# ---------------------------------------
# DATABASE HELPERS
# ---------------------------------------

def get_db_connection(user="root", password="your_password", host="localhost", database="your_db_name"):
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")
    return engine

def df_to_db(df, table_name, engine, if_exists="replace"):
    df.to_sql(table_name, con=engine, if_exists=if_exists, index=False)
    print(f"Written → {table_name} | shape: {df.shape}")

def query_db(query, engine):
    return pd.read_sql_query(query, con=engine)