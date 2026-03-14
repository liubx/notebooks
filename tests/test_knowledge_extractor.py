"""Tests for knowledge card extractor."""

import pytest
from datetime import datetime
from pathlib import Path

from obsidian_km.knowledge import KnowledgeExtractor
from obsidian_km.knowledge.extractor import KnowledgePoint
from obsidian_km.config import Config
from obsidian_km.notes import NoteCreator


class TestKnowledgePointDataClass:
    """Tests for KnowledgePoint data class."""
    
    def test_create_knowledge_point(self, tmp_path):
        """Test creating a valid knowledge point."""
        kp = KnowledgePoint(
            title="React Hooks闭包陷阱",
            content="学习了React Hooks中的闭包陷阱问题",
            source_file=tmp_path / "test.md",
            source_section="学习板块",
            tags=["技术", "前端", "React"],
            value_score=0.8
        )
        
        assert kp.title == "React Hooks闭包陷阱"
        assert kp.value_score == 0.8
        assert len(kp.tags) == 3
    
    def test_knowledge_point_empty_title_raises_error(self, tmp_path):
        """Test that empty title raises ValueError."""
        with pytest.raises(ValueError, match="title cannot be empty"):
            KnowledgePoint(
                title="",
                content="Some content",
                source_file=tmp_path / "test.md",
                source_section="Section",
                tags=["技术"],
                value_score=0.5
            )
    
    def test_knowledge_point_invalid_score_raises_error(self, tmp_path):
        """Test that invalid value score raises ValueError."""
        with pytest.raises(ValueError, match="Value score must be between"):
            KnowledgePoint(
                title="Test",
                content="Content",
                source_file=tmp_path / "test.md",
                source_section="Section",
                tags=["技术"],
                value_score=1.5
            )


class TestKnowledgeExtractorSectionExtraction:
    """Tests for section extraction from notes."""
    
    def test_extract_sections_with_headings(self, test_vault_with_templates):
        """Test extracting sections from note with headings."""
        config = Config(vault_path=str(test_vault_with_templates))
        extractor = KnowledgeExtractor(config)
        
        content = """# Daily Note

## 学习板块

学习了React Hooks的使用方法。

## 工作板块

完成了项目任务。
"""
        
        sections = extractor._extract_sections(content)
        
        # Should have 3 sections: content before first ##, 学习板块, 工作板块
        assert len(sections) == 3
        assert sections[1][0] == "学习板块"
        assert "React Hooks" in sections[1][1]
        assert sections[2][0] == "工作板块"
    
    def test_extract_sections_without_headings(self, test_vault_with_templates):
        """Test extracting sections from note without headings."""
        config = Config(vault_path=str(test_vault_with_templates))
        extractor = KnowledgeExtractor(config)
        
        content = "This is a note without any headings."
        
        sections = extractor._extract_sections(content)
        
        assert len(sections) == 1
        assert sections[0][0] == ""
        assert sections[0][1] == content
    
    def test_extract_sections_with_triple_hash(self, test_vault_with_templates):
        """Test extracting sections with ### headings."""
        config = Config(vault_path=str(test_vault_with_templates))
        extractor = KnowledgeExtractor(config)
        
        content = """## Main Section

### Subsection 1

Content 1

### Subsection 2

Content 2
"""
        
        sections = extractor._extract_sections(content)
        
        assert len(sections) == 3
        assert sections[0][0] == "Main Section"
        assert sections[1][0] == "Subsection 1"
        assert sections[2][0] == "Subsection 2"


class TestKnowledgeExtractorValueEvaluation:
    """Tests for knowledge value evaluation."""
    
    def test_evaluate_with_knowledge_indicators(self, test_vault_with_templates):
        """Test evaluation with knowledge indicators."""
        config = Config(vault_path=str(test_vault_with_templates))
        extractor = KnowledgeExtractor(config)
        
        content = "学习了React Hooks的使用方法，理解了闭包陷阱的原理。"
        
        score = extractor._evaluate_knowledge_value(content)
        
        # Should have positive score due to indicators
        assert score > 0.0
    
    def test_evaluate_with_code_blocks(self, test_vault_with_templates):
        """Test evaluation with code blocks."""
        config = Config(vault_path=str(test_vault_with_templates))
        extractor = KnowledgeExtractor(config)
        
        content = """学习了Python装饰器：

```python
def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper
```
"""
        
        score = extractor._evaluate_knowledge_value(content)
        
        # Should have high score due to code block and indicator
        assert score > 0.3
    
    def test_evaluate_with_lists(self, test_vault_with_templates):
        """Test evaluation with lists."""
        config = Config(vault_path=str(test_vault_with_templates))
        extractor = KnowledgeExtractor(config)
        
        content = """总结了最佳实践：

- 使用useState管理状态
- 使用useEffect处理副作用
- 避免在循环中使用Hooks
"""
        
        score = extractor._evaluate_knowledge_value(content)
        
        # Should have positive score due to list and indicators
        assert score > 0.2
    
    def test_evaluate_short_content(self, test_vault_with_templates):
        """Test evaluation with short content."""
        config = Config(vault_path=str(test_vault_with_templates))
        extractor = KnowledgeExtractor(config)
        
        content = "今天很忙。"
        
        score = extractor._evaluate_knowledge_value(content)
        
        # Should have low score
        assert score < 0.3
    
    def test_evaluate_with_technical_tags(self, test_vault_with_templates):
        """Test evaluation with technical tags."""
        config = Config(vault_path=str(test_vault_with_templates))
        extractor = KnowledgeExtractor(config)
        
        content = "学习了新的技术栈 #技术/前端/React"
        
        score = extractor._evaluate_knowledge_value(content)
        
        # Should have positive score due to tag and indicator
        assert score >= 0.2


class TestKnowledgeExtractorTagExtraction:
    """Tests for tag extraction."""
    
    def test_extract_tags_from_content(self, test_vault_with_templates):
        """Test extracting tags from content."""
        config = Config(vault_path=str(test_vault_with_templates))
        extractor = KnowledgeExtractor(config)
        
        content = "学习了React #技术/前端/React #学习"
        
        tags = extractor._extract_tags(content)
        
        assert "技术/前端/React" in tags
        assert "学习" in tags
    
    def test_extract_tags_no_tags(self, test_vault_with_templates):
        """Test extracting tags when no tags present."""
        config = Config(vault_path=str(test_vault_with_templates))
        extractor = KnowledgeExtractor(config)
        
        content = "学习了React Hooks"
        
        tags = extractor._extract_tags(content)
        
        # Should default to 技术
        assert "技术" in tags
    
    def test_extract_tags_deduplication(self, test_vault_with_templates):
        """Test that duplicate tags are removed."""
        config = Config(vault_path=str(test_vault_with_templates))
        extractor = KnowledgeExtractor(config)
        
        content = "学习了React #技术 #技术 #前端"
        
        tags = extractor._extract_tags(content)
        
        # Should have unique tags only
        assert len([t for t in tags if t == "技术"]) == 1


class TestKnowledgeExtractorTitleGeneration:
    """Tests for title generation."""
    
    def test_generate_title_from_sentence(self, test_vault_with_templates):
        """Test generating title from first sentence."""
        config = Config(vault_path=str(test_vault_with_templates))
        extractor = KnowledgeExtractor(config)
        
        content = "学习了React Hooks的使用方法。这是一个很重要的概念。"
        
        title = extractor._generate_title(content)
        
        assert title == "学习了React Hooks的使用方法"
    
    def test_generate_title_long_sentence(self, test_vault_with_templates):
        """Test generating title from long sentence."""
        config = Config(vault_path=str(test_vault_with_templates))
        extractor = KnowledgeExtractor(config)
        
        content = "学习了React Hooks的使用方法，包括useState、useEffect、useContext等多个重要的Hooks，以及它们的使用场景和注意事项。"
        
        title = extractor._generate_title(content)
        
        # Should be truncated
        assert len(title) <= 50
        assert title.endswith("...")
    
    def test_generate_title_from_line(self, test_vault_with_templates):
        """Test generating title from first line."""
        config = Config(vault_path=str(test_vault_with_templates))
        extractor = KnowledgeExtractor(config)
        
        content = "React Hooks闭包陷阱\n这是一个常见的问题"
        
        title = extractor._generate_title(content)
        
        assert "React Hooks闭包陷阱" in title


class TestKnowledgeExtractorAnalyzeNote:
    """Tests for analyzing notes."""
    
    def test_analyze_note_with_knowledge(self, test_vault_with_templates):
        """Test analyzing a note with knowledge points."""
        config = Config(vault_path=str(test_vault_with_templates))
        extractor = KnowledgeExtractor(config)
        creator = NoteCreator(config)
        
        # Create a test note
        date = datetime(2024, 1, 15)
        note_path = creator.create_daily_note(date)
        
        # Add content with knowledge
        content = note_path.read_text(encoding='utf-8')
        content += """

## 学习板块

学习了React Hooks的使用方法，理解了闭包陷阱的原理。

```javascript
const [count, setCount] = useState(0);
```

总结了最佳实践：
- 使用useState管理状态
- 使用useEffect处理副作用
"""
        note_path.write_text(content, encoding='utf-8')
        
        # Analyze the note
        knowledge_points = extractor.analyze_note(note_path)
        
        # Should find at least one knowledge point
        assert len(knowledge_points) > 0
        assert any("React" in kp.title or "React" in kp.content for kp in knowledge_points)
    
    def test_analyze_note_no_knowledge(self, test_vault_with_templates):
        """Test analyzing a note without significant knowledge."""
        config = Config(vault_path=str(test_vault_with_templates))
        extractor = KnowledgeExtractor(config)
        creator = NoteCreator(config)
        
        # Create a test note
        date = datetime(2024, 1, 15)
        note_path = creator.create_daily_note(date)
        
        # Add minimal content
        content = note_path.read_text(encoding='utf-8')
        content += "\n\n## 工作板块\n\n今天很忙。\n"
        note_path.write_text(content, encoding='utf-8')
        
        # Analyze the note
        knowledge_points = extractor.analyze_note(note_path)
        
        # Should find no significant knowledge points (or only low-value ones)
        # The YAML front matter might be picked up, but it should have low value
        high_value_points = [kp for kp in knowledge_points if kp.value_score >= 0.5]
        assert len(high_value_points) == 0
    
    def test_analyze_note_file_not_found(self, test_vault_with_templates):
        """Test analyzing a non-existent note."""
        config = Config(vault_path=str(test_vault_with_templates))
        extractor = KnowledgeExtractor(config)
        
        non_existent = test_vault_with_templates / "non-existent.md"
        
        with pytest.raises(FileNotFoundError):
            extractor.analyze_note(non_existent)


class TestKnowledgeExtractorGenerateCard:
    """Tests for generating knowledge cards."""
    
    def test_generate_knowledge_card(self, test_vault_with_templates):
        """Test generating a knowledge card."""
        config = Config(vault_path=str(test_vault_with_templates))
        extractor = KnowledgeExtractor(config)
        creator = NoteCreator(config)
        
        # Create source note
        date = datetime(2024, 1, 15)
        source_path = creator.create_daily_note(date)
        
        # Create knowledge point
        kp = KnowledgePoint(
            title="React Hooks闭包陷阱",
            content="学习了React Hooks中的闭包陷阱问题，需要注意useEffect的依赖数组。",
            source_file=source_path,
            source_section="学习板块",
            tags=["技术/前端/React", "学习"],
            value_score=0.8
        )
        
        # Generate card
        card_path = extractor.generate_knowledge_card(kp, add_backlink=False)
        
        # Verify card was created
        assert card_path.exists()
        assert "Knowledge-Cards" in str(card_path)
        
        # Verify card content
        card_content = card_path.read_text(encoding='utf-8')
        assert "React Hooks闭包陷阱" in card_content
        assert "技术/前端/React" in card_content
        assert "2024-01-15" in card_content
        assert kp.content in card_content
    
    def test_generate_knowledge_card_with_backlink(self, test_vault_with_templates):
        """Test generating a knowledge card with backlink."""
        config = Config(vault_path=str(test_vault_with_templates))
        extractor = KnowledgeExtractor(config)
        creator = NoteCreator(config)
        
        # Create source note
        date = datetime(2024, 1, 15)
        source_path = creator.create_daily_note(date)
        
        # Create knowledge point
        kp = KnowledgePoint(
            title="React Hooks闭包陷阱",
            content="学习了React Hooks中的闭包陷阱问题。",
            source_file=source_path,
            source_section="学习板块",
            tags=["技术/前端/React"],
            value_score=0.8
        )
        
        # Generate card with backlink
        card_path = extractor.generate_knowledge_card(kp, add_backlink=True)
        
        # Verify backlink was added to source
        source_content = source_path.read_text(encoding='utf-8')
        card_name = card_path.stem
        assert f"[[{card_name}]]" in source_content
        assert "## 知识卡片" in source_content
    
    def test_generate_multiple_cards_same_source(self, test_vault_with_templates):
        """Test generating multiple cards from same source."""
        config = Config(vault_path=str(test_vault_with_templates))
        extractor = KnowledgeExtractor(config)
        creator = NoteCreator(config)
        
        # Create source note
        date = datetime(2024, 1, 15)
        source_path = creator.create_daily_note(date)
        
        # Create first knowledge point
        kp1 = KnowledgePoint(
            title="React Hooks闭包陷阱",
            content="学习了React Hooks中的闭包陷阱问题。",
            source_file=source_path,
            source_section="学习板块",
            tags=["技术/前端/React"],
            value_score=0.8
        )
        
        # Create second knowledge point
        kp2 = KnowledgePoint(
            title="useEffect依赖数组",
            content="理解了useEffect依赖数组的重要性。",
            source_file=source_path,
            source_section="学习板块",
            tags=["技术/前端/React"],
            value_score=0.7
        )
        
        # Generate both cards
        card1_path = extractor.generate_knowledge_card(kp1, add_backlink=True)
        card2_path = extractor.generate_knowledge_card(kp2, add_backlink=True)
        
        # Verify both cards exist
        assert card1_path.exists()
        assert card2_path.exists()
        
        # Verify both backlinks in source
        source_content = source_path.read_text(encoding='utf-8')
        assert f"[[{card1_path.stem}]]" in source_content
        assert f"[[{card2_path.stem}]]" in source_content


class TestKnowledgeExtractorExtractFromDailyNote:
    """Tests for extracting from daily notes."""
    
    def test_extract_from_daily_note(self, test_vault_with_templates):
        """Test extracting knowledge from daily note."""
        config = Config(vault_path=str(test_vault_with_templates))
        extractor = KnowledgeExtractor(config)
        creator = NoteCreator(config)
        
        # Create a daily note with knowledge
        date = datetime(2024, 1, 15)
        note_path = creator.create_daily_note(date)
        
        content = note_path.read_text(encoding='utf-8')
        content += """

## 学习板块

学习了React Hooks的使用方法，理解了闭包陷阱的原理。这是一个非常重要的概念，需要深入理解。

```javascript
const [count, setCount] = useState(0);
```
"""
        note_path.write_text(content, encoding='utf-8')
        
        # Extract knowledge points
        knowledge_points = extractor.extract_from_daily_note(date)
        
        # Should find knowledge points
        assert len(knowledge_points) > 0
    
    def test_extract_from_daily_note_auto_generate(self, test_vault_with_templates):
        """Test extracting and auto-generating cards."""
        config = Config(vault_path=str(test_vault_with_templates))
        extractor = KnowledgeExtractor(config)
        creator = NoteCreator(config)
        
        # Create a daily note with knowledge
        date = datetime(2024, 1, 15)
        note_path = creator.create_daily_note(date)
        
        content = note_path.read_text(encoding='utf-8')
        content += """

## 学习板块

学习了React Hooks的使用方法，理解了闭包陷阱的原理。这是一个非常重要的概念。

```javascript
const [count, setCount] = useState(0);
```
"""
        note_path.write_text(content, encoding='utf-8')
        
        # Extract and auto-generate
        knowledge_points = extractor.extract_from_daily_note(date, auto_generate=True)
        
        # Should find knowledge points
        assert len(knowledge_points) > 0
        
        # Verify cards were created
        cards_path = test_vault_with_templates / "3-Resources" / "Tech" / "Knowledge-Cards"
        assert cards_path.exists()
        card_files = list(cards_path.glob("*.md"))
        assert len(card_files) > 0
    
    def test_extract_from_nonexistent_daily_note(self, test_vault_with_templates):
        """Test extracting from non-existent daily note."""
        config = Config(vault_path=str(test_vault_with_templates))
        extractor = KnowledgeExtractor(config)
        
        # Try to extract from non-existent note
        date = datetime(2024, 1, 15)
        knowledge_points = extractor.extract_from_daily_note(date)
        
        # Should return empty list
        assert len(knowledge_points) == 0


class TestKnowledgeExtractorExtractFromNoteFile:
    """Tests for extracting from any note file."""
    
    def test_extract_from_note_file(self, test_vault_with_templates):
        """Test extracting knowledge from any note file."""
        config = Config(vault_path=str(test_vault_with_templates))
        extractor = KnowledgeExtractor(config)
        
        # Create a test note
        test_note = test_vault_with_templates / "test-note.md"
        test_note.write_text("""# Test Note

## 技术学习

学习了Python装饰器的使用方法，理解了装饰器的原理和应用场景。

```python
def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper
```

总结了最佳实践：
- 使用functools.wraps保留原函数信息
- 装饰器可以接受参数
- 可以使用类实现装饰器
""", encoding='utf-8')
        
        # Extract knowledge points
        knowledge_points = extractor.extract_from_note_file(test_note)
        
        # Should find knowledge points
        assert len(knowledge_points) > 0
        assert any("装饰器" in kp.content or "装饰器" in kp.title for kp in knowledge_points)
    
    def test_extract_from_note_file_auto_generate(self, test_vault_with_templates):
        """Test extracting and auto-generating from note file."""
        config = Config(vault_path=str(test_vault_with_templates))
        extractor = KnowledgeExtractor(config)
        
        # Create a test note
        test_note = test_vault_with_templates / "test-note.md"
        test_note.write_text("""# Test Note

## 技术学习

学习了Python装饰器的使用方法，理解了装饰器的原理和应用场景。这是一个非常重要的概念。

```python
def decorator(func):
    def wrapper():
        print("Before")
        func()
    return wrapper
```
""", encoding='utf-8')
        
        # Extract and auto-generate
        knowledge_points = extractor.extract_from_note_file(test_note, auto_generate=True)
        
        # Should find knowledge points
        assert len(knowledge_points) > 0
        
        # Verify cards were created
        cards_path = test_vault_with_templates / "3-Resources" / "Tech" / "Knowledge-Cards"
        card_files = list(cards_path.glob("*.md"))
        assert len(card_files) > 0


class TestKnowledgeExtractorEdgeCases:
    """Tests for edge cases."""
    
    def test_extract_from_empty_note(self, test_vault_with_templates):
        """Test extracting from empty note."""
        config = Config(vault_path=str(test_vault_with_templates))
        extractor = KnowledgeExtractor(config)
        
        # Create empty note
        empty_note = test_vault_with_templates / "empty.md"
        empty_note.write_text("", encoding='utf-8')
        
        # Extract knowledge points
        knowledge_points = extractor.analyze_note(empty_note)
        
        # Should return empty list
        assert len(knowledge_points) == 0
    
    def test_extract_with_special_characters_in_title(self, test_vault_with_templates):
        """Test extracting knowledge with special characters."""
        config = Config(vault_path=str(test_vault_with_templates))
        extractor = KnowledgeExtractor(config)
        creator = NoteCreator(config)
        
        # Create source note
        date = datetime(2024, 1, 15)
        source_path = creator.create_daily_note(date)
        
        # Create knowledge point with special characters
        kp = KnowledgePoint(
            title="React: Hooks & 闭包陷阱 (重要)",
            content="学习了React Hooks中的闭包陷阱问题。",
            source_file=source_path,
            source_section="学习板块",
            tags=["技术"],
            value_score=0.8
        )
        
        # Generate card (should handle special characters)
        card_path = extractor.generate_knowledge_card(kp)
        
        # Verify card was created
        assert card_path.exists()
    
    def test_backlink_not_duplicated(self, test_vault_with_templates):
        """Test that backlinks are not duplicated."""
        config = Config(vault_path=str(test_vault_with_templates))
        extractor = KnowledgeExtractor(config)
        creator = NoteCreator(config)
        
        # Create source note
        date = datetime(2024, 1, 15)
        source_path = creator.create_daily_note(date)
        
        # Create knowledge point
        kp = KnowledgePoint(
            title="Test Knowledge",
            content="Test content for knowledge extraction.",
            source_file=source_path,
            source_section="Test",
            tags=["技术"],
            value_score=0.8
        )
        
        # Generate card twice
        card_path = extractor.generate_knowledge_card(kp, add_backlink=True)
        extractor.generate_knowledge_card(kp, add_backlink=True)
        
        # Verify backlink appears only once
        source_content = source_path.read_text(encoding='utf-8')
        card_name = card_path.stem
        count = source_content.count(f"[[{card_name}]]")
        assert count == 1
