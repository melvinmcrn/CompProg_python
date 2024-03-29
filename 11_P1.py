import numpy as np

data = np.array([[15,3.78],
                 [29,2.0],
                 [10,2.5],
                 [25,2.85],
                 [30,3.96]])

logit_pi = -3.98 + 0.2*data[:,0] + 0.5*data[:,1]

p_xi = 1 / (1 + np.e**-logit_pi)

n = int(input())

if n < 1 or n > len(list(p_xi)):
    print('Error')

elif p_xi[n-1] > 0.5:
    print('True')

else:
    print('False')
