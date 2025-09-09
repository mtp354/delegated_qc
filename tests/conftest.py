"""
Test configuration and fixtures for the delegated_qc package.
"""

import pytest
import sys
import os

# Add the package to the path for testing
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture
def sample_data():
    """Provide sample data for tests."""
    return {
        "test_string": "Hello, Quantum World!",
        "test_number": 42,
        "test_list": [1, 2, 3, 4, 5],
    }


@pytest.fixture
def mock_quantum_circuit():
    """Mock quantum circuit for testing (when qiskit is available)."""
    try:
        from qiskit import QuantumCircuit
        qc = QuantumCircuit(2, 2)
        qc.h(0)
        qc.cx(0, 1)
        qc.measure_all()
        return qc
    except ImportError:
        pytest.skip("Qiskit not available for testing")