# Obsidian Knowledge Management Workflow System

An AI-driven knowledge management system for Obsidian using PARA + Zettelkasten methodology, with Feishu integration via MCP.

## Features

- **PARA Structure**: Organize notes using Projects, Areas, Resources, and Archives
- **Zettelkasten Method**: Create atomic knowledge cards with bidirectional links
- **AI-Driven Conversation**: Natural language interface for note creation and management
- **Smart Sync**: Intelligent synchronization with Feishu platform
- **Task Management**: Unified task center with categorization
- **Knowledge Extraction**: Automatic knowledge card generation from daily notes

## Installation

```bash
pip install -e .
```

For development:

```bash
pip install -e ".[dev]"
```

## Configuration

Create a `.obsidian-km` directory in your vault root with the following files:

### config.json

```json
{
  "vault_path": "/path/to/your/vault",
  "templates_path": "Templates",
  "daily_notes_path": "0-Daily",
  "projects_path": "1-Projects",
  "areas_path": "2-Areas",
  "resources_path": "3-Resources",
  "archives_path": "4-Archives",
  "attachments_path": "Attachments",
  "task_center_path": "任务中心.md",
  "feishu_sync_center_path": "飞书同步中心.md",
  "auto_sync_interval": 300,
  "date_format": "YYYY-MM-DD",
  "time_format": "HH:mm:ss"
}
```

### feishu-credentials.json (optional)

```json
{
  "app_id": "cli_xxxxxxxxxxxxx",
  "app_secret": "xxxxxxxxxxxxxxxxxxxxx",
  "api_base_url": "https://open.feishu.cn/open-apis"
}
```

## Testing

Run all tests:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=obsidian_km --cov-report=html
```

Run specific test types:

```bash
pytest -m unit          # Unit tests only
pytest -m property      # Property-based tests only
pytest -m integration   # Integration tests only
```

## Development

This project uses:
- Python 3.9+
- pytest for testing
- Hypothesis for property-based testing
- pytest-cov for coverage reporting

## License

MIT
