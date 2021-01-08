# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
# from IPython.display import set_matplotlib_formats

# Plotting setup
# set_matplotlib_formats("pdf", "svg")
plt.rcParams["text.usetex"] = False
plt.rcParams["text.latex.preamble"] = r"\usepackage{amsfonts} \usepackage{amsmath}"


import torch
import torch.nn as nn
import torch.nn.functional as F



colors = ['#EE6352', '#59CD90','#3FA7D6','#FAC05E','#F79D84']


fig, axes = plt.subplots(nrows=1,ncols=3,figsize=(16,10))


xs = np.arange(0,10, .1)


# generative process in real world
# a, b = 1, 10
# y = np.sin(a * x) + np.sin(b * x)


# for i in range(5):
h0 = np.random.normal(0,1)
h1 = np.random.normal(5,1)

y = np.sin(xs * h0) + np.sin(xs * h1)


axes[0].plot(xs, np.sin(xs * h0), linestyle=(0,(1,1)), color = colors[1])
axes[1].plot(xs, np.sin(xs * h1), linestyle=(0,(1,1)), color = colors[2])
axes[2].plot(xs, y, linestyle=(0,(1,1)), color = colors[0])

plt.show()
