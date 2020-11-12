import os
import sys
import numpy as np 
import matplotlib.pyplot as plt
from pluto_jm import pyPLUTO as pp

fname_glob = sys.argv[1]
wdir = "out_" + fname_glob + "/"
nlinf = pp.nlast_info(w_dir=wdir, datatype="float")
#nlast = 100
nlast = nlinf["nlast"]

nstart = 0
if len(sys.argv) > 2:
	nstart = int(sys.argv[2])

nrange = np.arange(nstart,nlast,1.0)
weighted = np.zeros_like(nrange)
Psum = np.zeros_like(nrange)
Psum_tr = np.zeros_like(nrange)

cmaps = ["Spectral", "afmhot", "viridis", "plasma"]

def plot_blob(D, variable, P, PVmag, cmap, my_title, subplot_id, vminmax, particles=True):
	plt.subplot(subplot_id)
	plt.title(my_title)
	plt.pcolormesh(D.x1, D.x2, variable, vmin=vminmax[0], vmax=vminmax[1], cmap=cmap)
	plt.pcolormesh(-D.x1, D.x2, variable, vmin=vminmax[0], vmax=vminmax[1], cmap=cmap)
	plt.colorbar()
	if particles:
		plt.scatter(P.x1, P.x2, s=10, c=PVmag, cmap=plt.get_cmap('hot'), vmin=0, vmax=0.5) 
		plt.scatter(-P.x1, P.x2, s=10, c=PVmag, cmap=plt.get_cmap('hot'), vmin=0, vmax=0.5)  
	plt.xlim(-20,20)
	plt.ylim(0,80)

def make_4_plot(D, lorentz, cmaps, P, PVmag, nn, particles=True, time=None):
	plt.figure(figsize=(7.5,12))
	plot_blob(D, lorentz, P, PVmag, cmaps[3], "Bulk Lorentz", 221, (1,3), particles=particles)
	plot_blob(D, D.tr1.T, P, PVmag, cmaps[1], "Blob Tracer", 222, (0,1), particles=particles)
	plot_blob(D, D.rho.T, P, PVmag, cmaps[2], "Density", 223, (0,10), particles=particles)
	plot_blob(D, D.prs.T, P, PVmag, cmaps[0], "Pressure", 224, (0,1.5), particles=particles)
	if particles:
		savename = 'particles-blob_{:03d}.png'.format(int(nn))
	else:
		savename = '{}/{}_{:03d}.png'.format(wdir,fname_glob, int(nn))

	plt.suptitle("{} secs".format(time))
	plt.savefig(savename) # Only to be saved as either .png or .jpg
	plt.clf()
	plt.close("all")



plot_colors = True
# plot_colors = False

for i, nn in enumerate(nrange):
	#nn = nlinf["nlast"]

	D = pp.pload(int(nn),w_dir=wdir, datatype="float") # Loading the data into a pload object D.
	#D = pp.pload(100,w_dir=wdir, datatype="float") # Loading the data into a pload object D.
	I = pp.Image()

	# load particles 
	#P = pp.ploadparticles(int(nn), datatype='flt', w_dir=wdir) # Loading particle data.
	#PVmag = np.sqrt(P.vx1**2 + P.vx2**2 + P.vx3**2) # estimating the velocity magnitude

	P = None
	PVmag = None
	print ([p for p in dir(D)])

	time = nn * 1.0 * 1.000e+02
	print (time)
	print (20.0 * 100.0 * 3e10)


	#B = sqrt(D.Bx1**2 + D.Bx2**2 + D.Bx3**2)
	#B_cgs = B * 8.232e-03
	#P_B = B_cgs*B_cgs / 8.0 / pi
	#P_tot = D.prs*5.393e-06
	#I.pldisplay(D, D.vx2,x1=D.x1,x2=D.x2,label1='x',label2='y',
	#            title=r'Density $\rho$ [MHD jet]',cbar=(True,'vertical'),figsize=[7,12])
	lorentz = 1.0 / np.sqrt(1.0 - D.vx2.T**2)

	if plot_colors:
		#make_4_plot(D, lorentz, cmaps, P, PVmag, nn, particles=True)
		make_4_plot(D, lorentz, cmaps, P, PVmag, nn, particles=False, time=time)

		weighted[i] = np.mean(lorentz[D.tr1.T>0.1])

	select = (D.vx2 > 1e-15) 
	Psum[i] = np.sum(D.prs[select])
	select = (D.vx2 > 1e-15) * (D.tr1 > 0.01)
	Psum_tr[i] = np.sum(D.prs[select])

plt.plot(nrange * 3.264 * 0.01, Psum)
plt.plot(nrange * 3.264 * 0.01, Psum_tr)
plt.semilogy()
plt.show()
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