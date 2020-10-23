# 2020-3D-Object-Detection

For some reason some of the packages didn't work when I put them in the yml file. So you have to download these packages in addition to creating the environment using the yml file.

Use pip install [package name]

- mayavi
- PyQt5

And if you want to demo in a jupyter notebook do this

instructions taken from https://github.com/kuixu/kitti_object_vis/tree/master/jupyter


install ipywidgets and ipyevents, enable them as notebook extensions

([conda_env_name])$ pip install ipywidgets ipyevents
([conda_env_name])$ jupyter nbextension enable --py --sys-prefix widgetsnbextension
([conda_env_name])$ jupyter nbextension enable --py --sys-prefix ipyevents

install and enable mayavi extension

([conda_env_name])$ jupyter nbextension install --py --sys-prefix mayavi
([conda_env_name])$ jupyter nbextension enable --py --sys-prefix mayavi

To test on Jupyter notebook, first set ETS_TOOLKIT

([conda_env_name])$ export ETS_TOOLKIT='null'

All this is assuming you have jupyter notebook already installed