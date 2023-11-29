# wetwin
__Collaborative digital twin modelling__

## Introduction

## Showing results on the web

The interactive notebooks in this wetwin package are based on [Solara](https://github.com/widgetti/solara). This has several advantages over using ipywidgets and ipyleaflet directly. The main one is that in addition to use in notebooks the pages can also be served efficiently in a direct way, using `solara run myapp.py`. The code between a notebook and the app can be identical except for one call at the end to start the app. Another advantage is the use of reactive variables, which are variables that can be linked to multiple widgets and each widget can change and use the variable. This makes it easy to have two panels showing data for the same time, for example. With callback functions, this would quickly become very complex.

## Solara

Solara is a python package for the development of interactive web-based interfaces. The package is compatible with the use of Jupyter notebooks, but you can also run a app using the solara server. The matter mode is much more efficient and can handle multiple users. In that case the app runs separately for each user, but with only one server. A simple example to see this in action is at (https://giswqs-solara.hf.space), which runs the app.py found here (https://huggingface.co/spaces/giswqs/solara/tree/main). There is also exellent documentation for Solara at (https://solara.dev/docs/quickstart)

## Connecting Wetwin frontend to Solara

In the past wetwin aimed to implement its own datatypes, that were similar to the reactive variables, but all of this code has now been removed and the examples make use of Solara only. There are a few new widgets and functions to support the development of visualization of geophysical data, like maps and time-series, but the added functionality is limited and the Solara documentation, together with the examples should give a good idea of the possibilities. 
## Examples

- `jupyter notebook wetwin_solara_widgets.ipynb` gives a brief overview of some widgets in a notebook.

## Getting started

The wetwin code makes use of several puython packages, that are need to be installed before you can run the examples successfully. You can do this manually or use conda or pip.

### Installing prerequisites with conda 

If you use anaconda or a variant of it, the we recommend to create a new environment. This makes sure that the new packages do not interfere with your other work. Here are the steps:

- `conda env create -f environment.yml` This will create a new environment called wetwin and installs the packages. This can take some time.
- `conda activate wetwin` This activates the wetwin environment. Your prompt should now contain (wetwin)
- `python -m ipykernel install --user --name=wetwin-kernel` Register a jupyter kernel with the wetwin environment. The name should also show up in vscode for example.

### Installing prerequisites with pip

Alternatively, the packages can be installed in a virtual environment with pip. We do not recommend to install packages in the main environment, especially on linux, since this poses a risk to the stability of your system. We also do not recommend to mix installation with conda and pip. Here are the steps:

- `python3 -m venv .venv` Create a new virtual python environment.
- `source .venv/bin/activate` Activate the new environment.
- `python3 -m pip install -r requirements.txt` Install the packages listed in the file requirements.txt
- `python -m ipykernel install --user --name=wetwin-kernel` Register a jupyter kernel with the wetwin environment. The name should also show up in vscode for example.


Note that when you use the command promps then you have to activate the enviroment at every new terminal session.