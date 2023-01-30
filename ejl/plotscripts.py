import numpy as np
import matplotlib.pyplot as plt
from . import plottools as ept


def plot_frame(frame, ax=None, cax=None, output_fname=None, vmin=None, vmax=None, xticks=None, yticks=None, cmap='jet', label="$Counts$"):
    
    if ax is None:
        ax = plt.gca()
    if vmin is None:
        vmin = 0
    if vmax is None:
        vmax = np.max(np.abs(frame))

    images = ax.get_images()  
    if len(images) != 1:
        fig = ax.figure

        plt.sca(ax)
        plt.cla()
        
        shape = np.shape(frame)
        x = np.arange(shape[1] + 1)
        y = np.arange(shape[0] + 1)

        plt.imshow(frame, extent=[x[0], x[-1], y[0], y[-1]], vmin=vmin, vmax=vmax, cmap=cmap, origin='lower', interpolation='None')
        #plt.pcolormesh(x, y, frame, vmin=vmin, vmax=vmax, cmap=cmap, rasterized=True)
    
        dx = shape[1]/4
        dy = shape[0]/4
        
        if xticks is None:
            plt.xticks(dx*np.arange(5))
        if xticks is None:
            plt.yticks(dy*np.arange(5))
        
        ax.invert_yaxis()
        plt.xlim(x[0], x[-1])
        plt.ylim(y[-1], y[0])
    else:
        images[0].set_data(frame)
        images[0].set(clim=(vmin, vmax), cmap=cmap)
        

    if cax is not None:
        ept.axes_text(0, ept.axes_dims(cax)[1]+.15, label, ax=cax)                     
        cb = plt.colorbar(orientation='vertical', cax=cax)
        ept.tick_format('ejl')
    
    if output_fname is not None:
        plt.savefig(output_fname + ".png", dpi=200)
        #plt.savefig(output_fname + ".svg", dpi=200)
        
    
