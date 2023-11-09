# Quos package

for simulating quantum computing based on oscillatory quanta

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

quos.piqo('Hadamard 1 1,PauliX 2 2,PauliY 3 3,PauliZ 4 4')

will generate a matplotlib plot of a quantum circuit consisting of

- Hadamard for qubit # 1 at operation sequence 1,
- Pauli X gate for qubit # 2 at operation sequence 2,
- Pauli Y gate for qubit # 3 at operation sequence 3,
- Pauli Z gate for qubit # 4 at operation sequence 4.

### Modules included

icons

### Version History

- 0.0.1 2023-11-07 Initial release
- 0.0.2 2023-11-07 Minor corrections
- 0.0.3 2023-11-07 Minor corrections
- 0.0.4 2023-11-07 Minor corrections
- 0.0.5 2023-11-09 Removed dependancy on networkx package
