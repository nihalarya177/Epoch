import pandas as pd

# from pycaret.classification import *
from .summarizer import get_openai_response
from scipy.stats import chi2_contingency


def get_top_correlated_features(df: pd.DataFrame, column: str, thresh=0.6):
    features = []
    num_corrs = df.corrwith(df[column])
    num_corrs.drop(column, inplace=True)
    for i, j in num_corrs.items():
        if abs(j) > i:
            features.append(j)
    return features


def get_df_description(df: pd.DataFrame):
    pd.set_option("display.max_colwidth", None)
    resp = get_openai_response(
        f"Explain this table without adding extra information in very simple way \n \n {df.head(n=20).reset_index(drop=True).__str__()}"
    )
    return resp["choices"][0].text


def get_top_correlated_features(
    df: pd.DataFrame, column: str, thresh=0.6, cat_thresh=0.3
):
    features = []
    num_corrs = df.corrwith(df[column])
    num_corrs.drop(column, inplace=True)
    for i, j in num_corrs.items():
        if abs(j) > thresh:
            features.append(i)
    cat = df.select_dtypes("category")
    for i in cat:
        if i == column:
            continue
        carmer = carmers_stats(df, col1=column, col2=i)
        if carmer > cat_thresh:
            features.append(i)
    return features


def carmers_stats(df, col1, col2):
    # create a contingency table
    contingency_table = pd.crosstab(df[col1], df[col2])

    # calculate the chi-square statistic and p-value
    chi2, p, dof, expected = chi2_contingency(contingency_table)

    # calculate the Cramer's V statistic
    n = contingency_table.sum().sum()
    phi2 = chi2 / n
    r, k = contingency_table.shape
    phi2corr = max(0, phi2 - ((k - 1) * (r - 1)) / (n - 1))
    r_corr = r - ((r - 1) ** 2) / (n - 1)
    k_corr = k - ((k - 1) ** 2) / (n - 1)
    cramers_v = np.sqrt(phi2corr / min((k_corr - 1), (r_corr - 1)))

    return cramers_v
