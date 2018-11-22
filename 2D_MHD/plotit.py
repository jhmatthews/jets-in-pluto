import os
import sys
from numpy import *
from matplotlib.pyplot import *
import pyPLUTO as pp

wdir = 'out_f1/'
nlinf = pp.nlast_info(w_dir=wdir, datatype="float")

D = pp.pload(nlinf['nlast'],w_dir=wdir, datatype="float") # Loading the data into a pload object D.
I = pp.Image()

print ([p for p in dir(D)])
I.pldisplay(D, D.Bx3,x1=D.x1,x2=D.x2,label1='x',label2='y',
            title=r'Density $\rho$ [MHD jet]',cbar=(True,'vertical'),figsize=[7,12])

# Code to plot field lines. Requires 2 arrays xarr and yarr as
# the starting point of integration i.e. x and y co-ordinate of the field point.
#I.myfieldlines(D,linspace(D.x1.min(),D.x1.max(),10),linspace(D.x2.min(),D.x2.min(),10),
               # colors='w',ls='-',lw=1.5)

savefig('jet_final.png') # Only to be saved as either .png or .jpg
show()