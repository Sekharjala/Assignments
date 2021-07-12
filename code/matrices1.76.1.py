#Code by GVV Sharma
#December 7, 2019
#released under GNU GPL
#Proof of Baudhyana Theorem

import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex
#end if




#points 
A = np.array([1,2]) 
B = np.array([3,6]) 
 



#Generating all lines
x_AB = line_gen(A,B)
#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.05), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1), B[1] * (1) , 'B')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
#plt.savefig('./figs/tri_sss.pdf')
#plt.savefig('./figs/tri_sss.png')
#subprocess.run(shlex.split("termux-open ./figs/tri_sss.pdf"))
#else
plt.show()


