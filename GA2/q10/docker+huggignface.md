## 📦 Hugging Face Spaces — Concise README

### ❓ What is Hugging Face Spaces?

**Hugging Face Spaces** is a zero-infra platform to host and share interactive ML demos and apps.
It supports **Gradio**, **Streamlit**, and **Docker** deployments, making it ideal for rapid prototyping and public sharing.

---

## 🚀 Popular Alternatives

| Platform            | Strengths                       | Free Tier        | Pricing | Best For             |
| ------------------- | ------------------------------- | ---------------- | ------- | -------------------- |
| **Gradio.app**      | Python-first, simple UI sharing | Generous         | $0      | Quick demos          |
| **Streamlit Cloud** | Dashboards, data viz            | 1 GB RAM, public | $8/mo   | Data apps            |
| **Replicate**       | Serverless inference            | Credits          | Usage   | Production APIs      |
| **BentoML**         | Docker APIs, open-source        | Self-host        | —       | Enterprise/self-host |
| **Northflank**      | Full-stack cloud deploy         | Trial            | $20/mo  | Secure scaling       |
| **Google Colab**    | Notebooks, free GPUs            | 12 hr            | $0      | Research             |

---

## 🌳 Decision Tree — What to Use When

* **Need permanent public ML demo?** → **Hugging Face Spaces**
* **Temporary experiments / notebooks?** → **Google Colab**
* **Dashboard-style apps / viz?** → **Streamlit Cloud**
* **Production inference APIs?**

  * Pay-per-use → **Replicate**
  * Self-host infra → **BentoML / Northflank**
* **Gradio-only simple UI?** → **Gradio.app**

👉 Typical ML workflow:
**Spaces/Gradio (prototype) → Replicate (API) → Northflank/BentoML (scale)**

---

# 🐳 Docker in Hugging Face Spaces

### How it Works

* Add a **Dockerfile** to your Space repo.
* Push to `main` → Hugging Face builds & deploys container.
* Image hosted at:
  `registry.hf.space/<user>-<space>:latest`
* Can run locally after HF login (`docker pull`).

---

## ⚠️ Key Limitations

* Containers run as **non-root (UID 1000)** → must set:

  ```dockerfile
  USER user
  WORKDIR $HOME/app
  COPY --chown=user .
  ```
* **No volume mounts** → bundle assets into image.
* **Hardware caps (free tier)** → limited CPU/RAM/disk.
* **Auto-sleep** after inactivity.
* **Private Spaces** require HF auth to pull images.

---

## 🧠 Gotchas for Developers

* Set `USER` **before** pip/COPY → avoid permission errors.
* Test file ownership locally.
* Secrets available as env vars at runtime.
* Container restarts on wake (stateless).

---
