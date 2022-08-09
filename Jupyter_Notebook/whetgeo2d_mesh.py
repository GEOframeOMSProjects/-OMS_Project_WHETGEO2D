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



def reconstruct_gmsh_mesh(filename):
    '''
    Read the .mesh file and return the coordinates of nodes and the 
    nodes of triangles
	
	:param filename: name of the file containing the grid.
	:type filename: string
	
	return:
	
	triangles: set of vertices for each face of the grid
	type triangles: numpy.ndarray
	
	nodes: coordinate (x,z) of each vertex of the grid
	type nodes: numpy.ndarray
	
	ID: label of the face used to match the set of parameters
	type ID: numpy.array
	
	x_c: x coordinate of the faces' centroid
	type x_c: numpy.array
	
	z_c: z coordinate of the faces' centroid
	type z_c: numpy.array
    
    author: Niccolò Tubini
    '''
    my_cols = ["0", "1", "2", "3", "4"]
    df = pd.read_csv(filename, names=my_cols, sep='\\s+')

    n_vertices = int(df["0"][df["0"][df["0"] == 'Vertices'].index[0]+1])
    n_edges = int(df["0"][df["0"][df["0"] == 'Edges'].index[0]+1])
    n_triangles = int(df["0"][df["0"][df["0"] == 'Triangles'].index[0]+1])

    # Nodes x coordinates
    xx = df['0'][5:5+n_vertices].values
    x = np.insert(xx,0,-999)

    # Nodes y coordinates 
    zz = df['1'][5:5+n_vertices].values
    z = np.insert(zz,0,-999)



    # Indeces of the nodes that make up a triangle. Note that nodes starts from 1 so it is necessary to add -999
    # in x and y array at index 0
    triangles = df.loc[4+n_vertices+n_edges+5: 4+n_vertices+n_edges+5+n_triangles-1,"0":"2"].values
    triangles = triangles.astype(np.int64)
    ID = df.loc[4+n_vertices+n_edges+5: 4+n_vertices+n_edges+5+n_triangles-1,"3"].values

    triang = tri.Triangulation(x, z,triangles)
    
    nodes = np.column_stack((x,z))
    
    x_c = np.zeros(np.shape(triangles)[0])
    z_c = np.zeros(np.shape(triangles)[0])
    for elem in range(0,np.shape(triangles)[0]):
        x_c[elem] = (float(nodes[[triangles[elem,0]],0])+float(nodes[[triangles[elem,1]],0])+float(nodes[[triangles[elem,2]],0]))/3
        z_c[elem] = (float(nodes[[triangles[elem,0]],1])+float(nodes[[triangles[elem,1]],1])+float(nodes[[triangles[elem,2]],1]))/3


    return [triangles, nodes, ID, x_c, z_c]



def show_domain(ax, nodes, elements, values, **kwargs):

    '''
	This function plots the physical domain.

	:param ax: An axes of the current figure.
	:type ax: matplotlib axes object
		
	:param nodes: Coordinates (x,z) of grid vertices.
	:type nodes: numpy.ndarray float		

	:param elements: Set of vertices defining each face (element) of the grid.
	:type elements: numpy.ndarray float	
	
	:param values: faces' label identifying different subdomains.
	:type values: numpy.array int	
	
	:Keyword Arguments
    * *param color_list* (list) list of colors (HEX) to create the colormap	
	* *param color_list* (list) list of names for each subdomain.
		
    @author: Niccolò Tubini	
	'''

    ## palette for soil layers
    color_list = ['#fed98e','#d95f0e','#ca6f1e','#784212','#ba4a00','#935116','#873600','#af601a','#935116','#ba4a00','#ca6f1e','#6e2c00']
    
    layer_list = ['layer 1','layer 2','layer 3','layer 4','layer 5','layer 6','layer 7','layer 8','layer 9','layer 10']

    color_list = kwargs.get('color_list', color_list)
    layer_list = kwargs.get('layer_list', layer_list)
   

    soil_cmap = matplotlib.colors.ListedColormap(color_list)
    
    unique_values = np.unique(values).astype(int)
    
    number_of_layers = len(unique_values)
    vmin = min(unique_values)
    vmax = max(unique_values)
    
    
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
    
    ax.set_aspect('equal')
    

    cmap = matplotlib.cm.get_cmap(soil_cmap)
    norm = matplotlib.colors.Normalize(vmin=vmin, vmax=vmax)

#     cmap(norm(cmap))
    
    pc = quatplot(y,z, np.asarray(elements), values, ax=ax, 
             edgecolor=None, cmap=cmap, norm=norm)
    
    
    patches = []
    norm = matplotlib.colors.Normalize(vmin=vmin, vmax=vmax)
    for i in unique_values:
        patches.append(mpatches.Patch(color=cmap(norm(i)), label=layer_list[i-1]))
    
    plt.legend(handles=patches, bbox_to_anchor=(0.65,1.1), ncol=2)
    
    plt.xlabel('$x$ [m]')
    plt.ylabel('$z$ [m]')
    

    plt.show()
    
    
def show_unstructured_grid(ax, nodes, elements):
    '''
	This function plots the grid elements.

	:param ax: An axes of the current figure.
	:type ax: matplotlib axes object
		
	:param nodes: Coordinates (x,z) of grid vertices.
	:type nodes: numpy.ndarray float		

	:param elements: Set of vertices defining each face (element) of the grid.
	:type elements: numpy.ndarray float	

    @author: Niccolò Tubini					
	'''

    triang = tri.Triangulation(nodes[:,0], nodes[:,1], elements)    
    ax.set_aspect('equal')
    ax.triplot(triang, lw=0.5, color='red')
    plt.xlabel("$x$ [m]")
    plt.ylabel("$z$ [m]")

    plt.show()
    
	
	
	
    
def create_structured_mesh(x_left, x_right, z_top, IMAX, KMAX, regions_xlim, regions_zlim, labels, bottom_bc_label, right_bc_label, left_bc_label, top_bc_label, file_name):
    '''
	This function allows the user to discretize the domain with a cartesian
	grid. It can be used whenever to computational domain has simple geometry
	both in terms of boundaries (square or rectangle) and subdomains.
	
	:param x_left: x coordinate of the left border.
	:type x_left: numpy.float
	
	:param x_right: x coordinate of the right border.
	:type x_right: numpy.float
	
	:param z_top: z coordinate of the top boundary defined with respect to the bottom
	:type z_top: numpy.float

	:param IMAX: number of cells in the x-direction
	:type IMAX: int
	
	:param KMAX: number of cells in the z-direction
	:type KMAX: int
	
	:param regions_xlim**: x coordinate limits of subdomains
	:type regions_xlim: numpy.ndarray (float)

	:param regions_zlim**: z coordinate limits of subdomains
	:type regions_zlim: numpy.ndarray (float)

	:param labels: labels of subdomains
	:type labels: numpy.ndarray (int)
	
	:param bottom_bc_label: bottom boundary condition label
	:type bottom_bc_label: numpy.int
	
	:param right_bc_label: right boundary condition label
	:type right_bc_label: numpy.int
	
	:param left_bc_label: left boundary condition label
	:type left_bc_label: numpy.int
	
	:param top_bc_label: top boundary condition label
	:type top_bc_label: numpy.int

	:param file_name: file name containing the grid
	:type file_name: string
	
	return:
	
	quad: set of vertices for each face of the grid
	type quad: numpy.ndarray
	
	nodes: coordinate (x,z) of each vertex of the grid
	type nodes: numpy.ndarray
	
	ID: label of the face used to match the set of parameters
	type ID: numpy.array
	
	x_c: x coordinate of the faces' centroid
	type x_c: numpy.array
	
	z_c: z coordinate of the faces' centroid
	type z_c: numpy.array
    
    author: Niccolò Tubini
    '''
    z_bottom = 0
    
    dx = (x_right-x_left)/IMAX
    x_c = np.zeros(IMAX)
    x_dual = np.zeros(IMAX+1)

    for i in range(0,IMAX+1,1):
        if (i==IMAX):
            x_dual[i] = x_left + dx*i
        else:
            x_c[i] = x_left + dx/2 + dx*i
            x_dual[i] = x_left + dx*i

    dz = (z_top-z_bottom)/KMAX
    z_c = np.zeros((KMAX,IMAX))
    z_dual = np.zeros((KMAX+1,IMAX))
    for k in range(0,KMAX+1,1):
        if k==KMAX:
            z_dual[k,:] = z_bottom + dz*k
        else:
            z_dual[k,:] = z_bottom + dz*k
            z_c[k,:] = z_bottom + dz/2 + dz*k
    
    
    
    n_vertices = (IMAX+1)*(KMAX+1) # numeber of vertices
    x_vertices = np.zeros(n_vertices) # x-coordinates of vertices
    z_vertices = np.zeros(n_vertices) # z-coordinates of vertices

    tmp_n = 0

    for k in range (0,KMAX+1):
        for i in range(0,IMAX+1,1):
            x_vertices[tmp_n] = x_left + dx*i
            z_vertices[tmp_n] = z_bottom + dz*k
            tmp_n = tmp_n+1
    
    
    n_elements = IMAX*KMAX # number of control volumes
    elements = np.zeros((n_elements,5), dtype=np.int) # vertices defining each control volume of the grid
    elements_centroid = np.zeros((n_elements,2)) # coordinates of the control volumes
    tmp_n = 0
    for k in range(0,KMAX):
        for i in range(0,IMAX):
            elements_centroid[tmp_n,0] = x_left + dx/2+i*dx
            elements_centroid[tmp_n,1] = z_bottom + dz/2+k*dz
            elements[tmp_n,0] = i+1 + (IMAX+1)*k
            elements[tmp_n,1] = i+2 + (IMAX+1)*k
            elements[tmp_n,3] = i+1 + (IMAX+1)*(k+1)
            elements[tmp_n,2] = i+2 + (IMAX+1)*(k+1)
            elements[tmp_n,4] = 0 # default value for element label. This label is used to associate soil parameters to each element

            tmp_n = tmp_n+1
            
            
            
    for r in range(0,len(regions_xlim)):
        for i in range(0,n_elements):
            if(elements_centroid[i,0]>=regions_xlim[r][0] and elements_centroid[i,0]<=regions_xlim[r][1] and
           elements_centroid[i,1]>=regions_zlim[r][0] and elements_centroid[i,1]<=regions_zlim[r][1]):
                elements[i,4] = labels[r]

                
                
    n_border_edges = IMAX*2 + KMAX*2 # number of edges that are on the boundary of the domain
    border_edges = np.zeros((n_border_edges,3),dtype=np.int) # boundary edges 
    tmp_n = 0
    #bottom
    for i in range(0,IMAX):
        border_edges[tmp_n,0] = i+1 
        border_edges[tmp_n,1] = i+2
        border_edges[tmp_n,2] = bottom_bc_label
        tmp_n = tmp_n+1
    #right
    for k in range(0,KMAX):
        border_edges[tmp_n,0] = IMAX+1 + (IMAX+1)*k 
        border_edges[tmp_n,1] = IMAX+1 + (IMAX+1)*(k+1)
        border_edges[tmp_n,2] = right_bc_label
        tmp_n = tmp_n+1
    #top
    for i in range(0,IMAX):
        border_edges[tmp_n,0] = n_vertices-i
        border_edges[tmp_n,1] = n_vertices-(i+1)
        border_edges[tmp_n,2] = top_bc_label
        tmp_n = tmp_n+1
    #left
    for k in range(0,KMAX):
        border_edges[tmp_n,0] = n_vertices-(IMAX) - (IMAX+1)*k
        border_edges[tmp_n,1] = n_vertices-(IMAX) - (IMAX+1)*(k+1)
        border_edges[tmp_n,2] = left_bc_label
        tmp_n = tmp_n+1
        
        
        
    with open(file_name, 'w') as file:
        file.write( str(n_vertices) + ',' + str(n_elements) + ',' + str(n_border_edges))
        file.write('\n')
        for i in range(0,n_vertices):
            file.write( str(x_vertices[i]) + ',' + str(z_vertices[i]) )
            file.write('\n')
        for i in range(0,n_elements):
            file.write( str(int(elements[i,0])) + ',' + str(int(elements[i,1])) + ',' + str(int(elements[i,2])) + ',' + str(int(elements[i,3])) + ',' + str(int(elements[i,4])) )
            file.write('\n')
        for i in range(0, n_border_edges):
            file.write( str(int(border_edges[i,0])) + ',' + str(int(border_edges[i,1])) + ',' + str(int(border_edges[i,2])) )
            file.write('\n')
            
            
            
def reconstruct_structured_csv(filename, IMAX, KMAX):
    '''
    Read the .csv file and return the coordinates of nodes and the 
    nodes of quadrangles for a cartesian grid.
	
	:param filename: name of the file containing the grid.
	:type filename: string
	
	return:
	
	quad: set of vertices for each face of the grid
	type quad: numpy.ndarray
	
	nodes: coordinate (x,z) of each vertex of the grid
	type nodes: numpy.ndarray
	
	ID: label of the face used to match the set of parameters
	type ID: numpy.array
	
	x_c: x coordinate of the faces' centroid
	type x_c: numpy.array
	
	z_c: z coordinate of the faces' centroid
	type z_c: numpy.array
    
    author: Niccolò Tubini
    '''
    my_cols = ["0", "1", "2", "3","4"]
    df = pd.read_csv(filename, names=my_cols, sep=',')

    # Nodes x coordinates
    tmp = df['0'][1:1+int(df['0'][0])].values
    x = np.insert(tmp,0,-999)

    # Nodes y coordinates 
    tmp = df['1'][1:1+int(df['0'][0])].values
    z = np.insert(tmp,0,-999)

    nodes = np.column_stack((x,z))
 
    # Indeces of the nodes that make up a quadrangle. Note that nodes starts from 1 so it is necessary to add -999
    # in x and y array at index 0
    quad = df.loc[1+int(df['0'][0]):int(df['0'][0])+int(df['1'][0]),"0":"5"].values
    quad = quad.astype(np.int64)
    ID = quad[:,4]
    
    x_c = np.zeros(IMAX*KMAX)
    z_c = np.zeros(IMAX*KMAX)

    nodes = np.column_stack((x,z))
    elem = quad[:,0:4].astype(np.int64)
    for elem in range(0,np.shape(quad)[0]):
        x_c[elem] = (nodes[quad[elem][0],0] + nodes[quad[elem][1],0] + nodes[quad[elem][2],0] + nodes[quad[elem][3],0])/4
        z_c[elem] = (nodes[quad[elem][0],1] + nodes[quad[elem][1],1] + nodes[quad[elem][2],1] + nodes[quad[elem][3],1])/4
    return [quad, nodes, x_c, z_c, ID]