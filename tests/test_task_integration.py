"""
任务管理器集成测试

测试完整的任务管理工作流程。
"""

import pytest
from pathlib import Path
from datetime import date
from obsidian_km.tasks.manager import TaskManager


def test_end_to_end_task_management_workflow(test_vault):
    """测试端到端任务管理工作流程"""
    # 创建测试文件结构
    vault = Path(test_vault)
    today = date.today().isoformat()
    
    # 1. 创建日常笔记中的任务
    daily_dir = vault / "0-Daily" / "2024" / "01"
    daily_dir.mkdir(parents=True, exist_ok=True)
    
    daily_note = daily_dir / "2024-01-15.md"
    daily_note.write_text(
        "# 2024-01-15\n\n"
        "## 今日任务\n\n"
        f"- [ ] 完成周报 📅 {today} @张三 #重要 #task/work\n"
        "- [x] 晨跑 #task/personal\n"
        "- [ ] 学习 Python #task/personal\n",
        encoding='utf-8'
    )
    
    # 2. 创建工作项目中的任务
    work_project = vault / "1-Projects" / "Work" / "电商系统"
    work_project.mkdir(parents=True, exist_ok=True)
    
    project_tasks = work_project / "tasks.md"
    project_tasks.write_text(
        "# 电商系统任务\n\n"
        "- [ ] 设计数据库 📅 2024-01-20 #重要 #project/电商系统\n"
        "- [ ] 实现用户认证 📅 2024-01-22 @李四 #project/电商系统\n"
        "- [x] 需求分析 #project/电商系统\n",
        encoding='utf-8'
    )
    
    # 3. 创建个人项目中的任务
    personal_project = vault / "1-Projects" / "Personal" / "装修计划"
    personal_project.mkdir(parents=True, exist_ok=True)
    
    personal_tasks = personal_project / "tasks.md"
    personal_tasks.write_text(
        "# 装修计划任务\n\n"
        "- [ ] 选择装修公司 📅 2024-01-18 #紧急\n"
        "- [ ] 购买家具\n",
        encoding='utf-8'
    )
    
    # 4. 初始化任务管理器
    manager = TaskManager(test_vault)
    
    # 5. 获取所有任务
    all_tasks = manager.get_all_tasks()
    assert len(all_tasks) == 8  # 3 + 3 + 2
    
    # 6. 测试任务分类
    classified = manager.classify_tasks(all_tasks)
    from obsidian_km.tasks.models import TaskCategory
    assert len(classified[TaskCategory.PERSONAL]) == 2  # 2 个人任务（日常笔记中的）
    assert len(classified[TaskCategory.WORK]) == 1  # 1 工作任务
    assert len(classified[TaskCategory.PROJECT]) == 5  # 3 工作项目任务 + 2 个人项目任务
    
    # 7. 测试今日任务
    today_tasks = manager.get_today_tasks(all_tasks)
    assert len(today_tasks) == 1
    assert "完成周报" in today_tasks[0].content
    
    # 8. 测试重要紧急任务
    important_urgent = manager.get_important_urgent_tasks(all_tasks)
    assert len(important_urgent) == 3  # 2 重要 + 1 紧急
    
    # 9. 测试统计信息
    stats = manager.calculate_statistics(all_tasks)
    assert stats.total == 8
    assert stats.completed == 2
    assert stats.in_progress == 6
    assert stats.today == 1
    assert stats.important_urgent == 3
    
    # 10. 生成任务中心
    output_path = manager.generate_task_center()
    task_center = vault / output_path
    assert task_center.exists()
    
    # 11. 验证任务中心内容
    content = task_center.read_text(encoding='utf-8')
    assert "# 任务中心" in content
    assert "## 📊 任务统计" in content
    assert "总任务数: 8" in content
    assert "已完成: 2" in content
    assert "进行中: 6" in content
    assert "## 📅 今日任务" in content
    assert "完成周报" in content
    assert "## 💼 工作任务" in content
    assert "## 📁 项目任务" in content
    assert "### 电商系统" in content
    assert "## 👤 个人任务" in content


def test_task_manager_with_empty_vault(test_vault):
    """测试空 vault 的任务管理"""
    manager = TaskManager(test_vault)
    
    # 获取所有任务
    all_tasks = manager.get_all_tasks()
    assert len(all_tasks) == 0
    
    # 生成任务中心
    output_path = manager.generate_task_center()
    task_center = Path(test_vault) / output_path
    assert task_center.exists()
    
    # 验证内容
    content = task_center.read_text(encoding='utf-8')
    assert "总任务数: 0" in content
    assert "*暂无今日任务*" in content
    assert "*暂无工作任务*" in content


def test_task_manager_with_complex_tags(test_vault):
    """测试复杂标签的任务管理"""
    vault = Path(test_vault)
    
    # 创建包含复杂标签的任务
    test_file = vault / "test.md"
    test_file.write_text(
        "- [ ] 任务1 #project/电商系统 #重要 #紧急 📅 2024-01-20 @张三\n"
        "- [ ] 任务2 #task/work #area/技术管理\n"
        "- [ ] 任务3 #task/personal #area/健康\n",
        encoding='utf-8'
    )
    
    manager = TaskManager(test_vault)
    all_tasks = manager.get_all_tasks()
    
    assert len(all_tasks) == 3
    
    # 验证第一个任务的元数据
    task1 = all_tasks[0]
    assert task1.due_date == "2024-01-20"
    assert task1.assignee == "张三"
    assert "重要" in task1.priority
    assert "紧急" in task1.priority
    assert task1.project_name == "电商系统"
    
    # 验证分类
    classified = manager.classify_tasks(all_tasks)
    from obsidian_km.tasks.models import TaskCategory
    assert len(classified[TaskCategory.PROJECT]) == 1
    assert len(classified[TaskCategory.WORK]) == 1
    assert len(classified[TaskCategory.PERSONAL]) == 1
