"""Tests for template system."""

import pytest
from datetime import datetime
from pathlib import Path

from obsidian_km.templates import TemplateLoader, TemplateVariables


class TestTemplateLoader:
    """Tests for TemplateLoader class."""
    
    def test_load_template_with_extension(self, test_vault_with_templates):
        """Test loading template with .md extension."""
        loader = TemplateLoader(test_vault_with_templates / "Templates")
        
        template = loader.load_template("daily-note.md")
        
        assert template
        assert "{{date}}" in template
        assert "{{day_of_week}}" in template
    
    def test_load_template_without_extension(self, test_vault_with_templates):
        """Test loading template without .md extension."""
        loader = TemplateLoader(test_vault_with_templates / "Templates")
        
        template = loader.load_template("daily-note")
        
        assert template
        assert "{{date}}" in template
    
    def test_load_nonexistent_template(self, test_vault_with_templates):
        """Test loading non-existent template raises error."""
        loader = TemplateLoader(test_vault_with_templates / "Templates")
        
        with pytest.raises(FileNotFoundError):
            loader.load_template("nonexistent")
    
    def test_replace_variables(self, test_vault_with_templates):
        """Test variable replacement."""
        loader = TemplateLoader(test_vault_with_templates / "Templates")
        
        template = "Hello {{name}}, today is {{date}}!"
        variables = {
            "name": "World",
            "date": "2024-01-15"
        }
        
        result = loader.replace_variables(template, variables)
        
        assert result == "Hello World, today is 2024-01-15!"
    
    def test_replace_variables_with_special_chars(self, test_vault_with_templates):
        """Test variable replacement with special regex characters."""
        loader = TemplateLoader(test_vault_with_templates / "Templates")
        
        template = "Path: {{path}}"
        variables = {
            "path": "C:\\Users\\test"
        }
        
        result = loader.replace_variables(template, variables)
        
        assert result == "Path: C:\\Users\\test"
    
    def test_apply_template(self, test_vault_with_templates):
        """Test applying template with variables."""
        loader = TemplateLoader(test_vault_with_templates / "Templates")
        
        variables = {
            "date": "2024-01-15",
            "day_of_week": "星期一",
            "prev_date": "2024-01-14",
            "next_date": "2024-01-16"
        }
        
        result = loader.apply_template("daily-note", variables)
        
        assert "2024-01-15" in result
        assert "星期一" in result
        assert "[[2024-01-14]]" in result
        assert "[[2024-01-16]]" in result
    
    def test_apply_template_keep_unfilled(self, test_vault_with_templates):
        """Test applying template keeping unfilled variables."""
        loader = TemplateLoader(test_vault_with_templates / "Templates")
        
        variables = {
            "date": "2024-01-15"
        }
        
        result = loader.apply_template("daily-note", variables, keep_unfilled=True)
        
        assert "2024-01-15" in result
        assert "{{day_of_week}}" in result
    
    def test_apply_template_remove_unfilled(self, test_vault_with_templates):
        """Test applying template removing unfilled variables."""
        loader = TemplateLoader(test_vault_with_templates / "Templates")
        
        variables = {
            "date": "2024-01-15"
        }
        
        result = loader.apply_template("daily-note", variables, keep_unfilled=False)
        
        assert "2024-01-15" in result
        assert "{{day_of_week}}" not in result
    
    def test_get_template_variables(self, test_vault_with_templates):
        """Test extracting variables from template."""
        loader = TemplateLoader(test_vault_with_templates / "Templates")
        
        variables = loader.get_template_variables("daily-note")
        
        assert "date" in variables
        assert "day_of_week" in variables
        assert "prev_date" in variables
        assert "next_date" in variables
    
    def test_list_templates(self, test_vault_with_templates):
        """Test listing all templates."""
        loader = TemplateLoader(test_vault_with_templates / "Templates")
        
        templates = loader.list_templates()
        
        assert "daily-note" in templates
        assert "project" in templates
        assert "meeting" in templates
        assert "knowledge-card" in templates
        assert "adr" in templates
        assert "code-snippet" in templates
        assert "problem-solving" in templates
        assert "weekly-review" in templates
        assert "monthly-review" in templates
    
    def test_list_templates_empty_dir(self, tmp_path):
        """Test listing templates in empty directory."""
        loader = TemplateLoader(tmp_path / "empty")
        
        templates = loader.list_templates()
        
        assert templates == []


class TestTemplateVariables:
    """Tests for TemplateVariables class."""
    
    def test_for_daily_note(self):
        """Test generating daily note variables."""
        date = datetime(2024, 1, 15)  # Monday
        
        variables = TemplateVariables.for_daily_note(date)
        
        assert variables['date'] == '2024-01-15'
        assert variables['day_of_week'] == '星期一'
        assert variables['prev_date'] == '2024-01-14'
        assert variables['next_date'] == '2024-01-16'
    
    def test_for_daily_note_sunday(self):
        """Test daily note variables for Sunday."""
        date = datetime(2024, 1, 14)  # Sunday
        
        variables = TemplateVariables.for_daily_note(date)
        
        assert variables['day_of_week'] == '星期日'
    
    def test_for_project_minimal(self):
        """Test generating project variables with minimal input."""
        variables = TemplateVariables.for_project(
            title="Test Project",
            category="work"
        )
        
        assert variables['title'] == 'Test Project'
        assert variables['category'] == 'work'
        assert variables['project_name'] == 'Test Project'
        assert variables['start_date']  # Should have default
        assert variables['created']
        assert variables['modified']
    
    def test_for_project_full(self):
        """Test generating project variables with all inputs."""
        variables = TemplateVariables.for_project(
            title="Test Project",
            category="personal",
            start_date="2024-01-01",
            due_date="2024-12-31",
            project_name="test-project"
        )
        
        assert variables['title'] == 'Test Project'
        assert variables['category'] == 'personal'
        assert variables['start_date'] == '2024-01-01'
        assert variables['due_date'] == '2024-12-31'
        assert variables['project_name'] == 'test-project'
    
    def test_for_meeting_minimal(self):
        """Test generating meeting variables with minimal input."""
        variables = TemplateVariables.for_meeting(
            title="Team Meeting"
        )
        
        assert variables['title'] == 'Team Meeting'
        assert variables['date']  # Should have default
        assert variables['time']  # Should have default
        assert variables['created']
    
    def test_for_meeting_full(self):
        """Test generating meeting variables with all inputs."""
        variables = TemplateVariables.for_meeting(
            title="Team Meeting",
            date="2024-01-15",
            time="14:00",
            participants="Alice, Bob, Charlie",
            project_tag="project/test"
        )
        
        assert variables['title'] == 'Team Meeting'
        assert variables['date'] == '2024-01-15'
        assert variables['time'] == '14:00'
        assert variables['participants'] == 'Alice, Bob, Charlie'
        assert variables['project_tag'] == 'project/test'
    
    def test_for_knowledge_card(self):
        """Test generating knowledge card variables."""
        variables = TemplateVariables.for_knowledge_card(
            title="React Hooks",
            main_tag="技术/前端/React",
            source="2024-01-15"
        )
        
        assert variables['title'] == 'React Hooks'
        assert variables['main_tag'] == '技术/前端/React'
        assert variables['source'] == '2024-01-15'
        assert variables['created']
    
    def test_for_adr(self):
        """Test generating ADR variables."""
        variables = TemplateVariables.for_adr(
            title="选择React作为前端框架",
            number="0001",
            status="已接受"
        )
        
        assert variables['title'] == '选择React作为前端框架'
        assert variables['number'] == '0001'
        assert variables['status'] == '已接受'
        assert variables['date']
        assert variables['created']
    
    def test_for_code_snippet(self):
        """Test generating code snippet variables."""
        variables = TemplateVariables.for_code_snippet(
            title="Python装饰器",
            language="python",
            code="def decorator(func):\n    return func"
        )
        
        assert variables['title'] == 'Python装饰器'
        assert variables['language'] == 'python'
        assert variables['language_tag'] == '技术/python'
        assert variables['code'] == "def decorator(func):\n    return func"
        assert variables['created']
    
    def test_for_problem_solving(self):
        """Test generating problem solving variables."""
        variables = TemplateVariables.for_problem_solving(
            title="解决CORS跨域问题",
            tech_tag="技术/Web",
            error_message="Access-Control-Allow-Origin error"
        )
        
        assert variables['title'] == '解决CORS跨域问题'
        assert variables['tech_tag'] == '技术/Web'
        assert variables['error_message'] == 'Access-Control-Allow-Origin error'
        assert variables['created']
    
    def test_for_weekly_review(self):
        """Test generating weekly review variables."""
        variables = TemplateVariables.for_weekly_review(
            year=2024,
            week=3,
            date_range="2024-01-15 ~ 2024-01-21",
            daily_notes_links="- [[2024-01-15]]\n- [[2024-01-16]]"
        )
        
        assert variables['title'] == '2024年第3周回顾'
        assert variables['year'] == '2024'
        assert variables['week'] == '03'
        assert variables['date_range'] == '2024-01-15 ~ 2024-01-21'
        assert variables['daily_notes_links'] == "- [[2024-01-15]]\n- [[2024-01-16]]"
        assert variables['created']
    
    def test_for_monthly_review(self):
        """Test generating monthly review variables."""
        variables = TemplateVariables.for_monthly_review(
            year=2024,
            month=1,
            weekly_reviews_links="- [[2024-W01]]\n- [[2024-W02]]"
        )
        
        assert variables['title'] == '2024年1月回顾'
        assert variables['year'] == '2024'
        assert variables['month'] == '01'
        assert variables['weekly_reviews_links'] == "- [[2024-W01]]\n- [[2024-W02]]"
        assert variables['created']


class TestTemplateIntegration:
    """Integration tests for template system."""
    
    def test_create_daily_note_from_template(self, test_vault_with_templates):
        """Test creating a daily note from template."""
        loader = TemplateLoader(test_vault_with_templates / "Templates")
        date = datetime(2024, 1, 15)
        
        variables = TemplateVariables.for_daily_note(date)
        result = loader.apply_template("daily-note", variables)
        
        assert "2024-01-15" in result
        assert "星期一" in result
        assert "[[2024-01-14]]" in result
        assert "[[2024-01-16]]" in result
        assert "## 工作板块" in result
        assert "## 学习板块" in result
        assert "## 生活板块" in result
    
    def test_create_project_from_template(self, test_vault_with_templates):
        """Test creating a project from template."""
        loader = TemplateLoader(test_vault_with_templates / "Templates")
        
        variables = TemplateVariables.for_project(
            title="电商系统",
            category="work",
            start_date="2024-01-01",
            due_date="2024-03-31"
        )
        result = loader.apply_template("project", variables)
        
        assert "电商系统" in result
        assert "work" in result
        assert "2024-01-01" in result
        assert "2024-03-31" in result
        assert "## 项目概述" in result
        assert "## 里程碑" in result
        assert "## 任务列表" in result
    
    def test_create_meeting_from_template(self, test_vault_with_templates):
        """Test creating a meeting note from template."""
        loader = TemplateLoader(test_vault_with_templates / "Templates")
        
        variables = TemplateVariables.for_meeting(
            title="技术方案讨论",
            date="2024-01-15",
            time="14:00",
            participants="张三, 李四"
        )
        result = loader.apply_template("meeting", variables)
        
        assert "技术方案讨论" in result
        assert "2024-01-15" in result
        assert "14:00" in result
        assert "张三, 李四" in result
        assert "## 会议议题" in result
        assert "## 决策事项" in result
    
    def test_create_knowledge_card_from_template(self, test_vault_with_templates):
        """Test creating a knowledge card from template."""
        loader = TemplateLoader(test_vault_with_templates / "Templates")
        
        variables = TemplateVariables.for_knowledge_card(
            title="React Hooks闭包陷阱",
            main_tag="技术/前端/React",
            source="2024-01-15"
        )
        result = loader.apply_template("knowledge-card", variables)
        
        assert "React Hooks闭包陷阱" in result
        assert "技术/前端/React" in result
        assert "[[2024-01-15]]" in result
        assert "## 核心概念" in result
        assert "## 详细说明" in result
