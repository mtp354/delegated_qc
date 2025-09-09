"""
Tests for the delegated_qc package.
"""

import pytest
import delegated_qc


def test_package_import():
    """Test that the package can be imported."""
    assert delegated_qc is not None


def test_version():
    """Test that the version is accessible."""
    assert hasattr(delegated_qc, "__version__")
    assert isinstance(delegated_qc.__version__, str)
    assert delegated_qc.__version__ == "0.1.0"


def test_author():
    """Test that the author information is accessible."""
    assert hasattr(delegated_qc, "__author__")
    assert isinstance(delegated_qc.__author__, str)
    assert delegated_qc.__author__ == "Matthew Prest"


def test_email():
    """Test that the email information is accessible."""
    assert hasattr(delegated_qc, "__email__")
    assert isinstance(delegated_qc.__email__, str)
    assert "@" in delegated_qc.__email__


class TestBasicStructure:
    """Test basic package structure."""

    def test_all_exports(self):
        """Test that __all__ contains expected exports."""
        expected_exports = ["__version__", "__author__", "__email__"]
        assert all(item in delegated_qc.__all__ for item in expected_exports)

    def test_no_unexpected_imports(self):
        """Test that no unexpected imports are available yet."""
        # These should not be available until implemented
        unexpected = [
            "DelegatedQCProtocol",
            "CHSHVerifier", 
            "QuantumClient",
            "QuantumServer"
        ]
        for item in unexpected:
            assert not hasattr(delegated_qc, item), f"Unexpected import available: {item}"