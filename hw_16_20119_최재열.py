
from skimage import exposure
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import os

#########################################################

def convolve(image, kernel):
    (iH, iW) = len(image), len(image[0])
    (kH, kW) = len(kernel), len(kernel[0])
    pad = kH//2
    pad_image = np.pad(image.copy(), ((pad, pad), (pad, pad)))
    output_image = np.zeros_like(image)

    for y in np.arange(iH):
        for x in np.arange(iW):
            roi = pad_image[y:y+kH, x:x+kW]
            k = (roi*kernel).sum()
            k = 0 if k<0 else 255 if k>255 else k
            output_image[y,x] = k

    output_image = exposure.rescale_intensity(output_image, out_range=(0,255)).astype("uint8")
    return output_image

#########################################################

original = np.array((
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]), dtype="float")

sharpen = np.array((
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]), dtype="float")

smallBlur = np.full((7,7),1/49)

laplacian = np.array((
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]), dtype="float")

sobelX = np.array((
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]), dtype="float")

sobelY = np.array((
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]), dtype="float")


kernelBank = (
    ("original", original),
    ("sharpen", sharpen),
    ("smallBlur", smallBlur),
    ("laplacian", laplacian),
    ("sobelX", sobelX),
    ("sobelY", sobelY)
)

#########################################################

image = Image.open("images/test2.jpg").convert("L")
image = np.array(image)
fig = plt.figure()

for i, filter in enumerate(kernelBank):
    ax = fig.add_subplot(2,3,i+1)
    convolveOutput = convolve(image, filter[1])
    ax.set_title(filter[0])
    ax.imshow(convolveOutput, cmap="gray")

plt.show()

#########################################################