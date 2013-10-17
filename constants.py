#!/user/bin/env python
import math

pi=math.pi
ry =13.6056981
a=5.7799887002e-10
c=11.5889763e-10
kz_factor=a/c

conskx=2*pi/5.7799887002e-10;
consky=2*pi/5.7799887002e-10;
conskz=2*pi/11.5889763e-10;
consene=2.179891343883900e-18;

m0 =9.1095e-031;
hbar2 =1.1122e-068;

q_charge=1.602176565E-19;
mxy=hbar2*conskx*conskx/(2*q_charge*m0);
mz=hbar2*conskz*conskz/(2*q_charge*m0);
