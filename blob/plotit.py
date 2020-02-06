import os
import sys
from numpy import *
from matplotlib.pyplot import *
from pluto_jm import pyPLUTO as pp

wdir = 'out_f1/'
nlinf = pp.nlast_info(w_dir=wdir, datatype="float")

nrange = np.arange(0,700,1.0)
weighted = np.zeros_like(nrange)

cmaps = ["Spectral", "afmhot", "viridis", "plasma"]

for i, nn in enumerate(nrange):
	#nn = nlinf["nlast"]

	D = pp.pload(int(nn),w_dir=wdir, datatype="float") # Loading the data into a pload object D.
	#D = pp.pload(100,w_dir=wdir, datatype="float") # Loading the data into a pload object D.
	I = pp.Image()

	print ([p for p in dir(D)])

	#B = sqrt(D.Bx1**2 + D.Bx2**2 + D.Bx3**2)
	#B_cgs = B * 8.232e-03
	#P_B = B_cgs*B_cgs / 8.0 / pi
	#P_tot = D.prs*5.393e-06
	#I.pldisplay(D, D.vx2,x1=D.x1,x2=D.x2,label1='x',label2='y',
	#            title=r'Density $\rho$ [MHD jet]',cbar=(True,'vertical'),figsize=[7,12])
	lorentz = 1.0 / sqrt(1.0 - D.vx2.T**2)
	figure(figsize=(6,10))

	subplot(2,2,1)
	title("Bulk Lorentz")
	pcolormesh(D.x1, D.x2, lorentz,vmin=1, vmax=3, cmap=cmaps[3])
	pcolormesh(-D.x1, D.x2, lorentz,vmin=1, vmax=3, cmap=cmaps[3])
	colorbar()

	subplot(2,2,2)
	title("Blob Tracer")
	pcolormesh(D.x1, D.x2, D.tr1.T,vmin=0, vmax=1, cmap=cmaps[1])
	pcolormesh(-D.x1, D.x2, D.tr1.T,vmin=0, vmax=1, cmap=cmaps[1])
	colorbar()

	subplot(2,2,3)
	title("Density")
	pcolormesh(D.x1, D.x2, D.rho.T, vmin=0, vmax=10, cmap=cmaps[2])
	pcolormesh(-D.x1, D.x2, D.rho.T,vmin=0, vmax=10,  cmap=cmaps[2])
	colorbar()

	subplot(2,2,4)
	title("Pressure")
	pcolormesh(D.x1, D.x2, D.prs.T, vmin=0, vmax=1.5, cmap=cmaps[3])
	pcolormesh(-D.x1, D.x2, D.prs.T, vmin=0, vmax=1.5, cmap=cmaps[3])
	colorbar()

	weighted[i] = np.mean(lorentz[D.tr1.T>0.1])
	#i+=1


	# I.pldisplay(D, D.Bx1,x1=D.x1,x2=D.x2,label1='x',label2='y',
	#             title=r'Density $\rho$ [MHD jet]',cbar=(True,'vertical'),figsize=[7,12])

	# Code to plot field lines. Requires 2 arrays xarr and yarr as
	# # the starting point of integration i.e. x and y co-ordinate of the field point.
	# I.myfieldlines(D,linspace(D.x1.min(),D.x1.max(),20),linspace(D.x2.min(),D.x2.min(),20),
	#                colors='w',ls='-',lw=1.5)

	savefig('blob_{:03d}.png'.format(int(nn))) # Only to be saved as either .png or .jpg
	clf()

plot(nrange * 3.264 * 0.01, weighted)
show()
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