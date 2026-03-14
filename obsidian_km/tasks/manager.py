"""
任务管理器

管理任务的分类、统计和任务中心生成。
"""

from pathlib import Path
from typing import List, Dict
from datetime import datetime, date, timedelta
from .models import Task, TaskCategory, TaskStatistics
from .scanner import TaskScanner


class TaskManager:
    """任务管理器"""
    
    def __init__(self, vault_path: str):
        """
        初始化任务管理器
        
        Args:
            vault_path: Vault 根目录路径
        """
        self.vault_path = Path(vault_path)
        self.scanner = TaskScanner(vault_path)
    
    def get_all_tasks(self) -> List[Task]:
        """获取所有任务"""
        return self.scanner.scan_all()
    
    def classify_tasks(self, tasks: List[Task]) -> Dict[TaskCategory, List[Task]]:
        """
        按类型分类任务
        
        Args:
            tasks: 任务列表
        
        Returns:
            按类型分类的任务字典
        """
        classified = {
            TaskCategory.PERSONAL: [],
            TaskCategory.WORK: [],
            TaskCategory.PROJECT: []
        }
        
        for task in tasks:
            classified[task.category].append(task)
        
        return classified
    
    def get_today_tasks(self, tasks: List[Task]) -> List[Task]:
        """
        获取今日任务
        
        Args:
            tasks: 任务列表
        
        Returns:
            今日任务列表
        """
        today = date.today().isoformat()
        return [task for task in tasks if task.due_date == today]
    
    def get_week_tasks(self, tasks: List[Task]) -> List[Task]:
        """
        获取本周任务
        
        Args:
            tasks: 任务列表
        
        Returns:
            本周任务列表
        """
        today = date.today()
        week_end = today + timedelta(days=7)
        
        week_tasks = []
        for task in tasks:
            if task.due_date:
                try:
                    task_date = datetime.strptime(task.due_date, '%Y-%m-%d').date()
                    if today <= task_date <= week_end:
                        week_tasks.append(task)
                except ValueError:
                    # 忽略无效日期格式
                    pass
        
        return week_tasks
    
    def get_important_urgent_tasks(self, tasks: List[Task]) -> List[Task]:
        """
        获取重要紧急任务
        
        Args:
            tasks: 任务列表
        
        Returns:
            重要紧急任务列表
        """
        return [
            task for task in tasks
            if '重要' in task.priority or '紧急' in task.priority
        ]
    
    def calculate_statistics(self, tasks: List[Task]) -> TaskStatistics:
        """
        计算任务统计信息
        
        Args:
            tasks: 任务列表
        
        Returns:
            任务统计信息
        """
        stats = TaskStatistics()
        
        stats.total = len(tasks)
        stats.completed = sum(1 for task in tasks if task.completed)
        stats.in_progress = sum(1 for task in tasks if not task.completed)
        
        stats.today = len(self.get_today_tasks(tasks))
        stats.this_week = len(self.get_week_tasks(tasks))
        stats.important_urgent = len(self.get_important_urgent_tasks(tasks))
        
        # 按类型统计
        for task in tasks:
            if task.category == TaskCategory.PERSONAL:
                stats.personal += 1
            elif task.category == TaskCategory.WORK:
                stats.work += 1
            elif task.category == TaskCategory.PROJECT:
                stats.project += 1
        
        return stats
    
    def generate_task_center(self, output_path: str = "任务中心.md") -> str:
        """
        生成任务中心文档
        
        Args:
            output_path: 输出文件路径（相对于 vault 根目录）
        
        Returns:
            生成的文档路径
        """
        # 获取所有任务
        all_tasks = self.get_all_tasks()
        
        # 分类任务
        classified = self.classify_tasks(all_tasks)
        
        # 获取特殊任务列表
        today_tasks = self.get_today_tasks(all_tasks)
        week_tasks = self.get_week_tasks(all_tasks)
        important_urgent = self.get_important_urgent_tasks(all_tasks)
        
        # 计算统计信息
        stats = self.calculate_statistics(all_tasks)
        
        # 生成文档内容
        content = self._generate_content(
            classified, today_tasks, week_tasks, important_urgent, stats
        )
        
        # 写入文件
        full_path = self.vault_path / output_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return output_path
    
    def _generate_content(
        self,
        classified: Dict[TaskCategory, List[Task]],
        today_tasks: List[Task],
        week_tasks: List[Task],
        important_urgent: List[Task],
        stats: TaskStatistics
    ) -> str:
        """生成任务中心文档内容"""
        lines = []
        
        # 标题
        lines.append("# 任务中心\n")
        lines.append(f"*更新时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n")
        lines.append("")
        
        # 统计信息
        lines.append("## 📊 任务统计\n")
        lines.append(f"- 总任务数: {stats.total}")
        lines.append(f"- 已完成: {stats.completed}")
        lines.append(f"- 进行中: {stats.in_progress}")
        lines.append(f"- 今日任务: {stats.today}")
        lines.append(f"- 本周任务: {stats.this_week}")
        lines.append(f"- 重要紧急: {stats.important_urgent}")
        lines.append("")
        lines.append(f"**按类型统计:**")
        lines.append(f"- 个人任务: {stats.personal}")
        lines.append(f"- 工作任务: {stats.work}")
        lines.append(f"- 项目任务: {stats.project}")
        lines.append("")
        
        # 今日任务
        lines.append("## 📅 今日任务\n")
        if today_tasks:
            for task in today_tasks:
                lines.append(self._format_task(task))
        else:
            lines.append("*暂无今日任务*")
        lines.append("")
        
        # 本周任务
        lines.append("## 📆 本周任务\n")
        if week_tasks:
            for task in week_tasks:
                lines.append(self._format_task(task))
        else:
            lines.append("*暂无本周任务*")
        lines.append("")
        
        # 重要紧急任务
        lines.append("## ⚠️ 重要紧急任务\n")
        if important_urgent:
            for task in important_urgent:
                lines.append(self._format_task(task))
        else:
            lines.append("*暂无重要紧急任务*")
        lines.append("")
        
        # 工作任务
        lines.append("## 💼 工作任务\n")
        work_tasks = [t for t in classified[TaskCategory.WORK] if not t.completed]
        if work_tasks:
            for task in work_tasks:
                lines.append(self._format_task(task))
        else:
            lines.append("*暂无工作任务*")
        lines.append("")
        
        # 项目任务
        lines.append("## 📁 项目任务\n")
        project_tasks = [t for t in classified[TaskCategory.PROJECT] if not t.completed]
        if project_tasks:
            # 按项目分组
            by_project = {}
            for task in project_tasks:
                project = task.project_name or "未分类项目"
                if project not in by_project:
                    by_project[project] = []
                by_project[project].append(task)
            
            for project, tasks in by_project.items():
                lines.append(f"### {project}\n")
                for task in tasks:
                    lines.append(self._format_task(task))
                lines.append("")
        else:
            lines.append("*暂无项目任务*")
        lines.append("")
        
        # 个人任务
        lines.append("## 👤 个人任务\n")
        personal_tasks = [t for t in classified[TaskCategory.PERSONAL] if not t.completed]
        if personal_tasks:
            for task in personal_tasks:
                lines.append(self._format_task(task))
        else:
            lines.append("*暂无个人任务*")
        lines.append("")
        
        return "\n".join(lines)
    
    def _format_task(self, task: Task) -> str:
        """格式化任务为 Markdown 行"""
        checkbox = "[x]" if task.completed else "[ ]"
        
        # 构建任务行
        parts = [f"- {checkbox} {task.content}"]
        
        # 添加来源链接
        parts.append(f"  - 来源: [[{task.file_path}]]")
        
        return "\n".join(parts)
