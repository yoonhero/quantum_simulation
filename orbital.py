import matplotlib.pyplot as plt
from matplotlib import cm, colors
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from IPython.display import set_matplotlib_formats
set_matplotlib_formats("retina")
import scipy.special as spe
import os
import glob
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 


def psi_R(r, n=1, l=0):
    coeff = np.sqrt((2.0/n)**3 * spe.factorial(n-l-1) / (2.0*n*spe.factorial(n+l)))

    laguerre = spe.assoc_laguerre(2.0*r/n, n-l-1, 2*l+1)

    return coeff * np.exp(-r/n) * (2.0*r/n)**l * laguerre

def psi_ang(phi, theta, l=0, m=0):
    sphHarm = spe.sph_harm(m, l, phi, theta)

    return sphHarm.real

def make_orbital(n, l, m):
    phi, theta = np.linspace(0, np.pi, 100), np.linspace(0, 2*np.pi, 100)

    phi, theta = np.meshgrid(phi, theta)

    Ylm = psi_ang(theta, phi, l=l, m=m)

    x = np.sin(phi) * np.cos(theta) * abs(Ylm)
    y = np.sin(phi) * np.sin(theta) * abs(Ylm)
    z = np.cos(phi) * abs(Ylm)

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection="3d")

    fcolors = (Ylm - Ylm.min()) / (Ylm.max() - Ylm.min())

    ax.plot_surface(x, y, z, facecolors=cm.seismic(fcolors), alpha=0.3)

    cset = ax.contour(x, y, z, 20, zdir="z", offset=-1, cmap="summer")
    cset = ax.contour(x, y, z, 20, zdir="y", offset=1, cmap="winter")
    cset = ax.contour(x, y, z, 20, zdir="x", offset=-1, cmap="autumn")

    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_ylim(-1, 1)

    filepath = f"./orbital/orbital_l{l}_m{m}.png"
    fig.savefig(filepath)

    return filepath
    

if __name__ == "__main__": 

    if not os.path.exists("./orbital"):
        os.makedirs("./orbital")

    data = [
        (1, 0, 0),
        (2, 1, 0),
        (2, 1, 1),
        (3, 2, 0),
        (3, 2, 1),
        (3, 2, 2)
    ]

    orbital_images = []
    for _, (n, l, m) in enumerate(data):
        src = make_orbital(n, l, m)
        orbital_images.append(src)

    # orbital_images = glob.glob("./orbital/*")

    pil_images = []

    for im in orbital_images:
        temp_img = Image.open(im)
        ## Text Description
        pil_images.append(temp_img)
    
    pil_images[0].save('orbital.gif', save_all=True, append_images=pil_images[1:], duration=1000, loop=0)
    