import scipy
import os, os.path
from scipy import ndimage

image_directory = "images"

def count_circles(filepath):
    # read image into numpy array
    # $ wget http://pythonvision.org/media/files/images/dna.jpeg
    f = open(filepath)
    dna = scipy.misc.imread(f) # gray-scale image

    # smooth the image (to remove small objects); set the threshold
    dnaf = ndimage.gaussian_filter(dna, 16)
    T = 25 # set threshold by hand to avoid installing `mahotas` or
           # `scipy.stsci.image` dependencies that have threshold() functions

    # find connected components
    labeled, nr_objects = ndimage.label(dnaf > T) # `dna[:,:,0]>T` for red-dot case
    return nr_objects

def analyze():
    summary = []
    for root, _, files in os.walk(image_directory):
        for f in files:
            fullpath = os.path.join(root, f)
            summary.append((fullpath, count_circles(fullpath)))
    return summary

if __name__ == "__main__":
    analyze()
