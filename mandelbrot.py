#!/usr/bin/python

import numpy
import matplotlib.pyplot as plt

py = 1024
px = 1024
max_iteration = int(input("How many iterations? "))
image = numpy.zeros([px, py])

print("[*] Calculating mandelbrot set.\n")

def formula(real, imaginary, iteration):
    c = complex(real, imaginary)
    zn = 0.0

    for i in range(iteration):
        zn = zn * zn + c
        if(zn.real * zn.real + zn.imag * zn.imag) >= 4:
            return i

    return iteration

def main():
    for x0, real in enumerate(numpy.linspace(-2.5, 1, num=px)):
        for y0, imaginary in enumerate(numpy.linspace(-1, 1, num=py)):
            image[x0, y0] = formula(real, imaginary, max_iteration)

    print("[*] Generating image.\n")
    plt.imshow(image, cmap='CMRmap_r')
    plt.show()

if __name__ == '__main__':
    main()
