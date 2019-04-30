import os
import sys
from numpy import *
from matplotlib.pyplot import *
from pluto_jm import pyPLUTO as pp

wdir = 'out_pluto/'
nlinf = pp.nlast_info(w_dir=wdir, datatype="float")

D = pp.pload(60,w_dir=wdir, datatype="float") # Loading the data into a pload object D.
#D = pp.pload(100,w_dir=wdir, datatype="float") # Loading the data into a pload object D.
I = pp.Image()

print ([p for p in dir(D)])

B = sqrt(D.Bx1**2 + D.Bx2**2 + D.Bx3**2)
B_cgs = B * 8.232e-03
P_B = B_cgs*B_cgs / 8.0 / pi
P_tot = D.prs*5.393e-06
I.pldisplay(D, B,x1=D.x1,x2=D.x2,label1='x',label2='y',
            title=r'Density $\rho$ [MHD jet]',cbar=(True,'vertical'),figsize=[7,12])



# I.pldisplay(D, D.Bx1,x1=D.x1,x2=D.x2,label1='x',label2='y',
#             title=r'Density $\rho$ [MHD jet]',cbar=(True,'vertical'),figsize=[7,12])

# Code to plot field lines. Requires 2 arrays xarr and yarr as
# the starting point of integration i.e. x and y co-ordinate of the field point.
I.myfieldlines(D,linspace(D.x1.min(),D.x1.max(),50),linspace(D.x2.max(),D.x2.max(),50),
               colors='w',ls='-',lw=1.5)

savefig('jet_final.png') # Only to be saved as either .png or .jpg

# plt.clf()
# I.pldisplay(D, np.log10(D.vx2),x1=D.x1,x2=D.x2,label1='x',label2='y',
#             title=r'Density $\rho$ [MHD jet]',cbar=(True,'vertical'),figsize=[7,12])

# #I.pldisplay(D, D.Bx1,x1=D.x1,x2=D.x2,label1='x',label2='y',
# #            title=r'Density $\rho$ [MHD jet]',cbar=(True,'vertical'),figsize=[7,12])

# # Code to plot field lines. Requires 2 arrays xarr and yarr as
# # the starting point of integration i.e. x and y co-ordinate of the field point.
# #I.myfieldlines(D,linspace(D.x1.min(),D.x1.max(),50),linspace(D.x2.min(),D.x2.min(),50),
#  #               colors='w',ls='-',lw=1.5)
# savefig('jet_vx2_final.png') # Only to be saved as either .png or .jpg

# show()