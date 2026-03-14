"""Markdown to Feishu format converter."""

import re
from typing import List, Dict, Any


class MarkdownToFeishuConverter:
    """
    Converts Markdown content to Feishu document format.
    
    Supports:
    - Headings (h1-h6)
    - Lists (ordered and unordered)
    - Task lists
    - Code blocks
    - Tables
    - Links
    - Images
    - Bold and italic text
    """
    
    def convert(self, markdown: str) -> List[Dict[str, Any]]:
        """
        Convert Markdown to Feishu format.
        
        Args:
            markdown: Markdown content string
            
        Returns:
            List of Feishu document blocks
        """
        blocks = []
        lines = markdown.split('\n')
        i = 0
        
        while i < len(lines):
            line = lines[i]
            
            # Skip empty lines
            if not line.strip():
                i += 1
                continue
            
            # Check for code blocks
            if line.strip().startswith('```'):
                code_block, lines_consumed = self._parse_code_block(lines[i:])
                if code_block:
                    blocks.append(code_block)
                    i += lines_consumed
                    continue
            
            # Check for headings
            heading = self._parse_heading(line)
            if heading:
                blocks.append(heading)
                i += 1
                continue
            
            # Check for task lists
            task = self._parse_task_list(line)
            if task:
                blocks.append(task)
                i += 1
                continue
            
            # Check for unordered lists
            if line.strip().startswith(('-', '*', '+')):
                list_block, lines_consumed = self._parse_list(lines[i:], ordered=False)
                if list_block:
                    blocks.append(list_block)
                    i += lines_consumed
                    continue
            
            # Check for ordered lists
            if re.match(r'^\d+\.', line.strip()):
                list_block, lines_consumed = self._parse_list(lines[i:], ordered=True)
                if list_block:
                    blocks.append(list_block)
                    i += lines_consumed
                    continue
            
            # Check for tables
            if '|' in line:
                table, lines_consumed = self._parse_table(lines[i:])
                if table:
                    blocks.append(table)
                    i += lines_consumed
                    continue
            
            # Default: treat as paragraph
            paragraph = self._parse_paragraph(line)
            blocks.append(paragraph)
            i += 1
        
        return blocks
    
    def _parse_heading(self, line: str) -> Dict[str, Any]:
        """Parse heading line."""
        match = re.match(r'^(#{1,6})\s+(.+)$', line.strip())
        if not match:
            return None
        
        level = len(match.group(1))
        text = match.group(2)
        
        return {
            "type": "heading",
            "level": level,
            "text": self._convert_inline_styles(text)
        }
    
    def _parse_paragraph(self, line: str) -> Dict[str, Any]:
        """Parse paragraph line."""
        return {
            "type": "text",
            "text": self._convert_inline_styles(line.strip())
        }
    
    def _parse_code_block(self, lines: List[str]) -> tuple:
        """Parse code block."""
        if not lines[0].strip().startswith('```'):
            return None, 0
        
        # Extract language
        first_line = lines[0].strip()
        language = first_line[3:].strip() if len(first_line) > 3 else ""
        
        # Find closing ```
        code_lines = []
        i = 1
        while i < len(lines):
            if lines[i].strip() == '```':
                break
            code_lines.append(lines[i])
            i += 1
        
        if i >= len(lines):
            # No closing ```, treat as regular text
            return None, 0
        
        return {
            "type": "code",
            "language": language,
            "code": '\n'.join(code_lines)
        }, i + 1
    
    def _parse_task_list(self, line: str) -> Dict[str, Any]:
        """Parse task list item."""
        match = re.match(r'^-\s+\[([ xX])\]\s+(.+)$', line.strip())
        if not match:
            return None
        
        checked = match.group(1).lower() == 'x'
        text = match.group(2)
        
        return {
            "type": "task",
            "checked": checked,
            "text": self._convert_inline_styles(text)
        }
    
    def _parse_list(self, lines: List[str], ordered: bool) -> tuple:
        """Parse list (ordered or unordered)."""
        items = []
        i = 0
        
        pattern = r'^\d+\.' if ordered else r'^[-*+]'
        
        while i < len(lines):
            line = lines[i].strip()
            if not line:
                break
            
            if not re.match(pattern, line):
                break
            
            # Extract list item text
            if ordered:
                text = re.sub(r'^\d+\.\s+', '', line)
            else:
                text = re.sub(r'^[-*+]\s+', '', line)
            
            items.append(self._convert_inline_styles(text))
            i += 1
        
        if not items:
            return None, 0
        
        return {
            "type": "list",
            "ordered": ordered,
            "items": items
        }, i
    
    def _parse_table(self, lines: List[str]) -> tuple:
        """Parse table."""
        if not lines or '|' not in lines[0]:
            return None, 0
        
        # Parse header
        header_line = lines[0].strip()
        headers = [cell.strip() for cell in header_line.split('|') if cell.strip()]
        
        # Check for separator line
        if len(lines) < 2 or not re.match(r'^[\s|:-]+$', lines[1]):
            return None, 0
        
        # Parse rows
        rows = []
        i = 2
        while i < len(lines):
            line = lines[i].strip()
            if not line or '|' not in line:
                break
            
            cells = [cell.strip() for cell in line.split('|') if cell.strip()]
            if len(cells) == len(headers):
                rows.append([self._convert_inline_styles(cell) for cell in cells])
            i += 1
        
        return {
            "type": "table",
            "headers": [self._convert_inline_styles(h) for h in headers],
            "rows": rows
        }, i
    
    def _convert_inline_styles(self, text: str) -> str:
        """
        Convert inline Markdown styles to Feishu format.
        
        Supports:
        - Bold: **text** or __text__
        - Italic: *text* or _text_
        - Links: [text](url)
        - Images: ![alt](url)
        - Code: `code`
        """
        # Convert images first (before links, since images start with !)
        text = re.sub(r'!\[(.+?)\]\((.+?)\)', r'<img src="\2" alt="\1">', text)
        
        # Convert links
        text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', text)
        
        # Convert bold
        text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
        text = re.sub(r'__(.+?)__', r'<b>\1</b>', text)
        
        # Convert italic
        text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
        text = re.sub(r'_(.+?)_', r'<i>\1</i>', text)
        
        # Convert inline code
        text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
        
        return text
