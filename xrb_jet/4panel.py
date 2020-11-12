import os
import sys
import numpy as np 
import matplotlib.pyplot as plt
from pluto_jm import pyPLUTO as pp

wdir = 'out_xrb/'
nlinf = pp.nlast_info(w_dir=wdir, datatype="float")
#nlast = 100
nlast = nlinf["nlast"]

nrange = np.arange(0,nlast,1.0)
weighted = np.zeros_like(nrange)
Psum = np.zeros_like(nrange)
Psum_tr = np.zeros_like(nrange)

cmaps = ["Spectral", "afmhot", "viridis", "plasma"]

def plot_blob(D, variable, P, PVmag, cmap, my_title, subplot_id, vminmax, particles=True):
	plt.subplot(subplot_id)
	plt.title(my_title)
	plt.pcolormesh(D.x1, D.x2, variable, vmin=vminmax[0], vmax=vminmax[1], cmap=cmap)
	plt.pcolormesh(-D.x1, D.x2, variable, vmin=vminmax[0], vmax=vminmax[1], cmap=cmap)
	#plt.colorbar()
	if particles:
		plt.scatter(P.x1, P.x2, s=10, c=PVmag, cmap=plt.get_cmap('hot'), vmin=0, vmax=0.5) 
		plt.scatter(-P.x1, P.x2, s=10, c=PVmag, cmap=plt.get_cmap('hot'), vmin=0, vmax=0.5)  
	plt.xlim(-20,20)
	plt.ylim(0,20)
	return (plt.gca())

def make_4_plot(D, lorentz, cmaps, P, PVmag, nn, particles=True, iplot=0, grid=(2,4)):
	
	#plot_blob(D, np.log10(lorentz), P, PVmag, cmaps[3], "Bulk Lorentz", "{}{}{}".format(grid[0], grid[1], 4+iplot+1), (-1,0.5), particles=particles)
	ax1 = plot_blob(D, D.tr1.T, P, PVmag, cmaps[1], "Tracer", "{}{}{}".format(grid[0], grid[1], iplot+1), (0,1), particles=particles)
	#plot_blob(D, D.rho.T, P, PVmag, cmaps[2], "Density", "24{}".format(4+iplot+1), (0,10), particles=particles)
	#plot_blob(D, np.log10(D.prs.T**1.8), P, PVmag, cmaps[0], "Pressure", "24{}".format(4+iplot+1), (-2,2), particles=particles)
	ax2 = plot_blob(D, D.vx2.T, P, PVmag, cmaps[0], "$v_y$", "{}{}{}".format(grid[0], grid[1], 4+iplot+1), (-0.5,0.5), particles=particles)

	ax1.set_xticklabels([])
	if iplot != 0:
		ax1.set_yticklabels([])
		ax2.set_yticklabels([])

	if particles:
		savename = 'particles-blob_{:03d}.png'.format(int(nn))
	else:
		savename = 'blob_{:03d}.png'.format(int(nn))





plot_colors = True
# plot_colors = False
#plt.figure(figsize=(7.5,6))
from jm_util import *
set_plot_defaults()
plt.figure(figsize=(10,6))

n_to_plot = np.linspace(0,nlast,4)
for i, nn in enumerate(n_to_plot):
	#nn = nlinf["nlast"]


	D = pp.pload(int(nn),w_dir=wdir, datatype="float") # Loading the data into a pload object D.
	#D = pp.pload(100,w_dir=wdir, datatype="float") # Loading the data into a pload object D.
	I = pp.Image()
	P = D
	time = nn * 1.0 * 1.000e+02
	print (time)

	# load particles 
	#P = pp.ploadparticles(int(nn), datatype='flt', w_dir=wdir) # Loading particle data.
	#PVmag = np.sqrt(P.vx1**2 + P.vx2**2 + P.vx3**2) # estimating the velocity magnitude
	P = None
	PVmag = None
	print ([p for p in dir(D)])

	#B = sqrt(D.Bx1**2 + D.Bx2**2 + D.Bx3**2)
	#B_cgs = B * 8.232e-03
	#P_B = B_cgs*B_cgs / 8.0 / pi
	#P_tot = D.prs*5.393e-06
	#I.pldisplay(D, D.vx2,x1=D.x1,x2=D.x2,label1='x',label2='y',
	#            title=r'Density $\rho$ [MHD jet]',cbar=(True,'vertical'),figsize=[7,12])
	lorentz = 1.0 / np.sqrt(1.0 - D.vx2.T**2)

	if plot_colors:
		#make_4_plot(D, lorentz, cmaps, P, PVmag, nn, particles=True)
		make_4_plot(D, lorentz, cmaps, P, PVmag, nn, particles=False, iplot=i)

		weighted[i] = np.mean(lorentz[D.tr1.T>0.1])

	select = (D.vx2 > 1e-15) 
	Psum[i] = np.sum(D.prs[select])
	select = (D.vx2 > 1e-15) * (D.tr1 > 0.01)
	Psum_tr[i] = np.sum(D.prs[select])

plt.subplots_adjust(hspace=0.05,wspace=0.1, top=0.98)
plt.savefig("4panel.png") # Only to be saved as either .png or .jpg
# plt.clf()
# plt.close("all")

# plt.plot(nrange * 3.264 * 0.01, Psum)
# plt.plot(nrange * 3.264 * 0.01, Psum_tr)
# plt.semilogy()
# plt.show()
# plot(nrange * 3.264 * 0.01, weighted)
# show()
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