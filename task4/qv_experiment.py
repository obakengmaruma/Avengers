from qiskit import *
from qiskit.circuit.library import *
from qiskit_aer import *
import time
import numpy as np

def quant_vol(qubits=15, depth=10, shots=1):
   sim = AerSimulator(method='statevector', device='CPU')
   circuit = QuantumVolume(qubits, depth, seed=0)
   circuit.measure_all()
   circuit = transpile(circuit, sim)

   start = time.time()
   result = sim.run(circuit, shots=shots, seed_simulator=12345).result()
   time_val = time.time() - start
   return time_val


num_qubits = np.arange(2, 15)
qv_depth = 5
num_shots = 1000

results_array = []

for i in num_qubits:
   results_array.append(quant_vol(qubits=i, shots=num_shots, depth=qv_depth))
   print(f"Qubits: {i}, Time: {results_array[-1]}")

import matplotlib.pyplot as plt

plt.xlabel('Number of qubits')
plt.ylabel('Time (sec)')
plt.plot(num_qubits, results_array)
plt.title('Quantum Volume Experiment with depth=' + str(qv_depth))
plt.savefig('shots1000.png')
print("Plot saved as qv_experiment.png")
