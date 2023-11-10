# Quos package

for plotting and simulating quantum computing circuits employing oscillatory qudits

### How to install

pip install matplotlib
pip install quos

### How to upgrade

pip install --upgrade quos

### How to import

import quos
or
from quos import \*

### How to use

quos.qplt('H 1 1,X 1 2,Z 2 3,Y 2 4,C 3 1 X 3 3,H 4 2')

will generate a matplotlib plot of a quantum circuit consisting of

- H (Hadamard gate) at time 1 on qudit 1
- X (Pauli X gate) at time 1 on qudit 2
- Z (Pauli Z gate) at time 2 on qudit 3
- Y (Pauli Y gate) at time 2 on qudit 4
- C (control point) at time 3 on qudit 1 controlling
- X (Pauli X gate) at time 3 on qudit 3
- H (Hadamard gate) at time 4 on qudit 2

### Modules included

icons

### Version History

- 0.0.1 2023-11-07 Initial release
- 0.0.2 2023-11-07 Minor corrections
- 0.0.3 2023-11-07 Minor corrections
- 0.0.4 2023-11-07 Minor corrections
- 0.0.5 2023-11-09 Removed dependancy on networkx package
- 0.0.6 2023-11-09 Enabled plotting of CNOT gate
