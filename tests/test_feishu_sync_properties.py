"""
属性测试：飞书同步引擎

测试飞书同步的正确性属性
"""

import pytest
from hypothesis import given, strategies as st, settings, assume
from datetime import datetime, timedelta
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
import tempfile
import shutil

from obsidian_km.sync.feishu_sync import FeishuSyncEngine, SyncConflict
from obsidian_km.mcp.client import MCPClient
from obsidian_km.mcp.models import FeishuTask, FeishuDocument, SyncResult
from obsidian_km.tasks.models import Task, TaskCategory
from obsidian_km.config import FeishuCredentials


# 策略：生成任务内容
@st.composite
def task_content_strategy(draw):
    """生成任务内容"""
    content = draw(st.text(min_size=5, max_size=100, alphabet=st.characters(
        whitelist_categories=('Lu', 'Ll', 'Nd'),
        whitelist_characters=' '
    )))
    return content.strip()


# 策略：生成任务
@st.composite
def task_strategy(draw):
    """生成任务对象"""
    content = draw(task_content_strategy())
    completed = draw(st.booleans())
    due_date = draw(st.one_of(
        st.none(),
        st.dates(min_value=datetime(2024, 1, 1).date(), max_value=datetime(2025, 12, 31).date()).map(lambda d: d.isoformat())
    ))
    assignee = draw(st.one_of(st.none(), st.sampled_from(['张三', '李四', '王五'])))
    priority = draw(st.lists(st.sampled_from(['重要', '紧急']), max_size=2))
    tags = draw(st.lists(st.sampled_from(['#task/work', '#project/测试项目', '#sync/feishu']), max_size=3))
    
    return Task(
        content=content,
        completed=completed,
        file_path="test.md",
        line_number=1,
        due_date=due_date,
        assignee=assignee,
        priority=priority,
        tags=tags,
        category=TaskCategory.WORK
    )


@pytest.fixture
def temp_vault():
    """创建临时 vault"""
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)


@pytest.fixture
def mock_mcp_client():
    """创建 mock MCP 客户端"""
    client = Mock(spec=MCPClient)
    client.is_connected.return_value = True
    client.connect.return_value = True
    return client


# Feature: obsidian-knowledge-management-workflow, Property 18: 飞书任务同步数据完整性
@given(task=task_strategy())
@settings(max_examples=100, deadline=None)
def test_property_18_feishu_task_sync_data_integrity(task):
    """
    属性 18：对于任意标记为同步的任务，飞书任务应该包含所有指定字段
    
    验证需求: 20.4
    """
    # 创建临时目录
    temp_vault = tempfile.mkdtemp()
    
    try:
        # 创建 mock MCP 客户端
        mock_mcp_client = Mock(spec=MCPClient)
        mock_mcp_client.is_connected.return_value = True
        mock_mcp_client.connect.return_value = True
        
        # 确保任务标记为需要同步
        if '#sync/feishu' not in task.tags:
            task.tags.append('#sync/feishu')
        
        # 创建测试文件
        test_file = Path(temp_vault) / task.file_path
        test_file.parent.mkdir(parents=True, exist_ok=True)
        
        # 写入任务内容
        checkbox = "[x]" if task.completed else "[ ]"
        tags_str = ' '.join(task.tags)
        content = f"- {checkbox} {task.content} {tags_str}\n"
        test_file.write_text(content, encoding='utf-8')
        
        # Mock MCP 客户端的 create_task 方法
        def mock_create_task(feishu_task, tasklist_id=None):
            # 验证飞书任务包含所有必需字段
            assert feishu_task.title is not None, "任务标题不能为空"
            assert feishu_task.description is not None, "任务描述不能为空"
            assert feishu_task.status in ["pending", "completed"], "任务状态必须是 pending 或 completed"
            
            # 如果本地任务有这些字段，飞书任务也应该有
            if task.due_date:
                assert feishu_task.due_date == task.due_date, "截止日期应该同步"
            
            if task.assignee:
                assert feishu_task.assignee == task.assignee, "负责人应该同步"
            
            if '重要' in task.priority or '紧急' in task.priority:
                assert feishu_task.priority == "high", "优先级应该同步"
            
            # 状态应该匹配
            expected_status = "completed" if task.completed else "pending"
            assert feishu_task.status == expected_status, "任务状态应该匹配"
            
            return SyncResult(
                success=True,
                message="Task created",
                feishu_id="task_12345",
                feishu_url="https://feishu.cn/task/12345",
                sync_time=datetime.now()
            )
        
        mock_mcp_client.create_task.side_effect = mock_create_task
        
        # 创建同步引擎并同步
        engine = FeishuSyncEngine(mock_mcp_client, temp_vault)
        result = engine.sync_task_to_feishu(task)
        
        # 验证同步成功
        assert result.success, f"同步应该成功: {result.error}"
        assert mock_mcp_client.create_task.called, "应该调用 create_task"
    
    finally:
        # 清理临时目录
        shutil.rmtree(temp_vault)


# Feature: obsidian-knowledge-management-workflow, Property 20: 同步元数据记录
@given(task=task_strategy())
@settings(max_examples=100, deadline=None)
def test_property_20_sync_metadata_recording(task):
    """
    属性 20：对于任意同步的任务或文档，应该记录完整的同步元数据
    
    验证需求: 20.6, 21.4
    """
    # 创建临时目录
    temp_vault = tempfile.mkdtemp()
    
    try:
        # 创建 mock MCP 客户端
        mock_mcp_client = Mock(spec=MCPClient)
        mock_mcp_client.is_connected.return_value = True
        mock_mcp_client.connect.return_value = True
        
        # 确保任务标记为需要同步
        if '#sync/feishu' not in task.tags:
            task.tags.append('#sync/feishu')
        
        # 创建测试文件
        test_file = Path(temp_vault) / task.file_path
        test_file.parent.mkdir(parents=True, exist_ok=True)
        
        checkbox = "[x]" if task.completed else "[ ]"
        tags_str = ' '.join(task.tags)
        content = f"- {checkbox} {task.content} {tags_str}\n"
        test_file.write_text(content, encoding='utf-8')
        
        # Mock MCP 客户端
        feishu_id = "task_12345"
        feishu_url = "https://feishu.cn/task/12345"
        sync_time = datetime.now()
        
        mock_mcp_client.create_task.return_value = SyncResult(
            success=True,
            message="Task created",
            feishu_id=feishu_id,
            feishu_url=feishu_url,
            sync_time=sync_time
        )
        
        # 同步任务
        engine = FeishuSyncEngine(mock_mcp_client, temp_vault)
        result = engine.sync_task_to_feishu(task)
        
        assert result.success, "同步应该成功"
        
        # 读取文件，验证元数据
        updated_content = test_file.read_text(encoding='utf-8')
        
        # 验证所有必需的元数据字段
        assert f"feishu_task_id: {feishu_id}" in updated_content, "应该记录 feishu_task_id"
        assert f"feishu_url: {feishu_url}" in updated_content, "应该记录 feishu_url"
        assert "last_sync:" in updated_content, "应该记录 last_sync"
        assert "sync_status: synced" in updated_content, "应该记录 sync_status"
    
    finally:
        # 清理临时目录
        shutil.rmtree(temp_vault)


# Feature: obsidian-knowledge-management-workflow, Property 25: 同步冲突检测
@given(
    task=task_strategy(),
    local_modified_after_sync=st.booleans(),
    feishu_modified_after_sync=st.booleans()
)
@settings(max_examples=100, deadline=None)
def test_property_25_sync_conflict_detection(
    task,
    local_modified_after_sync,
    feishu_modified_after_sync
):
    """
    属性 25：对于任意两端都有修改的内容，应该检测到冲突
    
    验证需求: 22.10, 22.11, 22.12
    """
    # 只测试两端都修改的情况
    assume(local_modified_after_sync and feishu_modified_after_sync)
    
    # 创建临时目录
    temp_vault = tempfile.mkdtemp()
    
    try:
        # 创建 mock MCP 客户端
        mock_mcp_client = Mock(spec=MCPClient)
        mock_mcp_client.is_connected.return_value = True
        mock_mcp_client.connect.return_value = True
        
        # 创建测试文件
        test_file = Path(temp_vault) / task.file_path
        test_file.parent.mkdir(parents=True, exist_ok=True)
        
        # 写入任务内容，包含同步元数据
        # 使用过去的时间作为最后同步时间
        last_sync_time = datetime.now() - timedelta(hours=1)
        checkbox = "[x]" if task.completed else "[ ]"
        tags_str = ' '.join(task.tags)
        
        content = f"""- {checkbox} {task.content} {tags_str}
  - feishu_task_id: task_12345
  - feishu_url: https://feishu.cn/task/12345
  - last_sync: {last_sync_time.isoformat()}
  - sync_status: synced
"""
        test_file.write_text(content, encoding='utf-8')
        
        # 修改文件时间为当前时间（模拟本地修改）
        # 这样文件修改时间会晚于 last_sync_time
        import os
        import time
        time.sleep(0.1)  # 确保时间差异
        current_time = datetime.now().timestamp()
        os.utime(test_file, (current_time, current_time))
        
        # Mock 飞书任务（状态与本地不同，模拟飞书端也被修改）
        feishu_task = FeishuTask(
            title=task.content,
            description="",
            status="completed" if not task.completed else "pending",  # 与本地相反
            feishu_task_id="task_12345",
            feishu_url="https://feishu.cn/task/12345"
        )
        
        mock_mcp_client.get_task.return_value = feishu_task
        
        # 尝试从飞书同步
        engine = FeishuSyncEngine(mock_mcp_client, temp_vault)
        
        # 应该抛出 SyncConflict 异常
        with pytest.raises(SyncConflict) as exc_info:
            engine.sync_from_feishu_task(task)
        
        # 验证冲突消息包含有用信息
        conflict_message = str(exc_info.value)
        assert "冲突" in conflict_message, "冲突消息应该包含'冲突'关键词"
        
        # 验证文件被标记为冲突状态
        updated_content = test_file.read_text(encoding='utf-8')
        assert "#sync-conflict/feishu" in updated_content, "应该标记为冲突状态"
    
    finally:
        # 清理临时目录
        shutil.rmtree(temp_vault)


# 单元测试：验证基本功能
def test_sync_task_to_feishu_basic(temp_vault, mock_mcp_client):
    """测试基本的任务同步功能"""
    task = Task(
        content="测试任务",
        completed=False,
        file_path="test.md",
        line_number=1,
        tags=['#sync/feishu'],
        category=TaskCategory.WORK
    )
    
    # 创建测试文件
    test_file = Path(temp_vault) / task.file_path
    test_file.write_text("- [ ] 测试任务 #sync/feishu\n", encoding='utf-8')
    
    # Mock MCP 客户端
    mock_mcp_client.create_task.return_value = SyncResult(
        success=True,
        message="Task created",
        feishu_id="task_12345",
        feishu_url="https://feishu.cn/task/12345",
        sync_time=datetime.now()
    )
    
    # 同步任务
    engine = FeishuSyncEngine(mock_mcp_client, temp_vault)
    result = engine.sync_task_to_feishu(task)
    
    assert result.success
    assert result.feishu_id == "task_12345"
    assert mock_mcp_client.create_task.called


def test_sync_document_to_feishu_basic(temp_vault, mock_mcp_client):
    """测试基本的文档同步功能"""
    file_path = "test_doc.md"
    test_file = Path(temp_vault) / file_path
    
    content = """---
tags:
  - sync/feishu-doc
---

# 测试文档

这是测试内容。
"""
    test_file.write_text(content, encoding='utf-8')
    
    # Mock MCP 客户端
    mock_mcp_client.create_document.return_value = SyncResult(
        success=True,
        message="Document created",
        feishu_id="doc_12345",
        feishu_url="https://feishu.cn/doc/12345",
        sync_time=datetime.now()
    )
    
    # 同步文档
    engine = FeishuSyncEngine(mock_mcp_client, temp_vault)
    result = engine.sync_document_to_feishu(file_path)
    
    assert result.success
    assert result.feishu_id == "doc_12345"
    assert mock_mcp_client.create_document.called


def test_sync_from_feishu_task_no_conflict(temp_vault, mock_mcp_client):
    """测试从飞书同步任务（无冲突）"""
    task = Task(
        content="测试任务",
        completed=False,
        file_path="test.md",
        line_number=1,
        category=TaskCategory.WORK
    )
    
    # 创建测试文件，包含同步元数据
    test_file = Path(temp_vault) / task.file_path
    # 使用更早的同步时间，确保不会触发冲突检测
    last_sync = datetime.now() - timedelta(hours=24)
    
    content = f"""- [ ] 测试任务
  - feishu_task_id: task_12345
  - last_sync: {last_sync.isoformat()}
"""
    test_file.write_text(content, encoding='utf-8')
    
    # 设置文件修改时间为同步时间之前（模拟文件没有在同步后被修改）
    import os
    import time
    mtime = (last_sync - timedelta(hours=1)).timestamp()
    os.utime(test_file, (mtime, mtime))
    
    # Mock 飞书任务（已完成）
    feishu_task = FeishuTask(
        title="测试任务",
        status="completed",
        feishu_task_id="task_12345"
    )
    
    mock_mcp_client.get_task.return_value = feishu_task
    
    # 从飞书同步
    engine = FeishuSyncEngine(mock_mcp_client, temp_vault)
    result = engine.sync_from_feishu_task(task)
    
    assert result.success
    
    # 验证任务状态已更新
    updated_content = test_file.read_text(encoding='utf-8')
    assert "- [x]" in updated_content, "任务应该标记为已完成"


def test_conflict_detection_marks_file(temp_vault, mock_mcp_client):
    """测试冲突检测会标记文件"""
    task = Task(
        content="测试任务",
        completed=False,
        file_path="test.md",
        line_number=1,
        category=TaskCategory.WORK
    )
    
    # 创建测试文件
    test_file = Path(temp_vault) / task.file_path
    last_sync = datetime.now() - timedelta(hours=1)
    
    content = f"""- [ ] 测试任务 #sync/feishu
  - feishu_task_id: task_12345
  - last_sync: {last_sync.isoformat()}
"""
    test_file.write_text(content, encoding='utf-8')
    
    # 修改文件时间
    import os
    import time
    time.sleep(0.1)
    os.utime(test_file, None)
    
    # Mock 飞书任务（状态不同）
    feishu_task = FeishuTask(
        title="测试任务",
        status="completed",  # 与本地不同
        feishu_task_id="task_12345"
    )
    
    mock_mcp_client.get_task.return_value = feishu_task
    
    # 尝试同步
    engine = FeishuSyncEngine(mock_mcp_client, temp_vault)
    
    with pytest.raises(SyncConflict):
        engine.sync_from_feishu_task(task)
    
    # 验证文件被标记为冲突
    updated_content = test_file.read_text(encoding='utf-8')
    assert "#sync-conflict/feishu" in updated_content
