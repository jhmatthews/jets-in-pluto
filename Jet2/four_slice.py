# import visit_utils, we will use it to help encode our movie
import numpy as np 
import matplotlib.pyplot as plt
from scipy.interpolate import interp2d
import matplotlib.colors as colors
from pluto_jm import pyPLUTO as pp
#u = VN.vtk_to_numpy(data.GetCellData().GetArray('velocity'))
wdir = 'out_pluto/'
nlinf = pp.nlast_info(w_dir=wdir, datatype="float")
nn = nlinf["nlast"]
nn = 65
D = pp.pload(nn,w_dir=wdir, datatype="float") # Loading the data into a pload object D.
B = np.sqrt(D.Bx1**2 + D.Bx2**2 + D.Bx3**2)
plt.rcParams["text.usetex"] = "True"
xmax = 80
ymax = 200

cbar_pad = 0.07
cbar_fraction = 0.05
top = 0.97
left = 0.05
right = 0.95
bottom= 0.2
width = right-left
start = [left+i*(width/4.0)for i in range(4)]
delta = 0.03
cbar_width = (width / 4.0) - (2.0* delta)
total_aspect = 1.0
def total_aspect_ratio(aspect_per_fig, nx, ny, left = 0.1, right=0.95, top = 0.95, bottom = 0.2, wspace = 0, hspace = 0, colorbar_extras = 0):
	'''
	aspect_per_fig is y/x
	'''

	xfraction_per_fig = ((right - left) - ((nx - 1) * wspace)) / nx 
	yfraction_per_fig = ((top - bottom - colorbar_extras) - ((ny - 1) * hspace)) / ny
	
	total_ratio = (xfraction_per_fig * aspect_per_fig) / yfraction_per_fig

	return total_ratio

aspect = total_aspect_ratio(75/30.0, 4,1, left = left, right=right, top = top, bottom = bottom, wspace = 0, hspace = 0, colorbar_extras=0.0)
fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=True, figsize=(10,10*aspect))


plt.subplot(1,4,1)
im1 = plt.pcolormesh(-D.x1, D.x2, np.log10(D.rho.T), cmap="viridis")
plt.ylim(0,ymax )
plt.xlim(-xmax,0)
plt.gca().tick_params(direction="in")

#cbaxes = fig.add_axes([0.1, 0.8, 0.1, 0.8]) 
cax = fig.add_axes([left+delta, 0.12, cbar_width, 0.02]) 
cbar = plt.colorbar(cax = cax, orientation="horizontal", anchor=False, extend="both")
cbar.set_ticklabels(["${}$".format(i) for i in [-0.5,0,0.5]])
cbar.set_label(r"$\log(\rho)$", fontsize=12)


plt.subplot(1,4,2)
im1 = plt.pcolormesh(D.x1, D.x2, D.vx2.T, cmap="RdBu", vmin=-1, vmax=1)
plt.ylim(0,ymax)
plt.xlim(0,xmax)
#plt.gca().set_xticklabels([])
plt.gca().set_yticklabels([])
plt.gca().tick_params(direction="in")

cax = fig.add_axes([start[1]+delta, 0.12, cbar_width, 0.02]) 
cbar = plt.colorbar(cax = cax, orientation="horizontal", ticks=[-1,-0.5,0,0.5,1], panchor=False)
cbar.set_ticklabels(["${}$".format(i) for i in [-1,-0.5,0,0.5,1]])
cbar.set_label(r"$v_z/c$", fontsize=12)

velocity = np.sqrt(D.vx1**2 + D.vx2**2 + D.vx3**2)
B = np.sqrt(D.Bx1**2 + D.Bx2**2 + D.Bx3**2)
B_cgs = B * 8.232e-03
P_B = B_cgs*B_cgs / 8.0 / np.pi
P_tot = D.prs*5.393e-06 + P_B
Pram = D.rho * velocity * velocity * 5.393e-06

plt.subplot(1,4,3)
im1 = plt.pcolormesh(-D.x1, D.x2, D.Bx2.T, cmap="Spectral_r")
plt.ylim(0,ymax)
plt.xlim(-xmax,0)
#plt.gca().set_xticklabels([])
plt.gca().set_yticklabels([])
plt.gca().tick_params(direction="in")

# cbaxes = fig.add_axes([0.1, 0.8, 0.1, 0.8]) 
cax = fig.add_axes([start[2]+delta, 0.12, cbar_width, 0.02]) 
cbar = plt.colorbar(cax = cax, orientation="horizontal", panchor=False, extend="both")
cbar.set_ticklabels(["${}$".format(i) for i in [-0.5,0,0.5]])
cbar.set_label(r"$\log(B_y)$", fontsize=12)

plt.subplot(1,4,4)
im1 = plt.pcolormesh(D.x1, D.x2, B.T, cmap="plasma")
plt.ylim(0,ymax)
plt.xlim(0,xmax)
#plt.gca().set_xticklabels([])
plt.gca().set_yticklabels([])
plt.gca().tick_params(direction="in")

# cbaxes = fig.add_axes([0.1, 0.8, 0.1, 0.8]) 
cax = fig.add_axes([start[3]+delta, 0.12, cbar_width, 0.02]) 
cbar = plt.colorbar(cax = cax, orientation="horizontal", panchor=False, extend="both")
#cbar.set_ticklabels(["${}$".format(i) for i in [-0.5,0,0.5]])
cbar.set_label(r"$P_B$", fontsize=12)

plt.subplots_adjust(hspace=0.0, wspace=0.0, top=top, bottom=bottom, left=left, right=right)
plt.savefig("four_slice.png", dpi=300)

