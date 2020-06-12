# AutoFAQ

To generate frequently asked questions from sizable text

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

[filter_qs_kaggle]: https://www.kaggle.com/teja0110/filtered-questions/output
[filtered_qs_airtable]: https://airtable.com/shro9LCLITgxhYqWO/tbl1FuamJ4Nnk1TYC/viwc92aO0cm7B1fTI
[markdowns]: /markdowns
[pdfs]: /pdfs
[how_md_to_pdf]: https://gist.github.com/justincbagley/ec0a6334cc86e854715e459349ab1446
