<img src="./multimedia/umc_utrecht.png" width=200 align="right">

# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Project Organization

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump. 
│                         This is a good place for including data dictionaries.
│
├── dissemination      <- To be shared with outer audiences.
│   ├── documents      <- Articles, written reports, etc.
│   │   └── paper      <- LaTeX template for a paper
│   ├── figures        <- Generated graphics and figures to be used in reporting
│   ├── posters        <- Typically for conferences
│   └── presentations  <- Usually PowerPoints (and their corresponding PDF)
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│                         TODO: switch to MkDocs
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── multimedia         <- Handy images, icons, GIFs, etc.
│
├── notebooks          <- Jupyter notebooks. Naming convention is a two-digit number (for ordering),
│                         the creator's initials, and a short description, all in camel case, 
│                         for instance 01_amt_exploratory_data_analysis
│
├── references         <- Manuals, PDFs, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── results            <- Intermediate and/or final results (figures, variables, etc.).
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── helpers        <- Auxiliary scripts
│   │   └── helpers.py
│   │
│   ├── modeling       <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```

--------
<p><small>Project based on <a target="_blank" href="https://github.com/UPOD-datascience/cookiecutter-ds">UPOD's Cookiecutter template for Data Science</a>.</small></p>
