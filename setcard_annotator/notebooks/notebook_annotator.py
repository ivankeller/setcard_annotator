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
examples = [
    '../../../data_for_tests/examples_for_annotator/IMG_20170518_204728_0.png', 
    '../../../data_for_tests/examples_for_annotator/IMG_20170518_205001_7.png',
]
#examples = '../../../data_for_tests/examples_for_annotator'

# output directory for annotation saved as json files
# If None annotations are saved in default `labels` sub-directory 
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


