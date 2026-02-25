# T9-CTN-GenAI

AI-powered CTN (Car Training Network) development with the T9 project.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest --tb=short -v

# Lint code
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
```

## Project Structure

```
T9-CTN-GenAI/
├── src/sprint_analysis/     # Sprint analysis module
├── notebooks/               # Jupyter notebooks (examples)
└── .github/workflows/       # CI/CD workflows
```

## CI/CD Architecture

### Pipeline Details

| Component | Description |
|-----------|-------------|
| **Runner** | Self-hosted `imprunner` (Linux x64) |
| **Triggers** | Push to main, PR to main, Manual dispatch |
| **Diagnostics** | System info, CPU/Memory, Docker, Python, Git, Tools, Disk |
| **CI Job** | Checkout → Python 3.11 → Install deps → Lint → Test |
| **Quality Gates** | flake8 linting + pytest tests |

### Branch Protection

- PR required to merge to `main`
- At least 1 approval required
- CodeQL scan required
- Code quality results must pass

## Development

- Python 3.11+
