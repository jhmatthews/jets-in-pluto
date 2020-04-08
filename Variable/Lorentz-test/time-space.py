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


times = np.zeros(nlast+1)
L = np.zeros_like(times)
vjet = np.zeros_like(times)
width = np.zeros_like(times)

plotsim = False
# numbers = np.arange()

pressure = np.zeros((nlast, 600))
density = np.zeros_like(pressure)
mach = np.zeros_like(pressure)
vx2 = np.zeros_like(pressure)

for j, i in enumerate(range(nstart,nlast,1)):
	D = pp.pload(i,w_dir=wdir, datatype="float") # Loading the data into a pload object D.

	pressure[i,:] = D.prs[0]
	density[i,:] = D.rho[0]
	cs = 5./3. * np.sqrt(D.prs[0]/D.rho[0]) 
	cs[(cs == 0) + np.isnan(cs)] = 1e-20
	mach_temp = D.vx2[0] / cs
	mach_temp[(mach_temp == 0)] = 1e-50
	mach[i,:] = mach_temp
	vx2[i,:]= D.vx2[0]


figure(figsize=(6,8))
times = np.arange(0,nlast,1) * 3.264e3 * OUT_DELTA
subplot(411)
pcolormesh(times/1e6, D.x2, np.log10(density.T), vmin=-3, vmax=0.5, cmap="viridis")
cbar = colorbar()
cbar.set_label(r"$\log \rho$")
ylabel ("z")

subplot(412)
pcolormesh(times/1e6, D.x2, np.log10(pressure.T), vmin=-6, vmax=-3, cmap="plasma")
cbar = colorbar()
cbar.set_label(r"$\log P$")
ylabel ("z")

subplot(413)
pcolormesh(times/1e6, D.x2, np.log10(mach.T), vmax = 1, vmin=-1, cmap="Spectral_r")
cbar = colorbar()
cbar.set_label("$M$")
ylabel ("z")
subplot(414)
pcolormesh(times/1e6, D.x2, vx2.T, vmin=0, vmax=1, cmap="Blues")
cbar = colorbar()
cbar.set_label("$v_z$")
xlabel("Time (Myr)", fontsize=14)
ylabel ("z")
subplots_adjust(hspace=0.05, bottom=0.1, top=0.98, right=0.96)
savefig("time_space.png", dpi=200)




	

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