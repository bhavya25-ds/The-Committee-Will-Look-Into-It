# utils.py
# The Committee Will Look Into It
# This file contains all the functions resued in the actual notebooks 1-5.


import os
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns


# ---------------------------------------
# CONSTANTS
# ---------------------------------------

DB_PATH = "committee_data.db"
FIG_SIZE = (20, 7)
BG_COLOR = "#f9f6f1"

THREAD_DIRS = {
    1: "01_Exam_Frauds",
    2: "02_Gender_Injustice",
    3: "03_MP_Performance",
    4: "04_Suppression_of_Dissent",
    5: "05_Corruption_Electoral_Bonds",
}


# ---------------------------------------
# THEME
# ---------------------------------------

def set_style():
    sns.set_theme(style="whitegrid")
    plt.rcParams.update({
        "figure.figsize":        FIG_SIZE,
        "figure.facecolor":      BG_COLOR,
        "axes.facecolor":        BG_COLOR,
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
    with pd.option_context(
        'display.max_columns', None, 
        'display.max_rows', None, 
        'display.max_colwidth', None,
        'display.width', None
    ):
        print(f"=== {name} ===")
        print(f"Shape       : {df.shape[0]} rows × {df.shape[1]} cols")
        print(f"Duplicates  : {df.duplicated().sum()}")
        
        null_info = pd.DataFrame({
            'Dtype': df.dtypes,
            'Nulls': df.isnull().sum(),
            'Null %': (df.isnull().mean() * 100).round(2),
            'Uniques': df.nunique()
        })
        print(f"\nColumn Summary:\n{null_info.to_string()}")
        
        num_cols = df.select_dtypes(include=['number']).columns
        if len(num_cols) > 0:
            stats = df[num_cols].agg(['min', 'max', 'mean', 'median']).T.round(2)
            print(f"\nNumeric Stats:\n{stats.to_string()}")
            
        print(f"\nSample:\n{df.head(3).to_string()}\n")

def missing_report(df, name="DataFrame", sparse_threshold=50):
    """
    Prints null counts, null %, dtype, and flags columns with >sparse_threshold% nulls as SPARSE.
    """
    
    print(f"  {name}")
    print(f"Shape       : {df.shape[0]} rows × {df.shape[1]} cols\n")

    null_counts = df.isnull().sum()
    null_pct    = (df.isnull().mean() * 100).round(2)

    report = pd.DataFrame({
        "dtype"      : df.dtypes,
        "null_count" : null_counts,
        "null_%"     : null_pct,
    })
    report["flag"] = report["null_%"].apply(
        lambda x: "SPARSE" if x > sparse_threshold else ""
    )

    print(report.to_string())

    sparse_cols = report[report["flag"] != ""].index.tolist()
    if sparse_cols:
        print(f"\nSparse columns (>{sparse_threshold}% null): {sparse_cols}")
    else:
        print(f"\nNo columns exceed {sparse_threshold}% null threshold.")




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
            .astype(str)
            .str.strip()
            .str.upper()
            .replace(replacements)
            .str.title()
    )
    return df


def fill_numeric_nulls(df, cols, fill_value=0):
    for col in cols:
        if col in df.columns:
            df[col]= df[col].fillna(fill_value)
    return df


def drop_totals(df, col, keywords= ("Total", "Total State (S)", "Total UT (S)", "Total All India", "All India", "India Total", "ALL INDIA", "TOTAL CITIES", "All India (Total)")):
    mask= df[col].str.lower().str.strip().isin([k.lower() for k in keywords])
    dropped= mask.sum()
    df= df[~mask].reset_index(drop=True)
    print(f"Dropped {dropped} aggregate rows from '{col}'")
    return df


def clean_amount(series):
    """Convert Indian currency strings like '1,00,00,000' or '₹10 Cr' to plain integers."""
    return(
        series.astype(str)
        .str.replace(r"[₹,\s]", "", regex=True)
        .str.replace(r"[Cc][Rr]", "0000000", regex=True)
        .str.replace(r"[Ll][Aa][Kk][Hh]", "00000", regex=True)
        .pipe(pd.to_numeric, errors="coerce")         
    )


def conviction_rate(convicted, tried):
    """
    Returns conviction rate as a percentage.
    Both inputs can be scalars or Series.
    Returns NaN where tried == 0 to avoid division by zero.
    """
    convicted = pd.to_numeric(convicted, errors="coerce")
    tried     = pd.to_numeric(tried,     errors="coerce")
    return (convicted / tried.replace(0, pd.NA)) * 100


def per_lakh(count, population):
    """
    Returns incidents per lakh (100,000) population.
    Both inputs can be scalars or Series.
    Returns NaN where population == 0 to avoid division by zero.
    """
    count      = pd.to_numeric(count,      errors="coerce")
    population = pd.to_numeric(population, errors="coerce")
    return (count / population.replace(0, pd.NA)) * 1e5


def wide_to_long(df, id_cols, value_name="crime_count", var_name="year"):
    # Example (NCRB data):
    #   long_df = wide_to_long(df, id_cols=["state_ut", "crime_head"], value_name="cases", var_name="year")
    #   Turns year columns (2019, 2020, 2021 …) into a single 'year' column with one row per state-crime-year.
    
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
    fig.savefig(path, bbox_inches= "tight", dpi= dpi, facecolor= BG_COLOR)
    print(f"Chart saved- {path}")
    return path


def label_bars(ax, fmt= "{:.0f}", pad=2, fontsize=10, color= "#333333"):
    for p in ax.patches:
        h= p.get_height()
        if pd.notna(h) and h != 0:
            ax.annotate(
                fmt.format(h),
                xy= (p.get_x() + p.get_width() / 2, h),
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
    base = THREAD_DIRS.get(thread_num, f"thread_{thread_num}")
    path = os.path.join(base, filename)
    return load_data(path, **kwargs)




# ---------------------------------------
# DATABASE HELPERS
# ---------------------------------------

def get_db_connection(db_path=DB_PATH):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def df_to_db(df, table_name, conn, if_exists="replace"):
    df.to_sql(table_name, conn, if_exists=if_exists, index=False)
    print(f"Written → {table_name} | shape: {df.shape}")

def query_db(query, conn):
    return pd.read_sql_query(query, conn)