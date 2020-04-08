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
#nlast = 300
#D = pp.pload(100,w_dir=wdir, datatype="float") # Loading the data into a pload object D.

# t, flux = np.loadtxt("Lightcurve.dat", unpack=True)
# t *= 1000.0
# flux *= 1e43
# ETA = 1e3


times = np.zeros(nlast+1)
L = np.zeros_like(times)
vjet = np.zeros_like(times)
width = np.zeros_like(times)
volume = np.zeros_like(times)

plotsim = True
plotsim=False
# numbers = np.arange()

for j, i in enumerate(range(nstart,nlast,1)):
	D = pp.pload(i,w_dir=wdir, datatype="float") # Loading the data into a pload object D.


	if plotsim:

		fig3 = figure(figsize=(8,12))
		#gs = fig3.add_gridspec(4, 2)
		#subplot(1,2,1)
		gamma = np.sqrt(1.0 / (1 - D.vx2**2))
		# pcolormesh(-D.x1, D.x2, gamma.T, cmap="Spectral_r", vmin=1, vmax=4)
		pcolormesh(-D.x1, D.x2, D.vx2.T, cmap="Spectral_r", vmin=0.5, vmax=1)
		text(-20,80,r"$\Gamma$", color="w", fontsize=18)
		#colorbar(orientation="horizontal")

		#subplot(gs[1:,:])
		pcolormesh(D.x1, D.x2,np.log10(D.rho.T), cmap="viridis", vmin=-3, vmax=0.5)
		#title("Log Density")
		text(20,80,r"$\log \rho$", color="w", fontsize=18)
		#colorbar(orientation="horizontal")

		# subplots_adjust(hspace=0.2, wspace=0.2,bottom=0.05)

		# subplot(1,2,2)
		# iarg = np.argmin(np.fabs((t)-(i * 3.264e3 * OUT_DELTA)))
		# plot(t[:iarg], flux[:iarg], lw=3)
		# xlabel("t (Myr)", fontsize=18)
		# ylabel("Q (erg/s)", fontsize=18)
		# semilogy()
		xlim(-40,40)
		ylim(0,160)

		savefig("jet{:03d}.png".format(i, dpi=100))
		#savefig("jet{:03d}.jpg".format(i, dpi=100))
		clf()
		close("all")

		#scatter(D.vx2, D.tr1)
		#savefig("scatter{:03d}.png".format(i, dpi=100))

	U_e = D.prs * 0.3
	#lum[j] = 
	L[j] = np.max(D.x2[(D.tr1[0] > 0)])
	width[j] = np.max(D.x1[(D.tr1.T[0] > 0)])
	times[j] = i * 3.264e3 * OUT_DELTA
	vjet[j] = np.max(D.vx2)

	sizes = np.zeros_like(D.tr1)
	sizes.T[:,] = D.x1
	volume[j] = np.sum(2.0 * np.pi * sizes * D.dx1[0] * D.dx2[0] * D.tr1)


GAMMA = 3.2
ETA_BASE = 1e-4 * GAMMA * GAMMA
ETA_BASE = 1e-4
RADIUS = 4.2

# get power-law atmosphere
r = L
r_c = 50.0
beta = 0.5
exponent = -3.0 * beta / 2.0
rho = 1.0 + np.power(r/r_c, 2.0)
rho = np.power(rho, exponent)
rho = 1.0

eta = (ETA_BASE) / rho
# power = flux 
# rho = (1.0/ETA) * 6e-27
# area = (1.0 * 1000.0 * PARSEC)**2 * PI
# vcubed = power / rho / area 
# vjet2 = vcubed ** (1./3.)
epsilon = 0.7
advance = epsilon * np.sqrt(eta) / (1+np.sqrt(eta))* vjet

epsilon = 4.0
Q = GAMMA * (GAMMA - 1) / vjet 

##sizes.T[:,] = D.x1
# now do a version with the post-shock pressure 
#advance2 = np.sqrt(GAMMA**2 * eta * vjet * vjet)
#volume = np.sum(2.0 * np.pi * sizes * D.dx1[0] * D.dx2[0] * D.tr1)
A_j = np.pi * (RADIUS) ** 2
A_c = volume / 4 / L
#Q *= A_j
#print (A_c, A_j)

advance2 = np.sqrt(GAMMA * (GAMMA - 1) * eta * (A_j / A_c))
advance2 = GAMMA * np.sqrt(eta) / ((A_j / A_c) + np.sqrt(eta) * GAMMA)


t_eng,l_eng = np.loadtxt("english.dat", unpack=True)
#ee = 3.0 * D.prs / D.rho
#h = 1 + ee + (D.prs / D.rho)
#LL = eta * h 
print (advance2, A_j/A_c)
#advance = 

Lnew = np.zeros_like(times)
Lnew2 = np.zeros_like(times)
for i in range(1,len(times)-1):
	Lnew[i] = Lnew[i-1] + ((times[i] - times[i-1]) * YR * advance[i] * C) / 1000.0 / PARSEC
	Lnew2[i] = Lnew2[i-1] + ((times[i] - times[i-1]) * YR * advance2[i] * C) / 1000.0 / PARSEC

figure(figsize=(7,5))
subplot(211)
#power, v_j, g_time, time_physical = np.loadtxt("vel.dat", unpack=True, usecols=(1,2,3,4))
#plot(time_physical/YR/1e6, v_j)
#semilogy()
#xlim(0,5)
#ylim(0,1)
plot(times, A_c)
#plot(times, A_j)
plot(times[:nlast-1] / 1e6, L[:nlast-1],  label="Sim") 
plot(times / 1e6, Lnew, label="Predicted 1") 
plot(times / 1e6, Lnew2, label="Predicted 2") 
plot(t_eng,l_eng, label="English") 
ylabel("Jet Length (kpc)")
legend()
#xlabel ("Time (Myr)")
#semilogy()
xlim(0,100)
ylim(0,100)

subplot(212)
plot(times/1e6, vjet, alpha=0.7, lw=3, label="Input v")
#plot(t/1e6, vjet2/C, label="Measured v", lw=1)
#plot(times/1e6, advance, label="Advance speed predict 1")
plot(times/1e6, advance2, label="Advance speed predict 2")

plot(times/1e6,np.gradient(L*1000.0*PARSEC, times*YR)/C, label="Advance speed sim")
#plot(time_physical/YR/1e6, v_j)
xlabel ("Time (Myr)")
legend()

semilogy()
xlim(0,100)
# ylim(0.9,1)
ylim(1e-4,10)

savefig("advance.png")




# D = pp.pload(100,w_dir=wdir, datatype="float") # Loading the data into a pload object D.
# gamma = np.sqrt(1.0 / (1 - D.vx2**2))

# dens = D.rho * gamma 
# ee = 3.0 * D.prs / D.rho 
# h = 1 + ee + (D.prs / D.rho)

# E = D.rho * h * gamma * gamma - D.prs 
# m = D.rho * h * gamma * gamma * D.vx2


# enthalpy = 4.0 * D.prs + (D.rho)
# rhov2 = D.rho * D.vx2 * D.vx2
# momentum = (enthalpy * gamma * gamma * D.vx2 * D.vx2) + D.prs
# momentum = gamma * gamma * rhov2 + D.prs

# #energy = gamma * (gamma - 1) * D.rho * D.vx2 * 1.0 * 1.0 + (4.0 * D.prs)
# plot(D.x2,E[0]) 
# plot(D.x2,m[0])
# plot(D.x2,dens[0])
# plot(D.x2,D.tr1[0])
# plot(D.x2,gamma[0])
# semilogy()
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