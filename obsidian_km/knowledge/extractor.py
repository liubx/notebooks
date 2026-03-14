"""Knowledge card extractor for identifying and extracting knowledge points from notes."""

import re
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass

from obsidian_km.config import Config
from obsidian_km.notes import NoteCreator


@dataclass
class KnowledgePoint:
    """Represents an identified knowledge point."""
    
    title: str
    content: str
    source_file: Path
    source_section: str
    tags: List[str]
    value_score: float  # 0.0 to 1.0, higher means more valuable
    
    def __post_init__(self):
        """Validate knowledge point data."""
        if not self.title:
            raise ValueError("Knowledge point title cannot be empty")
        if not 0.0 <= self.value_score <= 1.0:
            raise ValueError("Value score must be between 0.0 and 1.0")


class KnowledgeExtractor:
    """Extracts knowledge points from daily notes and generates knowledge cards."""
    
    # Patterns that indicate valuable knowledge
    KNOWLEDGE_INDICATORS = [
        r'学习了',
        r'理解了',
        r'发现',
        r'总结',
        r'原理',
        r'最佳实践',
        r'技巧',
        r'注意',
        r'问题.*解决',
        r'经验',
    ]
    
    # Minimum content length for a knowledge point (characters)
    MIN_CONTENT_LENGTH = 20
    
    # Minimum value score to consider extracting
    MIN_VALUE_SCORE = 0.3
    
    def __init__(self, config: Config):
        """
        Initialize knowledge extractor.
        
        Args:
            config: Configuration object
        """
        self.config = config
        self.vault_path = Path(config.vault_path)
        self.note_creator = NoteCreator(config)
    
    def analyze_note(self, note_path: Path) -> List[KnowledgePoint]:
        """
        Analyze a note and identify knowledge points.
        
        Args:
            note_path: Path to the note file
        
        Returns:
            List of identified knowledge points
        """
        if not note_path.exists():
            raise FileNotFoundError(f"Note not found: {note_path}")
        
        content = note_path.read_text(encoding='utf-8')
        knowledge_points = []
        
        # Extract sections from the note
        sections = self._extract_sections(content)
        
        for section_title, section_content in sections:
            # Skip if section is too short
            if len(section_content) < self.MIN_CONTENT_LENGTH:
                continue
            
            # Evaluate if this section contains valuable knowledge
            value_score = self._evaluate_knowledge_value(section_content)
            
            if value_score >= self.MIN_VALUE_SCORE:
                # Extract tags from content
                tags = self._extract_tags(section_content)
                
                # Create knowledge point
                kp = KnowledgePoint(
                    title=section_title or self._generate_title(section_content),
                    content=section_content,
                    source_file=note_path,
                    source_section=section_title or "Main content",
                    tags=tags,
                    value_score=value_score
                )
                knowledge_points.append(kp)
        
        return knowledge_points
    
    def _extract_sections(self, content: str) -> List[Tuple[str, str]]:
        """
        Extract sections from note content.
        
        Sections are identified by markdown headings (## or ###).
        
        Args:
            content: Note content
        
        Returns:
            List of (section_title, section_content) tuples
        """
        sections = []
        
        # Split by headings
        lines = content.split('\n')
        current_title = ""
        current_content = []
        
        for line in lines:
            # Check if line is a heading (## or ###)
            heading_match = re.match(r'^(#{2,3})\s+(.+)$', line)
            
            if heading_match:
                # Save previous section if it exists
                if current_content:
                    sections.append((current_title, '\n'.join(current_content).strip()))
                
                # Start new section
                current_title = heading_match.group(2).strip()
                current_content = []
            else:
                # Add line to current section
                current_content.append(line)
        
        # Add last section
        if current_content:
            sections.append((current_title, '\n'.join(current_content).strip()))
        
        return sections
    
    def _evaluate_knowledge_value(self, content: str) -> float:
        """
        Evaluate the value of content as knowledge.
        
        Uses heuristics to determine if content is worth extracting:
        - Contains knowledge indicators (learning, discovery, etc.)
        - Has sufficient length
        - Contains technical terms or concepts
        - Has structure (lists, code blocks, etc.)
        
        Args:
            content: Content to evaluate
        
        Returns:
            Value score between 0.0 and 1.0
        """
        score = 0.0
        
        # Check for knowledge indicators
        indicator_count = 0
        for pattern in self.KNOWLEDGE_INDICATORS:
            if re.search(pattern, content, re.IGNORECASE):
                indicator_count += 1
        
        # Add score based on indicators (max 0.4)
        score += min(indicator_count * 0.1, 0.4)
        
        # Check content length (longer content is more valuable)
        if len(content) > 100:
            score += 0.2
        if len(content) > 300:
            score += 0.1
        
        # Check for code blocks (indicates technical content)
        if '```' in content:
            score += 0.2
        
        # Check for lists (indicates structured information)
        if re.search(r'^\s*[-*]\s+', content, re.MULTILINE):
            score += 0.1
        
        # Check for technical tags
        if re.search(r'#技术', content):
            score += 0.1
        
        return min(score, 1.0)
    
    def _extract_tags(self, content: str) -> List[str]:
        """
        Extract tags from content.
        
        Args:
            content: Content to extract tags from
        
        Returns:
            List of tags found in content
        """
        # Find all hashtags
        tags = re.findall(r'#([\w/]+)', content)
        
        # Default to 技术 if no tags found
        if not tags:
            tags = ['技术']
        
        return list(set(tags))
    
    def _generate_title(self, content: str) -> str:
        """
        Generate a title from content.
        
        Uses the first sentence or first line as title.
        
        Args:
            content: Content to generate title from
        
        Returns:
            Generated title
        """
        # Try to get first sentence
        sentences = re.split(r'[。！？\n]', content)
        for sentence in sentences:
            sentence = sentence.strip()
            if sentence and len(sentence) > 5:
                # Limit title length
                if len(sentence) > 50:
                    return sentence[:47] + "..."
                return sentence
        
        # Fallback to first 50 characters
        return content[:50].strip() + "..."
    
    def generate_knowledge_card(
        self,
        knowledge_point: KnowledgePoint,
        add_backlink: bool = True
    ) -> Path:
        """
        Generate a knowledge card from a knowledge point.
        
        Args:
            knowledge_point: Knowledge point to generate card from
            add_backlink: If True, add a link to the card in the source note
        
        Returns:
            Path to the created knowledge card
        """
        # Determine main tag
        main_tag = knowledge_point.tags[0] if knowledge_point.tags else '技术'
        
        # Get source note name (without extension)
        source_name = knowledge_point.source_file.stem
        
        # Create knowledge card
        card_path = self.note_creator.create_knowledge_card(
            title=knowledge_point.title,
            main_tag=main_tag,
            source=source_name
        )
        
        # Read the card content
        card_content = card_path.read_text(encoding='utf-8')
        
        # Replace the empty sections with actual content
        # Find the "## 核心概念" section and add content
        card_content = card_content.replace(
            "## 核心概念\n\n",
            f"## 核心概念\n\n{knowledge_point.content}\n\n"
        )
        
        # Add all tags to the card
        if len(knowledge_point.tags) > 1:
            # Add additional tags to the YAML front matter
            yaml_end = card_content.find('---', 3)  # Find second ---
            if yaml_end != -1:
                additional_tags = '\n'.join(f"  - {tag}" for tag in knowledge_point.tags[1:])
                insert_pos = yaml_end
                card_content = (
                    card_content[:insert_pos] +
                    additional_tags + '\n' +
                    card_content[insert_pos:]
                )
        
        # Write updated content
        card_path.write_text(card_content, encoding='utf-8')
        
        # Add backlink to source note if requested
        if add_backlink:
            self._add_backlink_to_source(knowledge_point.source_file, card_path)
        
        return card_path
    
    def _add_backlink_to_source(self, source_path: Path, card_path: Path) -> None:
        """
        Add a backlink to the knowledge card in the source note.
        
        Args:
            source_path: Path to the source note
            card_path: Path to the knowledge card
        """
        if not source_path.exists():
            return
        
        # Read source content
        source_content = source_path.read_text(encoding='utf-8')
        
        # Get card name (without extension)
        card_name = card_path.stem
        
        # Check if backlink already exists
        if f"[[{card_name}]]" in source_content:
            return
        
        # Add backlink at the end of the note
        backlink_section = f"\n\n## 知识卡片\n\n- [[{card_name}]]\n"
        
        # Check if "知识卡片" section already exists
        if "## 知识卡片" in source_content:
            # Add to existing section
            source_content = source_content.replace(
                "## 知识卡片\n\n",
                f"## 知识卡片\n\n- [[{card_name}]]\n"
            )
        else:
            # Add new section
            source_content += backlink_section
        
        # Write updated content
        source_path.write_text(source_content, encoding='utf-8')
    
    def extract_from_daily_note(
        self,
        date: datetime,
        auto_generate: bool = False
    ) -> List[KnowledgePoint]:
        """
        Extract knowledge points from a daily note.
        
        Args:
            date: Date of the daily note
            auto_generate: If True, automatically generate knowledge cards
        
        Returns:
            List of identified knowledge points
        """
        # Get daily note path
        note_path = self.note_creator.get_daily_note_path(date)
        
        if not note_path.exists():
            return []
        
        # Analyze the note
        knowledge_points = self.analyze_note(note_path)
        
        # Auto-generate cards if requested
        if auto_generate:
            for kp in knowledge_points:
                self.generate_knowledge_card(kp)
        
        return knowledge_points
    
    def extract_from_note_file(
        self,
        note_path: Path,
        auto_generate: bool = False
    ) -> List[KnowledgePoint]:
        """
        Extract knowledge points from any note file.
        
        Args:
            note_path: Path to the note file
            auto_generate: If True, automatically generate knowledge cards
        
        Returns:
            List of identified knowledge points
        """
        # Analyze the note
        knowledge_points = self.analyze_note(note_path)
        
        # Auto-generate cards if requested
        if auto_generate:
            for kp in knowledge_points:
                self.generate_knowledge_card(kp)
        
        return knowledge_points
