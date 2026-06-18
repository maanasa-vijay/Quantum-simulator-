import numpy as np

state0=np.array([1,0])
state1=np.array([0,1])
state10=np.kron(state1,state0)
CNOT = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
])
print(CNOT @ state10)