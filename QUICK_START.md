# 🖥️ COPY-PASTE TERMINAL COMMANDS

## ✅ WHAT YOU DID (Virtual Environment Setup)

You created a virtual environment:
```powershell
python3 -m venv .venv
```

## ✅ TO ACTIVATE IT IN POWERSHELL

**Option 1 (Recommended):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**If you get an execution policy error, run this ONCE:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try again:
```powershell
.\.venv\Scripts\Activate.ps1
```

**Option 2 (Use Command Prompt instead):**
```cmd
.\.venv\Scripts\activate.bat
```

---

## ✅ HOW TO SEE TEST OUTPUT (3 SIMPLE STEPS)

### Step 1: Navigate to project
```powershell
cd "C:\Users\pedamaka\OneDrive - Cisco\Desktop\python-calculator"
```

### Step 2: Run tests
```powershell
python -m unittest discover -s src -v
```

### Step 3: You'll see output like this:
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

---

## 📋 OTHER QUICK COMMANDS

### Simple test output (no details)
```powershell
python -m unittest discover -s src
```

Output:
```
......
------
Ran 6 tests in 0.000s

OK
```

### Test one specific operation
```powershell
cd src
python -m unittest test_calculator.TestCalculator.test_addition -v
cd ..
```

### Test manually in Python
```powershell
python
```

Then type:
```python
import sys
sys.path.insert(0, 'src')
from calculator import calculator

print(calculator('add', 5, 3))      # Output: 8
print(calculator('multiply', 4, 5)) # Output: 20
print(calculator('divide', 10, 2))  # Output: 5.0

exit()
```

---

## 🚨 TROUBLESHOOTING

**Problem: "source is not recognized"**
- You tried to use Linux/Bash command in PowerShell
- Solution: Use `.\.venv\Scripts\Activate.ps1` instead

**Problem: "python: command not found"**
- Python isn't in your PATH
- Solution: Use `python3` instead of `python`
- Or reinstall Python and select "Add Python to PATH"

**Problem: Tests fail or don't run**
- Check you're in correct folder: should show `...python-calculator>`
- Run: `ls` to verify files exist
- Run: `python -m unittest discover -s src -v` from project root

---

## ✨ QUICK SUMMARY

Your project is **100% working**! Just run:

```powershell
cd "C:\Users\pedamaka\OneDrive - Cisco\Desktop\python-calculator"
python -m unittest discover -s src -v
```

**You'll see all 6 tests pass with ✅ OK status!**

