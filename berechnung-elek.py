import numpy as np
from uncertainties import ufloat
from uncertainties.umath import *

p = 19  #mm
L = 143 #mm
d = 3.8 #mm

mystery = (p*L) / (2 * d)

print(mystery)

a = ufloat(330, 10)

print(a/mystery)