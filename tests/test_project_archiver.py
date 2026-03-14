"""Tests for project archiver."""

import pytest
from datetime import datetime
from pathlib import Path
from hypothesis import given, strategies as st, settings, assume, HealthCheck

from obsidian_km.archive import ProjectArchiver
from obsidian_km.config import Config


class TestProjectArchiver:
    """Test project archiver functionality."""
    
    def test_get_archive_path_default_year(self, test_vault):
        """Test getting archive path with default year."""
        config = Config(vault_path=str(test_vault))
        archiver = ProjectArchiver(config)
        
        current_year = datetime.now().year
        archive_path = archiver.get_archive_path("TestProject")
        
        expected = test_vault / "4-Archives" / str(current_year) / "TestProject"
        assert archive_path == expected
    
    def test_get_archive_path_specific_year(self, test_vault):
        """Test getting archive path with specific year."""
        config = Config(vault_path=str(test_vault))
        archiver = ProjectArchiver(config)
        
        archive_path = archiver.get_archive_path("TestProject", year=2023)
        
        expected = test_vault / "4-Archives" / "2023" / "TestProject"
        assert archive_path == expected
    
    def test_archive_project_basic(self, test_vault_with_templates):
        """Test basic project archiving."""
        config = Config(vault_path=str(test_vault_with_templates))
        archiver = ProjectArchiver(config)
        
        # Create a test project
        project_path = test_vault_with_templates / "1-Projects" / "Work" / "TestProject"
        project_path.mkdir(parents=True)
        
        readme_path = project_path / "README.md"
        readme_path.write_text("# Test Project\n\nProject content")
        
        # Archive the project
        archive_dest = archiver.archive_project(project_path)
        
        # Verify project was moved
        assert not project_path.exists()
        assert archive_dest.exists()
        assert archive_dest.is_dir()
        
        # Verify archive path
        current_year = datetime.now().year
        expected_dest = test_vault_with_templates / "4-Archives" / str(current_year) / "TestProject"
        assert archive_dest == expected_dest
        
        # Verify README exists in archive
        archived_readme = archive_dest / "README.md"
        assert archived_readme.exists()
    
    def test_archive_project_with_metadata(self, test_vault_with_templates):
        """Test archiving project with YAML front matter."""
        config = Config(vault_path=str(test_vault_with_templates))
        archiver = ProjectArchiver(config)
        
        # Create a test project with YAML front matter
        project_path = test_vault_with_templates / "1-Projects" / "Work" / "TestProject"
        project_path.mkdir(parents=True)
        
        readme_content = """---
title: Test Project
type: project
status: 已完成
---

# Test Project

Project content
"""
        readme_path = project_path / "README.md"
        readme_path.write_text(readme_content)
        
        # Archive the project
        archive_date = "2024-01-15"
        archive_dest = archiver.archive_project(project_path, archive_date=archive_date)
        
        # Verify archived_date was added
        archived_readme = archive_dest / "README.md"
        content = archived_readme.read_text()
        
        assert "archived_date: 2024-01-15" in content
        assert "title: Test Project" in content
        assert "status: 已完成" in content
    
    def test_archive_project_without_yaml(self, test_vault_with_templates):
        """Test archiving project without YAML front matter."""
        config = Config(vault_path=str(test_vault_with_templates))
        archiver = ProjectArchiver(config)
        
        # Create a test project without YAML
        project_path = test_vault_with_templates / "1-Projects" / "Work" / "TestProject"
        project_path.mkdir(parents=True)
        
        readme_content = "# Test Project\n\nProject content"
        readme_path = project_path / "README.md"
        readme_path.write_text(readme_content)
        
        # Archive the project
        archive_date = "2024-01-15"
        archive_dest = archiver.archive_project(project_path, archive_date=archive_date)
        
        # Verify YAML front matter was added
        archived_readme = archive_dest / "README.md"
        content = archived_readme.read_text()
        
        assert content.startswith("---\n")
        assert "archived_date: 2024-01-15" in content
        assert "# Test Project" in content
    
    def test_archive_project_preserves_content(self, test_vault_with_templates):
        """Test that archiving preserves all file content."""
        config = Config(vault_path=str(test_vault_with_templates))
        archiver = ProjectArchiver(config)
        
        # Create a test project with multiple files
        project_path = test_vault_with_templates / "1-Projects" / "Work" / "TestProject"
        project_path.mkdir(parents=True)
        
        # Create README
        readme_content = "# Test Project\n\n[[OtherNote]] #project/test"
        (project_path / "README.md").write_text(readme_content)
        
        # Create other files
        (project_path / "notes.md").write_text("Some notes with [[links]]")
        (project_path / "tasks.md").write_text("- [ ] Task 1 #important")
        
        # Create subfolder
        subfolder = project_path / "docs"
        subfolder.mkdir()
        (subfolder / "design.md").write_text("Design document")
        
        # Archive the project
        archive_dest = archiver.archive_project(project_path)
        
        # Verify all files exist and content is preserved
        assert (archive_dest / "README.md").exists()
        assert (archive_dest / "notes.md").exists()
        assert (archive_dest / "tasks.md").exists()
        assert (archive_dest / "docs" / "design.md").exists()
        
        # Verify content is preserved
        notes_content = (archive_dest / "notes.md").read_text()
        assert "[[links]]" in notes_content
        
        tasks_content = (archive_dest / "tasks.md").read_text()
        assert "#important" in tasks_content
    
    def test_archive_project_nonexistent_path(self, test_vault):
        """Test archiving nonexistent project raises error."""
        config = Config(vault_path=str(test_vault))
        archiver = ProjectArchiver(config)
        
        nonexistent_path = test_vault / "1-Projects" / "Work" / "NonExistent"
        
        with pytest.raises(FileNotFoundError):
            archiver.archive_project(nonexistent_path)
    
    def test_archive_project_file_not_directory(self, test_vault):
        """Test archiving a file instead of directory raises error."""
        config = Config(vault_path=str(test_vault))
        archiver = ProjectArchiver(config)
        
        # Create a file instead of directory
        file_path = test_vault / "1-Projects" / "test.md"
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text("Not a directory")
        
        with pytest.raises(ValueError):
            archiver.archive_project(file_path)
    
    def test_archive_project_without_readme(self, test_vault_with_templates):
        """Test archiving project without README.md."""
        config = Config(vault_path=str(test_vault_with_templates))
        archiver = ProjectArchiver(config)
        
        # Create a test project without README
        project_path = test_vault_with_templates / "1-Projects" / "Work" / "TestProject"
        project_path.mkdir(parents=True)
        
        (project_path / "notes.md").write_text("Some notes")
        
        # Archive the project (should not fail)
        archive_dest = archiver.archive_project(project_path)
        
        # Verify project was moved
        assert archive_dest.exists()
        assert (archive_dest / "notes.md").exists()
    
    def test_archive_project_updates_existing_archived_date(self, test_vault_with_templates):
        """Test that archiving updates existing archived_date field."""
        config = Config(vault_path=str(test_vault_with_templates))
        archiver = ProjectArchiver(config)
        
        # Create a test project with existing archived_date
        project_path = test_vault_with_templates / "1-Projects" / "Work" / "TestProject"
        project_path.mkdir(parents=True)
        
        readme_content = """---
title: Test Project
archived_date: 2023-12-31
---

# Test Project
"""
        readme_path = project_path / "README.md"
        readme_path.write_text(readme_content)
        
        # Archive the project with new date
        archive_date = "2024-01-15"
        archive_dest = archiver.archive_project(project_path, archive_date=archive_date)
        
        # Verify archived_date was updated
        archived_readme = archive_dest / "README.md"
        content = archived_readme.read_text()
        
        assert "archived_date: 2024-01-15" in content
        assert "archived_date: 2023-12-31" not in content


# Feature: obsidian-knowledge-management-workflow, Property 14: 项目归档路径生成
@given(
    project_name=st.text(min_size=1, max_size=50, alphabet=st.characters(
        whitelist_categories=('Lu', 'Ll', 'Nd'),
        whitelist_characters='-_'
    )),
    year=st.integers(min_value=2000, max_value=2099)
)
@settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
def test_property_archive_path_generation(tmp_path_factory, project_name, year):
    """
    Property 14: 对于任意项目，归档后应该在正确的路径.
    
    **验证需求: 13.1, 13.4**
    """
    # Skip empty project names
    if not project_name.strip():
        assume(False)
    
    # Create a temporary vault
    test_vault = tmp_path_factory.mktemp("vault")
    config = Config(vault_path=str(test_vault))
    archiver = ProjectArchiver(config)
    
    # Get archive path
    archive_path = archiver.get_archive_path(project_name, year=year)
    
    # Verify path format: 4-Archives/YYYY/project_name
    assert archive_path.parent.parent.name == "4-Archives"
    assert archive_path.parent.name == str(year)
    assert archive_path.name == project_name
    
    # Verify full path
    expected_path = test_vault / "4-Archives" / str(year) / project_name
    assert archive_path == expected_path


# Feature: obsidian-knowledge-management-workflow, Property 15: 归档保持内容完整性
@given(
    num_files=st.integers(min_value=1, max_value=10),
    has_links=st.booleans(),
    has_tags=st.booleans()
)
@settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
def test_property_archive_preserves_content(tmp_path_factory, num_files, has_links, has_tags):
    """
    Property 15: 对于任意项目，归档前后内容应该完全一致.
    
    **验证需求: 13.2**
    """
    # Create a temporary vault with PARA structure
    test_vault = tmp_path_factory.mktemp("vault")
    
    # Create PARA structure
    projects_path = test_vault / "1-Projects" / "Work"
    projects_path.mkdir(parents=True)
    
    archives_path = test_vault / "4-Archives"
    archives_path.mkdir(parents=True)
    
    config = Config(vault_path=str(test_vault))
    archiver = ProjectArchiver(config)
    
    # Create a test project with multiple files
    project_path = projects_path / "TestProject"
    project_path.mkdir()
    
    # Store original content for verification
    original_content = {}
    
    for i in range(num_files):
        file_name = f"file{i}.md"
        content = f"# File {i}\n\nContent for file {i}"
        
        if has_links:
            content += f"\n\n[[Link{i}]] [[AnotherLink]]"
        
        if has_tags:
            content += f"\n\n#tag{i} #project/test #important"
        
        file_path = project_path / file_name
        file_path.write_text(content)
        original_content[file_name] = content
    
    # Archive the project
    archive_dest = archiver.archive_project(project_path)
    
    # Verify all files exist and content is identical
    for file_name, original in original_content.items():
        archived_file = archive_dest / file_name
        assert archived_file.exists()
        
        archived_content = archived_file.read_text()
        
        # Content should be identical (except README.md which gets metadata)
        if file_name == "README.md":
            # README might have added YAML, but original content should be preserved
            assert original in archived_content or archived_content.replace("---\narchived_date:", "").strip().startswith(original.strip())
        else:
            assert archived_content == original


# Feature: obsidian-knowledge-management-workflow, Property 16: 归档添加元数据
@given(
    archive_date=st.dates(min_value=datetime(2000, 1, 1).date(),
                          max_value=datetime(2099, 12, 31).date()),
    has_yaml=st.booleans()
)
@settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
def test_property_archive_adds_metadata(tmp_path_factory, archive_date, has_yaml):
    """
    Property 16: 对于任意归档项目，应该包含归档日期字段.
    
    **验证需求: 13.3**
    """
    # Create a temporary vault with PARA structure
    test_vault = tmp_path_factory.mktemp("vault")
    
    # Create PARA structure
    projects_path = test_vault / "1-Projects" / "Work"
    projects_path.mkdir(parents=True)
    
    archives_path = test_vault / "4-Archives"
    archives_path.mkdir(parents=True)
    
    config = Config(vault_path=str(test_vault))
    archiver = ProjectArchiver(config)
    
    # Create a test project
    project_path = projects_path / "TestProject"
    project_path.mkdir()
    
    # Create README with or without YAML
    if has_yaml:
        readme_content = """---
title: Test Project
type: project
---

# Test Project

Content
"""
    else:
        readme_content = "# Test Project\n\nContent"
    
    readme_path = project_path / "README.md"
    readme_path.write_text(readme_content)
    
    # Archive the project
    archive_date_str = archive_date.strftime('%Y-%m-%d')
    archive_dest = archiver.archive_project(project_path, archive_date=archive_date_str)
    
    # Verify archived_date field exists in README
    archived_readme = archive_dest / "README.md"
    assert archived_readme.exists()
    
    content = archived_readme.read_text()
    
    # Should have YAML front matter
    assert content.startswith("---\n")
    
    # Should contain archived_date field
    assert f"archived_date: {archive_date_str}" in content
    
    # Original content should be preserved
    if has_yaml:
        assert "title: Test Project" in content
        assert "type: project" in content
    
    assert "# Test Project" in content
    assert "Content" in content


class TestProjectArchiverEdgeCases:
    """Tests for edge cases and error handling."""
    
    def test_archive_project_with_special_characters(self, test_vault_with_templates):
        """Test archiving project with special characters in name."""
        config = Config(vault_path=str(test_vault_with_templates))
        archiver = ProjectArchiver(config)
        
        # Create a test project with special characters
        project_path = test_vault_with_templates / "1-Projects" / "Work" / "项目-2024"
        project_path.mkdir(parents=True)
        
        (project_path / "README.md").write_text("# 项目-2024")
        
        # Archive the project
        archive_dest = archiver.archive_project(project_path)
        
        # Verify project was moved
        assert archive_dest.exists()
        assert archive_dest.name == "项目-2024"
    
    def test_archive_project_with_nested_folders(self, test_vault_with_templates):
        """Test archiving project with nested folder structure."""
        config = Config(vault_path=str(test_vault_with_templates))
        archiver = ProjectArchiver(config)
        
        # Create a test project with nested folders
        project_path = test_vault_with_templates / "1-Projects" / "Work" / "TestProject"
        project_path.mkdir(parents=True)
        
        # Create nested structure
        (project_path / "README.md").write_text("# Test")
        (project_path / "docs").mkdir()
        (project_path / "docs" / "api").mkdir()
        (project_path / "docs" / "api" / "spec.md").write_text("API Spec")
        (project_path / "src").mkdir()
        (project_path / "src" / "main.py").write_text("print('hello')")
        
        # Archive the project
        archive_dest = archiver.archive_project(project_path)
        
        # Verify nested structure is preserved
        assert (archive_dest / "docs" / "api" / "spec.md").exists()
        assert (archive_dest / "src" / "main.py").exists()
        
        # Verify content is preserved
        spec_content = (archive_dest / "docs" / "api" / "spec.md").read_text()
        assert spec_content == "API Spec"
    
    def test_archive_project_malformed_yaml(self, test_vault_with_templates):
        """Test archiving project with malformed YAML front matter."""
        config = Config(vault_path=str(test_vault_with_templates))
        archiver = ProjectArchiver(config)
        
        # Create a test project with malformed YAML
        project_path = test_vault_with_templates / "1-Projects" / "Work" / "TestProject"
        project_path.mkdir(parents=True)
        
        # Malformed YAML (missing closing ---)
        readme_content = """---
title: Test Project
type: project

# Test Project

Content
"""
        readme_path = project_path / "README.md"
        readme_path.write_text(readme_content)
        
        # Archive the project (should handle gracefully)
        archive_dest = archiver.archive_project(project_path)
        
        # Verify archived_date was added
        archived_readme = archive_dest / "README.md"
        content = archived_readme.read_text()
        
        assert "archived_date:" in content
    
    def test_archive_project_empty_folder(self, test_vault_with_templates):
        """Test archiving an empty project folder."""
        config = Config(vault_path=str(test_vault_with_templates))
        archiver = ProjectArchiver(config)
        
        # Create an empty project folder
        project_path = test_vault_with_templates / "1-Projects" / "Work" / "EmptyProject"
        project_path.mkdir(parents=True)
        
        # Archive the project
        archive_dest = archiver.archive_project(project_path)
        
        # Verify project was moved
        assert archive_dest.exists()
        assert archive_dest.is_dir()
        assert not project_path.exists()
    
    def test_archive_project_year_boundary(self, test_vault_with_templates):
        """Test archiving projects in different years."""
        config = Config(vault_path=str(test_vault_with_templates))
        archiver = ProjectArchiver(config)
        
        # Create two projects
        project1_path = test_vault_with_templates / "1-Projects" / "Work" / "Project2023"
        project1_path.mkdir(parents=True)
        (project1_path / "README.md").write_text("# Project 2023")
        
        project2_path = test_vault_with_templates / "1-Projects" / "Work" / "Project2024"
        project2_path.mkdir(parents=True)
        (project2_path / "README.md").write_text("# Project 2024")
        
        # Archive to different years
        archive1 = archiver.archive_project(project1_path, archive_date="2023-12-31")
        archive2 = archiver.archive_project(project2_path, archive_date="2024-01-15")
        
        # Verify they're in different year folders
        assert "2023" in str(archive1)
        assert "2024" in str(archive2)
        assert archive1.parent != archive2.parent
