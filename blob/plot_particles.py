from pylab import *
#import pyPLUTO as pp # importing the pyPLUTO class.
from pluto_jm import pyPLUTO as pp
print (pp.__file__)

w_dir = "out_f1/"

f1 = plt.figure(figsize=[8,8])
ax = f1.add_subplot(111)
ns = 50


P = pp.ploadparticles(ns, datatype='flt', w_dir=w_dir) # Loading particle data.
PVmag = np.sqrt(P.vx1**2 + P.vx2**2 + P.vx3**2) # estimating the velocity magnitude
im1 = ax.scatter(P.x1, P.x2, s=10, c=PVmag, cmap=plt.get_cmap('hot''')) # scatter plot
cax1 = f1.add_axes([0.91,0.12,0.03,0.75])
plt.colorbar(im1,cax=cax1) # vertical colorbar for particle data.
D = pp.pload(ns, datatype='float', w_dir=w_dir)
im2 = ax.imshow(D.rho.T, origin='image',extent=[D.x1.min(), D.x1.max(), D.x2.min(), D.x2.max()]) # plotting fluid data.
cax2 = f1.add_axes([0.125,0.92,0.75,0.03])
plt.colorbar(im2,cax=cax2,orientation='horizontal') # vertical colorbar for fluid data.
ax.set_xlabel(r'X-axis',fontsize=18)
ax.set_ylabel(r'Y-axis',fontsize=18)
ax.minorticks_on()
plt.axis([0.0,1.0,0.0,1.0])
plt.show()