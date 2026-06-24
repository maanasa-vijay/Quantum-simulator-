import streamlit as st  # Added for deployment
import numpy as np
import matplotlib.pyplot as plt
import time

start_total=time.time()
#defining my state vector
state0=np.array([1,0])
state1=np.array([0,1])
state00=np.kron(state0,state0)
memory_usage = state00.nbytes
print(f"Memory usage of state vector: {memory_usage} bytes")

H=1/np.sqrt(2) * np.array([[1,1], [1,-1]], dtype=complex)
I=np.array([[1,0],[0,1]] , dtype=complex)
Hgate_0=np.kron(H,I) #creating the hadamard gate

CNOT = np.array([
[1, 0, 0, 0],
[0, 1, 0, 0],
[0, 0, 0, 1],
[0, 0, 1, 0]
])

gate_time_start=time.time()
final_state=CNOT @(Hgate_0 @ state00) #applying the CNOT gate
gate_time_end=time.time()

amplitudes=np.abs(final_state) #measuring probabilities
probabilities=amplitudes**2

# --- Visualization for Streamlit ---
st.title("Bell State Simulator")
st.write("Final State Vector:", final_state)
st.write("Probabilities of measuring each state:", probabilities)

plt.figure()
plt.bar(['00', '01', '10', '11'], probabilities)
plt.xlabel('State')
plt.ylabel('Probability')
plt.title('Measurement Probability Distribution')


st.pyplot(plt)
