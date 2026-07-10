# PG Data Science and Analytics – Semester III Practicals

This repository contains practical programs, Jupyter notebooks, Python scripts, and datasets for the **PG Data Science and Analytics Course – IIIrd Semester Practicals**. The projects and exercises cover concepts in **Machine Learning (ML)**, **Natural Language Processing (NLP)**, and **Internet of Things (IoT)**, web scraping, and parsing.

---

## 📁 Repository Structure & Contents

```text
PG_S3/
├── Datasets/                      # Datasets for practical exercises
├── PG_S3_ML/                      # Machine Learning Practicals
├── PG_S3_NLP/                     # Natural Language Processing Practicals
│   └── PG_S3_NLP_Lab/             # NLP Laboratory assignments
├── PG_S3_IoT/                     # Web Scraping & Parsing
│   └── PG_S3_IoT_0f_web_scrape/
│       ├── IoT_Webscrape_local/   # Local HTML DOM tree navigation and parsing
│       ├── IoT_Parsing/           # Data parsers (CSV, JSON, Plain Text, XML)
│       └── IoT_Data_Cleaning/     # Data cleaning and regular expressions
```

---

## 🛠 Required Libraries & Packages

### 1. Natural Language Processing (NLP)
* **`spacy`** (`>=3.8.13`): Industrial-strength NLP library used for tokenization, Part-of-Speech (PoS) tagging, dependency parsing, and pre-trained language pipelines.
* **`nltk`** (`>=3.9.4`): Natural Language Toolkit used for word/sentence tokenization, stopword removal, N-gram modeling, and accessing corpus datasets (e.g., Gutenberg).
* **`textblob`** (`>=0.20.0`): Simple library built on NLTK/Pattern for sentiment analysis, noun phrase extraction, and language processing.
* **`wordcloud`** (`>=1.9.6`): Visual generator for creating word clouds based on word frequencies.

### 2. Machine Learning & Data Manipulation
* **`scikit-learn`** (`>=1.9.0`): Core machine learning library used for Random Forest classification/regression (`RandomForestClassifier`), feature scaling, vectorization (`CountVectorizer`), and model evaluation (`accuracy_score`, `classification_report`, `confusion_matrix`).
* **`category-encoders`** (`>=2.9.0`): Scikit-learn compatible transformer classes for encoding categorical variables (e.g., One-Hot, Ordinal, Target Encoding).
* **`pandas`** (`>=3.0.3`): Data manipulation and analysis library used for handling tabular datasets, DataFrames, and CSV processing.
* **`numpy`** (`>=1.24.1`): Fundamental package for scientific computing and numerical matrix operations.
* **`scipy`** & **`joblib`**: Mathematical computation tools and parallel processing utilities required by scikit-learn.

### 3. Data Visualization
* **`matplotlib`** (`>=3.11.0`): Comprehensive plotting library for 2D charts and data visualizations.
* **`seaborn`** (`>=0.13.2`): Statistical data visualization library built on top of Matplotlib for attractive statistical graphics.

### 4. Web Scraping & IoT Data Acquisition
* **`beautifulsoup4`** (`bs4`): Library for pulling data out of HTML and XML files (`BeautifulSoup`).
* **`requests`** (`>=2.31.0`): HTTP library used to send network requests and fetch web pages (`requests.get`).
* **`lxml`** (`>=5.0.0`): Fast and feature-rich XML/HTML parser utilized by BeautifulSoup (`BeautifulSoup(response.text, 'lxml')`).
* **`fake-useragent`** (`>=2.2.0`): Utility to generate randomized web browser User-Agent headers to prevent blocking during web scraping.

### 5. Standard Python Library Modules
* **`csv`**, **`json`**, **`xml.etree.ElementTree`**: Built-in parsers used in `IoT_Parsing` for structured data ingestion.
* **`re`**: Regular expressions used for text normalization and data cleaning in IoT and NLP workflows.
* **`time`** (`sleep`) & **`random`**: Used for ethical web scraping pacing and rate-limiting control.

---

## ⚙️ Environment Setup

To install all required dependencies into your virtual environment:

```bash
# Using pip and requirements.txt
pip install -r requirements.txt
```

After installation, make sure to download the necessary NLTK corpora and spaCy language models:

```bash
# Download required NLTK datasets
python -m nltk.downloader stopwords punkt gutenberg

# Download spaCy English language model
python -m spacy download en_core_web_sm
```
