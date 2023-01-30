import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
import math


def figure(figDims=(3, 2.5), figMargins=(.5, .5, .1, .1), figSpaces=(.25, .25),
                  axNs=(1, 1), axRatio=1, calcFigH=False, calcFigW=False, dpi=200):

    figW, figH = figDims
    figLM, figBM, figRM, figTM = figMargins
    figWS, figHS = figSpaces
    axNx, axNy = axNs

    if(calcFigH):
        figH = (-(-figBM-figTM-(axNy-1)*figHS)+axRatio *
                axNy * (figW-figLM-figRM-(axNx-1)*figWS)/axNx)
    elif(calcFigW):
        figW = (-(-figLM-figRM-(axNx-1)*figWS)+axRatio *
                axNx * (figH-figBM-figTM-(axNy-1)*figHS)/axNy)

    axW = (figW-figLM-figRM-figWS*(axNx-1))/(axNx)
    axH = (figH-figBM-figTM-figHS*(axNy-1))/(axNy)

    fig, ax = plt.subplots(axNy, axNx, figsize=(figW, figH), dpi=dpi)
    plt.subplots_adjust(figLM/figW, figBM/figH, 1-figRM /
                        figW, 1-figTM/figH, figWS/axW, figHS/axH)

    return fig, ax, (axW, axH)


def tick_format(fmt='ejl', axis='xy', ax=None):
    if ax == None:
        ax = plt.gca()
    
    if fmt == 'ejl':
        formatter = ticker.StrMethodFormatter("{x:g}")
    elif fmt == 'log':
        formatter = ticker.FuncFormatter(lambda x,p: r"$10$\textsuperscript{%d}"%np.log10(x))

    if(axis == 'x' or axis == 'xy'):
        ax.xaxis.set_major_formatter(formatter)
    if(axis == 'y' or axis == 'xy'):
        ax.yaxis.set_major_formatter(formatter)       


def axes_dims(ax=None):
    if ax == None:
        ax = plt.gca()
    fig = ax.get_figure()
    return ax.bbox.width/fig.dpi, ax.bbox.height/fig.dpi


def fig_dims(fig=None):
    if fig == None:
        fig = plt.gcf()
    return fig.get_size_inches()


def axes_text(x=0, y=0, textString="", ax=None, **kwargs):
    if ax == None:
        ax = plt.gca()
    axW, axH = axes_dims(ax)
    plt.text(x/axW,y/axH,textString,transform=ax.transAxes,**kwargs)


def axes(cbDims=(0,1), cbMargins=(0,0), fig=None):

    if fig == None:
        fig = plt.gcf()
    figW, figH = fig_dims(fig)
    cbW, cbH = cbDims
    cbLM, cbBM = cbMargins

    cbAx = fig.add_axes([cbLM/figW, cbBM/figH, cbW/figW, cbH/figH])

    return cbAx

def calc_ticks(ymax):
    
    ytops = np.array([1,1.6,2.5,4,6.4,10])
    yexp = int(math.floor(math.log10(ymax)))
    yti = np.where(ytops-10**(math.log10(ymax)%1)>0)[0][0]
    yfact = ytops[yti]
    ymax = yfact*10**yexp
    
    if yti in [0, 2, 5]:
        N_ticks = 6
    else:
    	N_ticks = 5
        
    return np.linspace(0, ymax, N_ticks)

def axis_ticks(ticks, axis='y', bezel=.1):
    
    amax = ticks[-1] + bezel*(ticks[-1] - ticks[0])
    amin = ticks[0] - bezel*(ticks[-1] - ticks[0])
    
    if axis == 'y':
        plt.ylim(amin, amax)
    if axis == 'x':
        plt.ylim(amin, amax)
    
    
