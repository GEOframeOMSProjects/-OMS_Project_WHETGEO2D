# -*- coding: utf-8 -*-
"""
    Created on 2 August 2022

/*
 * GNU GPL v3 License (by, nc, nd, sa)
 *
 * Copyright 2021 Niccolo` Tubini
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 */
 
@author: Niccolò Tubini, Enrico Borinato, Riccardo Rigon
"""

import os
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import matplotlib.collections
import matplotlib.colors as cl
import matplotlib.patches as mpatches
import matplotlib.dates as mdates
import matplotlib.ticker as mtick
import matplotlib.tri as tri


def plot_2D(ax, nodes, elements, values, **kwargs):
    ''' 
    Plot heat maps with unstructured grid.

    :param ax: An axes of the current figure.
    :type ax: matplotlib axes object

    :param nodes: Coordinates (x,z) of grid vertices.
    :type nodes: numpy.ndarray float		

    :param elements: Set of vertices defining each face (element) of the grid.
    :type elements: numpy.ndarray float	

    :param values: Values to plot.
    :type values: numpy.array float		

   :Keyword Arguments
        * *param color_list* (list) list of colors (HEX) to create the colormap	
        * *param colormap_desired_bins*	(np.int) number of bins for the colormap
        * *param colorbar* (boolean, default True) plot the colorbar
        * *param colorbar_name* (string) label of the colorbar

    @author: Niccolò Tubini
    '''
    ## palette 
    color_list = ['#f1eef6', '#bdc9e1', '#74a9cf', '#2b8cbe', '#045a8d']
    color_list = kwargs.get('color_list', color_list)
    
    ## colormap
    colormap_desired_bins = 10
    colormap_desired_bins = kwargs.get('colormap_desired_bins', colormap_desired_bins)
    
    ## colorbar
    colorbar = True
    colorbar = kwargs.get('colorbar', colorbar)
    
    colorbar_name = ''
    colorbar_name = kwargs.get('colorbar_name', colorbar_name)

    my_cmap = matplotlib.colors.LinearSegmentedColormap.from_list("",color_list, N=colormap_desired_bins)
    
    
    y = nodes[:,0]
    z = nodes[:,1]

    def quatplot(y,z, quatrangles, values, ax=None, **kwargs):

        if not ax: ax=plt.gca()
        yz = np.c_[y,z]
        verts= yz[quatrangles]
        pc = matplotlib.collections.PolyCollection(verts, **kwargs)
        pc.set_array(values)
        ax.add_collection(pc)
        ax.autoscale()
        return pc

#     fig, ax = plt.subplots(figsize=(12,12/1.618))
    
    vmin = min(values)
    vmax = max(values)
    
    ax.set_aspect('equal')
    ax.set_aspect('equal')

    cmap = matplotlib.cm.get_cmap(my_cmap)
    norm = matplotlib.colors.Normalize(vmin=vmin, vmax=vmax)

    pc = quatplot(y,z, np.asarray(elements), values, ax=ax, 
             edgecolor=None, cmap=cmap, norm=norm)

    sm = plt.cm.ScalarMappable(cmap=my_cmap, norm=plt.Normalize(vmin=vmin, vmax=vmax))
    cbar = plt.colorbar(sm, ax=ax)
    cbar.set_label(colorbar_name, rotation=0, labelpad=20)
    
    plt.xlabel('$x$ [m]')
    plt.ylabel('$z$ [m]')
    

#     plt.show()
    
#     return ax
    
    
    
def find_closest_element(target_x, target_z, x, z):
    ''' 
    Find the closest element to a user defined point (x,z)
    
    :param target_x: x coordinate of the target point
    :type target_x: np.float

    :param target_z: z coordinate of the target point
    :type target_z: np.float		

    :param x: x coordinate of the faces' centroid
    :type x: numpy.array float	

    :param z: z coordinate of the faces' centroid
    :type z: numpy.array float			

    return:
    idx: face index
    type idx: int

    @author: Niccolò Tubini
    '''	
    idx = (np.sqrt( (x - target_x)**2 + (z - target_z)**2  )).argmin()
    return idx
    