"""
任务管理器测试

包含单元测试和属性测试。
"""

import pytest
from hypothesis import given, strategies as st, settings, HealthCheck
from pathlib import Path
from datetime import date, timedelta
from obsidian_km.tasks.models import Task, TaskCategory, TaskStatistics
from obsidian_km.tasks.manager import TaskManager
from obsidian_km.tasks.parser import TaskParser
from obsidian_km.tasks.scanner import TaskScanner


# ============================================================================
# 单元测试
# ============================================================================

def test_task_parser_parse_simple_task(test_vault):
    """测试解析简单任务"""
    # 创建测试文件
    test_file = Path(test_vault) / "test.md"
    test_file.write_text("- [ ] 完成设计文档\n", encoding='utf-8')
    
    parser = TaskParser(test_vault)
    tasks = parser.parse_file("test.md")
    
    assert len(tasks) == 1
    assert tasks[0].content == "完成设计文档"
    assert tasks[0].completed == False
    assert tasks[0].file_path == "test.md"
    assert tasks[0].line_number == 1


def test_task_parser_parse_completed_task(test_vault):
    """测试解析已完成任务"""
    test_file = Path(test_vault) / "test.md"
    test_file.write_text("- [x] 完成设计文档\n", encoding='utf-8')
    
    parser = TaskParser(test_vault)
    tasks = parser.parse_file("test.md")
    
    assert len(tasks) == 1
    assert tasks[0].completed == True


def test_task_parser_extract_due_date(test_vault):
    """测试提取截止日期"""
    test_file = Path(test_vault) / "test.md"
    test_file.write_text("- [ ] 完成设计文档 📅 2024-01-20\n", encoding='utf-8')
    
    parser = TaskParser(test_vault)
    tasks = parser.parse_file("test.md")
    
    assert len(tasks) == 1
    assert tasks[0].due_date == "2024-01-20"


def test_task_parser_extract_assignee(test_vault):
    """测试提取负责人"""
    test_file = Path(test_vault) / "test.md"
    test_file.write_text("- [ ] 完成设计文档 @张三\n", encoding='utf-8')
    
    parser = TaskParser(test_vault)
    tasks = parser.parse_file("test.md")
    
    assert len(tasks) == 1
    assert tasks[0].assignee == "张三"


def test_task_parser_extract_tags(test_vault):
    """测试提取标签"""
    test_file = Path(test_vault) / "test.md"
    test_file.write_text("- [ ] 完成设计文档 #重要 #project/ProjectA\n", encoding='utf-8')
    
    parser = TaskParser(test_vault)
    tasks = parser.parse_file("test.md")
    
    assert len(tasks) == 1
    assert "重要" in tasks[0].tags
    assert "project/ProjectA" in tasks[0].tags
    assert "重要" in tasks[0].priority


def test_task_parser_determine_category_by_tag(test_vault):
    """测试通过标签确定任务分类"""
    test_file = Path(test_vault) / "test.md"
    test_file.write_text(
        "- [ ] 个人任务 #task/personal\n"
        "- [ ] 工作任务 #task/work\n"
        "- [ ] 项目任务 #task/project/ProjectA\n",
        encoding='utf-8'
    )
    
    parser = TaskParser(test_vault)
    tasks = parser.parse_file("test.md")
    
    assert len(tasks) == 3
    assert tasks[0].category == TaskCategory.PERSONAL
    assert tasks[1].category == TaskCategory.WORK
    assert tasks[2].category == TaskCategory.PROJECT
    assert tasks[2].project_name == "ProjectA"


def test_task_parser_determine_category_by_path(test_vault):
    """测试通过文件路径确定任务分类"""
    # 创建项目文件夹
    work_project = Path(test_vault) / "1-Projects" / "Work" / "ProjectA"
    work_project.mkdir(parents=True, exist_ok=True)
    
    test_file = work_project / "tasks.md"
    test_file.write_text("- [ ] 项目任务\n", encoding='utf-8')
    
    parser = TaskParser(test_vault)
    tasks = parser.parse_file("1-Projects/Work/ProjectA/tasks.md")
    
    assert len(tasks) == 1
    assert tasks[0].category == TaskCategory.PROJECT
    assert tasks[0].project_name == "ProjectA"


def test_task_scanner_scan_all(test_vault):
    """测试扫描所有任务"""
    # 创建多个文件
    file1 = Path(test_vault) / "file1.md"
    file1.write_text("- [ ] 任务1\n", encoding='utf-8')
    
    file2 = Path(test_vault) / "file2.md"
    file2.write_text("- [ ] 任务2\n- [x] 任务3\n", encoding='utf-8')
    
    scanner = TaskScanner(test_vault)
    tasks = scanner.scan_all()
    
    assert len(tasks) == 3


def test_task_scanner_scan_directory(test_vault):
    """测试扫描指定目录"""
    # 创建目录结构
    daily_dir = Path(test_vault) / "0-Daily"
    daily_dir.mkdir(parents=True, exist_ok=True)
    
    file1 = daily_dir / "2024-01-15.md"
    file1.write_text("- [ ] 今日任务\n", encoding='utf-8')
    
    file2 = Path(test_vault) / "other.md"
    file2.write_text("- [ ] 其他任务\n", encoding='utf-8')
    
    scanner = TaskScanner(test_vault)
    tasks = scanner.scan_directory("0-Daily")
    
    assert len(tasks) == 1
    assert tasks[0].content == "今日任务"


def test_task_manager_classify_tasks(test_vault):
    """测试任务分类"""
    tasks = [
        Task("任务1", False, "test.md", 1, category=TaskCategory.PERSONAL),
        Task("任务2", False, "test.md", 2, category=TaskCategory.WORK),
        Task("任务3", False, "test.md", 3, category=TaskCategory.PROJECT),
        Task("任务4", False, "test.md", 4, category=TaskCategory.PERSONAL),
    ]
    
    manager = TaskManager(test_vault)
    classified = manager.classify_tasks(tasks)
    
    assert len(classified[TaskCategory.PERSONAL]) == 2
    assert len(classified[TaskCategory.WORK]) == 1
    assert len(classified[TaskCategory.PROJECT]) == 1


def test_task_manager_get_today_tasks(test_vault):
    """测试获取今日任务"""
    today = date.today().isoformat()
    tomorrow = (date.today() + timedelta(days=1)).isoformat()
    
    tasks = [
        Task("今日任务", False, "test.md", 1, due_date=today),
        Task("明日任务", False, "test.md", 2, due_date=tomorrow),
        Task("无日期任务", False, "test.md", 3),
    ]
    
    manager = TaskManager(test_vault)
    today_tasks = manager.get_today_tasks(tasks)
    
    assert len(today_tasks) == 1
    assert today_tasks[0].content == "今日任务"


def test_task_manager_get_week_tasks(test_vault):
    """测试获取本周任务"""
    today = date.today().isoformat()
    next_week = (date.today() + timedelta(days=10)).isoformat()
    
    tasks = [
        Task("本周任务", False, "test.md", 1, due_date=today),
        Task("下周任务", False, "test.md", 2, due_date=next_week),
    ]
    
    manager = TaskManager(test_vault)
    week_tasks = manager.get_week_tasks(tasks)
    
    assert len(week_tasks) == 1
    assert week_tasks[0].content == "本周任务"


def test_task_manager_get_important_urgent_tasks(test_vault):
    """测试获取重要紧急任务"""
    tasks = [
        Task("重要任务", False, "test.md", 1, priority=["重要"]),
        Task("紧急任务", False, "test.md", 2, priority=["紧急"]),
        Task("普通任务", False, "test.md", 3, priority=[]),
    ]
    
    manager = TaskManager(test_vault)
    important_urgent = manager.get_important_urgent_tasks(tasks)
    
    assert len(important_urgent) == 2


def test_task_manager_calculate_statistics(test_vault):
    """测试计算任务统计"""
    today = date.today().isoformat()
    
    tasks = [
        Task("任务1", False, "test.md", 1, category=TaskCategory.PERSONAL, due_date=today),
        Task("任务2", True, "test.md", 2, category=TaskCategory.WORK),
        Task("任务3", False, "test.md", 3, category=TaskCategory.PROJECT, priority=["重要"]),
        Task("任务4", False, "test.md", 4, category=TaskCategory.PERSONAL),
    ]
    
    manager = TaskManager(test_vault)
    stats = manager.calculate_statistics(tasks)
    
    assert stats.total == 4
    assert stats.completed == 1
    assert stats.in_progress == 3
    assert stats.today == 1
    assert stats.important_urgent == 1
    assert stats.personal == 2
    assert stats.work == 1
    assert stats.project == 1


def test_task_manager_generate_task_center(test_vault):
    """测试生成任务中心"""
    # 创建测试文件
    test_file = Path(test_vault) / "test.md"
    test_file.write_text(
        "- [ ] 个人任务 #task/personal\n"
        "- [ ] 工作任务 #task/work\n"
        "- [ ] 项目任务 #task/project/ProjectA\n",
        encoding='utf-8'
    )
    
    manager = TaskManager(test_vault)
    output_path = manager.generate_task_center()
    
    # 检查文件是否生成
    task_center = Path(test_vault) / output_path
    assert task_center.exists()
    
    # 检查内容
    content = task_center.read_text(encoding='utf-8')
    assert "# 任务中心" in content
    assert "## 📊 任务统计" in content
    assert "## 💼 工作任务" in content
    assert "## 📁 项目任务" in content
    assert "## 👤 个人任务" in content


# ============================================================================
# 属性测试
# ============================================================================

# Feature: obsidian-knowledge-management-workflow, Property 17: 任务分类和统计
@given(
    personal_count=st.integers(min_value=0, max_value=10),
    work_count=st.integers(min_value=0, max_value=10),
    project_count=st.integers(min_value=0, max_value=10)
)
@settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
def test_property_task_classification_and_statistics(test_vault, personal_count, work_count, project_count):
    """
    属性 17：对于任意任务集合，应该正确分类和统计
    
    验证需求: 17.6, 17.7, 17.8
    """
    # 生成任务集合
    tasks = []
    
    # 添加个人任务
    for i in range(personal_count):
        tasks.append(Task(
            content=f"个人任务{i}",
            completed=False,
            file_path="test.md",
            line_number=i,
            category=TaskCategory.PERSONAL
        ))
    
    # 添加工作任务
    for i in range(work_count):
        tasks.append(Task(
            content=f"工作任务{i}",
            completed=False,
            file_path="test.md",
            line_number=personal_count + i,
            category=TaskCategory.WORK
        ))
    
    # 添加项目任务
    for i in range(project_count):
        tasks.append(Task(
            content=f"项目任务{i}",
            completed=False,
            file_path="test.md",
            line_number=personal_count + work_count + i,
            category=TaskCategory.PROJECT,
            project_name="TestProject"
        ))
    
    manager = TaskManager(test_vault)
    
    # 测试分类
    classified = manager.classify_tasks(tasks)
    assert len(classified[TaskCategory.PERSONAL]) == personal_count
    assert len(classified[TaskCategory.WORK]) == work_count
    assert len(classified[TaskCategory.PROJECT]) == project_count
    
    # 测试统计
    stats = manager.calculate_statistics(tasks)
    assert stats.total == personal_count + work_count + project_count
    assert stats.personal == personal_count
    assert stats.work == work_count
    assert stats.project == project_count
