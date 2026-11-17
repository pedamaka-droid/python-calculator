# 🔧 How to Activate .venv Virtual Environment

## 🎯 THE CORRECT COMMAND (PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
```

**That's it!** No `source` command needed on Windows PowerShell.

---

## 📋 STEP-BY-STEP INSTRUCTIONS

### Step 1: Navigate to Project
```powershell
cd "C:\Users\pedamaka\OneDrive - Cisco\Desktop\python-calculator"
```

### Step 2: Activate Virtual Environment
```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 3: Success!
You should see this in your terminal:
```
(.venv) PS C:\Users\pedamaka\OneDrive - Cisco\Desktop\python-calculator>
```

Notice the `(.venv)` prefix! That means it's activated.

---

## ⚠️ IF YOU GET AN ERROR

If you see this error:
```
.\.venv\Scripts\Activate.ps1 : File ... cannot be loaded because running 
scripts is disabled on this system.
```

**Run this command ONCE:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try activation again:
```powershell
.\.venv\Scripts\Activate.ps1
```

---

## ✅ AFTER ACTIVATION

Your prompt will show `(.venv)` at the start.

Now you can:
- Run tests: `python -m unittest discover -s src -v`
- Exit venv: `deactivate`
- Install packages: `pip install <package-name>`

---

## 🔄 ALTERNATIVE: Use Command Prompt Instead

If PowerShell keeps giving you trouble, use Command Prompt (cmd.exe):

```cmd
cd "C:\Users\pedamaka\OneDrive - Cisco\Desktop\python-calculator"
.\.venv\Scripts\activate.bat
```

This doesn't require any execution policy changes!

---

## 📊 QUICK REFERENCE TABLE

| Platform | Shell | Command |
|----------|-------|---------|
| **Windows** | PowerShell | `.\.venv\Scripts\Activate.ps1` |
| **Windows** | Command Prompt | `.\.venv\Scripts\activate.bat` |
| **Windows** | Git Bash | `source .venv/Scripts/activate` |
| **Linux/Mac** | Bash/Zsh | `source .venv/bin/activate` |

---

## ✨ IMPORTANT NOTES

✅ You **DON'T** need to activate the venv to run tests!

You can always run tests without activation:
```powershell
python -m unittest discover -s src -v
```

The venv is mainly useful for:
- Installing packages with `pip`
- Keeping project dependencies isolated
- Avoiding conflicts with other projects

---

## 🚀 QUICK COPY-PASTE

### PowerShell (Best for learning)
```powershell
cd "C:\Users\pedamaka\OneDrive - Cisco\Desktop\python-calculator"
.\.venv\Scripts\Activate.ps1
```

### Command Prompt (Easiest)
```cmd
cd "C:\Users\pedamaka\OneDrive - Cisco\Desktop\python-calculator"
.\.venv\Scripts\activate.bat
```

### If Execution Policy Error
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\.venv\Scripts\Activate.ps1
```

---

## ❌ DON'T USE THESE (They're for Linux/Bash)

- `source .\.venv\Scripts\activate` ❌
- `source .venv\Scripts\activate` ❌
- Bash commands in PowerShell won't work!

---

**Most Important:** Use `.\.venv\Scripts\Activate.ps1` in PowerShell!

