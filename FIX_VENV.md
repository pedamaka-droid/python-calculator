# 🔧 FIX: Virtual Environment Activation in PowerShell

## ❌ PROBLEM YOU FACED

You tried to activate the virtual environment like this:
```powershell
source .\.venv\Scripts\activate
```

**Error:**
```
source : The term 'source' is not recognized as the name of a cmdlet, function, script file, or operable program.
```

---

## ✅ SOLUTION

The `source` command is for **Linux/Bash**, not PowerShell!

In **PowerShell**, use:
```powershell
.\.venv\Scripts\Activate.ps1
```

---

## 🚨 If Activation Still Fails

You might get this error:
```
.\.venv\Scripts\Activate.ps1 : File ... cannot be loaded because running scripts is disabled on this system.
```

**Fix: Run this ONE TIME (as Administrator):**

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

This allows PowerShell scripts to run. Then activate:
```powershell
.\.venv\Scripts\Activate.ps1
```

---

## ✅ AFTER ACTIVATION

Your terminal prompt will change to:
```
(.venv) PS C:\Users\pedamaka\OneDrive - Cisco\Desktop\python-calculator>
```

Notice the `(.venv)` prefix! That means you're in the virtual environment.

---

## 🧪 NOW RUN TESTS

Once activated, run:
```powershell
python -m unittest discover -s src -v
```

Output:
```
test_addition (test_calculator.TestCalculator.test_addition)
Test addition operation. ... ok
test_division (test_calculator.TestCalculator.test_division)
...
Ran 6 tests in 0.000s

OK
```

---

## 📋 QUICK REFERENCE

| Command | Purpose | Platform |
|---------|---------|----------|
| `.\.venv\Scripts\Activate.ps1` | Activate venv | PowerShell |
| `.\.venv\Scripts\activate.bat` | Activate venv | Command Prompt (cmd) |
| `source .venv/Scripts/activate` | Activate venv | Linux/Mac/Git Bash |
| `deactivate` | Exit venv | All platforms |

---

## 🎯 ALTERNATIVE: RUN TESTS WITHOUT VENV

You DON'T need to activate the venv to run tests! Just run:

```powershell
cd "C:\Users\pedamaka\OneDrive - Cisco\Desktop\python-calculator"
python -m unittest discover -s src -v
```

**This works immediately without any activation!**

---

## 💡 WHY USE A VIRTUAL ENVIRONMENT?

Virtual environments are good for:
- ✅ Isolating project dependencies
- ✅ Avoiding conflicts between projects
- ✅ Easy dependency management with pip
- ✅ Reproducible environments across machines

For this simple project (no external dependencies), you can skip it.

