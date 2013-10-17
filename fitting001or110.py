import numpy as np
from scipy.optimize import leastsq
import pylab as pl
import scitools.filetable as ft
from math import *
from scitools.all import *
import sys
from constants import *
import pickle

try:
    datsf=sys.argv[1]
    fittingdirection=sys.argv[2]
    bandindex=int(sys.argv[3])
except:
    print "Usage:", sys.argv[0], "datastripoff fittingdirection  bandindex"; sys.exit(1)

def func(kx,ky,kz,p,ini):
     A, B = p
     return A*(kx**2+ky**2)+B*kz**2+ini
  
def residuals(p,ene,kx,ky,kz,ini):
     return ene - func(kx,ky,kz,p,ini)

if bandindex==128:
    band="c1"
elif bandindex==126:
    band="v1"
elif bandindex==124:
    band="v2"
elif bandindex==122:
    band="v3"
else:
   print "wrong bandindex number"
   sys.exit(1)

if fittingdirection=="001":
    s=open('gz7CIISeso.dat','r')
elif fittingdirection=="110":
    s=open('gx7CIISeso.dat','r')
else:
    print "only 110 or 001 is working so far"
    sys.exit(1)

table=ft.read(s)
s.close()

end=int(datsf)

kx = table[0:end, 0]
ky = table[0:end, 1]
kz = table[0:end, 2]

e1=(table[0:end,bandindex-1]+table[0:end,bandindex])/2*ry

r4=sqrt(kx**2+ky**2+(kz_factor*kz)**2)

plot(r4,e1,'r-')
hold('on')	
#guess the parameters for the initilazation  
g0 = [-0.1,-0.2]
plsq = leastsq(residuals, g0, args=(e1,kx,ky,kz,e1[0]))

plot(r4,func(kx,ky,kz, plsq[0],e1[0]),'bo')
xlabel('Wave vector [2pi/a]')
ylabel('Energy [eV]')
legend('original','fitting')

if fittingdirection=="001":
    mzmass=mz/plsq[0][1]
    print u"fitting parameters (mz)", mzmass 
    title('Energy Band (001) for ' + band)
    filename = "mz" + str(bandindex) + ".txt"
    f = open(filename, 'w')
    f.write("%20.10f\n" %mzmass)
    f.write("%20.19f\n" %e1[0])
    f.close()
    hardcopy('mz'+str(bandindex)+'.eps')
    show()
	
if fittingdirection=="110":
    mxymass=mxy/plsq[0][0]
    print u"fitting parameters (mxy)", mxymass 
    title('Energy Band (110) for '+ band)
    filename = "mxy" + str(bandindex) + ".txt"
    f = open(filename, 'w')
    f.write("%20.10f\n" %mxymass)
    f.write("%20.19f\n" %e1[0])
    f.close()
    hardcopy('mxy'+str(bandindex)+'.eps')

    show()

