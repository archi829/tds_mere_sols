# Dependency Updates & Security Automation

## What is Dependabot?

**Dependabot** is GitHub’s native tool for automated dependency management. It scans your repository for outdated or vulnerable dependencies and automatically creates pull requests to update them. It supports major ecosystems like npm, pip, Maven, Gradle, Docker, and more.

**Why use it?**

* Automated version bumps & security patches
* Native GitHub integration (no extra infra)
* Pull-request–based workflow
* Alerts via GitHub Security Advisories

---

## Popular Modern Alternatives

* **Renovate** – Highly configurable, 30+ package managers, monorepo-friendly, multi-platform (GitHub/GitLab/Azure).
* **Snyk** – Deep vulnerability analysis + automated fixes across dependencies, containers, and IaC.
* **Aikido** – Context-aware security scanning with fewer false positives.
* **Socket.dev / FOSSA** – Supply-chain risk & license compliance focus.

---

## Decision Tree: What Should You Use?

```
Do you use GitHub only with simple repos?
├── Yes → Dependabot (zero-setup, native)
└── No →
    Need multi-platform (GitLab/Azure/Bitbucket)?
    ├── Yes → Renovate
    └── No →
        Monorepo or many ecosystems?
        ├── Yes → Renovate
        └── No →
            Strong vulnerability/security focus?
            ├── Yes → Snyk / Aikido
            └── No → Dependabot
```

**Rule of thumb**

* Small/medium GitHub repo → Dependabot
* Monorepo / polyglot stack → Renovate
* Security-first org → Snyk/Aikido

---

## Common Dependabot Customization Scenarios

Teams customize Dependabot mainly to reduce PR noise and align with CI/CD workflows.

### 1) Group updates (noise reduction)

Bundle multiple minor/patch updates into one PR.

```yaml
groups:
  minor-and-patch:
    patterns: ["*"]
    update-types: ["minor", "patch"]
```

### 2) CI/CD labeling & auto-assignment

Trigger workflows or route reviews automatically.

```yaml
labels: ["dependencies", "security"]
assignees: ["@org/security-team"]
```

### 3) Scheduled updates (off-hours)

Run updates weekly at low-traffic times.

```yaml
schedule:
  interval: "weekly"
  day: "sunday"
  time: "02:00"
  timezone: "UTC"
```

### 4) Ignore problematic deps

Avoid breaking updates or pinned libs.

```yaml
ignore:
  - dependency-name: "tensorflow"
  - dependency-name: "react"
    versions: ["19.x"]
```

### 5) Limit open PRs

Prevent PR floods in large repos.

```yaml
open-pull-requests-limit: 5
```

---

## Example `.github/dependabot.yml`

```yaml
version: 2

updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
      day: "sunday"
      time: "02:00"
      timezone: "UTC"
    labels: ["dependencies"]
    assignees: ["@org/devs"]
    open-pull-requests-limit: 5
    groups:
      minor-and-patch:
        patterns: ["*"]
        update-types: ["minor", "patch"]
    ignore:
      - dependency-name: "react"
        versions: ["19.x"]

  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
```

---

## When to Consider Alternatives

* Many repos / monorepos → Renovate
* Multiple platforms → Renovate
* Compliance / SBOM / vuln depth → Snyk / Aikido / FOSSA
* Supply-chain risk analysis → Socket.dev

---

**Summary:**
Dependabot is the simplest and best default for GitHub-centric projects. Customize it mainly for grouping, scheduling, and CI integration. Move to Renovate or security-focused tools when scale or security depth increases.

---

