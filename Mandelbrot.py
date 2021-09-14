"""

The term Mandelbrot set is used to refer both to a general class of fractal sets and to a particular instance of such a set. In general, a Mandelbrot set marks the set of points in the complex plane such that the corresponding Julia set is connected and not computable.

The Mandelbrot set is the set obtained from the quadratic recurrence equation:

 z_(n+1)=z_n²+C 

with z_0=C, where points C in the complex plane for which the orbit of z_n does not tend to infinity are in the set. Setting z_0 equal to any point in the set that is not a periodic point gives the same result. The Mandelbrot set was originally called a mu molecule by Mandelbrot. J. Hubbard and A. Douady proved that the Mandelbrot set is connected.

[N.B. '_' sign indicate subscript letter here]

How the project works: 

This script might take a few seconds to a few minutes to produce the output, depending on your computer. Reducing N, the size of the square array we are filling, will reduce the amount of computations. The result will be a view of the Mandelbrot set in all of its fractal glory. 

The pyplot.imshow() function is very simple; give it a 2D array and it will render a picture where each pixel represents one value taken from the 2D array. The color of the pixel is picked from a colormap—each value of the array is linearly normalized in the [0, 1] interval. The pyplot.imshow() function renders a figure, but it won't show it. As usual, we should call pyplot.show() to see the figure. However, having two functions with such similar names is arguably confusing. The remaining parts of the script generate our example data. The 2D array Z is created and then filled with a double loop. This loop samples the [-2.2, 0.8]*[-1.5, 1.5] square. For each sample, the iter_count function computes the Mandelbrot set iterations. The data in the Z array could have come from a file or any other source.

"""

import numpy as np

import matplotlib.cm as cm

from matplotlib import pyplot as plt 

plt.style.use("dark_background")



def iter_count ( C, max_iter ):

    X = C

    for n in range ( max_iter ):

       if abs(X) > 2:

          return n

       X = X**2 + C 

    return max_iter

    

N = 512 

max_iter = 64 

xmin, xmax, ymin, ymax = -2.2, .8, -1.5, 1.5 

X = np.linspace(xmin, xmax, N) 

Y = np.linspace(ymin, ymax, N) 

Z = np.empty((N, N)) 



for i, y in enumerate(Y): 

   for j, x in enumerate(X): 

      Z[i, j] = iter_count(complex(x, y), max_iter)

      

plt.imshow(Z, cmap = cm.gray)

plt.xticks([])

plt.yticks([])

plt.grid(False)

plt.box(False)

plt.suptitle('"A man is known by his heroes!" -- Benoît B. Mandelbrot, Mathematician', fontsize= 10, color="white")

plt.title('Mandelbrot set', color="white", fontsize=15)

plt.figtext(0.84, 0.01, "© Mǟɖ↻ôɖɆⱤ™", color="white", fontsize=9)

plt.show()

plt.savefig('myfig.png', dpi= 200)
