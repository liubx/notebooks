"""Tests for sync center module."""

import pytest
from pathlib import Path
from datetime import datetime
from hypothesis import given, strategies as st, settings

from obsidian_km.sync.sync_center import (
    SyncCenter,
    SyncItem,
    SyncItemType,
    SyncStatus,
    SyncStatistics
)


@pytest.fixture
def test_vault(tmp_path):
    """Create a test vault with sync items."""
    vault = tmp_path / "test-vault"
    vault.mkdir()
    
    # Create test files with different sync statuses
    
    # 1. Pending task sync
    daily_dir = vault / "0-Daily" / "2024" / "01"
    daily_dir.mkdir(parents=True)
    
    daily_file = daily_dir / "2024-01-15.md"
    daily_file.write_text("""---
date: 2024-01-15
---

# 2024-01-15

## 工作任务

- [ ] 完成设计文档 #sync/feishu #重要
- [x] 代码审查 #synced/feishu
  - feishu_task_id: task_12345
  - feishu_url: https://feishu.cn/task/12345
  - last_sync: 2024-01-15T10:00:00
  - sync_status: synced
""", encoding='utf-8')
    
    # 2. Pending document sync
    project_dir = vault / "1-Projects" / "Work" / "ProjectA"
    project_dir.mkdir(parents=True)
    
    project_file = project_dir / "README.md"
    project_file.write_text("""---
title: ProjectA
tags:
  - sync/feishu-doc
---

# ProjectA

This is a project document.
""", encoding='utf-8')
    
    # 3. Synced document
    synced_doc = project_dir / "design.md"
    synced_doc.write_text("""---
title: Design Document
feishu_sync:
  platform: feishu
  doc_type: doc
  feishu_doc_id: "doc_xxxxx"
  feishu_url: "https://feishu.cn/doc/xxxxx"
  last_sync: 2024-01-15T11:00:00
  sync_status: synced
tags:
  - synced/feishu
---

# Design Document

Content here.
""", encoding='utf-8')
    
    # 4. Error task
    error_file = daily_dir / "2024-01-16.md"
    error_file.write_text("""---
date: 2024-01-16
---

# 2024-01-16

- [ ] 失败的任务 #sync-error/feishu
""", encoding='utf-8')
    
    # 5. Conflict document
    conflict_doc = project_dir / "conflict.md"
    conflict_doc.write_text("""---
title: Conflict Document
tags:
  - sync-conflict/feishu
---

# Conflict Document

This has a conflict.
""", encoding='utf-8')
    
    return str(vault)


def test_scan_all_sync_items(test_vault):
    """Test scanning all sync items."""
    center = SyncCenter(test_vault)
    
    items = center.scan_all_sync_items()
    
    # Should find all sync items
    assert len(items) > 0
    
    # Check that we have different types
    task_items = [item for item in items if item.item_type == SyncItemType.TASK]
    doc_items = [item for item in items if item.item_type == SyncItemType.DOCUMENT]
    
    assert len(task_items) > 0
    assert len(doc_items) > 0


def test_scan_pending_task(test_vault):
    """Test scanning pending task sync."""
    center = SyncCenter(test_vault)
    
    items = center.scan_all_sync_items()
    
    # Find the pending task
    pending_tasks = [
        item for item in items
        if item.item_type == SyncItemType.TASK
        and item.status == SyncStatus.PENDING
        and "完成设计文档" in item.title
    ]
    
    assert len(pending_tasks) == 1
    task = pending_tasks[0]
    
    assert task.file_path.endswith("2024-01-15.md")
    assert task.feishu_id is None
    assert task.line_number is not None


def test_scan_synced_task(test_vault):
    """Test scanning synced task."""
    center = SyncCenter(test_vault)
    
    items = center.scan_all_sync_items()
    
    # Find the synced task
    synced_tasks = [
        item for item in items
        if item.item_type == SyncItemType.TASK
        and item.status == SyncStatus.SYNCED
        and "代码审查" in item.title
    ]
    
    assert len(synced_tasks) == 1
    task = synced_tasks[0]
    
    assert task.feishu_id == "task_12345"
    assert task.feishu_url == "https://feishu.cn/task/12345"
    assert task.last_sync == "2024-01-15T10:00:00"


def test_scan_pending_document(test_vault):
    """Test scanning pending document sync."""
    center = SyncCenter(test_vault)
    
    items = center.scan_all_sync_items()
    
    # Find the pending document
    pending_docs = [
        item for item in items
        if item.item_type == SyncItemType.DOCUMENT
        and item.status == SyncStatus.PENDING
        and "ProjectA" in item.title
    ]
    
    assert len(pending_docs) == 1
    doc = pending_docs[0]
    
    assert doc.file_path.endswith("README.md")
    assert doc.feishu_id is None


def test_scan_synced_document(test_vault):
    """Test scanning synced document."""
    center = SyncCenter(test_vault)
    
    items = center.scan_all_sync_items()
    
    # Find the synced document
    synced_docs = [
        item for item in items
        if item.item_type == SyncItemType.DOCUMENT
        and item.status == SyncStatus.SYNCED
        and "Design Document" in item.title
    ]
    
    assert len(synced_docs) == 1
    doc = synced_docs[0]
    
    assert doc.feishu_id == "doc_xxxxx"
    assert doc.feishu_url == "https://feishu.cn/doc/xxxxx"
    assert doc.last_sync == "2024-01-15T11:00:00"


def test_scan_error_task(test_vault):
    """Test scanning error task."""
    center = SyncCenter(test_vault)
    
    items = center.scan_all_sync_items()
    
    # Find the error task
    error_tasks = [
        item for item in items
        if item.item_type == SyncItemType.TASK
        and item.status == SyncStatus.ERROR
    ]
    
    assert len(error_tasks) == 1
    task = error_tasks[0]
    
    assert "失败的任务" in task.title


def test_scan_conflict_document(test_vault):
    """Test scanning conflict document."""
    center = SyncCenter(test_vault)
    
    items = center.scan_all_sync_items()
    
    # Find the conflict document
    conflict_docs = [
        item for item in items
        if item.item_type == SyncItemType.DOCUMENT
        and item.status == SyncStatus.CONFLICT
    ]
    
    assert len(conflict_docs) == 1
    doc = conflict_docs[0]
    
    assert "Conflict Document" in doc.title


def test_classify_sync_items(test_vault):
    """Test classifying sync items by status."""
    center = SyncCenter(test_vault)
    
    items = center.scan_all_sync_items()
    classified = center.classify_sync_items(items)
    
    # Check that all statuses are present
    assert SyncStatus.PENDING in classified
    assert SyncStatus.SYNCED in classified
    assert SyncStatus.ERROR in classified
    assert SyncStatus.CONFLICT in classified
    
    # Check counts
    assert len(classified[SyncStatus.PENDING]) > 0
    assert len(classified[SyncStatus.SYNCED]) > 0
    assert len(classified[SyncStatus.ERROR]) > 0
    assert len(classified[SyncStatus.CONFLICT]) > 0


def test_calculate_statistics(test_vault):
    """Test calculating sync statistics."""
    center = SyncCenter(test_vault)
    
    items = center.scan_all_sync_items()
    stats = center.calculate_statistics(items)
    
    # Check total
    assert stats.total == len(items)
    
    # Check status counts
    assert stats.pending > 0
    assert stats.synced > 0
    assert stats.error > 0
    assert stats.conflict > 0
    
    # Check type counts
    assert stats.tasks_total > 0
    assert stats.docs_total > 0
    
    # Check that totals match
    assert stats.total == stats.tasks_total + stats.docs_total
    assert stats.pending == stats.tasks_pending + stats.docs_pending
    assert stats.synced == stats.tasks_synced + stats.docs_synced
    assert stats.error == stats.tasks_error + stats.docs_error
    assert stats.conflict == stats.tasks_conflict + stats.docs_conflict
    
    # Check last update time
    assert stats.last_update is not None


def test_generate_sync_center_document(test_vault):
    """Test generating sync center document."""
    center = SyncCenter(test_vault)
    
    output_path = center.generate_sync_center_document()
    
    # Check that file was created
    full_path = Path(test_vault) / output_path
    assert full_path.exists()
    
    # Read and check content
    content = full_path.read_text(encoding='utf-8')
    
    # Check structure
    assert "# 飞书同步中心" in content
    assert "## 📊 同步统计" in content
    assert "## ⏳ 待同步" in content
    assert "## ✅ 已同步" in content
    assert "## ❌ 同步失败" in content
    assert "## ⚠️ 同步冲突" in content
    
    # Check that items are listed
    assert "完成设计文档" in content
    assert "代码审查" in content
    assert "ProjectA" in content
    assert "Design Document" in content


def test_extract_task_content():
    """Test extracting task content."""
    center = SyncCenter("/tmp/vault")
    
    # Test with tags and metadata
    line = "- [ ] 完成设计文档 #sync/feishu #重要 📅 2024-01-20 @张三"
    content = center._extract_task_content(line)
    
    assert content == "完成设计文档"
    
    # Test with completed task
    line = "- [x] 代码审查 #synced/feishu"
    content = center._extract_task_content(line)
    
    assert content == "代码审查"


def test_extract_document_title():
    """Test extracting document title."""
    center = SyncCenter("/tmp/vault")
    
    # Test with YAML front matter
    content = """---
title: Test Document
---

# My Document Title

Content here.
"""
    
    title = center._extract_document_title(content)
    assert title == "My Document Title"
    
    # Test without YAML
    content = """# Another Title

Content here.
"""
    
    title = center._extract_document_title(content)
    assert title == "Another Title"
    
    # Test without title
    content = "Just content"
    title = center._extract_document_title(content)
    assert title == "Untitled"


def test_detect_sync_status():
    """Test detecting sync status from text."""
    center = SyncCenter("/tmp/vault")
    
    # Test pending
    assert center._detect_sync_status("#sync/feishu") == SyncStatus.PENDING
    assert center._detect_sync_status("#sync/feishu-doc") == SyncStatus.PENDING
    assert center._detect_sync_status("#sync/feishu-wiki") == SyncStatus.PENDING
    
    # Test synced
    assert center._detect_sync_status("#synced/feishu") == SyncStatus.SYNCED
    
    # Test error
    assert center._detect_sync_status("#sync-error/feishu") == SyncStatus.ERROR
    
    # Test conflict
    assert center._detect_sync_status("#sync-conflict/feishu") == SyncStatus.CONFLICT
    
    # Test no sync tag
    assert center._detect_sync_status("no sync tag") is None


# Feature: obsidian-knowledge-management-workflow, Property 26: 同步中心状态聚合
@given(
    num_pending=st.integers(min_value=0, max_value=10),
    num_synced=st.integers(min_value=0, max_value=10),
    num_error=st.integers(min_value=0, max_value=10),
    num_conflict=st.integers(min_value=0, max_value=10)
)
@settings(max_examples=100)
def test_property_sync_center_aggregation(
    num_pending, num_synced, num_error, num_conflict
):
    """
    Property 26: 对于任意时刻，同步中心应该正确聚合和分类所有同步项
    
    验证需求: 23.2, 23.3, 23.4, 23.5, 23.7
    """
    # Create sync items with different statuses
    sync_items = []
    
    # Add pending items
    for i in range(num_pending):
        sync_items.append(SyncItem(
            file_path=f"pending_{i}.md",
            item_type=SyncItemType.TASK if i % 2 == 0 else SyncItemType.DOCUMENT,
            status=SyncStatus.PENDING,
            title=f"Pending Item {i}"
        ))
    
    # Add synced items
    for i in range(num_synced):
        sync_items.append(SyncItem(
            file_path=f"synced_{i}.md",
            item_type=SyncItemType.TASK if i % 2 == 0 else SyncItemType.DOCUMENT,
            status=SyncStatus.SYNCED,
            title=f"Synced Item {i}",
            feishu_id=f"id_{i}",
            feishu_url=f"https://feishu.cn/{i}",
            last_sync="2024-01-15T10:00:00"
        ))
    
    # Add error items
    for i in range(num_error):
        sync_items.append(SyncItem(
            file_path=f"error_{i}.md",
            item_type=SyncItemType.TASK if i % 2 == 0 else SyncItemType.DOCUMENT,
            status=SyncStatus.ERROR,
            title=f"Error Item {i}"
        ))
    
    # Add conflict items
    for i in range(num_conflict):
        sync_items.append(SyncItem(
            file_path=f"conflict_{i}.md",
            item_type=SyncItemType.TASK if i % 2 == 0 else SyncItemType.DOCUMENT,
            status=SyncStatus.CONFLICT,
            title=f"Conflict Item {i}"
        ))
    
    # Create sync center
    center = SyncCenter("/tmp/vault")
    
    # Classify items
    classified = center.classify_sync_items(sync_items)
    
    # Verify classification
    assert len(classified[SyncStatus.PENDING]) == num_pending
    assert len(classified[SyncStatus.SYNCED]) == num_synced
    assert len(classified[SyncStatus.ERROR]) == num_error
    assert len(classified[SyncStatus.CONFLICT]) == num_conflict
    
    # Calculate statistics
    stats = center.calculate_statistics(sync_items)
    
    # Verify statistics
    assert stats.total == len(sync_items)
    assert stats.pending == num_pending
    assert stats.synced == num_synced
    assert stats.error == num_error
    assert stats.conflict == num_conflict
    
    # Verify type counts
    expected_tasks = sum(1 for item in sync_items if item.item_type == SyncItemType.TASK)
    expected_docs = sum(1 for item in sync_items if item.item_type == SyncItemType.DOCUMENT)
    
    assert stats.tasks_total == expected_tasks
    assert stats.docs_total == expected_docs
    
    # Verify totals match
    assert stats.total == stats.tasks_total + stats.docs_total
    assert stats.pending == stats.tasks_pending + stats.docs_pending
    assert stats.synced == stats.tasks_synced + stats.docs_synced
    assert stats.error == stats.tasks_error + stats.docs_error
    assert stats.conflict == stats.tasks_conflict + stats.docs_conflict


def test_skip_templates_folder(tmp_path):
    """Test that Templates folder is skipped during scanning."""
    vault = tmp_path / "vault"
    vault.mkdir()
    
    # Create a file in Templates folder
    templates_dir = vault / "Templates"
    templates_dir.mkdir()
    
    template_file = templates_dir / "template.md"
    template_file.write_text("""---
tags:
  - sync/feishu
---

# Template

This should be skipped.
""", encoding='utf-8')
    
    # Create a normal file
    daily_dir = vault / "0-Daily"
    daily_dir.mkdir()
    
    daily_file = daily_dir / "2024-01-15.md"
    daily_file.write_text("""---
tags:
  - sync/feishu
---

# Daily Note

This should be scanned.
""", encoding='utf-8')
    
    center = SyncCenter(str(vault))
    items = center.scan_all_sync_items()
    
    # Should only find the daily note, not the template
    assert len(items) == 1
    assert items[0].file_path.endswith("2024-01-15.md")


def test_empty_vault(tmp_path):
    """Test scanning an empty vault."""
    vault = tmp_path / "vault"
    vault.mkdir()
    
    center = SyncCenter(str(vault))
    items = center.scan_all_sync_items()
    
    assert len(items) == 0
    
    # Statistics should be all zeros
    stats = center.calculate_statistics(items)
    assert stats.total == 0
    assert stats.pending == 0
    assert stats.synced == 0
    assert stats.error == 0
    assert stats.conflict == 0


def test_multiple_tasks_in_file(tmp_path):
    """Test scanning multiple tasks in the same file."""
    vault = tmp_path / "vault"
    vault.mkdir()
    
    daily_file = vault / "daily.md"
    daily_file.write_text("""# Daily Note

- [ ] Task 1 #sync/feishu
- [ ] Task 2 #synced/feishu
- [ ] Task 3 #sync-error/feishu
- [ ] Task 4 #sync-conflict/feishu
- [ ] Task 5 (no sync tag)
""", encoding='utf-8')
    
    center = SyncCenter(str(vault))
    items = center.scan_all_sync_items()
    
    # Should find 4 tasks (excluding the one without sync tag)
    task_items = [item for item in items if item.item_type == SyncItemType.TASK]
    assert len(task_items) == 4
    
    # Check statuses
    statuses = [item.status for item in task_items]
    assert SyncStatus.PENDING in statuses
    assert SyncStatus.SYNCED in statuses
    assert SyncStatus.ERROR in statuses
    assert SyncStatus.CONFLICT in statuses
