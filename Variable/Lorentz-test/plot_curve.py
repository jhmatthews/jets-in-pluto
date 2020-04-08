import os
import sys
from numpy import *
from matplotlib.pyplot import *
from pluto_jm import pyPLUTO as pp
from constants import *

# def figsize(aspect_ratio, top, bottom,left,right):
nstart = 1
if len(sys.argv) > 1:
	nstart = int(sys.argv[1])

OUT_DELTA = 50

wdir = 'out_var2/'
nlinf = pp.nlast_info(w_dir=wdir, datatype="float")

nlast = nlinf["nlast"]
#D = pp.pload(100,w_dir=wdir, datatype="float") # Loading the data into a pload object D.

t, flux = np.loadtxt("Lightcurve.dat", unpack=True)
t *= 1000.0
flux *= 1e43
ETA = 1e3

plot(t/1e6,flux)
semilogy()
show()



	

# print ([p for p in dir(D)])

# P_tot = D.prs*5.393e-06
# #subplot(121)
# I.pldisplay(D, D.prs,x1=D.x1,x2=D.x2,label1='x',label2='y',
#             title=r'Density $\rho$ [MHD jet]',cbar=(True,'vertical'),figsize=[7,12])

#I.pldisplay(D, D.prs,x1=D.x1,x2=D.x2,label1='x',label2='y',
#            title=r'Density $\rho$ [MHD jet]',cbar=(True,'vertical'),figsize=[7,12])


# I.pldisplay(D, D.Bx1,x1=D.x1,x2=D.x2,label1='x',label2='y',
#             title=r'Density $\rho$ [MHD jet]',cbar=(True,'vertical'),figsize=[7,12])

# Code to plot field lines. Requires 2 arrays xarr and yarr as
# # the starting point of integration i.e. x and y co-ordinate of the field point.
# I.myfieldlines(D,linspace(D.x1.min(),D.x1.max(),50),linspace(D.x2.max(),D.x2.max(),50),
#                colors='w',ls='-',lw=1.5)

#savefig('jet_final.png') # Only to be saved as either .png or .jpg

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