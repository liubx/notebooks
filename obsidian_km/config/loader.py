"""Configuration loading and validation module."""

import json
from pathlib import Path
from typing import Optional
from dataclasses import dataclass


@dataclass
class FeishuCredentials:
    """Feishu API credentials."""
    app_id: str
    app_secret: str
    tenant_access_token: str = ""
    token_expires_at: str = ""
    api_base_url: str = "https://open.feishu.cn/open-apis"

    @classmethod
    def from_dict(cls, data: dict) -> "FeishuCredentials":
        """Create from dictionary."""
        return cls(
            app_id=data["app_id"],
            app_secret=data["app_secret"],
            tenant_access_token=data.get("tenant_access_token", ""),
            token_expires_at=data.get("token_expires_at", ""),
            api_base_url=data.get("api_base_url", "https://open.feishu.cn/open-apis")
        )


@dataclass
class Config:
    """System configuration."""
    vault_path: str
    templates_path: str = "Templates"
    daily_notes_path: str = "0-Daily"
    projects_path: str = "1-Projects"
    areas_path: str = "2-Areas"
    resources_path: str = "3-Resources"
    archives_path: str = "4-Archives"
    attachments_path: str = "Attachments"
    task_center_path: str = "任务中心.md"
    feishu_sync_center_path: str = "飞书同步中心.md"
    auto_sync_interval: int = 300
    date_format: str = "YYYY-MM-DD"
    time_format: str = "HH:mm:ss"

    @classmethod
    def from_dict(cls, data: dict) -> "Config":
        """Create from dictionary."""
        return cls(
            vault_path=data["vault_path"],
            templates_path=data.get("templates_path", "Templates"),
            daily_notes_path=data.get("daily_notes_path", "0-Daily"),
            projects_path=data.get("projects_path", "1-Projects"),
            areas_path=data.get("areas_path", "2-Areas"),
            resources_path=data.get("resources_path", "3-Resources"),
            archives_path=data.get("archives_path", "4-Archives"),
            attachments_path=data.get("attachments_path", "Attachments"),
            task_center_path=data.get("task_center_path", "任务中心.md"),
            feishu_sync_center_path=data.get("feishu_sync_center_path", "飞书同步中心.md"),
            auto_sync_interval=data.get("auto_sync_interval", 300),
            date_format=data.get("date_format", "YYYY-MM-DD"),
            time_format=data.get("time_format", "HH:mm:ss")
        )


class ConfigLoader:
    """Load and validate configuration files."""

    def __init__(self, config_dir: Optional[Path] = None):
        """
        Initialize config loader.
        
        Args:
            config_dir: Directory containing config files. Defaults to .obsidian-km in current directory.
        """
        if config_dir is None:
            config_dir = Path.cwd() / ".obsidian-km"
        self.config_dir = Path(config_dir)
        self.config_file = self.config_dir / "config.json"
        self.credentials_file = self.config_dir / "feishu-credentials.json"

    def load_config(self) -> Config:
        """
        Load system configuration.
        
        Returns:
            Config object
            
        Raises:
            FileNotFoundError: If config file doesn't exist
            ValueError: If config is invalid
        """
        if not self.config_file.exists():
            raise FileNotFoundError(f"Config file not found: {self.config_file}")
        
        with open(self.config_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        self._validate_config(data)
        return Config.from_dict(data)

    def load_credentials(self) -> Optional[FeishuCredentials]:
        """
        Load Feishu credentials.
        
        Returns:
            FeishuCredentials object or None if file doesn't exist
            
        Raises:
            ValueError: If credentials are invalid
        """
        if not self.credentials_file.exists():
            return None
        
        with open(self.credentials_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        self._validate_credentials(data)
        return FeishuCredentials.from_dict(data)

    def save_config(self, config: Config) -> None:
        """
        Save system configuration.
        
        Args:
            config: Config object to save
        """
        self.config_dir.mkdir(parents=True, exist_ok=True)
        
        data = {
            "vault_path": config.vault_path,
            "templates_path": config.templates_path,
            "daily_notes_path": config.daily_notes_path,
            "projects_path": config.projects_path,
            "areas_path": config.areas_path,
            "resources_path": config.resources_path,
            "archives_path": config.archives_path,
            "attachments_path": config.attachments_path,
            "task_center_path": config.task_center_path,
            "feishu_sync_center_path": config.feishu_sync_center_path,
            "auto_sync_interval": config.auto_sync_interval,
            "date_format": config.date_format,
            "time_format": config.time_format
        }
        
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def save_credentials(self, credentials: FeishuCredentials) -> None:
        """
        Save Feishu credentials.
        
        Args:
            credentials: FeishuCredentials object to save
        """
        self.config_dir.mkdir(parents=True, exist_ok=True)
        
        data = {
            "app_id": credentials.app_id,
            "app_secret": credentials.app_secret,
            "tenant_access_token": credentials.tenant_access_token,
            "token_expires_at": credentials.token_expires_at,
            "api_base_url": credentials.api_base_url
        }
        
        with open(self.credentials_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def _validate_config(self, data: dict) -> None:
        """Validate configuration data."""
        if "vault_path" not in data:
            raise ValueError("vault_path is required in config")
        
        vault_path = Path(data["vault_path"])
        if not vault_path.exists():
            raise ValueError(f"vault_path does not exist: {vault_path}")

    def _validate_credentials(self, data: dict) -> None:
        """Validate credentials data."""
        required_fields = ["app_id", "app_secret"]
        for field in required_fields:
            if field not in data or not data[field]:
                raise ValueError(f"{field} is required in credentials")
