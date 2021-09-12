from sage.all import *

from sage.crypto.sbox import SBox
S0 = SBox(12,5,6,11,9,0,10,13,3,14,15,8,4,7,1,2)


#4.15:
S1 = SBox(8,4,2,1,12,6,3,13,10,5,14,7,15,11,9,0)
print(S1.linear_approximation_table())

#4.16
S2 = SBox(14,2,1,3,13,9,0,6,15,4,5,10,8,12,7,11)
print(S2.difference_distribution_table())


#https://doc.sagemath.org/html/en/reference/cryptography/sage/crypto/sbox.html



