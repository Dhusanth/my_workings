# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 10:24:18 2018

@author: dhusanth.thangavadiv
"""

%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
values = [12, 55, 4, 32, 14]
 
colors = ['r', 'g', 'b', 'c', 'm']
 
labels = ['India', 'United States', 'Russia', 'China', 'Europe']
 
values = [12, 55, 4, 32, 14]
 
 
ind = np.arange(len(values))  # the x locations for the groups
width = 0.35  # the width of the bars
 
fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, values, width, 
                color=colors)
 
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xticks(ind)
ax.set_xticklabels(labels)
ax.legend()
 
 
def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.
 
    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """
 
    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off
 
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')
 
 
autolabel(rects1, "center")
 
 
plt.show()