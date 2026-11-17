# 🚀 ONE-PAGE QUICK REFERENCE

## 📌 TO SEE TEST OUTPUT NOW

```powershell
cd "C:\Users\pedamaka\OneDrive - Cisco\Desktop\python-calculator"
python -m unittest discover -s src -v
```

**Expected Output:**
```
test_addition (test_calculator.TestCalculator.test_addition)
Test addition operation. ... ok
...
Ran 6 tests in 0.000s

OK ✅
```

---

## 📂 WHAT'S IN YOUR PROJECT

| File | Purpose |
|------|---------|
| `src/calculator.py` | Calculator with 4 operations (add, subtract, multiply, divide) |
| `src/test_calculator.py` | 6 unit tests (all passing) |
| `.github/workflows/build.yaml` | Automatic testing on GitHub |
| `.gitignore` | Ignores __pycache__ and .venv |
| `requirements.txt` | Empty (uses Python stdlib only) |

---

## 📚 DOCUMENTATION

| File | Purpose | Read When |
|------|---------|-----------|
| **README.md** | Documentation index | First! |
| **MASTER_GUIDE.md** | Complete reference (9000+ words) | Need full details |
| **QUICK_START.md** | 3-step setup | Need quick reference |
| **HOW_TO_RUN_TESTS.md** | Test commands & output examples | Running tests |
| **COPY_PASTE_COMMANDS.md** | Ready-to-paste terminal commands | Copy-pasting |
| **FIX_VENV.md** | Virtual environment help | Having issues |

---

## 🧪 ALL 6 TESTS STATUS

✅ test_addition - PASSED
✅ test_subtraction - PASSED
✅ test_multiplication - PASSED
✅ test_division - PASSED
✅ test_division_by_zero - PASSED (error handling)
✅ test_invalid_operation - PASSED (error handling)

---

## 🎯 COMMON COMMANDS

### Run Tests
```powershell
python -m unittest discover -s src -v        # Verbose
python -m unittest discover -s src            # Simple (just dots)
```

### Virtual Environment
```powershell
python3 -m venv .venv                         # Create
.\.venv\Scripts\Activate.ps1                  # Activate (PowerShell)
.\.venv\Scripts\activate.bat                  # Activate (Cmd)
deactivate                                    # Exit
```

### Push to GitHub
```powershell
git init
git add .
git commit -m "Add calculator, unit tests, and CI workflow"
git branch -M main
git remote add origin https://github.com/<username>/python-calculator.git
git push -u origin main
```

---

## 🔧 TROUBLESHOOTING

| Problem | Solution |
|---------|----------|
| "source is not recognized" | Use PowerShell or cmd.exe, not bash |
| "python: command not found" | Use `python3` or install Python |
| Execution policy error | Run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| Tests don't run | Make sure you're in the right directory |

---

## 📍 YOUR PROJECT LOCATION

```
C:\Users\pedamaka\OneDrive - Cisco\Desktop\python-calculator
```

---

## ✨ WHAT YOU BUILT

A complete Python calculator project with:
- ✅ 4 arithmetic operations
- ✅ 6 comprehensive unit tests
- ✅ Automatic error handling
- ✅ GitHub Actions CI/CD
- ✅ Virtual environment
- ✅ Full documentation

**Status: COMPLETE & WORKING!** 🎉

---

**Next Step: Run the first command above to see all tests pass!** 👆

