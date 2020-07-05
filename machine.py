# Test machine learning
import array as arr;


a = arr.array ('d',[1.1,2.4,2.4]);
print (a);

# test matrix 
import numpy as np;

_A = [
        [1,2],
        [3,4],
        [5,6]
    ];

_B = [[1,2,5],[3,4,6]];

A = np.array(_A);
B = np.array(_B);

print ("Array A : \n",A);
print ("Array B : \n",B);
print ("A * B : \n", A @ B );


