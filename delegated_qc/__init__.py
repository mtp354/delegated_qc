"""
Delegated QC - A Qiskit implementation and extension of the RUV CHSH based 
verifiable blind delegated quantum computing protocol.
"""

__version__ = "0.1.0"
__author__ = "Matthew Prest"
__email__ = "matthewprestnz@gmail.com"

# Import main components when they're implemented
# from .core import DelegatedQCProtocol
# from .verification import CHSHVerifier
# from .client import QuantumClient
# from .server import QuantumServer

__all__ = [
    "__version__",
    "__author__",
    "__email__",
]

# Set up IBM Quantum account
# Uncomment and add your IBM Quantum API key to use IBM Quantum backends
# token = "Your_IBM_Quantum_API_Key_Here"

from qiskit_ibm_runtime import QiskitRuntimeService
# service = QiskitRuntimeService.save_account(
#     token=token, # IBM Cloud API key.
#     set_as_default=True, # Optionally set these as your default credentials.
#   )

service = QiskitRuntimeService(instance="mprest1")


from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime import EstimatorV2 as Estimator
 
# Create a new circuit with two qubits
qc = QuantumCircuit(2)
 
# Add a Hadamard gate to qubit 0
qc.h(0)
 
# Perform a controlled-X gate on qubit 1, controlled by qubit 0
qc.cx(0, 1)
 
# Set up six different observables.
 
observables_labels = ["IZ", "IX", "ZI", "XI", "ZZ", "XX"]
observables = [SparsePauliOp(label) for label in observables_labels]

backend = service.least_busy(simulator=False, operational=True)
# Convert to an ISA circuit and layout-mapped observables.
pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
isa_circuit = pm.run(qc)

# Construct the Estimator instance.
 
estimator = Estimator(mode=backend)
estimator.options.resilience_level = 1
estimator.options.default_shots = 5000
 
mapped_observables = [
    observable.apply_layout(isa_circuit.layout) for observable in observables
]
 
# One pub, with one circuit to run against five different observables.
job = estimator.run([(isa_circuit, mapped_observables)])
 
# Use the job ID to retrieve your job data later
print(f">>> Job ID: {job.job_id()}")
