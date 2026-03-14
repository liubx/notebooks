"""Tests for PARA folder structure initialization."""

import pytest
from pathlib import Path
from hypothesis import given, strategies as st, settings
from obsidian_km.structure import ParaStructureInitializer
from obsidian_km.config import Config


class TestParaStructureInitializer:
    """Test PARA structure initialization."""

    def test_initialize_creates_all_folders(self, test_vault, sample_config):
        """Test that initialize creates all required folders."""
        initializer = ParaStructureInitializer(sample_config)
        
        created_folders = initializer.initialize()
        
        # Verify all required folders exist
        assert initializer.verify_structure()
        
        # Verify specific folders
        assert (test_vault / "0-Daily").exists()
        assert (test_vault / "1-Projects").exists()
        assert (test_vault / "2-Areas").exists()
        assert (test_vault / "3-Resources").exists()
        assert (test_vault / "4-Archives").exists()
        assert (test_vault / "Attachments").exists()
        assert (test_vault / "Templates").exists()
        
        # Verify Projects subfolders
        assert (test_vault / "1-Projects" / "Work").exists()
        assert (test_vault / "1-Projects" / "Personal").exists()
        
        # Verify Areas subfolders
        assert (test_vault / "2-Areas" / "Work").exists()
        assert (test_vault / "2-Areas" / "Life").exists()
        
        # Verify Resources subfolders
        assert (test_vault / "3-Resources" / "Tech").exists()
        assert (test_vault / "3-Resources" / "Life").exists()
        
        # Verify Tech subfolders
        assert (test_vault / "3-Resources" / "Tech" / "Knowledge-Cards").exists()
        assert (test_vault / "3-Resources" / "Tech" / "Code-Snippets").exists()
        assert (test_vault / "3-Resources" / "Tech" / "ADR").exists()
        assert (test_vault / "3-Resources" / "Tech" / "Problem-Solving").exists()

    def test_initialize_idempotent(self, test_vault, sample_config):
        """Test that initialize can be called multiple times safely."""
        initializer = ParaStructureInitializer(sample_config)
        
        # First initialization
        created_first = initializer.initialize()
        assert len(created_first) > 0
        
        # Second initialization should not create new folders
        created_second = initializer.initialize()
        assert len(created_second) == 0
        
        # Structure should still be valid
        assert initializer.verify_structure()

    def test_get_required_folders(self, sample_config):
        """Test that get_required_folders returns all required folders."""
        initializer = ParaStructureInitializer(sample_config)
        
        required = initializer.get_required_folders()
        
        # Should have 17 folders (7 top-level + 2 Projects + 2 Areas + 2 Resources + 4 Tech)
        assert len(required) == 17
        
        # Check some key folders
        assert Path("0-Daily") in required
        assert Path("1-Projects/Work") in required
        assert Path("2-Areas/Life") in required
        assert Path("3-Resources/Tech/Knowledge-Cards") in required

    def test_verify_structure_empty_vault(self, test_vault, sample_config):
        """Test that verify_structure returns False for empty vault."""
        initializer = ParaStructureInitializer(sample_config)
        
        assert not initializer.verify_structure()

    def test_verify_structure_after_init(self, test_vault, sample_config):
        """Test that verify_structure returns True after initialization."""
        initializer = ParaStructureInitializer(sample_config)
        
        initializer.initialize()
        
        assert initializer.verify_structure()

    def test_get_missing_folders(self, test_vault, sample_config):
        """Test that get_missing_folders returns correct list."""
        initializer = ParaStructureInitializer(sample_config)
        
        # Before initialization, all folders should be missing
        missing_before = initializer.get_missing_folders()
        assert len(missing_before) == 17
        
        # After initialization, no folders should be missing
        initializer.initialize()
        missing_after = initializer.get_missing_folders()
        assert len(missing_after) == 0

    def test_partial_structure(self, test_vault, sample_config):
        """Test handling of partially created structure."""
        # Create only some folders manually
        (test_vault / "0-Daily").mkdir()
        (test_vault / "1-Projects").mkdir()
        
        initializer = ParaStructureInitializer(sample_config)
        
        # Should detect incomplete structure
        assert not initializer.verify_structure()
        
        # Should identify missing folders
        missing = initializer.get_missing_folders()
        assert len(missing) > 0
        assert Path("2-Areas") in missing
        
        # Initialize should complete the structure
        initializer.initialize()
        assert initializer.verify_structure()


# Feature: obsidian-knowledge-management-workflow, Property: 文件夹结构完整性
@given(vault_name=st.text(min_size=1, max_size=50, alphabet=st.characters(
    whitelist_categories=('Lu', 'Ll', 'Nd'), 
    whitelist_characters='-_'
)))
@settings(max_examples=100, deadline=None)
def test_property_folder_structure_completeness(vault_name):
    """
    Property: 对于任意 vault 路径，初始化后应该包含所有必需的 PARA 文件夹
    
    验证需求: 1.1, 1.2, 1.3, 1.4
    """
    import tempfile
    import shutil
    
    # Create temporary directory
    temp_dir = Path(tempfile.mkdtemp())
    
    try:
        # Create vault with arbitrary name
        vault_path = temp_dir / vault_name
        vault_path.mkdir(parents=True, exist_ok=True)
        
        # Create config for this vault
        config = Config(
            vault_path=str(vault_path),
            templates_path="Templates",
            daily_notes_path="0-Daily",
            projects_path="1-Projects",
            areas_path="2-Areas",
            resources_path="3-Resources",
            archives_path="4-Archives",
            attachments_path="Attachments"
        )
        
        # Initialize structure
        initializer = ParaStructureInitializer(config)
        initializer.initialize()
        
        # Property: All required folders must exist
        required_folders = initializer.get_required_folders()
        for folder in required_folders:
            folder_path = vault_path / folder
            assert folder_path.exists(), f"Required folder missing: {folder}"
            assert folder_path.is_dir(), f"Path is not a directory: {folder}"
        
        # Property: Structure verification must pass
        assert initializer.verify_structure(), "Structure verification failed"
        
        # Property: No folders should be missing
        missing = initializer.get_missing_folders()
        assert len(missing) == 0, f"Missing folders found: {missing}"
        
        # Property: Specific PARA folders must exist (Requirements 1.1, 1.2, 1.3, 1.4)
        # Requirement 1.1: Top-level PARA folders
        assert (vault_path / "0-Daily").exists()
        assert (vault_path / "1-Projects").exists()
        assert (vault_path / "2-Areas").exists()
        assert (vault_path / "3-Resources").exists()
        assert (vault_path / "4-Archives").exists()
        
        # Requirement 1.2: Projects subfolders
        assert (vault_path / "1-Projects" / "Work").exists()
        assert (vault_path / "1-Projects" / "Personal").exists()
        
        # Requirement 1.3: Areas subfolders
        assert (vault_path / "2-Areas" / "Work").exists()
        assert (vault_path / "2-Areas" / "Life").exists()
        
        # Requirement 1.4: Resources subfolders
        assert (vault_path / "3-Resources" / "Tech").exists()
        assert (vault_path / "3-Resources" / "Life").exists()
    finally:
        # Clean up
        shutil.rmtree(temp_dir)
