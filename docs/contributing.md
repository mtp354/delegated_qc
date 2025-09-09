# Contributing

## Development Setup

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/yourusername/delegated_qc.git
   cd delegated_qc
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install development dependencies:
   ```bash
   pip install -e .[dev]
   ```

5. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

## Code Standards

- Follow PEP 8 style guidelines
- Use Black for code formatting
- Use isort for import sorting
- Add type hints for all functions
- Write docstrings for all public functions
- Maintain test coverage above 90%

## Testing

Run tests with:
```bash
pytest tests/ -v
```

Run tests with coverage:
```bash
pytest tests/ --cov=delegated_qc --cov-report=html
```

## Pull Request Process

1. Create a feature branch from `develop`
2. Make your changes
3. Run tests and ensure they pass
4. Run pre-commit hooks
5. Update documentation if needed
6. Submit a pull request to `develop`

## Code Review

All submissions require review. We use GitHub pull requests for this purpose.