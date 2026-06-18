import numpy as np

state0=np.array([1,0])
state1=np.array([0,1])
state00=np.kron(state0,state0)
X=np.array([[0,1],[1,0]])
I=np.array([[1,0],[0,1]])
Xq1=np.kron(X,I)
Xq2=np.kron(I,X)
X_full= Xq2@Xq1
X_fullk=np.kron(X,X)
print(X_full @ state00)
print(X_fullk @ state00)


