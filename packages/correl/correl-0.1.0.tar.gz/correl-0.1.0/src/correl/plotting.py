#!/usr/bin/python
"""
Python module for various plotting helpers to display
generalized susceptibility matrices.
"""
import numpy as np
import scipy as sp
import matplotlib as mpl

def cdict_cw(points = 10_001):
    """
    returns:
        colormap dictionary inspired by Patrick Chalupa: the colormap
        is a sequential blue-white-red map and enhances the visibility
        of small deviations from the central value
    """
    half = points//2
    cp = np.linspace(0,1,points,endpoint=True)

    green = np.zeros(points)
    blue = np.zeros(points)
    red = np.zeros(points)

    green[:half]= 1-(1-2.*cp[:half])**(1/2)
    green[half]= 1
    green[half+1:]= 1-(1-2.*cp[:half][::-1])**(1/2)
    red[half]= 1
    red[half+1:]= 1-cp[1:half+1]
    blue[half]= 1
    blue[:half]= 1-cp[1:half+1][::-1]


    Gn = np.column_stack((cp[:],green[:],green[:]))
    Rd = np.column_stack((cp[:],red[:],red[:]))
    Bu = np.column_stack((cp[:],blue[:],blue[:]))

    return  {'green':  Gn,
             'blue':  Bu,
             'red':  Rd}


def cdict_gr(points = 10_001):
    """
    returns:
        colormap dictionary: the colormap is a sequential 
        green-brown-red map and enhances the visibility
        of small deviations from the central value
    """
    half = points//2
    cp = np.linspace(0,1,points,endpoint=True)

    green = np.zeros(points)
    blue = np.zeros(points)
    red = np.zeros(points)

    green[:half]= (1-2.*cp[:half])**(1/2)
    green[half]=green[half-1]/2
    red[half+1:]= 0.25+(np.array(1.-2*cp[:half])[::-1])**(1/2)
    red[half]= red[half+1]/2
    blue[np.where(red>1)]= red[np.where(red>1)]-1.
    red[np.where(red>1)] = 1.

    Gn = np.column_stack((cp[:],green[:],green[:]))
    Rd = np.column_stack((cp[:],red[:],red[:]))
    Bu = np.column_stack((cp[:],blue[:],blue[:]))

    return  {'green':  Gn,
             'blue':  Bu,
             'red':  Rd}

def cdict_gy(points = 10_001):
    """
    returns:
        colormap dictionary: the colormap is a sequential 
        green-black-yellow map and enhances the visibility
        of small deviations from the central value
    """
    half = points//2
    cp = np.linspace(0,1,points)

    green = np.zeros(points)
    blue = np.zeros(points)
    red = np.zeros(points)

    green[:half]= (1-2.*cp[:half])**(1/7)
    green[half+1:]= 0.8*(1-2.*cp[:half][::-1])**(1/7)
    green[half] = 0.
    red[half]= 0.
    red[half+1:]= 0.25+(np.array(1.-2*cp[:half])[::-1])**(1/7)
    blue[np.where(red>1)]= red[np.where(red>1)]-1.
    red[np.where(red>1)] = 1.

    Gn = np.column_stack((cp[:],green[:],green[:]))
    Rd = np.column_stack((cp[:],red[:],red[:]))
    Bu = np.column_stack((cp[:],blue[:],blue[:]))


    return  {'green':  Gn,
             'blue':  Bu,
             'red':  Rd}

def cmap_gy(points = 6_001):
    """
    returns:
        sequential green-black-yellow colormap with enhanced visibility
        of small deviations from the central value
    """
    return mpl.colors.LinearSegmentedColormap('reitner_gy',
                                              segmentdata = cdict_gy(points)
                                              ,N=points).reversed()

def cmap_gr(points = 6_001):
    """
    returns:
        sequential green-brown-red colormap with enhanced visibility
        of small deviations from the central value
    """
    return mpl.colors.LinearSegmentedColormap('reitner_gr',
                                              segmentdata = cdict_gr(points)
                                              ,N=points).reversed()
def cmap_w(points = 6_001):
    """
    returns:
        sequential blue-white-red colormap with enhanced visibility
        of small deviations from the central value
        Inspired by Patrick Chalupa
    """
    return mpl.colors.LinearSegmentedColormap('chalupa_white',
                                              segmentdata = cdict_cw(points)
                                              ,N=points).reversed()


# ---------------------------------------
# normalize colormap around zero value
# ---------------------------------------
class norm(mpl.colors.Normalize):
    """
    class to normalize matplotlib colorbar around midpoint from stackoverflow

    attributes:
        matrix (float, array) array to calculate colormap norm
        midpoint (float, optional) midpoint
        clip (bool, optional)

    """
    def __init__(self, matrix, midpoint=0, clip=False):
        # normalize only real part
        M= np.real(matrix)
        vmin = np.amin(M)
        vmax = np.amax(M)
        self.midpoint = midpoint
        mpl.colors.Normalize.__init__(self, vmin, vmax, clip)

    def __call__(self, value, clip=None):
        """
        args:
            value (float)
            clip (optional)
        
        returns:
            masked array for colorbar normalization
        """
        if self.vmax == 0:
            normalized_min = 0
        else:
            normalized_min = max(0, 1 / 2 * (1 - abs((self.midpoint - self.vmin) \
                                                     / (self.midpoint - self.vmax))))
        if self.vmin == 0:
            normalized_max = 1
        else:
            normalized_max = min(1, 1 / 2 * (1 + abs((self.vmax - self.midpoint) \
                                                     / (self.midpoint - self.vmin))))
        normalized_mid = 0.5
        x = [self.vmin, self.midpoint, self.vmax] 
        y = [normalized_min, normalized_mid, normalized_max]
        return sp.ma.masked_array(sp.interp(value, x, y))
