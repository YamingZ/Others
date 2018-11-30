import matplotlib.pyplot as plt
import numpy as np
import math as mt


B = np.linspace(0,20,200)
A = [2,4,8,16,32,64]
C = np.ones([200])*0.02
print(C)

for i in range(6):
    M = A[i]
    y = [(mt.sqrt(M) - 1)/mt.sqrt(M)*mt.log(M,2) * mt.erfc(mt.sqrt(3*mt.log(M,2)*(10**(x/10))/(2*M-2))) + \
        (mt.sqrt(M) - 2) / mt.sqrt(M) * mt.log(M, 2) * mt.erfc(mt.sqrt(3 * mt.log(M, 2)*(10**(x/10)) / (2 * M - 2))) for x in B]

    plt.plot(B,y,'.')
    plt.plot(B,C,'-')
    plt.semilogy(B,y)

    plt.ylim(0.0, 100)

plt.show()
