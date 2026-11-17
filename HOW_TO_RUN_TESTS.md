# 🖥️ How to See Test Output in Terminal

## Method 1: Using VS Code Terminal (Recommended)

### Step 1: Open Terminal in VS Code
```
Press: Ctrl + ` (backtick)
```
Or:
```
Menu: Terminal > New Terminal
```

### Step 2: Navigate to Project Folder (if not already there)
```powershell
cd "C:\Users\pedamaka\OneDrive - Cisco\Desktop\python-calculator"
```

### Step 3: Run Tests
```powershell
python -m unittest discover -s src -v
```

---

## ✅ Expected Output

```
test_addition (test_calculator.TestCalculator.test_addition)
Test addition operation. ... ok

test_subtraction (test_calculator.TestCalculator.test_subtraction)
Test subtraction operation. ... ok

test_multiplication (test_calculator.TestCalculator.test_multiplication)
Test multiplication operation. ... ok

test_division (test_calculator.TestCalculator.test_division)
Test division operation. ... ok

test_division_by_zero (test_calculator.TestCalculator.test_division_by_zero)
Test that division by zero raises ValueError. ... ok

test_invalid_operation (test_calculator.TestCalculator.test_invalid_operation)
Test that invalid operation raises ValueError. ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.002s

OK
```

---

## 📊 Other Useful Commands

### Run Tests Without Verbose Output
```powershell
python -m unittest discover -s src
```

Output:
```
......
------
Ran 6 tests in 0.001s

OK
```

### Run Only Tests from Specific File
```powershell
python -m unittest src.test_calculator -v
```

### Run Specific Test Method
```powershell
python -m unittest src.test_calculator.TestCalculator.test_addition -v
```

Output:
```
test_addition (test_calculator.TestCalculator.test_addition)
Test addition operation. ... ok
------
Ran 1 test in 0.001s

OK
```

### Run Tests and Show Failures (if any)
```powershell
python -m unittest discover -s src -v 2>&1
```

---

## 🔧 Test Individual Functions Manually

```powershell
python
```

Then in Python shell:
```python
>>> from src.calculator import calculator
>>> calculator('add', 5, 3)
8
>>> calculator('subtract', 10, 4)
6
>>> calculator('multiply', 4, 5)
20
>>> calculator('divide', 20, 4)
5.0
>>> calculator('divide', 10, 0)
ValueError: Cannot divide by zero
>>> exit()
```

---

## 📋 Terminal Layout Tips

### Split Terminal View (VS Code)
1. Click the split terminal icon in top-right of terminal
2. Run different commands in each pane

### Clear Terminal
```powershell
cls
```

### See Last Test Run Again
```powershell
cls; python -m unittest discover -s src -v
```

---

## ✨ Creating a Shortcut Command in Terminal

You can create a PowerShell profile to run tests quickly:

```powershell
# Add to PowerShell profile
function test { python -m unittest discover -s src -v }
```

Then just type:
```powershell
test
```

---

## 🎯 Summary

| Command | Purpose |
|---------|---------|
| `python -m unittest discover -s src -v` | Run all tests (verbose) |
| `python -m unittest discover -s src` | Run all tests (simple) |
| `python -m unittest src.test_calculator -v` | Run specific test file |
| `python -m unittest src.test_calculator.TestCalculator.test_addition -v` | Run single test |
| `python` | Enter Python shell for manual testing |
| `cls` | Clear terminal |

---

## 🚀 Next: Push to GitHub and See Workflow Output

Once you push to GitHub, you can see automated test output:

```powershell
git push -u origin main
```

Then:
1. Go to your repository on GitHub
2. Click the **Actions** tab
3. Click the latest workflow run
4. Click the **Run tests** step to see the output

