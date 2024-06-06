# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
#
# <h1><img align="right" width="20%" src="../multimedia/umc_utrecht.png"> {{cookiecutter.project_name}} </h1>
#
# # 01 - Notebook

# %% [markdown]
# ## Objective
# This notebook shows...
#
# ## Preliminaries

# %%
import pandas as pd
import pathlib

# %%
current_timestamp = pd.Timestamp.now()
print(f"Execution of this notebook started on {current_timestamp}")

# %% [markdown]
# Path definition

# %%
path_data_raw = pathlib.Path('..', 'data', 'raw')
path_data_processed = pathlib.Path('..', 'data', 'processed')
path_results = pathlib.Path('..', 'results')

# %% [markdown]
# ## ...

# %%


# %% [markdown]
# ## References
#
# * ...

# %%
current_timestamp = pd.Timestamp.now()
print(f"Execution of this notebook ended on {current_timestamp}")
