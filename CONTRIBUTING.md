# Contributing to XenTokeniser

Thank you for considering contributing to XenTokeniser! This guide will help you get started with the development process.

## Development Setup

1. **Fork the repository** and clone it locally:
   ```bash
   git clone https://github.com/your-username/XenTokeniser.git
   cd XenTokeniser
   ```

2. **Set up a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install the package in development mode** with all dependencies:
   ```bash
   pip install -e ".[dev]"
   pre-commit install
   ```

## Development Workflow

1. **Create a new branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** and ensure the code passes all checks:
   ```bash
   make check  # Runs linting, type checking, and tests
   ```

3. **Format your code** before committing:
   ```bash
   make format
   ```

4. **Commit your changes** with a descriptive message:
   ```bash
   git commit -m "Add your commit message here"
   ```

5. **Push your changes** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Open a Pull Request** against the `main` branch.

## Code Style

We use the following tools to maintain code quality:

- **Black** for code formatting
- **isort** for import sorting
- **Flake8** for linting
- **mypy** for static type checking

Run `make format` to automatically format your code before committing.

## Testing

Write tests for any new functionality. Run the tests with:

```bash
make test
```

## Documentation

- Update the relevant documentation when adding new features or changing behavior.
- Use Google-style docstrings for all public functions and classes.
- Document all parameters, return values, and exceptions.

## Pull Request Process

1. Ensure all tests pass and there are no linter errors.
2. Update the README.md with details of changes if needed.
3. Increase the version number in `xen_tokenizer/version.py` following [Semantic Versioning](https://semver.org/).
4. The PR will be reviewed by the maintainers.

## Reporting Issues

When reporting issues, please include:
- A clear description of the problem
- Steps to reproduce the issue
- Expected vs actual behavior
- Version of Python and XenTokeniser
- Any relevant error messages

## Code of Conduct

This project adheres to the Contributor Covenant [code of conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## License

By contributing, you agree that your contributions will be licensed under the project's license.
