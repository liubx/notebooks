"""Pytest configuration and fixtures."""

import pytest
import tempfile
import shutil
from pathlib import Path
from obsidian_km.config import ConfigLoader, Config, FeishuCredentials


@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing."""
    temp_path = tempfile.mkdtemp()
    yield Path(temp_path)
    shutil.rmtree(temp_path)


@pytest.fixture
def test_vault(temp_dir):
    """Create a test vault directory."""
    vault_path = temp_dir / "test-vault"
    vault_path.mkdir()
    yield vault_path


@pytest.fixture
def test_vault_with_templates(temp_dir):
    """Create a test vault directory with PARA structure and templates."""
    from obsidian_km.structure import ParaStructureInitializer
    
    vault_path = temp_dir / "test-vault"
    vault_path.mkdir()
    
    # Create config for initialization
    config = Config(
        vault_path=str(vault_path),
        templates_path="Templates",
        daily_notes_path="0-Daily",
        projects_path="1-Projects",
        areas_path="2-Areas",
        resources_path="3-Resources",
        archives_path="4-Archives",
        attachments_path="Attachments",
        task_center_path="任务中心.md",
        feishu_sync_center_path="飞书同步中心.md"
    )
    
    # Initialize PARA structure
    initializer = ParaStructureInitializer(config)
    initializer.initialize()
    
    # Copy template files from project root to test vault
    project_root = Path(__file__).parent.parent
    templates_src = project_root / "Templates"
    templates_dst = vault_path / "Templates"
    
    if templates_src.exists():
        for template_file in templates_src.glob("*.md"):
            shutil.copy(template_file, templates_dst / template_file.name)
    
    yield vault_path


@pytest.fixture
def config_dir(temp_dir):
    """Create a test config directory."""
    config_path = temp_dir / ".obsidian-km"
    config_path.mkdir()
    yield config_path


@pytest.fixture
def sample_config(test_vault):
    """Create a sample configuration."""
    return Config(
        vault_path=str(test_vault),
        templates_path="Templates",
        daily_notes_path="0-Daily",
        projects_path="1-Projects",
        areas_path="2-Areas",
        resources_path="3-Resources",
        archives_path="4-Archives",
        attachments_path="Attachments",
        task_center_path="任务中心.md",
        feishu_sync_center_path="飞书同步中心.md",
        auto_sync_interval=300,
        date_format="YYYY-MM-DD",
        time_format="HH:mm:ss"
    )


@pytest.fixture
def sample_credentials():
    """Create sample Feishu credentials."""
    return FeishuCredentials(
        app_id="cli_test123456",
        app_secret="test_secret_key",
        tenant_access_token="",
        token_expires_at="",
        api_base_url="https://open.feishu.cn/open-apis"
    )


@pytest.fixture
def config_loader(config_dir):
    """Create a ConfigLoader instance."""
    return ConfigLoader(config_dir)
