"""Note creator for different types of notes."""

from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Optional

from obsidian_km.config import Config
from obsidian_km.templates import TemplateLoader, TemplateVariables


class NoteCreator:
    """Creates different types of notes using templates."""
    
    def __init__(self, config: Config):
        """
        Initialize note creator.
        
        Args:
            config: Configuration object
        """
        self.config = config
        self.vault_path = Path(config.vault_path)
        self.template_loader = TemplateLoader(config.templates_path)
    
    def get_daily_note_path(self, date: datetime) -> Path:
        """
        Get the path for a daily note.
        
        Args:
            date: Date for the daily note
        
        Returns:
            Path to the daily note file
        """
        year = date.year
        month = date.month
        date_str = date.strftime('%Y-%m-%d')
        
        return self.vault_path / self.config.daily_notes_path / str(year) / f"{month:02d}" / f"{date_str}.md"
    
    def create_daily_note(
        self,
        date: Optional[datetime] = None,
        content: str = ""
    ) -> Path:
        """
        Create a daily note.
        
        Args:
            date: Date for the daily note (defaults to today)
            content: Additional content to append to the note
        
        Returns:
            Path to the created note
        """
        if date is None:
            date = datetime.now()
        
        # Get note path
        note_path = self.get_daily_note_path(date)
        
        # Create parent directories if they don't exist
        note_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Generate variables
        variables = TemplateVariables.for_daily_note(date)
        
        # Apply template
        note_content = self.template_loader.apply_template("daily-note", variables)
        
        # Append additional content if provided
        if content:
            note_content += f"\n\n{content}"
        
        # Write note
        note_path.write_text(note_content, encoding='utf-8')
        
        return note_path
    
    def get_project_path(
        self,
        project_name: str,
        category: str = 'work'
    ) -> Path:
        """
        Get the path for a project folder.
        
        Args:
            project_name: Name of the project
            category: Project category (work/personal)
        
        Returns:
            Path to the project folder
        """
        category_folder = 'Work' if category == 'work' else 'Personal'
        return self.vault_path / self.config.projects_path / category_folder / project_name
    
    def create_project(
        self,
        title: str,
        category: str = 'work',
        start_date: str = '',
        due_date: str = '',
        project_name: Optional[str] = None
    ) -> Path:
        """
        Create a project document.
        
        Args:
            title: Project title
            category: Project category (work/personal)
            start_date: Project start date (YYYY-MM-DD)
            due_date: Project due date (YYYY-MM-DD)
            project_name: Project name for folder (defaults to title)
        
        Returns:
            Path to the created project README
        """
        if project_name is None:
            project_name = title
        
        # Get project folder path
        project_path = self.get_project_path(project_name, category)
        
        # Create project folder
        project_path.mkdir(parents=True, exist_ok=True)
        
        # Generate variables
        variables = TemplateVariables.for_project(
            title=title,
            category=category,
            start_date=start_date,
            due_date=due_date,
            project_name=project_name
        )
        
        # Apply template
        note_content = self.template_loader.apply_template("project", variables)
        
        # Write README
        readme_path = project_path / "README.md"
        readme_path.write_text(note_content, encoding='utf-8')
        
        return readme_path
    
    def create_meeting_note(
        self,
        title: str,
        date: str = '',
        time: str = '',
        participants: str = '',
        project_tag: str = '',
        location: Optional[Path] = None
    ) -> Path:
        """
        Create a meeting note.
        
        Args:
            title: Meeting title
            date: Meeting date (YYYY-MM-DD)
            time: Meeting time (HH:MM)
            participants: Comma-separated list of participants
            project_tag: Project tag for the meeting
            location: Optional custom location for the note
        
        Returns:
            Path to the created meeting note
        """
        # Generate variables
        variables = TemplateVariables.for_meeting(
            title=title,
            date=date,
            time=time,
            participants=participants,
            project_tag=project_tag
        )
        
        # Apply template
        note_content = self.template_loader.apply_template("meeting", variables)
        
        # Determine location
        if location is None:
            # Default to today's daily note folder
            today = datetime.now()
            location = self.get_daily_note_path(today).parent
        
        # Create filename
        meeting_date = date if date else datetime.now().strftime('%Y-%m-%d')
        filename = f"{meeting_date}-{title}.md"
        note_path = location / filename
        
        # Create parent directories if needed
        note_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write note
        note_path.write_text(note_content, encoding='utf-8')
        
        return note_path
    
    def create_knowledge_card(
        self,
        title: str,
        main_tag: str = '技术',
        source: str = ''
    ) -> Path:
        """
        Create a knowledge card.
        
        Args:
            title: Knowledge card title
            main_tag: Main tag for the card
            source: Source note reference
        
        Returns:
            Path to the created knowledge card
        """
        # Get knowledge cards folder
        cards_path = self.vault_path / self.config.resources_path / 'Tech' / 'Knowledge-Cards'
        cards_path.mkdir(parents=True, exist_ok=True)
        
        # Generate variables
        variables = TemplateVariables.for_knowledge_card(
            title=title,
            main_tag=main_tag,
            source=source
        )
        
        # Apply template
        note_content = self.template_loader.apply_template("knowledge-card", variables)
        
        # Create filename (replace spaces with hyphens)
        filename = f"{title.replace(' ', '-')}.md"
        note_path = cards_path / filename
        
        # Write note
        note_path.write_text(note_content, encoding='utf-8')
        
        return note_path
    
    def create_code_snippet(
        self,
        title: str,
        language: str,
        code: str = ''
    ) -> Path:
        """
        Create a code snippet note.
        
        Args:
            title: Code snippet title
            language: Programming language
            code: Code content
        
        Returns:
            Path to the created code snippet
        """
        # Get code snippets folder
        snippets_path = self.vault_path / self.config.resources_path / 'Tech' / 'Code-Snippets'
        snippets_path.mkdir(parents=True, exist_ok=True)
        
        # Generate variables
        variables = TemplateVariables.for_code_snippet(
            title=title,
            language=language,
            code=code
        )
        
        # Apply template
        note_content = self.template_loader.apply_template("code-snippet", variables)
        
        # Create filename
        filename = f"{title.replace(' ', '-')}.md"
        note_path = snippets_path / filename
        
        # Write note
        note_path.write_text(note_content, encoding='utf-8')
        
        return note_path
    
    def create_adr(
        self,
        title: str,
        number: str,
        status: str = '提议'
    ) -> Path:
        """
        Create an ADR (Architecture Decision Record).
        
        Args:
            title: ADR title
            number: ADR number (e.g., '0001')
            status: ADR status (提议/已接受/已废弃)
        
        Returns:
            Path to the created ADR
        """
        # Get ADR folder
        adr_path = self.vault_path / self.config.resources_path / 'Tech' / 'ADR'
        adr_path.mkdir(parents=True, exist_ok=True)
        
        # Generate variables
        variables = TemplateVariables.for_adr(
            title=title,
            number=number,
            status=status
        )
        
        # Apply template
        note_content = self.template_loader.apply_template("adr", variables)
        
        # Create filename
        filename = f"ADR-{number}-{title}.md"
        note_path = adr_path / filename
        
        # Write note
        note_path.write_text(note_content, encoding='utf-8')
        
        return note_path
    
    def create_problem_solving(
        self,
        title: str,
        tech_tag: str = '技术',
        error_message: str = ''
    ) -> Path:
        """
        Create a problem solving record.
        
        Args:
            title: Problem title
            tech_tag: Technology tag
            error_message: Error message
        
        Returns:
            Path to the created problem solving record
        """
        # Get problem solving folder
        problem_path = self.vault_path / self.config.resources_path / 'Tech' / 'Problem-Solving'
        problem_path.mkdir(parents=True, exist_ok=True)
        
        # Generate variables
        variables = TemplateVariables.for_problem_solving(
            title=title,
            tech_tag=tech_tag,
            error_message=error_message
        )
        
        # Apply template
        note_content = self.template_loader.apply_template("problem-solving", variables)
        
        # Create filename
        filename = f"{title.replace(' ', '-')}.md"
        note_path = problem_path / filename
        
        # Write note
        note_path.write_text(note_content, encoding='utf-8')
        
        return note_path
