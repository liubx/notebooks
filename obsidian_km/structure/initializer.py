"""PARA folder structure initialization."""

from pathlib import Path
from typing import List
from obsidian_km.config import Config


class ParaStructureInitializer:
    """Initialize PARA folder structure in an Obsidian vault."""

    def __init__(self, config: Config):
        """
        Initialize the PARA structure initializer.
        
        Args:
            config: System configuration
        """
        self.config = config
        self.vault_path = Path(config.vault_path)

    def initialize(self) -> List[Path]:
        """
        Initialize the complete PARA folder structure.
        
        Creates all necessary folders according to the PARA methodology:
        - 0-Daily (with YYYY/MM subfolders for current year/month)
        - 1-Projects (with Work and Personal subfolders)
        - 2-Areas (with Work and Life subfolders)
        - 3-Resources (with Tech and Life subfolders)
        - 4-Archives
        - Attachments
        - Templates
        
        Returns:
            List of created folder paths
            
        Raises:
            OSError: If folder creation fails
        """
        created_folders = []
        
        # Create top-level PARA folders
        para_folders = [
            self.config.daily_notes_path,
            self.config.projects_path,
            self.config.areas_path,
            self.config.resources_path,
            self.config.archives_path,
            self.config.attachments_path,
            self.config.templates_path
        ]
        
        for folder in para_folders:
            folder_path = self.vault_path / folder
            if not folder_path.exists():
                folder_path.mkdir(parents=True, exist_ok=True)
                created_folders.append(folder_path)
        
        # Create Projects subfolders
        projects_subfolders = ["Work", "Personal"]
        for subfolder in projects_subfolders:
            subfolder_path = self.vault_path / self.config.projects_path / subfolder
            if not subfolder_path.exists():
                subfolder_path.mkdir(parents=True, exist_ok=True)
                created_folders.append(subfolder_path)
        
        # Create Areas subfolders
        areas_subfolders = ["Work", "Life"]
        for subfolder in areas_subfolders:
            subfolder_path = self.vault_path / self.config.areas_path / subfolder
            if not subfolder_path.exists():
                subfolder_path.mkdir(parents=True, exist_ok=True)
                created_folders.append(subfolder_path)
        
        # Create Resources subfolders
        resources_subfolders = ["Tech", "Life"]
        for subfolder in resources_subfolders:
            subfolder_path = self.vault_path / self.config.resources_path / subfolder
            if not subfolder_path.exists():
                subfolder_path.mkdir(parents=True, exist_ok=True)
                created_folders.append(subfolder_path)
        
        # Create Tech subfolders
        tech_subfolders = ["Knowledge-Cards", "Code-Snippets", "ADR", "Problem-Solving"]
        for subfolder in tech_subfolders:
            subfolder_path = self.vault_path / self.config.resources_path / "Tech" / subfolder
            if not subfolder_path.exists():
                subfolder_path.mkdir(parents=True, exist_ok=True)
                created_folders.append(subfolder_path)
        
        return created_folders

    def get_required_folders(self) -> List[Path]:
        """
        Get list of all required PARA folders.
        
        Returns:
            List of required folder paths (relative to vault root)
        """
        required = [
            # Top-level folders
            Path(self.config.daily_notes_path),
            Path(self.config.projects_path),
            Path(self.config.areas_path),
            Path(self.config.resources_path),
            Path(self.config.archives_path),
            Path(self.config.attachments_path),
            Path(self.config.templates_path),
            
            # Projects subfolders
            Path(self.config.projects_path) / "Work",
            Path(self.config.projects_path) / "Personal",
            
            # Areas subfolders
            Path(self.config.areas_path) / "Work",
            Path(self.config.areas_path) / "Life",
            
            # Resources subfolders
            Path(self.config.resources_path) / "Tech",
            Path(self.config.resources_path) / "Life",
            
            # Tech subfolders
            Path(self.config.resources_path) / "Tech" / "Knowledge-Cards",
            Path(self.config.resources_path) / "Tech" / "Code-Snippets",
            Path(self.config.resources_path) / "Tech" / "ADR",
            Path(self.config.resources_path) / "Tech" / "Problem-Solving",
        ]
        
        return required

    def verify_structure(self) -> bool:
        """
        Verify that all required PARA folders exist.
        
        Returns:
            True if all required folders exist, False otherwise
        """
        required_folders = self.get_required_folders()
        
        for folder in required_folders:
            folder_path = self.vault_path / folder
            if not folder_path.exists() or not folder_path.is_dir():
                return False
        
        return True

    def get_missing_folders(self) -> List[Path]:
        """
        Get list of missing required folders.
        
        Returns:
            List of missing folder paths
        """
        required_folders = self.get_required_folders()
        missing = []
        
        for folder in required_folders:
            folder_path = self.vault_path / folder
            if not folder_path.exists():
                missing.append(folder)
        
        return missing
