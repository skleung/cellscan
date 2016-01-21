import numpy as np
from skimage import io, color, filter as filters
from scipy import ndimage
import os, os.path

from skimage.morphology import watershed
from skimage.feature import peak_local_max
from skimage.measure import regionprops, label

image_directory = "images"

def count_circles(filepath):
    f = open(filepath)
    image = color.rgb2gray(io.imread(f))
    image = image < filters.threshold_otsu(image)

    distance = ndimage.distance_transform_edt(image)

    # Here's one way to measure the number of coins directly
    # from the distance map
    coin_centres = (distance > 0.8 * distance.max())
    num_coins = np.max(label(coin_centres))
    print "NUM COINS = ", num_coins
    return num_coins

def analyze():
    summary = []
    for root, _, files in os.walk(image_directory):
        for f in files:
            if not f.startswith('.'):
                fullpath = os.path.join(root, f)
                summary.append((fullpath, count_circles(fullpath)))
    return summary

if __name__ == "__main__":
    analyze()
