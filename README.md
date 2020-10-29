# 2020-3D-Object-Detection

For some reason some of the packages didn't work when I put them in the yml file. So you have to download these packages in addition to creating the environment using the yml file.

Use pip install [package name]

- mayavi
- PyQt5

## And if you want to demo in a jupyter notebook do this


### - install ipywidgets and ipyevents, enable them as notebook extensions

$ pip install ipywidgets ipyevents

$ jupyter nbextension enable --py widgetsnbextension

$ jupyter nbextension enable --py --sys-prefix ipyevents

### - install and enable mayavi extension

$ jupyter nbextension install --py mayavi --user

$ jupyter nbextension enable --py mayavi --user

### - To test on Jupyter notebook, first set ETS_TOOLKIT

$ export ETS_TOOLKIT='null'

**All this is assuming you have jupyter notebook already installed

instructions taken from https://github.com/kuixu/kitti_object_vis/tree/master/jupyter