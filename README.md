# databricks_ml

A beginner-friendly machine learning practice repository with:

- **NLP notebooks** in `ML for NLP/` (tokenization, stemming, lemmatization, TF-IDF, Word2Vec, NER, POS tagging)
- **Data-cleaning notebook** in `notebooks/data_clean.ipynb`
- **Simple Streamlit demos** in `Streamlit/` (widgets, dataframe viewer, and Iris classification)

## Repository structure

```text
databricks_ml/
├── ML for NLP/
│   ├── 5-Stemming+And+Its+Types-+Text+Preprocessing.ipynb
│   ├── 6-Lemmatization-+Text+Preprocessing.ipynb
│   ├── 7-Text+Preprocessing-Stopwords+With+NLTK.ipynb
│   ├── 8-Parts+Of+Speech+Tagging.ipynb
│   ├── 9-Named+Entity+Recognition.ipynb
│   ├── 15-Bag+Of+Words+Practical's.ipynb
│   ├── 16-TF-IDF+Practical.ipynb
│   ├── 26-Word2vec_Practical_Implementation.ipynb
│   └── NLTK.ipynb
├── notebooks/
│   └── data_clean.ipynb
├── Streamlit/
│   ├── app.py
│   ├── classification.py
│   └── widget.py
├── requirements.txt
└── environment.yml
```

## Setup

### Option 1: pip

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

### Option 2: Conda

```bash
conda env create -f environment.yml
conda activate databricks-env
```

## Run Streamlit apps

From the repository root:

```bash
streamlit run Streamlit/app.py
```

Other demos:

```bash
streamlit run Streamlit/widget.py
streamlit run Streamlit/classification.py
```

## Notes

- This repo is primarily educational and notebook-focused.
- Some notebook names include special characters (`+`, `'`), so quote paths in shell commands when needed.
