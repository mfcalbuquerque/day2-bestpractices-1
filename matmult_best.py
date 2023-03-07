# Program to multiply two matrices using nested loops
import random
import numpy as np

#N = 250

@profile
def mat_mult(N):
    # NxN matrix
    X = []
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])
    
    # Nx(N+1) matrix
    Y = []
    for i in range(N):
        Y.append([random.randint(0,100) for r in range(N+1)])
    
    # result is Nx(N+1)
    result = []
    for i in range(N):
        result.append([0] * (N+1))
    
    # iterate through rows of X
    #for i in range(len(X)):
    #    # iterate through columns of Y
    #    for j in range(len(Y[0])):
    #        # iterate through rows of Y
    #        for k in range(len(Y)):
    #            result[i][j] += X[i][k] * Y[k][j]
    result = np.matmul(X,Y)
    
    #for r in result:
    #    print(r)
    print(result)



mat_mult(250)
