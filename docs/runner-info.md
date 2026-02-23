# GitHub Actions Runner: imprunner

> **Document purpose:** This file is intended to be consumed by AI systems and human operators alike.
> It contains all statically available information about the self-hosted runner `imprunner` in the
> repository `Impulsleistung/T9-CTN-GenAI`, extracted on 2026-02-23.

---

## 1. Runner Identity

| Property | Value |
|---|---|
| **Name** | `imprunner` |
| **Type** | Self-hosted |
| **Runner ID** | 2 |
| **Repository** | `Impulsleistung/T9-CTN-GenAI` |
| **Settings URL** | `https://github.com/Impulsleistung/T9-CTN-GenAI/settings/actions/runners/2` |
| **Last observed status** | Idle (online, no active job) |
| **Extracted on** | 2026-02-23 13:00 CET |

---

## 2. Platform Configuration

| Property | Value |
|---|---|
| **OS** | Linux |
| **Architecture** | x64 |
| **Configuration string** | `Linux x64` |

---

## 3. Runner Labels

Labels are used in workflow YAML via the `runs-on:` key to route jobs to this runner.

| Label | Source |
|---|---|
| `self-hosted` | Built-in (always present on self-hosted runners) |
| `Linux` | Built-in (set automatically based on OS) |
| `X64` | Built-in (set automatically based on architecture) |

### How to target this runner in a workflow

```yaml
# Option 1 - by runner name (most specific)
runs-on: imprunner

# Option 2 - by labels (matches any self-hosted Linux x64 runner)
runs-on: [self-hosted, Linux, X64]
```

---

## 4. Workflow Usage

This runner is referenced by the following workflow files in `.github/workflows/`:

### 4.1 `ci.yml` — CI Workflow

- **Workflow name:** `CI`
- **File:** `.github/workflows/ci.yml` (222 lines, 6.85 KB)
- **Triggers:**
  - `push` to branch `main`
  - `pull_request` targeting branch `main`
  - `workflow_dispatch` (manual trigger)
- **Permissions:**
  - `contents: read`
  - `pull-requests: write`
  - `statuses: write`
- **Jobs using this runner:**

#### Job: `diagnostics`
- `runs-on: imprunner`
- **Purpose:** Collect and report runner environment information
- **Steps:**
  1. `System Information` — prints hostname, OS (`uname -a`), `/etc/os-release`
  2. `CPU and Memory` — prints CPU core count, CPU model from `/proc/cpuinfo`, `free -h`
  3. `Docker Information` — checks if Docker is installed, prints version and `docker info`
  4. `Python Information` — checks for `python3` or `python`, prints version and path
  5. `Git Information` — prints git version and first 10 lines of `git config --list`
  6. `Available Tools` — checks presence of: `node`, `npm`, `pip`, `pip3`, `docker`, `kubectl`, `curl`, `wget`
  7. `Disk Space` — runs `df -h`
  8. `Environment Variables` — prints `$PATH` entries and key vars: `RUNNER_OS`, `RUNNER_ARCH`, `GITHUB_REPOSITORY`, `GITHUB_RUN_ID`
  9. `Create Issue with Diagnostics` _(only on `workflow_dispatch`)_ — creates a GitHub Issue with the collected diagnostics

#### Job: `ci`
- `runs-on: imprunner`
- **Depends on:** `diagnostics` (runs after)
- **Purpose:** Lint and test the Python codebase
- **Steps:**
  1. `Checkout repository` — `actions/checkout@v4`
  2. `Set up Python` — `actions/setup-python@v5`, Python version `3.11`, pip cache enabled
  3. `Install dependencies` — upgrades pip, installs `flake8` and `pytest`, installs `requirements.txt` if present
  4. `Lint with flake8` — stops on syntax errors / undefined names; treats all other errors as warnings (max complexity 10, max line length 127)
  5. `Run tests with pytest` — runs `pytest --tb=short -v`; tolerates no-test scenario

---

## 5. Workflow Run History (as of 2026-02-23)

| Run # | Event | Branch | Status | Duration |
|---|---|---|---|---|
| CI #6 | push (commit `6bc3ee1`) | `main` | Queued | — |
| CI #5 | pull_request sync | `ci/improve-workflow` | Queued | — |
| CI #4 | pull_request sync | `ci/improve-workflow` | Queued | — |
| CI #3 | pull_request sync | `ci/improve-workflow` | Queued | — |
| CI #2 | pull_request sync | `ci/improve-workflow` | Cancelled | 3m 24s |
| CI #1 | pull_request open | `ci/improve-workflow` | Cancelled | 3m 43s |

> **Note:** All completed runs were cancelled before job execution. No successful diagnostic
> output has been captured yet. Queued runs are waiting for the runner to pick them up.
> The runner is currently **Idle** (online and ready to accept jobs).

---

## 6. Security & Permissions Context

| Setting | Value |
|---|---|
| **Workflow default token permissions** | Read and write |
| **Actions can create pull requests** | Yes (enabled) |
| **Branch ruleset on `main`** | `main-security` (Active) |
| **Ruleset: restrict deletions** | Enabled |
| **Ruleset: require PR before merge** | Enabled — 1 approval required |
| **Ruleset: block force pushes** | Enabled |
| **Ruleset: require code scanning (CodeQL)** | Enabled — High severity and above |
| **Ruleset: require code quality results** | Enabled — Errors must be resolved |

> The runner itself has no special security restrictions beyond the repository-level settings above.
> It runs as a self-hosted process with whatever OS-level permissions the service account has.

---

## 7. Key Facts for AI Consumption

- The runner name is `imprunner` and can be targeted directly with `runs-on: imprunner`.
- It is a **self-hosted Linux x64** machine — it is NOT a GitHub-hosted runner.
- No Docker-in-Docker or cloud metadata is guaranteed; capabilities depend on the host machine.
- The `diagnostics` job in `ci.yml` is specifically designed to probe and report the runner's
  actual software environment (Python, Docker, Git, Node, kubectl, curl, wget, disk, memory).
- The `GITHUB_TOKEN` has **read+write** permissions and is allowed to create pull requests.
- Jobs cannot be merged into `main` without a PR, 1 approval, and passing CodeQL scans.
- The runner was observed as **Idle** at the time of extraction — it is online and ready.

---

*This file was auto-generated by AI assistant on 2026-02-23 based on the GitHub repository settings,
workflow files, and Actions run history of `Impulsleistung/T9-CTN-GenAI`.*
