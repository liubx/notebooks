"""
任务解析器

解析 Markdown 文件中的任务列表语法，提取任务元数据。
"""

import re
from typing import Optional, List, Tuple
from pathlib import Path
from .models import Task, TaskCategory


class TaskParser:
    """任务解析器"""
    
    # 任务列表正则表达式
    TASK_PATTERN = re.compile(r'^(\s*)- \[([ xX])\] (.+)$')
    
    # 元数据正则表达式
    DUE_DATE_PATTERN = re.compile(r'📅\s*(\d{4}-\d{2}-\d{2})')
    ASSIGNEE_PATTERN = re.compile(r'@(\S+)')
    TAG_PATTERN = re.compile(r'#([\w/\u4e00-\u9fa5]+)')
    
    def __init__(self, vault_path: str):
        """
        初始化任务解析器
        
        Args:
            vault_path: Vault 根目录路径
        """
        self.vault_path = Path(vault_path)
    
    def parse_file(self, file_path: str) -> List[Task]:
        """
        解析文件中的所有任务
        
        Args:
            file_path: 文件路径（相对于 vault 根目录）
        
        Returns:
            任务列表
        """
        full_path = self.vault_path / file_path
        if not full_path.exists():
            return []
        
        tasks = []
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                for line_number, line in enumerate(f, start=1):
                    task = self._parse_line(line, file_path, line_number)
                    if task:
                        tasks.append(task)
        except Exception:
            # 忽略无法读取的文件
            pass
        
        return tasks
    
    def _parse_line(self, line: str, file_path: str, line_number: int) -> Optional[Task]:
        """
        解析单行任务
        
        Args:
            line: 行内容
            file_path: 文件路径
            line_number: 行号
        
        Returns:
            任务对象，如果不是任务则返回 None
        """
        match = self.TASK_PATTERN.match(line)
        if not match:
            return None
        
        # 提取任务状态和内容
        completed = match.group(2).lower() == 'x'
        content = match.group(3).strip()
        
        # 提取元数据
        due_date = self._extract_due_date(content)
        assignee = self._extract_assignee(content)
        tags = self._extract_tags(content)
        priority = self._extract_priority(tags)
        
        # 确定任务分类
        category, project_name = self._determine_category(file_path, tags)
        
        return Task(
            content=content,
            completed=completed,
            file_path=file_path,
            line_number=line_number,
            due_date=due_date,
            assignee=assignee,
            priority=priority,
            tags=tags,
            category=category,
            project_name=project_name
        )
    
    def _extract_due_date(self, content: str) -> Optional[str]:
        """提取截止日期"""
        match = self.DUE_DATE_PATTERN.search(content)
        return match.group(1) if match else None
    
    def _extract_assignee(self, content: str) -> Optional[str]:
        """提取负责人"""
        match = self.ASSIGNEE_PATTERN.search(content)
        return match.group(1) if match else None
    
    def _extract_tags(self, content: str) -> List[str]:
        """提取所有标签"""
        return self.TAG_PATTERN.findall(content)
    
    def _extract_priority(self, tags: List[str]) -> List[str]:
        """提取优先级标签"""
        priority_tags = []
        for tag in tags:
            if tag in ['重要', '紧急']:
                priority_tags.append(tag)
        return priority_tags
    
    def _determine_category(self, file_path: str, tags: List[str]) -> Tuple[TaskCategory, Optional[str]]:
        """
        确定任务分类
        
        Args:
            file_path: 文件路径
            tags: 标签列表
        
        Returns:
            (任务分类, 项目名称)
        """
        # 检查标签
        for tag in tags:
            if tag.startswith('task/personal'):
                return TaskCategory.PERSONAL, None
            elif tag.startswith('task/work'):
                return TaskCategory.WORK, None
            elif tag.startswith('task/project/'):
                project_name = tag.split('/', 2)[2] if len(tag.split('/')) > 2 else None
                return TaskCategory.PROJECT, project_name
            elif tag.startswith('project/'):
                project_name = tag.split('/', 1)[1] if len(tag.split('/')) > 1 else None
                return TaskCategory.PROJECT, project_name
        
        # 根据文件路径判断
        path_parts = Path(file_path).parts
        
        if len(path_parts) > 0:
            # 检查是否在项目文件夹中
            if path_parts[0] == '1-Projects':
                if len(path_parts) > 1:
                    if path_parts[1] == 'Work':
                        # 工作项目
                        project_name = path_parts[2] if len(path_parts) > 2 else None
                        return TaskCategory.PROJECT, project_name
                    elif path_parts[1] == 'Personal':
                        # 个人项目
                        project_name = path_parts[2] if len(path_parts) > 2 else None
                        return TaskCategory.PROJECT, project_name
            
            # 检查是否在工作领域中
            elif path_parts[0] == '2-Areas' and len(path_parts) > 1 and path_parts[1] == 'Work':
                return TaskCategory.WORK, None
            
            # 检查是否在生活领域中
            elif path_parts[0] == '2-Areas' and len(path_parts) > 1 and path_parts[1] == 'Life':
                return TaskCategory.PERSONAL, None
        
        # 默认为个人任务
        return TaskCategory.PERSONAL, None
