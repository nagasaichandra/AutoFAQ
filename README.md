# AutoFAQ

To generate frequently asked questions from sizable text

## All data used for [the paper][the-paper] are here:

```
https://www.kaggle.com/dataset/4042b656772a95f85e63ebc7438d8e91c86228aa76c9e64c536be7a39ee3fa54
```

short link: [bit.ly/platodata](bit.ly/platodata)

## File Descriptions

- `filtered.csv` -- the output of [this kaggle][filter_qs_kaggle]. Top 25 after heuristics.
- `filtered_and_rated_questions.csv` -- the downloaded CSV from [this AirTable][filtered_qs_airtable]. Same as `filtered.csv` but includes human evaluations.

## Generate the FAQ markdown files

```
python3 make_rated_md_docs.py
```

## [Click Here][markdowns] to see the pre-generated markdown documents

## [Click Here][pdfs] for select PDF files

> simply a print preview

> Note: [`pandoc`][how_md_to_pdf] can be used to generate pdfs too.

<details><summary>Or even try something like this</summary>

```
pandoc -f markdown -t latex markdowns/Cancer_faq.md -o latexs/Cancer_faq.tex
```

```
pandoc -f markdown -t latex markdowns/Cancer_faq.md  -o latexs//Cancer_faq.tex  \
    && pandoc -f markdown -t latex markdowns/Copenhagen\ Interpretation\ of\ Quantum\ Mechanics_faq.md  -o latexs//Copenhagen\ Interpretation\ of\ Quantum\ Mechanics_faq.tex  \
    && pandoc -f markdown -t latex markdowns/Cusanus,\ Nicolaus\ \[Nicolas\ of\ Cusa\]_faq.md  -o latexs//Cusanus,\ Nicolaus\ \[Nicolas\ of\ Cusa\]_faq.tex  \
    && pandoc -f markdown -t latex markdowns/Evolutionary\ Epistemology_faq.md  -o latexs//Evolutionary\ Epistemology_faq.tex  \
    && pandoc -f markdown -t latex markdowns/Infinite\ Regress\ Arguments_faq.md  -o latexs//Infinite\ Regress\ Arguments_faq.tex  \
    && pandoc -f markdown -t latex markdowns/Jean-Baptiste\ Du\ Bos_faq.md  -o latexs//Jean-Baptiste\ Du\ Bos_faq.tex  \
    && pandoc -f markdown -t latex markdowns/Kurt\ Gödel_faq.md  -o latexs//Kurt\ Gödel_faq.tex  \
    && pandoc -f markdown -t latex markdowns/Logicism\ and\ Neologicism_faq.md  -o latexs//Logicism\ and\ Neologicism_faq.tex  \
    && pandoc -f markdown -t latex markdowns/Medieval\ Theories\ of\ Causation_faq.md  -o latexs//Medieval\ Theories\ of\ Causation_faq.tex  \
    && pandoc -f markdown -t latex markdowns/Paul\ of\ Venice_faq.md  -o latexs//Paul\ of\ Venice_faq.tex  \
    && pandoc -f markdown -t latex markdowns/Philosophy\ of\ Biomedicine_faq.md  -o latexs//Philosophy\ of\ Biomedicine_faq.tex  \
    && pandoc -f markdown -t latex markdowns/The\ Epistemology\ of\ Religion_faq.md  -o latexs//The\ Epistemology\ of\ Religion_faq.tex
```

</details>

[filter_qs_kaggle]: https://www.kaggle.com/teja0110/filtered-questions/output
[filtered_qs_airtable]: https://airtable.com/shro9LCLITgxhYqWO/tbl1FuamJ4Nnk1TYC/viwc92aO0cm7B1fTI
[markdowns]: /markdowns
[pdfs]: /pdfs
[how_md_to_pdf]: https://gist.github.com/justincbagley/ec0a6334cc86e854715e459349ab1446
[the-paper]: /CSC_582__Auto_FAQ.pdf
