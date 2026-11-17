# 📚 PYTHON CALCULATOR - COMPLETE MASTER GUIDE

## ✅ PROJECT STATUS: COMPLETE & WORKING

Your Python Calculator project is **100% complete** with all files created and tests passing!

---

## 📁 PROJECT STRUCTURE

```
python-calculator/
├── .github/
│   └── workflows/
│       └── build.yaml              ✅ GitHub Actions CI/CD
├── src/
│   ├── calculator.py               ✅ Calculator function (4 operations)
│   └── test_calculator.py          ✅ 6 unit tests
├── .venv/                          (Virtual environment - optional)
├── .gitignore                      ✅ Git ignore rules
├── requirements.txt                ✅ Empty (uses stdlib only)
├── QUICK_START.md                  📖 Quick start guide
├── HOW_TO_RUN_TESTS.md             📖 Detailed test guide
└── FIX_VENV.md                     🔧 Virtual environment fix
```

---

## 🚀 QUICK START (3 Steps)

### Step 1: Open Terminal
Press `Ctrl + ` (backtick) in VS Code or Terminal > New Terminal

### Step 2: Navigate to Project
```powershell
cd "C:\Users\pedamaka\OneDrive - Cisco\Desktop\python-calculator"
```

### Step 3: Run Tests
```powershell
python -m unittest discover -s src -v
```

---

## ✅ EXPECTED OUTPUT

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
Ran 6 tests in 0.000s

OK ✅
```

---

## 🧮 CALCULATOR FUNCTIONS

The calculator supports 4 operations:

```python
from src.calculator import calculator

# Addition
calculator('add', 10, 5)        # → 15

# Subtraction
calculator('subtract', 10, 5)   # → 5

# Multiplication
calculator('multiply', 10, 5)   # → 50

# Division
calculator('divide', 10, 5)     # → 2.0

# Division by zero (raises error)
calculator('divide', 10, 0)     # → ValueError: Cannot divide by zero

# Invalid operation (raises error)
calculator('power', 2, 3)       # → ValueError: Unsupported operation: power
```

---

## 🧪 UNIT TESTS OVERVIEW

### Test Cases (6 total)

| Test Name | Purpose | Test Cases |
|-----------|---------|-----------|
| `test_addition` | Test addition operation | 5+3=8, -5+3=-2, 0+0=0 |
| `test_subtraction` | Test subtraction operation | 5-3=2, 3-5=-2, 0-0=0 |
| `test_multiplication` | Test multiplication operation | 5×3=15, -5×3=-15, 0×100=0 |
| `test_division` | Test division operation | 10÷2=5, 9÷3=3, 7÷2=3.5 |
| `test_division_by_zero` | Test error handling | 10÷0 raises ValueError ✓ |
| `test_invalid_operation` | Test error handling | power(2,3) raises ValueError ✓ |

---

## 📊 TEST OUTPUT TYPES

### Type 1: Verbose (Detailed)
```powershell
python -m unittest discover -s src -v
```
Shows: Each test name, description, and result

### Type 2: Simple
```powershell
python -m unittest discover -s src
```
Shows: Just dots (one per test) and summary

### Type 3: Single Test
```powershell
cd src
python -m unittest test_calculator.TestCalculator.test_addition -v
```
Shows: Only the specified test

---

## 🤖 GITHUB ACTIONS WORKFLOW

File: `.github/workflows/build.yaml`

**Triggers:**
- ✅ Every push to main branch
- ✅ Every pull request to main branch

**What it does:**
1. Checks out your code
2. Sets up Python 3.12
3. Installs dependencies from requirements.txt
4. Runs all tests with verbose output

**Expected result:**
- Green ✅ checkmark on GitHub Actions tab
- All 6 tests pass
- Build succeeds

---

## 🔧 VIRTUAL ENVIRONMENT (Optional)

### Create Virtual Environment
```powershell
python3 -m venv .venv
```

### Activate in PowerShell
```powershell
.\.venv\Scripts\Activate.ps1
```

If you get an error, run this ONCE:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Activate in Command Prompt
```cmd
.\.venv\Scripts\activate.bat
```

### Deactivate (exit venv)
```powershell
deactivate
```

**Note:** You DON'T need to activate the venv to run tests!

---

## 📤 PUSH TO GITHUB (Next Step)

### 1. Create Repository on GitHub
- Go to https://github.com/new
- Repository name: `python-calculator`
- Leave it empty (no README, .gitignore, or license)
- Click "Create repository"

### 2. Initialize and Push
```powershell
cd "C:\Users\pedamaka\OneDrive - Cisco\Desktop\python-calculator"

git init
git add .
git commit -m "Add calculator, unit tests, and CI workflow"
git branch -M main
git remote add origin https://github.com/<your-username>/python-calculator.git
git push -u origin main
```

Replace `<your-username>` with your actual GitHub username.

### 3. Verify on GitHub
1. Go to your repository on GitHub
2. Click the **Actions** tab
3. See the workflow run with ✅ green checkmark
4. Click "Run tests" step to see all tests passing

---

## 🧪 MANUAL TESTING (Without unittest)

### In Python Interactive Shell
```powershell
python
```

Then type:
```python
import sys
sys.path.insert(0, 'src')
from calculator import calculator

# Test each operation
print(calculator('add', 5, 3))        # 8
print(calculator('subtract', 10, 4))  # 6
print(calculator('multiply', 4, 5))   # 20
print(calculator('divide', 20, 4))    # 5.0

# Test error handling
try:
    calculator('divide', 10, 0)
except ValueError as e:
    print(f"Error: {e}")

exit()
```

---

## ❌ TROUBLESHOOTING

### Problem: "python: command not found"
```
Solution: Use python3 instead of python
OR reinstall Python and check "Add Python to PATH"
```

### Problem: "source is not recognized"
```
Solution: You're using Linux/Bash command in PowerShell
Use: .\.venv\Scripts\Activate.ps1 instead
```

### Problem: "ModuleNotFoundError: No module named 'calculator'"
```
Solution: Make sure you're in the project root directory
Run: ls (to verify files exist)
Then: python -m unittest discover -s src -v
```

### Problem: Execution policy error
```
Solution: Run this once:
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Then try to activate venv again
```

### Problem: Tests don't run
```
Check:
1. You're in C:\Users\pedamaka\OneDrive - Cisco\Desktop\python-calculator
2. Python is installed: python --version
3. Files exist: ls src/
4. Try: python -m unittest discover -s src -v
```

---

## 📋 COMMAND REFERENCE

| Task | Command |
|------|---------|
| Run all tests (verbose) | `python -m unittest discover -s src -v` |
| Run all tests (simple) | `python -m unittest discover -s src` |
| Run one test | `cd src && python -m unittest test_calculator.TestCalculator.test_addition -v` |
| Create venv | `python3 -m venv .venv` |
| Activate venv (PowerShell) | `.\.venv\Scripts\Activate.ps1` |
| Activate venv (Cmd) | `.\.venv\Scripts\activate.bat` |
| Exit venv | `deactivate` |
| Check Python version | `python --version` |
| List files | `ls` |
| Clear terminal | `cls` |

---

## 📊 WHAT YOU LEARNED

✅ Created a Python calculator function with error handling
✅ Wrote comprehensive unit tests covering all operations and edge cases
✅ Ran tests locally with verbose output
✅ Set up GitHub Actions CI/CD workflow
✅ Created project documentation
✅ Used virtual environments for Python projects
✅ Integrated automated testing with GitHub

---

## 🎓 KEY CONCEPTS

**Unit Testing:**
- Tests verify that functions work correctly
- One test per behavior/edge case
- Automated testing catches bugs early

**GitHub Actions:**
- Automatically runs tests on every push
- Ensures code quality before merge
- Visible status on repository

**Virtual Environments:**
- Isolate project dependencies
- Avoid conflicts between projects
- Reproducible across machines

**Error Handling:**
- ValueError for invalid operations
- Graceful handling of edge cases (division by zero)
- Clear error messages

---

## 📞 SUPPORT

For issues or questions:
1. Check the **FIX_VENV.md** file for virtual environment help
2. Check the **HOW_TO_RUN_TESTS.md** file for test running help
3. Check the **QUICK_START.md** file for quick reference
4. Review the error message carefully - it usually tells you the problem
5. Verify files exist: `ls` command lists all files

---

## ✨ NEXT STEPS

1. ✅ Verify tests pass locally (you just did this!)
2. ⬜ Push to GitHub (see instructions above)
3. ⬜ See workflow run on GitHub Actions tab
4. ⬜ Share your repository with others
5. ⬜ Extend calculator with more operations (optional)

---

**Project Location:** 
```
C:\Users\pedamaka\OneDrive - Cisco\Desktop\python-calculator
```

**Status:** ✅ **COMPLETE AND WORKING!**

**All 6 tests:** ✅ PASSING

Ready for GitHub! 🚀

