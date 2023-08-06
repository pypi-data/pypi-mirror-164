## qutrunk
qutrunk is an quantum programming framework developed by QuDoor corporation, provide the required APIs for quantum programming, it works as follow: 

Export quantum programs based on quantum circuit, qubit and quantum gate, etc. Then you can run the 
quantum circuit by the following two ways:
1. Use PC for quantum computing(work as the default way). 
2. Connect with QuBox(a quantum device developed by qudoor), to run quantum programs, it provide more powerful quantum computing. 

## Install
1. Install from whl package, run the following command directly:
```
pip install qutrunk
```

2. Install from source code, run the following command to install qutrunk by source code:
```
python3 setup.py install
```

## Example:
bell-pair quantum algorithm：

```
from qutrunk.circuit import QCircuit
from qutrunk.circuit.gates import H, CNOT, Measure

qc = QCircuit()
qr = qc.allocate(2) # allocate

H | qr[0]   # apply gate
CNOT | (qr[0], qr[1])
Measure | qr[0]
Measure | qr[1]

qc.print(qc)   # print circuit
res = qc.run(shots=1024) # run circuit
print(res.get_counts()) # print result
```

 ## License
 Apache Licence 2.0

 Copyright (c) 2022-2025 By QUDOOR Technolgies Inc. All Right Reserved.