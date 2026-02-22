## 2)
## Remove `.env` from Git History (Secrets Cleanup)

**Goal:**
Identify when `.env` (containing secrets) was added, remove it from the entire Git history, prevent future tracking, and push the cleaned repository to GitHub.

---

### 1️⃣ Find the commit that added `.env`

```bash
git log --diff-filter=A -- .env
```

**Why:** Shows commits where `.env` was first introduced (`A` = Added).

---

### 2️⃣ Remove `.env` from all history

```bash
uvx git-filter-repo --force --path .env --invert-paths
```

**Why:** Rewrites history to delete `.env` from every commit.

* `--path .env` → target file
* `--invert-paths` → remove instead of keep
* `--force` → allow non-fresh clone

---

### 3️⃣ Verify `.env` is fully gone

```bash
git log --all -- .env
git rev-list --all -- .env
```

**Why:** Confirms no commits reference `.env`.

---

### 4️⃣ Prevent future commits of secrets

Create `.gitignore`:

```
.env
```

Create `.env.example`:

```
API_KEY=your_api_key_here
DB_PASSWORD=your_db_password_here
```

---

### 5️⃣ Commit safe config files

```bash
git add .gitignore .env.example
git commit -m "Add .gitignore and .env.example; stop tracking secrets"
```

**Why:** Keeps template config while ignoring real secrets.

---

### 6️⃣ Add remote & force push rewritten history

```bash
git remote add origin https://github.com/<your-username>/<repo>.git
git push origin --force --all
git push origin --force --tags
```

**Why:** Uploads cleaned history (force required after rewrite).

---

### ✅ Result

* `.env` removed from entire Git history
* Secrets no longer exposed
* `.env` ignored going forward
* Example template provided
* Clean repo pushed to GitHub

**Repository URL:**
`https://github.com/archi829/tds-ga2-2-revert-env-commit.git`


# 3)
# 5) Host a JSON Data API on GitHub Pages
