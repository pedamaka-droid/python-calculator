# 📋 COPY-PASTE TERMINAL COMMANDS

**Simply copy and paste these commands into your VS Code terminal!**

---

## 🎯 IMMEDIATE: See Test Output (DO THIS NOW!)

### Copy the entire block below and paste into terminal:

```powershell
cd "C:\Users\pedamaka\OneDrive - Cisco\Desktop\python-calculator"
python -m unittest discover -s src -v
```

**Expected output:**
```
test_addition (test_calculator.TestCalculator.test_addition)
Test addition operation. ... ok
test_division (test_calculator.TestCalculator.test_division)
...
Ran 6 tests in 0.000s

OK
```

---

## 📊 ALTERNATIVE COMMANDS

### See Simple Output (Just Dots)
```powershell
cd "C:\Users\pedamaka\OneDrive - Cisco\Desktop\python-calculator"
python -m unittest discover -s src
```

### Run Single Test
```powershell
cd "C:\Users\pedamaka\OneDrive - Cisco\Desktop\python-calculator\src"
python -m unittest test_calculator.TestCalculator.test_addition -v
cd ..
```

### Manual Testing (Interactive Python)
```powershell
cd "C:\Users\pedamaka\OneDrive - Cisco\Desktop\python-calculator"
python
```

Then in Python shell type:
```python
import sys
sys.path.insert(0, 'src')
from calculator import calculator
print(calculator('add', 5, 3))
print(calculator('multiply', 4, 5))
exit()
```

---

## 🔧 SETUP VIRTUAL ENVIRONMENT

### Create Virtual Environment
```powershell
cd "C:\Users\pedamaka\OneDrive - Cisco\Desktop\python-calculator"
python3 -m venv .venv
```

### Activate in PowerShell
```powershell
.\.venv\Scripts\Activate.ps1
```

**If you get an error, run this ONCE:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try activation again:
```powershell
.\.venv\Scripts\Activate.ps1
```

### Deactivate (Exit Virtual Environment)
```powershell
deactivate
```

---

## 📤 PUSH TO GITHUB (Next Step)

### Step 1: Create Repository
Go to: https://github.com/new
- Repository name: `python-calculator`
- Leave empty (no README, .gitignore, or license)
- Click "Create repository"

### Step 2: Copy and Paste These Commands

Replace `<your-username>` with your GitHub username, then paste:

```powershell
cd "C:\Users\pedamaka\OneDrive - Cisco\Desktop\python-calculator"
git init
git add .
git commit -m "Add calculator, unit tests, and CI workflow"
git branch -M main
git remote add origin https://github.com/<your-username>/python-calculator.git
git push -u origin main
```

**Example with actual username:**
```powershell
cd "C:\Users\pedamaka\OneDrive - Cisco\Desktop\python-calculator"
git init
git add .
git commit -m "Add calculator, unit tests, and CI workflow"
git branch -M main
git remote add origin https://github.com/pedamaka/python-calculator.git
git push -u origin main
```

### Step 3: Verify on GitHub
1. Go to your repository on GitHub
2. Click "Actions" tab
3. See the workflow running with ✅ green checkmark

---

## 🧪 VERIFY FILES EXIST

```powershell
cd "C:\Users\pedamaka\OneDrive - Cisco\Desktop\python-calculator"
ls
ls src/
ls .github/workflows/
```

Should show:
- `src/calculator.py`
- `src/test_calculator.py`
- `.github/workflows/build.yaml`
- `requirements.txt`
- `.gitignore`

---

## 🔍 CHECK PYTHON VERSION

```powershell
python --version
```

Should output: `Python 3.10.x` or higher

---

## ❌ TROUBLESHOOTING COMMANDS

### Check if Python is installed
```powershell
python --version
```

### Check if Git is installed
```powershell
git --version
```

### Clear Terminal
```powershell
cls
```

### List Current Directory
```powershell
ls
```

### Navigate Back One Folder
```powershell
cd ..
```

### Check Current Path
```powershell
pwd
```

---

## 📌 MOST IMPORTANT COMMANDS

**#1 - See All Tests Pass (run this!):**
```powershell
cd "C:\Users\pedamaka\OneDrive - Cisco\Desktop\python-calculator"
python -m unittest discover -s src -v
```

**#2 - Push to GitHub:**
```powershell
cd "C:\Users\pedamaka\OneDrive - Cisco\Desktop\python-calculator"
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<your-username>/python-calculator.git
git push -u origin main
```

**#3 - Activate Virtual Environment:**
```powershell
.\.venv\Scripts\Activate.ps1
```

---

## ✨ QUICK REFERENCE TABLE

| What You Want | Command |
|---------------|---------|
| Run all tests (verbose) | `python -m unittest discover -s src -v` |
| Run all tests (simple) | `python -m unittest discover -s src` |
| Run one test | `cd src && python -m unittest test_calculator.TestCalculator.test_addition -v` |
| Create venv | `python3 -m venv .venv` |
| Activate venv | `.\.venv\Scripts\Activate.ps1` |
| Exit venv | `deactivate` |
| Check Python | `python --version` |
| Check Git | `git --version` |
| List files | `ls` |
| Clear terminal | `cls` |
| Go up one folder | `cd ..` |
| View current path | `pwd` |

---

**Ready to run? Copy the first command and paste it now! 🚀**

