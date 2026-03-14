"""Tests for note creator."""

import pytest
from datetime import datetime, timedelta
from pathlib import Path
from hypothesis import given, strategies as st, settings, HealthCheck

from obsidian_km.notes import NoteCreator
from obsidian_km.config import Config


class TestNoteCreatorDailyNotes:
    """Tests for daily note creation."""
    
    def test_get_daily_note_path(self, test_vault_with_templates):
        """Test getting daily note path."""
        config = Config(vault_path=str(test_vault_with_templates))
        creator = NoteCreator(config)
        
        date = datetime(2024, 1, 15)
        path = creator.get_daily_note_path(date)
        
        assert path == test_vault_with_templates / "0-Daily" / "2024" / "01" / "2024-01-15.md"
    
    def test_create_daily_note(self, test_vault_with_templates):
        """Test creating a daily note."""
        config = Config(vault_path=str(test_vault_with_templates))
        creator = NoteCreator(config)
        
        date = datetime(2024, 1, 15)
        note_path = creator.create_daily_note(date)
        
        assert note_path.exists()
        assert note_path.name == "2024-01-15.md"
        
        content = note_path.read_text(encoding='utf-8')
        assert "2024-01-15" in content
        assert "星期一" in content
        assert "[[2024-01-14]]" in content
        assert "[[2024-01-16]]" in content
    
    def test_create_daily_note_with_content(self, test_vault_with_templates):
        """Test creating a daily note with additional content."""
        config = Config(vault_path=str(test_vault_with_templates))
        creator = NoteCreator(config)
        
        date = datetime(2024, 1, 15)
        additional_content = "今天完成了重要任务"
        note_path = creator.create_daily_note(date, content=additional_content)
        
        content = note_path.read_text(encoding='utf-8')
        assert additional_content in content
    
    def test_create_daily_note_default_date(self, test_vault_with_templates):
        """Test creating a daily note with default date (today)."""
        config = Config(vault_path=str(test_vault_with_templates))
        creator = NoteCreator(config)
        
        note_path = creator.create_daily_note()
        
        assert note_path.exists()
        today = datetime.now().strftime('%Y-%m-%d')
        assert today in note_path.name


class TestNoteCreatorProjects:
    """Tests for project creation."""
    
    def test_get_project_path_work(self, test_vault_with_templates):
        """Test getting work project path."""
        config = Config(vault_path=str(test_vault_with_templates))
        creator = NoteCreator(config)
        
        path = creator.get_project_path("TestProject", category="work")
        
        assert path == test_vault_with_templates / "1-Projects" / "Work" / "TestProject"
    
    def test_get_project_path_personal(self, test_vault_with_templates):
        """Test getting personal project path."""
        config = Config(vault_path=str(test_vault_with_templates))
        creator = NoteCreator(config)
        
        path = creator.get_project_path("TestProject", category="personal")
        
        assert path == test_vault_with_templates / "1-Projects" / "Personal" / "TestProject"
    
    def test_create_project_work(self, test_vault_with_templates):
        """Test creating a work project."""
        config = Config(vault_path=str(test_vault_with_templates))
        creator = NoteCreator(config)
        
        readme_path = creator.create_project(
            title="电商系统",
            category="work",
            start_date="2024-01-01",
            due_date="2024-12-31"
        )
        
        assert readme_path.exists()
        assert readme_path.name == "README.md"
        assert "Work" in str(readme_path)
        
        content = readme_path.read_text(encoding='utf-8')
        assert "电商系统" in content
        assert "2024-01-01" in content
        assert "2024-12-31" in content
    
    def test_create_project_personal(self, test_vault_with_templates):
        """Test creating a personal project."""
        config = Config(vault_path=str(test_vault_with_templates))
        creator = NoteCreator(config)
        
        readme_path = creator.create_project(
            title="买房计划",
            category="personal"
        )
        
        assert readme_path.exists()
        assert "Personal" in str(readme_path)
        
        content = readme_path.read_text(encoding='utf-8')
        assert "买房计划" in content
    
    def test_create_project_custom_name(self, test_vault_with_templates):
        """Test creating a project with custom folder name."""
        config = Config(vault_path=str(test_vault_with_templates))
        creator = NoteCreator(config)
        
        readme_path = creator.create_project(
            title="E-commerce System",
            category="work",
            project_name="ecommerce"
        )
        
        assert "ecommerce" in str(readme_path)


class TestNoteCreatorOtherTypes:
    """Tests for other note types."""
    
    def test_create_meeting_note(self, test_vault_with_templates):
        """Test creating a meeting note."""
        config = Config(vault_path=str(test_vault_with_templates))
        creator = NoteCreator(config)
        
        note_path = creator.create_meeting_note(
            title="技术方案讨论",
            date="2024-01-15",
            time="14:00",
            participants="张三, 李四"
        )
        
        assert note_path.exists()
        assert "技术方案讨论" in note_path.name
        
        content = note_path.read_text(encoding='utf-8')
        assert "技术方案讨论" in content
        assert "2024-01-15" in content
        assert "14:00" in content
        assert "张三, 李四" in content
    
    def test_create_meeting_note_custom_location(self, test_vault_with_templates):
        """Test creating a meeting note in custom location."""
        config = Config(vault_path=str(test_vault_with_templates))
        creator = NoteCreator(config)
        
        custom_location = test_vault_with_templates / "1-Projects" / "Work" / "TestProject"
        custom_location.mkdir(parents=True, exist_ok=True)
        
        note_path = creator.create_meeting_note(
            title="项目会议",
            location=custom_location
        )
        
        assert note_path.exists()
        assert custom_location in note_path.parents
    
    def test_create_knowledge_card(self, test_vault_with_templates):
        """Test creating a knowledge card."""
        config = Config(vault_path=str(test_vault_with_templates))
        creator = NoteCreator(config)
        
        note_path = creator.create_knowledge_card(
            title="React Hooks闭包陷阱",
            main_tag="技术/前端/React",
            source="2024-01-15"
        )
        
        assert note_path.exists()
        assert "Knowledge-Cards" in str(note_path)
        
        content = note_path.read_text(encoding='utf-8')
        assert "React Hooks闭包陷阱" in content
        assert "技术/前端/React" in content
    
    def test_create_code_snippet(self, test_vault_with_templates):
        """Test creating a code snippet."""
        config = Config(vault_path=str(test_vault_with_templates))
        creator = NoteCreator(config)
        
        code = "def hello():\n    print('Hello, World!')"
        note_path = creator.create_code_snippet(
            title="Python Hello World",
            language="python",
            code=code
        )
        
        assert note_path.exists()
        assert "Code-Snippets" in str(note_path)
        
        content = note_path.read_text(encoding='utf-8')
        assert "Python Hello World" in content
        assert "python" in content
        assert code in content
    
    def test_create_adr(self, test_vault_with_templates):
        """Test creating an ADR."""
        config = Config(vault_path=str(test_vault_with_templates))
        creator = NoteCreator(config)
        
        note_path = creator.create_adr(
            title="选择React作为前端框架",
            number="0001",
            status="已接受"
        )
        
        assert note_path.exists()
        assert "ADR" in str(note_path)
        assert "ADR-0001" in note_path.name
        
        content = note_path.read_text(encoding='utf-8')
        assert "选择React作为前端框架" in content
        assert "已接受" in content
    
    def test_create_problem_solving(self, test_vault_with_templates):
        """Test creating a problem solving record."""
        config = Config(vault_path=str(test_vault_with_templates))
        creator = NoteCreator(config)
        
        note_path = creator.create_problem_solving(
            title="解决CORS跨域问题",
            tech_tag="技术/Web",
            error_message="Access-Control-Allow-Origin error"
        )
        
        assert note_path.exists()
        assert "Problem-Solving" in str(note_path)
        
        content = note_path.read_text(encoding='utf-8')
        assert "解决CORS跨域问题" in content
        assert "技术/Web" in content
        assert "Access-Control-Allow-Origin error" in content


# Feature: obsidian-knowledge-management-workflow, Property 8: 日期文件夹路径生成
@given(date=st.dates(min_value=datetime(2000, 1, 1).date(), 
                     max_value=datetime(2099, 12, 31).date()))
@settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
def test_property_daily_note_path_format(test_vault_with_templates, date):
    """
    Property 8: 对于任意日期，日常笔记路径应该遵循正确格式.
    
    验证需求: 1.5, 2.1
    """
    config = Config(vault_path=str(test_vault_with_templates))
    creator = NoteCreator(config)
    
    # Convert date to datetime
    dt = datetime.combine(date, datetime.min.time())
    
    note_path = creator.get_daily_note_path(dt)
    
    # Verify path format: 0-Daily/YYYY/MM/YYYY-MM-DD.md
    expected_suffix = f"0-Daily/{dt.year}/{dt.month:02d}/{dt.strftime('%Y-%m-%d')}.md"
    assert str(note_path).endswith(expected_suffix)
    
    # Verify path components
    parts = note_path.parts
    assert "0-Daily" in parts
    assert str(dt.year) in parts
    assert f"{dt.month:02d}" in parts
    assert note_path.name == f"{dt.strftime('%Y-%m-%d')}.md"


# Feature: obsidian-knowledge-management-workflow, Property 9: 日常笔记导航链接
@given(date=st.dates(min_value=datetime(2000, 1, 2).date(),  # Avoid edge case at year boundary
                     max_value=datetime(2099, 12, 30).date()))
@settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
def test_property_daily_note_navigation_links(test_vault_with_templates, date):
    """
    Property 9: 对于任意日期的日常笔记，应该包含正确的导航链接.
    
    验证需求: 2.6
    """
    config = Config(vault_path=str(test_vault_with_templates))
    creator = NoteCreator(config)
    
    # Convert date to datetime
    dt = datetime.combine(date, datetime.min.time())
    
    note_path = creator.create_daily_note(dt)
    content = note_path.read_text(encoding='utf-8')
    
    # Calculate expected dates
    prev_date = dt - timedelta(days=1)
    next_date = dt + timedelta(days=1)
    
    # Verify navigation links
    assert f"[[{prev_date.strftime('%Y-%m-%d')}]]" in content
    assert f"[[{next_date.strftime('%Y-%m-%d')}]]" in content


# Feature: obsidian-knowledge-management-workflow, Property 10: 项目文件夹创建
@given(
    project_name=st.text(min_size=1, max_size=50, alphabet=st.characters(
        whitelist_categories=('Lu', 'Ll', 'Nd'),
        whitelist_characters='-_'
    )),
    category=st.sampled_from(['work', 'personal'])
)
@settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
def test_property_project_folder_creation(test_vault_with_templates, project_name, category):
    """
    Property 10: 对于任意项目名称和类型，应该在正确路径创建文件夹.
    
    验证需求: 3.4, 3.5
    """
    config = Config(vault_path=str(test_vault_with_templates))
    creator = NoteCreator(config)
    
    # Skip if project name is empty after stripping
    if not project_name.strip():
        return
    
    readme_path = creator.create_project(
        title=project_name,
        category=category,
        project_name=project_name
    )
    
    # Verify project folder exists
    project_folder = readme_path.parent
    assert project_folder.exists()
    assert project_folder.is_dir()
    
    # Verify correct category path
    category_folder = 'Work' if category == 'work' else 'Personal'
    expected_path = test_vault_with_templates / "1-Projects" / category_folder / project_name
    assert project_folder == expected_path
    
    # Verify README exists
    assert readme_path.exists()
    assert readme_path.name == "README.md"


class TestNoteCreatorEdgeCases:
    """Tests for edge cases and error handling."""
    
    def test_create_daily_note_year_boundary(self, test_vault_with_templates):
        """Test creating daily notes at year boundary."""
        config = Config(vault_path=str(test_vault_with_templates))
        creator = NoteCreator(config)
        
        # New Year's Eve
        date1 = datetime(2023, 12, 31)
        note1 = creator.create_daily_note(date1)
        content1 = note1.read_text(encoding='utf-8')
        
        assert "[[2023-12-30]]" in content1
        assert "[[2024-01-01]]" in content1
        
        # New Year's Day
        date2 = datetime(2024, 1, 1)
        note2 = creator.create_daily_note(date2)
        content2 = note2.read_text(encoding='utf-8')
        
        assert "[[2023-12-31]]" in content2
        assert "[[2024-01-02]]" in content2
    
    def test_create_project_with_special_chars(self, test_vault_with_templates):
        """Test creating project with special characters in name."""
        config = Config(vault_path=str(test_vault_with_templates))
        creator = NoteCreator(config)
        
        # Use a safe project name for folder
        readme_path = creator.create_project(
            title="项目：电商系统 (2024)",
            category="work",
            project_name="ecommerce-2024"
        )
        
        assert readme_path.exists()
        content = readme_path.read_text(encoding='utf-8')
        assert "项目：电商系统 (2024)" in content
    
    def test_create_multiple_notes_same_day(self, test_vault_with_templates):
        """Test creating multiple notes on the same day overwrites."""
        config = Config(vault_path=str(test_vault_with_templates))
        creator = NoteCreator(config)
        
        date = datetime(2024, 1, 15)
        
        # Create first note
        note1 = creator.create_daily_note(date, content="First content")
        content1 = note1.read_text(encoding='utf-8')
        assert "First content" in content1
        
        # Create second note (should overwrite)
        note2 = creator.create_daily_note(date, content="Second content")
        content2 = note2.read_text(encoding='utf-8')
        assert "Second content" in content2
        assert "First content" not in content2
        
        # Verify same path
        assert note1 == note2
