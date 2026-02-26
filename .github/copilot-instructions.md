# Python Algorithms Project Guidelines

## Code Style

- **Line Length**: Maximum 120 characters (configured in [setup.cfg](../setup.cfg))
- **Language**: Python 3 with type hints where applicable
- **Formatter**: Use `autopep8` for automatic formatting
- **Linting**: Follow flake8 rules; unused imports/variables are flagged
- **Import Sorting**: Use `isort` (configured for line_length=120, multi_line_output=3)
- **Type Checking**: mypy is configured; warnings for missing optional types are expected

### Code Organization Pattern
All command-line modules follow this structure:
```python
def main():
    # Implementation here
    pass

if __name__ == '__main__':
    main()
```
See [combinate.py](../combinate.py) and [common_items.py](../common_items.py) for examples.

## Architecture

This is a **lightweight algorithm library** with independent modules. Each file is self-contained:
- **Algorithm modules**: Implement specific algorithms or utilities (combinations, set intersection, odd/even tests)
- **Generators**: Used where sequences are computed on-demand (e.g., [combinate.py](../combinate.py))
- **Defensive coding**: Handle edge cases like None values, empty containers, and type validation

No external service dependencies or complex abstractions—focus on clarity and correctness.

## Build and Test

### Environment Setup
```bash
# Create virtual environment (already setup in venv/)
python -m venv venv

# Activate (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Activate (bash/WSL)
source venv/Scripts/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Code Quality Commands
```bash
# Format code
autopep8 --in-place --aggressive --aggressive <file.py>

# Lint check
flake8 <file.py>

# Sort imports
isort <file.py>

# Type check
mypy <file.py>

# Run module directly
python <file.py>
```

## Project Conventions

### Function Design
- **Use generators** for producing sequences of values (yield instead of returning lists)
- **Handle defensive cases**: Check for None, empty containers, type validation at entry points
- Example: [common_items.py](../common_items.py) uses `or []` to handle None gracefully

### Docstring Pattern
Functions include simple inline examples via `f-string` print statements in `main()` rather than formal docstrings. When adding new functions, follow this pattern:
```python
def algorithm_function(input_data):
    # Simple implementation
    return result

def main():
    test_cases = [...]
    for test in test_cases:
        print(f'{test}: {algorithm_function(test)}')
```

### Exception Handling
Interactive modules (like [test_odd_even.py](../test_odd_even.py)) handle:
- `KeyboardInterrupt` (Ctrl+C) → safe exit
- `EOFError` (EOF) → safe exit  
- `ValueError` → user input validation with informative messages

## Integration Points

- **No external APIs** or services—all dependencies are development tools (linters, formatters, type checkers)
- **Standard library focus**—use built-in data structures (sets, lists, generators) rather than external packages
- **CLI entry points**—modules are runnable as standalone scripts for testing/demo purposes

## Code Quality Standards

- All modules must pass flake8 linting
- mypy type checking is enabled—resolve type warnings
- Maximum McCabe complexity: 15 (enforced via flake8)
- Trailing commas in multi-line imports/lists (isort configuration)
