#!/usr/bin/env python


import pandas as pd
import re


CSV_FILE = "filtered_and_rated_questions.csv"  # "filtered.csv"
Q_COL = "question"
A_COL = "summarized_paragraph"
S_COL = "sentence"
ARTICLE_TITLE_COL = "title"
AGG_G = "avg_grammar_rating"
AGG_A = "avg_answerability_rating"
AGG_M_Y = "sum_yes_meaningful"
AGG_M_N = "sum_no_meaning"
AGG_M_M = "sum_maybe_meaning"
URL_COL = "filename"
SYDNEY_MIRROR_HOST = "stanford.library.sydney.edu.au"
PLATO_ORIGINAL_HOST = "plato.stanford.edu"

df = pd.read_csv(CSV_FILE)


def fun(grouping):
    uniq_filenames = grouping[URL_COL].unique()
    article_titles = grouping[ARTICLE_TITLE_COL].unique()
    assert (
        len(uniq_filenames) == 1
    ), f"unexpected grouping-by-title lacks unique set of 1 for columns {URL_COL}"
    assert (
        len(article_titles) == 1
    ), f"unexpected grouping-by-title lacks unique set of 1 for columns {ARTICLE_TITLE_COL}"
    url = uniq_filenames[0]
    article_title = article_titles[0]
    url = url.replace(SYDNEY_MIRROR_HOST, PLATO_ORIGINAL_HOST)
    markdown = ""
    markdown += f"# [{article_title}](https://www.{url}) \n\n"
    mask = [Q_COL, A_COL, S_COL, AGG_G, AGG_A, AGG_M_Y, AGG_M_N, AGG_M_M]
    for _, (q, a, s, ag, aa, amy, amn, amm) in grouping[mask].iterrows():
        for match in re.findall(fr"{s}", a, re.IGNORECASE):
            a = a.replace(match, f"**{match}**")
        markdown += (
            f"## {q} \n"
            f"> _{A_COL}_ : {a}  \n\n"
            f"> _{AGG_G}_ : {ag}  \n"
            f"> _{AGG_A}_ : {aa}  \n"
            f"> _{AGG_M_Y}_ : {amy}  \n"
            f"> _{AGG_M_N}_ : {amn}  \n"
            f"> _{AGG_M_M}_ : {amm}  \n\n"
        )
    return markdown


md_df = df.groupby(ARTICLE_TITLE_COL).apply(fun)


for title, md in md_df.iteritems():
    with open(f"{title}_faq.md", "w") as f:
        f.write(md)
