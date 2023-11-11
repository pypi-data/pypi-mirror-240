# Quos package

for plotting and simulating quantum computing circuits employing oscillatory qudits

### How to install

pip install matplotlib
pip install quos

### How to upgrade

pip install --upgrade quos

### How to test

import quos
quos.qplt('1,3,0|H,1,1|X,2,1|Z,3,2|Y,4,2|C,1,3,X,3,3|RX 30,2,4|R 30 30 60,3,4')

to generate a matplotlib plot of a quantum circuit consisting of

- Q0 (qudit 0) on qudit not 3 at time 0
- Q0 (qudit 1) on qubit 3 at time 0
- H (Hadamard gate) on qudit 1 at time 1
- X (Pauli X gate) on qudit 2 at time 1
- Z (Pauli Z gate) on qudit 3 at time 2
- Y (Pauli Y gate) on qudit 4 at time 2
- C (control point) on qudit 1 at time 3 controlling
- X (Pauli X gate) on qudit 3 at time 3
- RX (rotation by 30 around X) on qudit 2 at time 4
- R (rotation by 30 30 60 around X Y Z) on qudit 3 at time 4

### Modules included

icons

### Version History

- 0.0.1 2023-11-07 Initial release
- 0.0.2 2023-11-07 Minor corrections
- 0.0.3 2023-11-07 Minor corrections
- 0.0.4 2023-11-07 Minor corrections
- 0.0.5 2023-11-09 Removed dependancy on networkx package
- 0.0.6 2023-11-09 Enabled plotting of CNOT gate
- 0.0.7 2023-11-10 Enabled arguments and plotting of qubits
