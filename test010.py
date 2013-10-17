import numpy as np
from scipy.optimize import leastsq
import pylab as pl
import scitools.filetable as ft
from math import *
from scitools.all import *
import sys
from constants import *

try:
    datsf=sys.argv[1]
    bandindex=int(sys.argv[2])
except:
    print "Usage:", sys.argv[0], "datastripoff bandindex"; sys.exit(1)

f=open('mz'+str(bandindex)+'.txt','r')
B=float(f.readline())
C=float(f.readline())
f.close()

f=open('mxy'+str(bandindex)+'.txt','r')
A=float(f.readline())
f.close()

def func(kx,ky,kz,p):
     A, B, C = p
     return A*(kx**2+ky**2)+B*kz**2+C
  

s=open('gm7CIISeso.dat','r')
table=ft.read(s)
s.close()

end=int(datsf)

kx = table[0:end, 0]
ky = table[0:end, 1]
kz = table[0:end, 2]

e1=(table[0:end,bandindex]+table[0:end,bandindex-1])/2*ry

r4=sqrt(kx**2+ky**2+(kz_factor*kz)**2)

plot(r4,e1,'r-')
hold('on')	
 
coeff=[mxy/A ,mz/B ,C]
plot(r4,func(kx,ky,kz, coeff[:]),'bo')
title('Test Energy Band (010)')
xlabel('Wave vector [2pi/a]')
ylabel('Energy [eV]')
legend('original','fitting')
show()
hardcopy('test010'+'bandindex'+str(bandindex)+'.eps')
