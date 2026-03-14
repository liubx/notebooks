"""Unit tests for configuration module."""

import pytest
import json
from pathlib import Path
from obsidian_km.config import ConfigLoader, Config, FeishuCredentials


class TestConfig:
    """Test Config dataclass."""

    def test_config_from_dict(self, test_vault):
        """Test creating Config from dictionary."""
        data = {
            "vault_path": str(test_vault),
            "templates_path": "Templates",
            "daily_notes_path": "0-Daily"
        }
        
        config = Config.from_dict(data)
        
        assert config.vault_path == str(test_vault)
        assert config.templates_path == "Templates"
        assert config.daily_notes_path == "0-Daily"

    def test_config_defaults(self, test_vault):
        """Test Config default values."""
        data = {"vault_path": str(test_vault)}
        
        config = Config.from_dict(data)
        
        assert config.templates_path == "Templates"
        assert config.daily_notes_path == "0-Daily"
        assert config.projects_path == "1-Projects"
        assert config.areas_path == "2-Areas"
        assert config.resources_path == "3-Resources"
        assert config.archives_path == "4-Archives"


class TestFeishuCredentials:
    """Test FeishuCredentials dataclass."""

    def test_credentials_from_dict(self):
        """Test creating FeishuCredentials from dictionary."""
        data = {
            "app_id": "cli_test123",
            "app_secret": "secret123"
        }
        
        creds = FeishuCredentials.from_dict(data)
        
        assert creds.app_id == "cli_test123"
        assert creds.app_secret == "secret123"
        assert creds.api_base_url == "https://open.feishu.cn/open-apis"

    def test_credentials_with_token(self):
        """Test FeishuCredentials with token."""
        data = {
            "app_id": "cli_test123",
            "app_secret": "secret123",
            "tenant_access_token": "token123",
            "token_expires_at": "2024-01-20T10:00:00"
        }
        
        creds = FeishuCredentials.from_dict(data)
        
        assert creds.tenant_access_token == "token123"
        assert creds.token_expires_at == "2024-01-20T10:00:00"


class TestConfigLoader:
    """Test ConfigLoader class."""

    def test_init_default_path(self):
        """Test ConfigLoader initialization with default path."""
        loader = ConfigLoader()
        
        assert loader.config_dir == Path.cwd() / ".obsidian-km"
        assert loader.config_file == Path.cwd() / ".obsidian-km" / "config.json"

    def test_init_custom_path(self, config_dir):
        """Test ConfigLoader initialization with custom path."""
        loader = ConfigLoader(config_dir)
        
        assert loader.config_dir == config_dir
        assert loader.config_file == config_dir / "config.json"

    def test_save_and_load_config(self, config_loader, sample_config):
        """Test saving and loading configuration."""
        config_loader.save_config(sample_config)
        
        loaded_config = config_loader.load_config()
        
        assert loaded_config.vault_path == sample_config.vault_path
        assert loaded_config.templates_path == sample_config.templates_path
        assert loaded_config.daily_notes_path == sample_config.daily_notes_path

    def test_load_config_file_not_found(self, config_loader):
        """Test loading config when file doesn't exist."""
        with pytest.raises(FileNotFoundError):
            config_loader.load_config()

    def test_load_config_invalid_vault_path(self, config_loader):
        """Test loading config with invalid vault path."""
        config_loader.config_dir.mkdir(parents=True, exist_ok=True)
        
        data = {"vault_path": "/nonexistent/path"}
        with open(config_loader.config_file, 'w') as f:
            json.dump(data, f)
        
        with pytest.raises(ValueError, match="vault_path does not exist"):
            config_loader.load_config()

    def test_load_config_missing_vault_path(self, config_loader):
        """Test loading config without vault_path."""
        config_loader.config_dir.mkdir(parents=True, exist_ok=True)
        
        data = {"templates_path": "Templates"}
        with open(config_loader.config_file, 'w') as f:
            json.dump(data, f)
        
        with pytest.raises(ValueError, match="vault_path is required"):
            config_loader.load_config()

    def test_save_and_load_credentials(self, config_loader, sample_credentials):
        """Test saving and loading credentials."""
        config_loader.save_credentials(sample_credentials)
        
        loaded_creds = config_loader.load_credentials()
        
        assert loaded_creds.app_id == sample_credentials.app_id
        assert loaded_creds.app_secret == sample_credentials.app_secret
        assert loaded_creds.api_base_url == sample_credentials.api_base_url

    def test_load_credentials_file_not_found(self, config_loader):
        """Test loading credentials when file doesn't exist."""
        result = config_loader.load_credentials()
        
        assert result is None

    def test_load_credentials_missing_app_id(self, config_loader):
        """Test loading credentials without app_id."""
        config_loader.config_dir.mkdir(parents=True, exist_ok=True)
        
        data = {"app_secret": "secret123"}
        with open(config_loader.credentials_file, 'w') as f:
            json.dump(data, f)
        
        with pytest.raises(ValueError, match="app_id is required"):
            config_loader.load_credentials()

    def test_load_credentials_missing_app_secret(self, config_loader):
        """Test loading credentials without app_secret."""
        config_loader.config_dir.mkdir(parents=True, exist_ok=True)
        
        data = {"app_id": "cli_test123"}
        with open(config_loader.credentials_file, 'w') as f:
            json.dump(data, f)
        
        with pytest.raises(ValueError, match="app_secret is required"):
            config_loader.load_credentials()

    def test_config_creates_directory(self, temp_dir):
        """Test that saving config creates directory if it doesn't exist."""
        config_dir = temp_dir / ".obsidian-km"
        loader = ConfigLoader(config_dir)
        
        vault_path = temp_dir / "vault"
        vault_path.mkdir()
        config = Config(vault_path=str(vault_path))
        
        loader.save_config(config)
        
        assert config_dir.exists()
        assert loader.config_file.exists()
