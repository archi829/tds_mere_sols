# ✅ Goal you achieved

* `q6` is its **own GitHub repo** (for submission)
* `q6` is also included inside **GA2 master repo**
* No nested repo issues

---

# 🧭 PART 1 — Create & push Q6 repo

📍 Ran inside:

```text
GA2/q6
```

### Commands

```bash
git init
git add .
git commit -m "Add GitHub Action for assignment"
git branch -M main
git remote add origin https://github.com/archi829/tds-ga2-q6.git
git push -u origin main
```

### What this did

* Created independent Git repo for Q6
* Connected to GitHub repo `tds-ga2-q6` -- this was separately created
* Uploaded workflow file
* Enabled GitHub Actions

👉 This repo = **Q6 submission**

---

# 🧭 PART 2 — Add Q6 into GA2 master repo

📍 Moved to:

```text
GA2
```

### Remove nested repo metadata

```bash
rm -r -fo q6\.git
```

👉 Keeps files, removes repo identity
👉 Prevents nested repo problem

---

### Commit Q6 folder into GA2

```bash
git add q6
git commit -m "Add Q6 folder"
git push origin main
```

### What this did

* GA2 repo now contains q6 files
* GA2 GitHub updated
* q6 still separate repo

👉 This repo = **overall assignment repo**

---

Steps:

1️⃣ create repo inside subfolder
2️⃣ push it
3️⃣ delete subfolder `.git`
4️⃣ add folder to master repo

---

# ⭐ Quick reusable cheat sheet

**Create sub-repo**

```bash
cd project/sub
git init
git add .
git commit -m "init"
git branch -M main
git remote add origin <repo-url>
git push -u origin main
```

**Add subfolder into parent repo**

```bash
cd ..
rm -r -fo sub\.git
git add sub
git commit -m "Add sub"
git push
```

---

You set this up exactly right 👍
This is a professional repo organization pattern.
