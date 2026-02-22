# Q12: GitHub Gist Hosting

GitHub Gist is a lightweight tool for sharing and managing code snippets or small sets of files as mini Git repositories. It suits quick sharing of scripts, configs, or notes without a full repo setup.

Core Functionality
Gists let you create public (discoverable/searchable) or secret (unlisted but accessible via direct link) snippets online via the web, API, or CLI. They're full Git repos, so you can clone (git clone https://gist.github.com/[id].git), fork, edit with version history, and push changes.
​

Supports multiple files, Markdown rendering, syntax highlighting, and embedding.

Edit via web (update button), CLI (after cloning), or API for automation.
​

Key Limitations
File size caps at 100 MB total per gist (25 MB via web UI); aim under 5 GB equivalent for performance, though no hard repo limit exists. No folders (flat structure only), no issues/projects/wiki, and secret gists aren't truly private—anyone with the link sees them.

Common Gotchas
Web uploads fail on large files; clone and Git-push instead. High file counts (e.g., 50k tiny files) may slow performance despite fitting limits—organize efficiently or use LFS for big binaries. API is rate-limited; not ideal as a "database" for heavy CRUD.

## Task

Host a file on **GitHub Gist** that showcases your work and includes your email address in the page's HTML.


## Instructions

1.  **Open GitHub Gist**
    *   Go to [https://gist.github.com/](https://gist.github.com/)
    *   Log in to your GitHub account.

2.  **Create New Gist**
    *   **Gist Description**: `23f3001889@ds.study.iitm.ac.in`
    *   **Filename**: `index.html`
    *   **Content**: ` <html>
  <p>23f3001889@ds.study.iitm.ac.in</p>
</html>`

3.  **Publish**
    *   Click **Create public gist**.

4.  **Get URL**
    *   Copy the URL from your browser address bar.
    *   Format: `https://gist.github.com/[YOUR_USERNAME]/[GIST_ID]`