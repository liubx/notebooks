# Project Structure

```
obsidian-km/
├── obsidian_km/              # Main package
│   ├── __init__.py
│   └── config/               # Configuration module
│       ├── __init__.py
│       └── loader.py         # Config loading and validation
│
├── tests/                    # Test suite
│   ├── __init__.py
│   ├── conftest.py          # Pytest fixtures
│   └── test_config.py       # Config module tests
│
├── .obsidian-km/            # Configuration directory
│   ├── config.json.example
│   └── feishu-credentials.json.example
│
├── docs/                    # Documentation
│   └── project-structure.md
│
├── .gitignore
├── pytest.ini               # Pytest configuration
├── requirements.txt         # Dependencies
├── setup.py                 # Package setup
└── README.md               # Project documentation
```

## Module Overview

### obsidian_km.config

Configuration management module that handles:
- Loading and validating system configuration from `config.json`
- Loading and validating Feishu credentials from `feishu-credentials.json`
- Providing dataclasses for type-safe configuration access

**Key Classes:**
- `Config`: System configuration dataclass
- `FeishuCredentials`: Feishu API credentials dataclass
- `ConfigLoader`: Configuration file loader and validator

## Configuration Files

### config.json

System configuration file that defines:
- Vault path and folder structure
- Path configurations for PARA structure
- Task and sync center paths
- Date/time formats
- Auto-sync interval

### feishu-credentials.json

Feishu API credentials file that contains:
- App ID and App Secret
- Access token (auto-updated)
- API base URL

## Testing

The project uses:
- **pytest**: Test framework
- **pytest-cov**: Coverage reporting
- **hypothesis**: Property-based testing

Test organization:
- `conftest.py`: Shared fixtures for all tests
- `test_*.py`: Test modules organized by feature

Run tests:
```bash
pytest                    # Run all tests
pytest -v                 # Verbose output
pytest --cov              # With coverage
pytest -m unit            # Unit tests only
```

## Development Workflow

1. Install in development mode:
   ```bash
   pip install -e ".[dev]"
   ```

2. Run tests before committing:
   ```bash
   pytest
   ```

3. Check coverage:
   ```bash
   pytest --cov=obsidian_km --cov-report=html
   open htmlcov/index.html
   ```
