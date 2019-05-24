import numpy as np
from uncertainties import ufloat
from uncertainties.umath import *

ub1 = 250
ub2 = 400

a1 = ufloat(8.6, 0.1) * 10**(3)
a2 = ufloat(7.70, 0.08) * 10**(3)

#a1 = ufloat(12472, 244)
#a2 = ufloat(9788, 154)

eDurchM1 = 8 * ub1 * a1**2
eDurchM2 = 8 * ub2 * a2**2

print(eDurchM1)
print(eDurchM2)