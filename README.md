<img src="./multimedia/umc_utrecht.png" width=200 align="right">

# Cookiecutter Data Science at UPOD

This is a Cookiecutter template for Data Science projects at UPOD. It is based on the [template by DataDriven](https://github.com/drivendata/cookiecutter-data-science/tree/master) (you can see the [original project's homepage here](http://drivendata.github.io/cookiecutter-data-science/)).


## How to use this Cookiecutter template:

1. Create a new environment (for example, using [`conda`](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands)). Make sure that it uses Python >= 3.8 (preferably Python 3.11). *Note that Python 2 is not supported!*
1. Install [Cookiecutter package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0.

   Using `conda`:

   ``` bash
   conda install -c conda-forge cookiecutter
   ```

   or

   Using `pip`:
   ``` bash
   pip install cookiecutter
   ```
1. Go to the directory where your project will be created and open a command prompt there.
1. Then, type

   ``` bash
   cookiecutter https://github.com/UPOD-datascience/cookiecutter-ds	
   ```
1. Fill in the required questions (pretty straightforward).
1. Start tracking your project with Git (optional, but much recommended)
1. DONE!

#### Bonus!
To easily link all your Python scripts in `./src/` with your notebooks (i.e., make them findable), open a command prompt *in your project's root* and type

``` bash
pip3 install --editable .
```
This way, all your scripts in the `./src` folder will be easily importable as `from src.funct import function`. 
  
## Documentation
`TODO`

> In the future, we want to support documentation using [`MkDocs`](https://www.mkdocs.org/). The main advantage is that it is easy to set up, it supports [Markdown formatting](https://www.markdownguide.org/), and it looks great.

To further customize the documentation, take a look at the [`Material for MkDocs documentation`](https://squidfunk.github.io/mkdocs-material/setup/) (sorry for the redundancy).


## Resulting directory structure

The directory structure of your new project will look like this:

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
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```

## Installing development requirements

    pip install -r requirements.txt


## Running the tests

    py.test tests


## Resources
* [Cookiecutter](https://github.com/cookiecutter/cookiecutter)
* [Original template by DataDriven](https://github.com/drivendata/cookiecutter-data-science/tree/master)
