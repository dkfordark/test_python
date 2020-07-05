# Bai3: Machine learning 
import numpy as np;
import matplotlib.pyplot as plt;

X = np.loadtxt('/home/tstart/Desktop/testPython/test_python/bai3 machine/univariate.txt',delimiter=',');
Theta = np.loadtxt('/home/tstart/Desktop/testPython/test_python/bai3 machine/univariate_theta.txt');

y = np.copy(X[:,-1]);

X[:,1] = X[:,0];

X[:,0] = 1;

predict = X @ Theta;

predict = 10000 * predict;

print ('%d người : %.2f$' %(X[0,1] * 10000, predict[0]));

np.savetxt('Bai3_predicted_value.txt',predict,fmt = '%.6f');

plt.plot(X[:,1:],y,'rx');

plt.plot(X[:,1:],predict/10000,'-b');

plt.show();


