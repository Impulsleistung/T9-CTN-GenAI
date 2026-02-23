# T9-CTN-GenAI

A GitHub repository for AI-powered CTN (Car Training Network) development with the T9 project.

## Overview

This repository contains the T9-CTN-GenAI project, which focuses on AI-assisted development for Car Training Network applications.

## Self-Hosted Runner

This project uses a self-hosted GitHub Actions runner named `imprunner` for CI/CD workflows.

### Runner Details

| Property | Value |
|----------|-------|
| **Name** | `imprunner` |
| **Type** | Self-hosted |
| **OS** | Linux |
| **Architecture** | x64 |

### Targeting the Runner

You can target this runner in your workflow files using:

```yaml
# Option 1 - by runner name
runs-on: imprunner

# Option 2 - by labels
runs-on: [self-hosted, Linux, X64]
```

## GitHub Actions Workflows

### CI Workflow (ci.yml)

The CI workflow automatically runs on:
- Push to `main` branch
- Pull requests targeting `main` branch
- Manual trigger (`workflow_dispatch`)

#### Jobs

1. **Diagnostics** - Collects and reports runner environment information:
   - System information (hostname, OS)
   - CPU and memory details
   - Docker information
   - Python information
   - Git information
   - Available tools
   - Disk space
   - Environment variables

2. **CI** - Runs linting and tests:
   - Checks out the repository
   - Sets up Python 3.11
   - Installs dependencies (flake8, pytest)
   - Runs flake8 linting
   - Runs pytest tests

### Running the Workflow Manually

You can trigger the CI workflow manually from the GitHub Actions tab:

1. Go to the repository on GitHub
2. Click on "Actions" tab
3. Select the "CI" workflow
4. Click "Run workflow"

## Development

### Requirements

- Python 3.11+
- flake8 (for linting)
- pytest (for testing)

### Installing Dependencies

```bash
pip install flake8 pytest
```

If you have a `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Running Tests

```bash
pytest --tb=short -v
```

### Running Linting

```bash
# Strict mode - stops on syntax errors and undefined names
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

# Warning mode - treats most errors as warnings
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```

## Project Structure

```
T9-CTN-GenAI/
├── .github/
│   └── workflows/
│       └── ci.yml          # CI workflow
├── docs/
│   └── runner-info.md      # Runner documentation
├── .gitignore
├── LICENSE
└── README.md
```

## Security

- Branch protection rules are enabled on `main`
- Pull requests are required to merge to `main`
- At least 1 approval required for PRs
- Force pushes are blocked
- Code scanning (CodeQL) is required
- Code quality results must pass

## License

See the [LICENSE](LICENSE) file for details.