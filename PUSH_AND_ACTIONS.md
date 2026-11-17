# 🚀 Git Push & GitHub Actions - Complete Commands

## 📤 STEP 1: Push Code to GitHub

**Copy and paste all these commands one by one:**

```powershell
cd "C:\Users\pedamaka\OneDrive - Cisco\Desktop\python-calculator"

git init

git branch -M main

git add .

git status

git commit -m "Add calculator, unit tests, and CI workflow" -m "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"

git remote add origin https://github.com/YOUR_USERNAME/python-calculator.git

git push -u origin main
```

**⚠️ IMPORTANT:** Replace `YOUR_USERNAME` with your GitHub username!
- Example: `https://github.com/pedamaka-droid/python-calculator.git`

---

## 📋 What Each Command Does

| Command | Purpose |
|---------|---------|
| `cd "C:\Users\pedamaka\OneDrive - Cisco\Desktop\python-calculator"` | Navigate to project |
| `git init` | Initialize Git repository |
| `git branch -M main` | Set main as default branch |
| `git add .` | Stage all files |
| `git status` | View files to commit |
| `git commit -m "..."` | Create commit with message |
| `git remote add origin https://...` | Connect to GitHub |
| `git push -u origin main` | Upload to GitHub |

---

## ✅ STEP 2: Verify Push Success

After `git push`, you should see:
```
Enumerating objects: X, done.
Counting objects: X%, done.
Writing objects: X%, done.
Total X (delta X), reused 0 (delta 0)
remote: Resolving deltas: 100% (X/X), done.
To https://github.com/pedamaka-droid/python-calculator.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

---

## 🔍 STEP 3: View GitHub Actions Workflow

1. **Open GitHub:**
   ```
   https://github.com/YOUR_USERNAME/python-calculator
   ```

2. **Click "Actions" tab** (top of page)

3. **Watch workflow run:**
   - 🟡 Yellow = Running
   - ✅ Green = Passed
   - ❌ Red = Failed

---

## 📊 STEP 4: View Test Output

1. Click on the workflow run
2. Click "test" job
3. Click "Run tests" step
4. See all 6 tests: `OK ✅`

**Expected output:**
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

## 🔄 STEP 5: Push Again (Future Updates)

To push changes again:

```powershell
git add .
git commit -m "Your message here"
git push
```

GitHub Actions will run automatically! No need to repeat the full setup.

---

## 🔗 Quick Links

| Link | Purpose |
|------|---------|
| `https://github.com/pedamaka-droid/python-calculator` | Your repository |
| `https://github.com/pedamaka-droid/python-calculator/actions` | GitHub Actions tab |
| `https://github.com/settings/tokens` | GitHub tokens (if needed) |

---

## ❓ Troubleshooting

| Problem | Solution |
|---------|----------|
| "No such file or directory" | Check path and cd to project first |
| "fatal: not a git repository" | Run `git init` first |
| "refused to merge unrelated histories" | Use `git pull origin main --allow-unrelated-histories` |
| Actions tab is empty | Make sure you pushed to `main` branch |
| Tests show ❌ Failed | Click workflow to see error details |

---

## ✨ Success Indicators

- ✅ Code appears on GitHub
- ✅ Actions tab shows workflow
- ✅ Workflow has green checkmark
- ✅ All 6 tests show "ok"
- ✅ Output ends with "OK ✅"

**YOU'RE DONE! 🎉**

