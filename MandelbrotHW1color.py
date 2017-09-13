from __future__ import division        #To avoid problem with integer division
from pylab import imshow,jet,show      #For density plot
from numpy import empty                #To define an empty array

N = 3000  #Grid size

#Define an array Mand whose (m,n)th entry represents the density plot hue on the
#pixel at the N-th row and M-th column
Mand = empty([N,N],int)


for a in range(N):                      #Loop for real axis

    for b in range(N):                  #Loop for imaginary axis
        c_real = ((4*a)/N)-2            #Real part of c
        c_imag = ((4*b)/N)-2            #Imaginary part of c
        c = c_real + c_imag*1j
        z = 0                           #We set z = 0 before running for a c

        for n in range(100):
            if abs(z)<=2:
                z = z*z + c
            else:
                Mand[b,a]=n             #Codes the number of iterations for abs(z) > 2
                break

#Store the Density Plot values from the 2D array Mand onto
#a X:[-2,2] Y:[-2,2] graph
imshow(Mand, origin="lower", extent=[-2,2,-2,2])

jet()  #Plot color scheme
show()  #Displays plot
