"""
任务数据模型
"""

from dataclasses import dataclass, field
from typing import Optional, List
from enum import Enum


class TaskCategory(Enum):
    """任务分类"""
    PERSONAL = "personal"  # 个人任务
    WORK = "work"  # 工作任务
    PROJECT = "project"  # 项目任务


@dataclass
class Task:
    """任务数据结构"""
    content: str  # 任务内容
    completed: bool  # 是否完成
    file_path: str  # 所在文件路径
    line_number: int  # 行号
    due_date: Optional[str] = None  # 截止日期
    assignee: Optional[str] = None  # 负责人
    priority: List[str] = field(default_factory=list)  # 优先级标签
    tags: List[str] = field(default_factory=list)  # 所有标签
    category: TaskCategory = TaskCategory.PERSONAL  # 任务类型
    project_name: Optional[str] = None  # 项目名称（如果是项目任务）
    
    def __post_init__(self):
        """初始化后处理，确保 category 是 TaskCategory 枚举"""
        if isinstance(self.category, str):
            self.category = TaskCategory(self.category)


@dataclass
class TaskStatistics:
    """任务统计信息"""
    total: int = 0  # 总任务数
    completed: int = 0  # 已完成任务数
    in_progress: int = 0  # 进行中任务数
    today: int = 0  # 今日任务数
    this_week: int = 0  # 本周任务数
    important_urgent: int = 0  # 重要紧急任务数
    
    # 按类型统计
    personal: int = 0
    work: int = 0
    project: int = 0
