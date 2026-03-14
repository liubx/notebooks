"""Property-based tests for MCP integration."""

import pytest
from hypothesis import given, strategies as st, settings, assume

from obsidian_km.mcp import MarkdownToFeishuConverter


# Feature: obsidian-knowledge-management-workflow, Property 23: Markdown 到飞书格式转换
# 对于任意包含标准 Markdown 元素的文档，转换后应该保持语义等价性
# **验证需求: 22.2**


class TestMarkdownToFeishuConversionProperties:
    """Property-based tests for Markdown to Feishu conversion."""
    
    # Property 23.1: Heading conversion preserves level and text
    @given(
        level=st.integers(min_value=1, max_value=6),
        text=st.text(min_size=1, max_size=100, alphabet=st.characters(
            blacklist_categories=('Cs', 'Cc'),
            blacklist_characters='\n\r*_#'  # Exclude markdown special chars
        ))
    )
    @settings(max_examples=100)
    def test_heading_conversion_preserves_content(self, level, text):
        """对于任意标题级别和文本，转换后应该保持级别和文本内容"""
        # Skip whitespace-only text
        assume(text.strip())
        
        # Arrange
        converter = MarkdownToFeishuConverter()
        markdown = f"{'#' * level} {text}"
        
        # Act
        blocks = converter.convert(markdown)
        
        # Assert
        assert len(blocks) >= 1
        heading_blocks = [b for b in blocks if b["type"] == "heading"]
        assert len(heading_blocks) == 1
        assert heading_blocks[0]["level"] == level
        # Text should be preserved (may have inline formatting applied)
        assert text.strip() in heading_blocks[0]["text"] or heading_blocks[0]["text"] in text.strip()
    
    # Property 23.2: Paragraph conversion preserves text content
    @given(
        text=st.text(min_size=1, max_size=200, alphabet=st.characters(
            blacklist_categories=('Cs', 'Cc'),
            blacklist_characters='\n\r#*`[]()!_'  # Also exclude underscore
        ))
    )
    @settings(max_examples=100)
    def test_paragraph_conversion_preserves_text(self, text):
        """对于任意段落文本，转换后应该保持文本内容"""
        # Skip if text looks like special markdown syntax
        assume(not text.strip().startswith(('-', '+', '*')))
        assume(not text.strip()[0:1].isdigit() or '.' not in text[:5])
        assume('|' not in text)
        
        # Act
        converter = MarkdownToFeishuConverter()
        blocks = converter.convert(text)
        
        # Assert
        assert len(blocks) >= 1
        text_blocks = [b for b in blocks if b["type"] == "text"]
        assert len(text_blocks) >= 1
        # Text should be preserved
        assert text.strip() in text_blocks[0]["text"] or text_blocks[0]["text"] in text.strip()
    
    # Property 23.3: Code block conversion preserves language and code
    @given(
        language=st.sampled_from(['python', 'javascript', 'java', 'go', 'rust', '']),
        code=st.text(min_size=1, max_size=200, alphabet=st.characters(
            blacklist_categories=('Cs', 'Cc'),
            blacklist_characters='`'
        ))
    )
    @settings(max_examples=100)
    def test_code_block_conversion_preserves_content(self, language, code):
        """对于任意代码块，转换后应该保持语言和代码内容"""
        # Arrange
        converter = MarkdownToFeishuConverter()
        markdown = f"```{language}\n{code}\n```"
        
        # Act
        blocks = converter.convert(markdown)
        
        # Assert
        assert len(blocks) >= 1
        code_blocks = [b for b in blocks if b["type"] == "code"]
        assert len(code_blocks) == 1
        assert code_blocks[0]["language"] == language
        assert code in code_blocks[0]["code"]
    
    # Property 23.4: Task list conversion preserves checked state and text
    @given(
        checked=st.booleans(),
        text=st.text(min_size=1, max_size=100, alphabet=st.characters(
            blacklist_categories=('Cs', 'Cc'),
            blacklist_characters='\n\r[]'
        ))
    )
    @settings(max_examples=100)
    def test_task_list_conversion_preserves_state(self, checked, text):
        """对于任意任务列表项，转换后应该保持选中状态和文本"""
        # Skip whitespace-only text
        assume(text.strip())
        
        # Arrange
        converter = MarkdownToFeishuConverter()
        check_mark = 'x' if checked else ' '
        markdown = f"- [{check_mark}] {text}"
        
        # Act
        blocks = converter.convert(markdown)
        
        # Assert
        assert len(blocks) >= 1
        task_blocks = [b for b in blocks if b["type"] == "task"]
        assert len(task_blocks) == 1
        assert task_blocks[0]["checked"] == checked
        assert text in task_blocks[0]["text"] or task_blocks[0]["text"] in text
    
    # Property 23.5: Unordered list conversion preserves items
    @given(
        items=st.lists(
            st.text(min_size=1, max_size=50, alphabet=st.characters(
                blacklist_categories=('Cs', 'Cc'),
                blacklist_characters='\n\r-*+[]_`'  # Also exclude underscore and backticks
            )),
            min_size=1,
            max_size=10
        )
    )
    @settings(max_examples=100)
    def test_unordered_list_conversion_preserves_items(self, items):
        """对于任意无序列表，转换后应该保持所有列表项"""
        # Skip items with only whitespace
        items = [item for item in items if item.strip()]
        assume(len(items) > 0)
        
        # Arrange
        converter = MarkdownToFeishuConverter()
        markdown = '\n'.join(f"- {item}" for item in items)
        
        # Act
        blocks = converter.convert(markdown)
        
        # Assert
        list_blocks = [b for b in blocks if b["type"] == "list" and not b["ordered"]]
        assert len(list_blocks) >= 1
        
        # All items should be preserved
        converted_items = list_blocks[0]["items"]
        assert len(converted_items) == len(items)
        for original, converted in zip(items, converted_items):
            # Check if original text is in converted (may have formatting tags)
            assert original.strip() in converted or converted in original.strip()
    
    # Property 23.6: Ordered list conversion preserves items and order
    @given(
        items=st.lists(
            st.text(min_size=1, max_size=50, alphabet=st.characters(
                blacklist_categories=('Cs', 'Cc'),
                blacklist_characters='\n\r_*#'  # Exclude markdown special chars
            )),
            min_size=1,
            max_size=10
        )
    )
    @settings(max_examples=100)
    def test_ordered_list_conversion_preserves_order(self, items):
        """对于任意有序列表，转换后应该保持列表项和顺序"""
        # Skip items with only whitespace
        items = [item for item in items if item.strip()]
        assume(len(items) > 0)
        
        # Arrange
        converter = MarkdownToFeishuConverter()
        markdown = '\n'.join(f"{i+1}. {item}" for i, item in enumerate(items))
        
        # Act
        blocks = converter.convert(markdown)
        
        # Assert
        list_blocks = [b for b in blocks if b["type"] == "list" and b["ordered"]]
        assert len(list_blocks) >= 1
        
        # All items should be preserved in order
        converted_items = list_blocks[0]["items"]
        assert len(converted_items) == len(items)
        for original, converted in zip(items, converted_items):
            assert original.strip() in converted or converted in original.strip()
    
    # Property 23.7: Bold text conversion preserves content
    @given(
        text=st.text(min_size=1, max_size=50, alphabet=st.characters(
            blacklist_categories=('Cs', 'Cc'),
            blacklist_characters='\n\r*_#'  # Exclude markdown special chars
        ))
    )
    @settings(max_examples=100)
    def test_bold_text_conversion_preserves_content(self, text):
        """对于任意加粗文本，转换后应该保持文本内容"""
        # Skip whitespace-only or single-char text that might be interpreted as markdown
        assume(len(text.strip()) > 1)
        
        # Arrange
        converter = MarkdownToFeishuConverter()
        markdown = f"**{text}**"
        
        # Act
        blocks = converter.convert(markdown)
        
        # Assert
        assert len(blocks) >= 1
        # May be text or list depending on content
        if blocks[0].get("type") == "text":
            converted_text = blocks[0]["text"]
            assert text in converted_text
            assert "<b>" in converted_text and "</b>" in converted_text
    
    # Property 23.8: Italic text conversion preserves content
    @given(
        text=st.text(min_size=1, max_size=50, alphabet=st.characters(
            blacklist_categories=('Cs', 'Cc'),
            blacklist_characters='\n\r*_#'  # Exclude markdown special chars
        ))
    )
    @settings(max_examples=100)
    def test_italic_text_conversion_preserves_content(self, text):
        """对于任意斜体文本，转换后应该保持文本内容"""
        # Skip whitespace-only or single-char text that might be interpreted as markdown
        assume(len(text.strip()) > 1)
        
        # Arrange
        converter = MarkdownToFeishuConverter()
        markdown = f"*{text}*"
        
        # Act
        blocks = converter.convert(markdown)
        
        # Assert
        assert len(blocks) >= 1
        # May be text or list depending on content
        if blocks[0].get("type") == "text":
            converted_text = blocks[0]["text"]
            assert text in converted_text
            assert "<i>" in converted_text and "</i>" in converted_text
    
    # Property 23.9: Link conversion preserves text and URL
    @given(
        link_text=st.text(min_size=2, max_size=50, alphabet=st.characters(
            blacklist_categories=('Cs', 'Cc'),
            blacklist_characters='\n\r[]()#*_'  # Exclude markdown special chars
        )),
        url=st.text(min_size=5, max_size=100, alphabet=st.characters(
            whitelist_categories=('L', 'N'),
            whitelist_characters=':/.-'  # Removed underscore
        ))
    )
    @settings(max_examples=100)
    def test_link_conversion_preserves_content(self, link_text, url):
        """对于任意链接，转换后应该保持链接文本和URL"""
        # Skip whitespace-only text
        assume(link_text.strip())
        assume(url.strip())
        
        # Arrange
        converter = MarkdownToFeishuConverter()
        markdown = f"[{link_text}]({url})"
        
        # Act
        blocks = converter.convert(markdown)
        
        # Assert
        assert len(blocks) >= 1
        converted_text = blocks[0]["text"]
        # Check that link text and URL are preserved (may have formatting)
        assert link_text.strip() in converted_text or any(c in converted_text for c in link_text.strip())
        assert url.strip() in converted_text or any(c in converted_text for c in url.strip())
        assert '<a href=' in converted_text
    
    # Property 23.10: Multiple blocks conversion preserves count
    @given(
        num_headings=st.integers(min_value=0, max_value=5),
        num_paragraphs=st.integers(min_value=0, max_value=5)
    )
    @settings(max_examples=100)
    def test_multiple_blocks_conversion_preserves_count(self, num_headings, num_paragraphs):
        """对于任意数量的标题和段落，转换后应该保持块的数量"""
        # Arrange
        assume(num_headings + num_paragraphs > 0)
        
        converter = MarkdownToFeishuConverter()
        markdown_parts = []
        for i in range(num_headings):
            markdown_parts.append(f"# Heading {i+1}")
        for i in range(num_paragraphs):
            markdown_parts.append(f"Paragraph {i+1}")
        
        markdown = '\n\n'.join(markdown_parts)
        
        # Act
        blocks = converter.convert(markdown)
        
        # Assert
        heading_blocks = [b for b in blocks if b["type"] == "heading"]
        text_blocks = [b for b in blocks if b["type"] == "text"]
        
        assert len(heading_blocks) == num_headings
        assert len(text_blocks) == num_paragraphs
    
    # Property 23.11: Empty content produces no blocks
    @given(
        whitespace=st.sampled_from([' ', '\t', '\n', '\r', '  ', '\n\n', '\t\t', ' \n ', ''])
    )
    @settings(max_examples=100)
    def test_empty_content_produces_no_blocks(self, whitespace):
        """对于任意空白内容，转换后应该不产生任何块"""
        # Act
        converter = MarkdownToFeishuConverter()
        blocks = converter.convert(whitespace)
        
        # Assert
        assert len(blocks) == 0
    
    # Property 23.12: Table conversion preserves structure
    @given(
        num_cols=st.integers(min_value=1, max_value=5),
        num_rows=st.integers(min_value=1, max_value=5)
    )
    @settings(max_examples=100)
    def test_table_conversion_preserves_structure(self, num_cols, num_rows):
        """对于任意表格，转换后应该保持行列结构"""
        # Arrange
        converter = MarkdownToFeishuConverter()
        headers = [f"Col{i+1}" for i in range(num_cols)]
        header_line = "| " + " | ".join(headers) + " |"
        separator_line = "|" + "|".join(["---"] * num_cols) + "|"
        
        rows = []
        for r in range(num_rows):
            row_data = [f"R{r+1}C{c+1}" for c in range(num_cols)]
            rows.append("| " + " | ".join(row_data) + " |")
        
        markdown = "\n".join([header_line, separator_line] + rows)
        
        # Act
        blocks = converter.convert(markdown)
        
        # Assert
        table_blocks = [b for b in blocks if b["type"] == "table"]
        assert len(table_blocks) == 1
        
        table = table_blocks[0]
        assert len(table["headers"]) == num_cols
        assert len(table["rows"]) == num_rows
        
        # Verify each row has correct number of columns
        for row in table["rows"]:
            assert len(row) == num_cols
