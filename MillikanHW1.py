from __future__ import division
from numpy import loadtxt,linspace
from pylab import plot,show,xlabel,ylabel

#PART A

data = loadtxt("millikan.txt",float)

plot(data[:,0],data[:,1],"ko")
xlabel("Frequency (Hz)")
ylabel("Voltage (J/C)")


#PART B

Ex = sum(data[:,0])/len(data)
Ey = sum(data[:,1])/len(data)
Exx = sum(data[:,0]**2)/len(data)
Exy = sum(data[:,0]*data[:,1])/len(data)

m = (Exy - Ex * Ey)/(Exx - Ex**2)
c = (Exx * Ey - Ex * Exy)/(Exx - Ex**2)

print "The slope is",m
print "The intercept is",c


#PART C

x = linspace(min(data[:,0]),max(data[:,0]),100)
y = m*x + c
plot(x,y)


#PART D

e = 1.602e-19       #Charge of electron
h = m*e             #Planck's constant from Millikan's data
h_true = 6.626e-34  #value accepted today for Planck's constant

Percent_Error = abs(h_true-h) * 100 /h_true

print "The value of Planck's constantin Millikan's data is",h,"which is a",Percent_Error,"% deviation from today's value."


show()
