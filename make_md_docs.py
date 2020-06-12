#!/usr/bin/env python


import pandas as pd
import re

CSV_FILE = "filtered_and_rated_questions.csv"  # "filtered.csv"
Q_COL = "question"
A_COL = "summarized_paragraph"
S_COL = "sentence"
ARTICLE_TITLE_COL = "title"
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
    markdown += f"# [{article_title}](https://{url}) \n\n"
    for _, (q, a, s) in grouping[[Q_COL, A_COL, S_COL]].iterrows():
        for match in re.findall(fr"{s}", a, re.IGNORECASE):
            a = a.replace(match, f"**{match}**")
        markdown += f"## {q} \n" f"> {a}  \n\n"
    return markdown


md_df = df.groupby(ARTICLE_TITLE_COL).apply(fun)


for title, md in md_df.iteritems():
    with open(f"{title}_faq.md", "w") as f:
        f.write(md)
