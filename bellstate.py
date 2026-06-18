import numpy as np
import time


start_total=time.time()
#defining  my state vector
state0=np.array([1,0])
state1=np.array([0,1])
state00=np.kron(state0,state0)
memory_usage = state00.nbytes
print(f"Memory usage of state vector: {memory_usage} bytes")
H=1/np.sqrt(2) *np.array([[1,1],[1,-1]], dtype=complex)
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
print(final_state)
print("probabilities of measuring each state")
print(probabilities)
print(np.sum(probabilities))

labels = ["|00>", "|01>", "|10>", "|11>"]
outcome = np.random.choice(labels, p=probabilities)
print(f"\nSingle measurement result: {outcome}")
counts = {"|00>": 0, "|01>": 0, "|10>": 0, "|11>": 0}

shots = 0
total_shots = 1000

print(f"\nRunning {total_shots} measurements...")

# Loop exactly 1000 times
while shots < total_shots:
    outcome = np.random.choice(labels, p=probabilities)
    counts[outcome] += 1
    shots+=1

print("\nResults after 1000 measurements:")
for state, count in counts.items():
    print(f"{state}: {count}")

end_total=time.time()
time_taken=end_total-start_total
print(f"\nTotal time: {time_taken} seconds")
gate_total=gate_time_end-gate_time_start
print(f"\nTotal gate time: {gate_total} seconds")



import matplotlib.pyplot as plt

# Extract labels and values from your counts dictionary
states = list(counts.keys())
frequencies = list(counts.values())

# Create the bar chart
plt.bar(states, frequencies, color='skyblue')
plt.xlabel('Quantum States')
plt.ylabel('Counts (out of 1000)')
plt.title('Bell State Measurement Distribution')
plt.show()