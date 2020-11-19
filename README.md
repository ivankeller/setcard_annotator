# setcard_annotator
A simple tool for annotating Set cards images from a Jupyter notebook.

(inspired by https://github.com/agermanidis/pigeon and cleanly refactored ;)


![annotator screen cast](./assets/annotator.gif)
## Set the environment
From the root directory of this project do:
```bash
pipenv install
pipenv shell
```

## Run the tests 
```bash
python -m unittest discover -v
```

## Run the annotator notebook
```bash
jupyter notebook
```

1. In Jupyter notebook navigate to `setcard_annotator/notebooks` and start the `notebook_annotator` notebook:  
<img alt="jupyter" width="400" src="./assets/jupyter.png">

2. On the top **configuration** cell provide:
    - the path to the input directory containing PNG or JPG images to annotate, or a list of image paths
    - (optional) the path for saving the annotations

3. Run the cells and annotate using the buttons.   
Annotations are saved one by one as individual JSON files in the `labels` sub-directory.
Thus the process can be stopped at anytime to be resumed later: the annotation tool shows only the images that have not been previously annotated (based on the filename).


