"""Project archiver for moving projects to archives."""

import shutil
from datetime import datetime
from pathlib import Path
from typing import Optional
import re

from obsidian_km.config import Config


class ProjectArchiver:
    """Handles archiving of completed projects."""
    
    def __init__(self, config: Config):
        """
        Initialize the project archiver.
        
        Args:
            config: Configuration object containing vault paths
        """
        self.config = config
        self.vault_path = Path(config.vault_path)
        self.projects_path = self.vault_path / config.projects_path
        self.archives_path = self.vault_path / config.archives_path
    
    def get_archive_path(self, project_name: str, year: Optional[int] = None) -> Path:
        """
        Get the archive path for a project.
        
        Args:
            project_name: Name of the project folder
            year: Year for archiving (defaults to current year)
        
        Returns:
            Path to the archived project folder
        """
        if year is None:
            year = datetime.now().year
        
        return self.archives_path / str(year) / project_name
    
    def archive_project(self, project_path: Path, archive_date: Optional[str] = None) -> Path:
        """
        Archive a project by moving it to the archives folder.
        
        This function:
        1. Moves the project folder to 4-Archives/YYYY/
        2. Adds archived_date field to YAML front matter in README.md
        3. Preserves all file content, links, and tags
        
        Args:
            project_path: Path to the project folder to archive
            archive_date: Archive date in YYYY-MM-DD format (defaults to today)
        
        Returns:
            Path to the archived project folder
        
        Raises:
            FileNotFoundError: If project path doesn't exist
            ValueError: If project path is not a directory
        """
        if not project_path.exists():
            raise FileNotFoundError(f"Project path does not exist: {project_path}")
        
        if not project_path.is_dir():
            raise ValueError(f"Project path is not a directory: {project_path}")
        
        # Get archive date
        if archive_date is None:
            archive_date = datetime.now().strftime('%Y-%m-%d')
        
        # Extract year from archive_date
        archive_year = int(archive_date.split('-')[0])
        
        # Get project name
        project_name = project_path.name
        
        # Get archive destination
        archive_dest = self.get_archive_path(project_name, year=archive_year)
        
        # Create archive year folder if it doesn't exist
        archive_dest.parent.mkdir(parents=True, exist_ok=True)
        
        # Move project folder to archives
        shutil.move(str(project_path), str(archive_dest))
        
        # Add archived_date metadata to README.md if it exists
        readme_path = archive_dest / "README.md"
        if readme_path.exists():
            self._add_archive_metadata(readme_path, archive_date)
        
        return archive_dest
    
    def _add_archive_metadata(self, readme_path: Path, archive_date: str) -> None:
        """
        Add archived_date field to YAML front matter.
        
        Args:
            readme_path: Path to the README.md file
            archive_date: Archive date in YYYY-MM-DD format
        """
        content = readme_path.read_text(encoding='utf-8')
        
        # Check if YAML front matter exists
        if content.startswith('---\n'):
            # Find the end of YAML front matter
            end_index = content.find('\n---\n', 4)
            if end_index != -1:
                # Insert archived_date before the closing ---
                yaml_content = content[4:end_index]
                
                # Check if archived_date already exists
                if 'archived_date:' not in yaml_content:
                    # Add archived_date field
                    new_yaml = yaml_content.rstrip() + f'\narchived_date: {archive_date}\n'
                    new_content = f'---\n{new_yaml}---\n' + content[end_index + 5:]
                    readme_path.write_text(new_content, encoding='utf-8')
                else:
                    # Update existing archived_date
                    new_yaml = re.sub(
                        r'archived_date:.*',
                        f'archived_date: {archive_date}',
                        yaml_content
                    )
                    new_content = f'---\n{new_yaml}\n---\n' + content[end_index + 5:]
                    readme_path.write_text(new_content, encoding='utf-8')
            else:
                # Malformed YAML, add at the beginning
                self._prepend_yaml_with_archive_date(readme_path, archive_date, content)
        else:
            # No YAML front matter, add it
            self._prepend_yaml_with_archive_date(readme_path, archive_date, content)
    
    def _prepend_yaml_with_archive_date(self, readme_path: Path, archive_date: str, content: str) -> None:
        """
        Prepend YAML front matter with archived_date to the file.
        
        Args:
            readme_path: Path to the README.md file
            archive_date: Archive date in YYYY-MM-DD format
            content: Current file content
        """
        yaml_header = f'---\narchived_date: {archive_date}\n---\n\n'
        new_content = yaml_header + content
        readme_path.write_text(new_content, encoding='utf-8')
