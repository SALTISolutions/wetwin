# wetwin
__Collaborative digital twin modelling__

## Introduction

## Showing results on the web

The interactive notebooks will move to use Solara (https://github.com/widgetti/solara). This has several advantages over using ipywidgets and ipyleaflet with voila. The main one is that in addition to use in notebooks the pages can also be served efficiently in a direct way, using `solara run myapp.py`. The code between a notebook and the app can be identical except for one call at the end to start the app.

This change in course changes many things in this repository. It will take some time to adapt to the new approach and rewrite the existing examples.

## Solara

Solara is a python package for the development of interactive web-based interfaces. The package is compatible with the use of Jupyter notebooks, but you can also run a app using the solara server. The matter mode is much more efficient and can handle multiple users. In that case the app runs separately for each user, but with only one server. A simple example to see this in action is at (https://giswqs-solara.hf.space), which runs the app.py found here (https://huggingface.co/spaces/giswqs/solara/tree/main). There is also exellent documentation for Solara at (https://solara.dev/docs/quickstart)

## Connecting Wetwin frontend to Solara

The wetwin frontend will be down-scaled to a few common widgets for the geosciences and a number of demos for use in this context. These examples will be a little bit more elaborate, also showing for example how to connect to data over internet and displaying data.

## Examples

- __wetwin_solara_widgets.ipynb__ gives a brief overview of some widgets in a notebook. 

## Older readme part

In addition to making data available on the web you can also run juptyer notebooks on the web. In this way you can show your results in an interactive manner without the need for installation of python on the computer of the person to whom you want to show your work. A url is enough! There are several options for hosting jupyter notebooks (eg colab), but here we'll use binder as an example: 

- Play notebook without source using 'Voila':
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/robot144/wetwin/HEAD?labpath=wetwin_dcsm_maps.ipynb) 
- Play notebook showing the source code: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/robot144/wetwin/HEAD?urlpath=voila%2Frender%2Fwetwin_dcsm_maps.ipynb)

In addition to this demo, there are a few notebooks that illustrate the wetwin tools. They illustrate how you can use the tools. In order of increasing complexity:

- for wetwin widgets wetwin_widgets.ipynb [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/robot144/wetwin/HEAD?labpath=wetwin_widgets.ipynb)
- for ipyleaflet maps maps.ipynb [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/robot144/wetwin/HEAD?labpath=maps.ipynb)
- for xarray for access to zarr data over internet, zunormm_data.ipynb [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/robot144/wetwin/HEAD?labpath=zunormm_data.ipynb)
- for access to csv data over internet with pandas, data_timeseries.ipynb [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/robot144/wetwin/HEAD?labpath=data_timeseries.ipynb)


### Some technical notes

- Voila is a package that strips the code and editing functionality from a notebook and just shows the text and results. Together with ipywidgets you can make the page interactive and make the code respond to the buttons that you add.
- you can install voila also locally (with pip or conda) and run eg `voila wetwin_widgets.ipynb` to preview the app locally first.
- The standard netCDF4 library cannot read from a regular download, ie one that is not backed by opendap. Using Xarray, this can be done however. The advantage is that a regular web-url will be enough to access the netcdf file. 
- The pandas package can easily read from a url.
- Storage for the data on github is limited to 100Mb per file. Some other storage options for the academic commmunity in the Netherlands can be obtained  using research-drive from surfsara (https://researchdrive.surfsara.nl/index.php/login), which can be obtained together with an account on Snellius or Lisa, or surfdrive as available to all employees of the TU Delft (surfdrive.surf.nl). It is also possible to rent storage commercially (eg at hetzner storage share 3 to 5 euro/Tb/month). If you also want to control access to the data with keys, then S3 is a good solution. Amazon is the creator of S3, but it's difficult to make sense of their prices, scaleways has a more understandable offer. There are many options.


