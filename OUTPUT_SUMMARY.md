# Python Calculator Project - Lesson 02 Demo 02 Output

## ✅ Project Setup Complete

### Project Structure
```
python-calculator/
├── .github/
│   └── workflows/
│       └── build.yaml          # GitHub Actions workflow
├── src/
│   ├── calculator.py           # Calculator function
│   └── test_calculator.py      # Unit tests
├── .gitignore                  # Git ignore rules
└── requirements.txt            # Python dependencies (empty)
```

---

## 📄 File Contents

### 1. src/calculator.py
Calculator function with 4 operations:
- **add**: Adds two numbers
- **subtract**: Subtracts two numbers
- **multiply**: Multiplies two numbers
- **divide**: Divides two numbers (raises ValueError on division by zero)

```python
def calculator(operation, num1, num2):
    """
    Performs basic arithmetic operations.
    
    Args:
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide')
        num1 (float): The first number
        num2 (float): The second number
    
    Returns:
        float: The result of the operation
    
    Raises:
        ValueError: If the operation is not supported or if dividing by zero
    """
```

---

### 2. src/test_calculator.py
Comprehensive unit tests with 6 test methods:
- `test_addition()` - 3 test cases for addition
- `test_subtraction()` - 3 test cases for subtraction
- `test_multiplication()` - 3 test cases for multiplication
- `test_division()` - 3 test cases for division
- `test_division_by_zero()` - Verifies ValueError on division by zero
- `test_invalid_operation()` - Verifies ValueError for unsupported operations

---

### 3. .github/workflows/build.yaml
GitHub Actions CI/CD workflow that:
- Runs on every push and pull request to main branch
- Sets up Python 3.12
- Installs dependencies from requirements.txt
- Runs all unit tests with verbose output

```yaml
name: Python Calculator CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run tests
        run: python -m unittest discover -s src -v
```

---

## 🧪 Test Execution Output

```
test_addition (test_calculator.TestCalculator.test_addition)
Test addition operation. ... ok

test_division (test_calculator.TestCalculator.test_division)
Test division operation. ... ok

test_division_by_zero (test_calculator.TestCalculator.test_division_by_zero)
Test that division by zero raises ValueError. ... ok

test_invalid_operation (test_calculator.TestCalculator.test_invalid_operation)
Test that invalid operation raises ValueError. ... ok

test_multiplication (test_calculator.TestCalculator.test_multiplication)
Test multiplication operation. ... ok

test_subtraction (test_calculator.TestCalculator.test_subtraction)
Test subtraction operation. ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK
```

✅ **All 6 tests passed successfully!**

---

## 🚀 Next Steps

### To push to GitHub:

1. **Create a GitHub repository** (empty, no README/license)
   - Go to https://github.com/new
   - Name: `python-calculator`
   - Leave it empty
   - Click "Create repository"

2. **Initialize and push:**
   ```powershell
   cd "C:\Users\pedamaka\OneDrive - Cisco\Desktop\python-calculator"
   git init
   git add .
   git commit -m "Add calculator, unit tests, and CI workflow"
   git branch -M main
   git remote add origin https://github.com/<your-username>/python-calculator.git
   git push -u origin main
   ```

3. **Verify on GitHub:**
   - Go to your repository
   - Click the "Actions" tab
   - See the workflow run with ✅ green checkmark
   - Confirm all 6 tests passed

---

## 📝 Summary

✅ Project structure created with proper organization
✅ Calculator function with 4 operations implemented
✅ 6 comprehensive unit tests covering all operations and edge cases
✅ All tests passing locally (OK status)
✅ GitHub Actions workflow configured and ready
✅ Project ready for GitHub push

---

**Location:** `C:\Users\pedamaka\OneDrive - Cisco\Desktop\python-calculator`
**Status:** ✅ Complete and Ready for GitHub
