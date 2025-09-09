# Delegated QC

[![CI/CD](https://github.com/mtp354/delegated_qc/actions/workflows/ci.yml/badge.svg)](https://github.com/mtp354/delegated_qc/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/mtp354/delegated_qc/branch/main/graph/badge.svg)](https://codecov.io/gh/mtp354/delegated_qc)
[![Documentation Status](https://readthedocs.org/projects/delegated-qc/badge/?version=latest)](https://delegated-qc.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/delegated-qc.svg)](https://badge.fury.io/py/delegated-qc)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Qiskit implementation and extension of the RUV CHSH based verifiable blind delegated quantum computing protocol.

## Features

- **Secure Delegated Quantum Computing**: Implement verifiable blind quantum computation protocols
- **CHSH-Based Verification**: Use CHSH inequality violations for quantum computation verification
- **Qiskit Integration**: Built on top of the Qiskit quantum computing framework
- **Extensible Architecture**: Modular design for easy extension and customization

## Installation

### From PyPI (when available)

```bash
pip install delegated-qc
```

### From Source

```bash
git clone https://github.com/mtp354/delegated_qc.git
cd delegated_qc
pip install -e .
```

### For Development

```bash
git clone https://github.com/mtp354/delegated_qc.git
cd delegated_qc
pip install -e .[dev]
pre-commit install
```

## Quick Start

```python
import delegated_qc

# Basic usage example (to be expanded as features are implemented)
print(f"Delegated QC version: {delegated_qc.__version__}")
```

## Documentation

Full documentation is available at [delegated-qc.readthedocs.io](https://delegated-qc.readthedocs.io/).

## Requirements

- Python 3.8 or higher
- Qiskit 0.45.0 or higher
- NumPy 1.21.0 or higher
- SciPy 1.7.0 or higher

## Contributing

We welcome contributions! Please see our [Contributing Guide](docs/contributing.md) for details.

### Development Setup

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/delegated_qc.git`
3. Create a virtual environment: `python -m venv venv`
4. Activate it: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
5. Install development dependencies: `pip install -e .[dev]`
6. Install pre-commit hooks: `pre-commit install`

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=delegated_qc

# Run specific test file
pytest tests/test_basic.py -v
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Citation

If you use this software in your research, please cite:

```bibtex
@software{delegated_qc,
  title={Delegated QC: A Qiskit Implementation of Verifiable Blind Delegated Quantum Computing},
  author={Prest, Matthew},
  year={2025},
  url={https://github.com/mtp354/delegated_qc}
}
```

## Acknowledgments

- Based on research in verifiable blind quantum computation protocols
- Built with the [Qiskit](https://qiskit.org/) quantum computing framework
- Inspired by RUV CHSH-based verification methods

## Support

- Documentation: [delegated-qc.readthedocs.io](https://delegated-qc.readthedocs.io/)
- Issues: [GitHub Issues](https://github.com/mtp354/delegated_qc/issues)
- Discussions: [GitHub Discussions](https://github.com/mtp354/delegated_qc/discussions)
