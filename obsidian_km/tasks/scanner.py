"""
任务扫描器

扫描 Vault 中的所有 Markdown 文件，查找任务。
"""

from pathlib import Path
from typing import List
from .models import Task
from .parser import TaskParser


class TaskScanner:
    """任务扫描器"""
    
    def __init__(self, vault_path: str):
        """
        初始化任务扫描器
        
        Args:
            vault_path: Vault 根目录路径
        """
        self.vault_path = Path(vault_path)
        self.parser = TaskParser(vault_path)
    
    def scan_all(self) -> List[Task]:
        """
        扫描所有 Markdown 文件中的任务
        
        Returns:
            所有任务列表
        """
        tasks = []
        
        # 遍历所有 .md 文件
        for md_file in self.vault_path.rglob('*.md'):
            # 跳过隐藏文件夹
            if any(part.startswith('.') for part in md_file.parts):
                continue
            
            # 获取相对路径
            relative_path = md_file.relative_to(self.vault_path)
            
            # 解析文件中的任务
            file_tasks = self.parser.parse_file(str(relative_path))
            tasks.extend(file_tasks)
        
        return tasks
    
    def scan_directory(self, directory: str) -> List[Task]:
        """
        扫描指定目录中的任务
        
        Args:
            directory: 目录路径（相对于 vault 根目录）
        
        Returns:
            任务列表
        """
        tasks = []
        dir_path = self.vault_path / directory
        
        if not dir_path.exists() or not dir_path.is_dir():
            return tasks
        
        # 遍历目录中的所有 .md 文件
        for md_file in dir_path.rglob('*.md'):
            # 跳过隐藏文件夹
            if any(part.startswith('.') for part in md_file.parts):
                continue
            
            # 获取相对路径
            relative_path = md_file.relative_to(self.vault_path)
            
            # 解析文件中的任务
            file_tasks = self.parser.parse_file(str(relative_path))
            tasks.extend(file_tasks)
        
        return tasks
    
    def scan_file(self, file_path: str) -> List[Task]:
        """
        扫描指定文件中的任务
        
        Args:
            file_path: 文件路径（相对于 vault 根目录）
        
        Returns:
            任务列表
        """
        return self.parser.parse_file(file_path)
