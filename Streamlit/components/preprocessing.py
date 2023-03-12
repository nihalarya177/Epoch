from AutoClean import AutoClean
import pandas as pd
import re
from string import punctuation
import emoji
from .data_profiling import get_data_profile_report
from jenkspy import JenksNaturalBreaks
import numpy as np


def auto_clean(df: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """Autoclean using py-autoclean

    Args:
        df (pd.Datafrmae)
    """
    pipeline = AutoClean(
        df,
        "manual",
        duplicates="auto",
        missing_num=False,
        missing_categ=False,
        outliers="winz",
        encode_categ=False,
        extract_datetime="D",
    )
    return pipeline.output


def na_handler(data: pd.DataFrame, threshold=0.1):
    # ------handling null values------
    # drop columns and rows with all null values
    data.dropna(axis=1, how="all", inplace=True)
    data.dropna(axis=0, how="all", inplace=True)
    # dropping column and rows which have null values more than set threshold
    thresh_ver = round(len(data) * threshold)
    thres_hor = round(data.shape[1] * threshold)
    print(thresh_ver, thres_hor)
    print(data.shape)
    data.dropna(axis=1, thresh=thresh_ver, inplace=True)
    print(data.shape)
    data.dropna(axis=0, thresh=thres_hor, inplace=True)
    print(data.shape)
    return data


def clean_text(text: str) -> str:
    """Clean text removes punctuations,special characters, extra whitespaces and demojize the emojis

    Args:
        text (str): Text to eb cleaned

    Returns:
        str: Cleaned Text
    """
    # remove special characters and lowercase text
    text = re.sub(r"[^\w\s]", "", text.lower())

    # remove punctuation
    text = "".join(c for c in text if c not in punctuation)

    # remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    # de-emojize
    text = emoji.demojize(text)

    return text


def govf(jnb, arr):
    sdam = np.sum((arr - arr.mean()) ** 2)
    sdcm = sum([np.sum((g - g.mean()) ** 2) for g in jnb.groups_])
    return (sdam - sdcm) / sdam


def binit(ser: pd.Series, MAXCAT: int) -> (pd.Series, object):
    opt = MAXCAT
    for k in range(2, MAXCAT):
        jnb = JenksNaturalBreaks(k)
        arr = np.array(ser)
        jnb.fit(arr)
        thresh = govf(jnb, arr)
        if thresh > 0.8:
            opt = k
            break

    jnb = JenksNaturalBreaks(opt)
    arr = np.array(ser)
    jnb.fit(arr)
    lab = jnb.labels_
    breaks = ["-inf"] + [str(i) for i in jnb.inner_breaks_] + ["+inf"]
    ans = []
    for i in lab:
        ans = ans + [breaks[i] + "< " + ser.name + " <" + breaks[i + 1]]
    return (pd.Series(ans), jnb)


def bin_numeric_columns(df: pd.DataFrame):
    for c in df:
        col = df[c]
        col_notna = col[col.notna()]
        col_, jnb_ = binit(col_notna, 10)

        col_cleaned = []
        counter = 0
        for i in range(len(col)):
            if pd.notna(col[i]):
                col_cleaned += [col_[i - counter]]
            else:
                col_cleaned += [None]
                counter = counter + 1
        df[c] = pd.Series(col_cleaned)
    return df


def downsampler(df: pd.DataFrame):
    ...


class PreprocessPipeline:
    def __init__(self, df: pd.DataFrame, thresh=0.1):
        self.df = na_handler(df, thresh)
        self.cleaned_df = auto_clean(self.df)
        self.report = get_data_profile_report(self.cleaned_df)
        self.process_report_df()

    def process_report_df(self):
        descriptions = self.report.description_set
        # categorical columns
        max_cat = len(self.df) // 5  # max categories is 20% of length of df
        cat_cols = []
        text_cols = []
        rejected_cols = []
        for var, var_details in descriptions["variables"].items():
            if (
                var_details["type"] == "Categorical"
                and var_details["n_distinct"] <= max_cat
                and var_details["p_distinct"] <= 0.8
            ):
                cat_cols.append(var)
            elif (
                var_details["type"] == "Categorical" and var_details["p_distinct"] > 0.5
            ):
                text_cols.append(var)
            elif var_details["type"] == "Categorical":
                rejected_cols.append(var)
        # removing rejected columns
        self.cleaned_df.drop(columns=rejected_cols, inplace=True)
        # astry category
        for i in cat_cols:
            self.cleaned_df[i] = self.cleaned_df[i].astype("category")

    def get_rule_mining_df(self):
        # only return int,float and category columns
        numeric_df = self.cleaned_df.select_dtypes(include=["number"])
        numeric_df = bin_numeric_columns(numeric_df)
        cat = self.cleaned_df.select_dtypes(include=["category"]).copy()

        return pd.concat([numeric_df, cat], axis=1)
