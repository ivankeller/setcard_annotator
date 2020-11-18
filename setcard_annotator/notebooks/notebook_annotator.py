# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: setgame
#     language: python
#     name: setgame
# ---

# # Annotate Set game cards
# Interractive annotator tool for Set card image  

# ## configuration

# +
# examples to annotate: list of path or directory with card images
examples = ''

# output directory for annotation saved as json files
# If None annotations are saved by default in `labels` sub-directory of the examples directory
output_dir = None
# -

# ## run the annotator

# %load_ext autoreload
# %autoreload 2

import sys
sys.path.append('../..')
from setcard_annotator.annotator import Annotator

annotator = Annotator(examples)
annotator.annotate()


