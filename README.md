# T9-CTN-GenAI

This repository contains the T9-CTN-GenAI project - a CI/CD pipeline using imprunner self-hosted Linux X64 runner.

## CI Workflow

This project uses GitHub Actions for continuous integration. The workflow is defined in `.github/workflows/ci.yml`.

### Trigger Conditions
- **Push**: Runs on all branches except `main`
- **Manual**: Can be triggered manually via `workflow_dispatch`

### CI Checks

The workflow performs the following checks:

| Check | Description |
|-------|-------------|
| **Diagnostics** | Collects system information including OS, CPU, memory, Docker, Python, Node.js, npm, Git, disk space, and environment variables |
| **Lint** | Runs flake8 for code quality checks |
| **Tests** | Runs pytest for unit testing |

### Workflow Flow

1. **Diagnostics Job** (`diagnostics`):
   - Gathers system information from the self-hosted runner
   - Tests availability of Docker, Python, Node.js, and other tools
   - Creates a GitHub issue with diagnostic details (on manual trigger)

2. **CI Job** (`ci`):
   - Runs after diagnostics job completes
   - Checks out the repository
   - Sets up Python 3.11
   - Installs dependencies (pip, flake8, pytest)
   - Runs flake8 linting
   - Runs pytest tests
   - Creates a summary GitHub issue with check results (on push)

### Output

On each push to a non-main branch, the workflow creates a GitHub issue with:
- Branch name and commit information
- Run URL to view the workflow execution
- Table summarizing check results (Diagnostics, Lint & Tests)

---

For more details, see the workflow file: [.github/workflows/ci.yml](.github/workflows/ci.yml)
