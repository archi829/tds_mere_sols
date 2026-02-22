# ✅ Recommended workflow for ALL future questions

## Step A — create question folder in GA2

```bash
cd GA2
mkdir q7
cd q7
```

---

## Step B — make it its own repo, (for each q, create a new repo also : <Q7 repo url>)

```bash
git init
git add .
git commit -m "Q7 init"
git branch -M main
git remote add origin <Q7 repo url>
git push -u origin main
```

---

## Step C — integrate into GA2

```bash
cd ..
rm -r -fo q7\.git
git add q7
git commit -m "Add Q7"
git push
```
