# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 12:54:15 2015

@author: koeus
"""
from __future__ import division
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from scipy.ndimage import filters
#import cv2

#############################################################
### DEFINITIONS OF ROUTINES TO SOLVE THE ASSIGNMENT TASKS ###
#############################################################

## first we need the image of lena to have something to work with
filepath = './Lenna.png'
sigmas   = [1,2,4,8]

im_color = Image.open(filepath)
im_bw    = im_color.convert('L')
im       = np.array(im_bw, 'f')


def gaussfilter(im, sigma):
    """ apply gaussian filter to image, and return copy of image """
    imf = filters


#############################################################
### Running the routines, outputting results              ###
#############################################################

if __name__ == '__main__':
    fig = plt.figure()
    plt.title('original')
    plt.imshow(im, cmap='gray')
    plt.colorbar(shrink=.92)
    print np.max(im)
    print im.dtype

    for sigma in sigmas:
        fig = plt.figure()
        plt.title('Gaussian Filter, sigma: {}'.format(sigma))
        plt.imshow(filters.gaussian_filter(im, sigma), cmap='gray')
        plt.colorbar(shrink=.92)

    plt.show()

