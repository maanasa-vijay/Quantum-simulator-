import  numpy as np

state0=np.array([1,0])
state1=np.array([0,1])
state00=np.kron(state0,state0)
state01=np.kron(state0,state1)
state10=np.kron(state1,state0)
state11=np.kron(state1,state1)

H=1/np.sqrt(2) *np.array([[1,1],[1,-1]], dtype=complex)
I=np.array([[1,0],[0,1]], dtype=complex)
# H_full_q1 targets Qubit 1 (MSB)
H_full_q1 = np.kron(H, I)

# H_full_q2 targets Qubit 2 (LSB)
H_full_q2 = np.kron(I, H)
Hfinal=H_full_q2 @ H_full_q1
print(Hfinal@ state00)
print(Hfinal@ state01)
print(Hfinal@ state10)
print(Hfinal@ state11)





