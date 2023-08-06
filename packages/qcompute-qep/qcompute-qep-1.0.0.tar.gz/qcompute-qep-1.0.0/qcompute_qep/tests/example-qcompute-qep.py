#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 Baidu, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This is a simple example to test if you can use the QEP module.
"""
from QCompute import *
from qcompute_qep.quantum.metrics import state_fidelity
from qcompute_qep.quantum.pauli import operator_to_ptm
from qcompute_qep.tomography import StateTomography
from qcompute_qep.utils.circuit import circuit_to_state

# Set the token. You must set your VIP token in order to access the hardware.
Define.hubToken = "Token"

# Step 1. Initialize the quantum program for preparing the Bell state
qp = QEnv()  # qp is short for "quantum program", instance of QProgram
qp.Q.createList(2)
H(qp.Q[0])
CX(qp.Q[0], qp.Q[1])

# Compute numerically the ideal target state for reference
ideal_state = circuit_to_state(qp, vector=False)

# Step 2. Set the quantum computer (instance of QComputer).
# For debugging, change qc to BackendName.LocalBaiduSim2
qc = BackendName.LocalBaiduSim2
# For test on real quantum hardware, change qc to BackendName.CloudIoPCAS
# qc = BackendName.CloudIoPCAS


# Step 3. Perform State Tomography, check how well the Bell state
# Initialize a StateTomography instance
st = StateTomography()
# Alternatively, you may initialize the StateTomography instance as follows:

# st = StateTomography(qp, qc, method='inverse', shots=8192)
# Call the tomography procedure and obtain the noisy quantum state
noisy_state = st.fit(qp, qc, method='inverse', shots=8192)

# Compute the fidelity between two quantum states
fid = state_fidelity(ideal_state, noisy_state.data)

print("***********************************************************************")
print("Testing whether 'qcompute-qep' is successfully installed or not now ...\n")

print('Fidelity between the ideal and noisy Bell states: F = {:.5f}'.format(fid))
print("Please change 'qc' to other quantum computer names for more tests.\n")

print("Package 'qcompute-qep' is successfully installed! Please enjoy!")
print("***********************************************************************")
