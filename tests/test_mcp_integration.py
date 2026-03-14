"""Unit tests for MCP integration."""

import pytest
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime

from obsidian_km.mcp import (
    MCPClient,
    MarkdownToFeishuConverter,
    FeishuTask,
    FeishuDocument,
    SyncResult
)
from obsidian_km.mcp.client import MCPConnectionError, MCPAPIError
from obsidian_km.config import FeishuCredentials


class TestFeishuTask:
    """Test FeishuTask model."""
    
    def test_task_creation(self):
        """Test creating a FeishuTask."""
        task = FeishuTask(
            title="Test Task",
            description="Test description",
            due_date="2024-01-20",
            assignee="张三",
            priority="high",
            status="pending"
        )
        
        assert task.title == "Test Task"
        assert task.description == "Test description"
        assert task.due_date == "2024-01-20"
        assert task.assignee == "张三"
        assert task.priority == "high"
        assert task.status == "pending"
    
    def test_task_to_dict(self):
        """Test converting task to dictionary."""
        task = FeishuTask(
            title="Test Task",
            description="Test description",
            due_date="2024-01-20",
            assignee="张三",
            priority="high"
        )
        
        data = task.to_dict()
        
        assert data["title"] == "Test Task"
        assert data["description"] == "Test description"
        assert data["due_date"] == "2024-01-20"
        assert data["assignee"] == "张三"
        assert data["priority"] == "high"
        assert data["status"] == "pending"


class TestFeishuDocument:
    """Test FeishuDocument model."""
    
    def test_document_creation(self):
        """Test creating a FeishuDocument."""
        doc = FeishuDocument(
            title="Test Document",
            content="Test content",
            doc_type="doc",
            folder_path="/test/folder"
        )
        
        assert doc.title == "Test Document"
        assert doc.content == "Test content"
        assert doc.doc_type == "doc"
        assert doc.folder_path == "/test/folder"
    
    def test_document_to_dict(self):
        """Test converting document to dictionary."""
        doc = FeishuDocument(
            title="Test Document",
            content="Test content",
            doc_type="wiki",
            folder_path="/test/folder"
        )
        
        data = doc.to_dict()
        
        assert data["title"] == "Test Document"
        assert data["content"] == "Test content"
        assert data["doc_type"] == "wiki"
        assert data["folder_path"] == "/test/folder"


class TestSyncResult:
    """Test SyncResult model."""
    
    def test_sync_result_success(self):
        """Test successful sync result."""
        result = SyncResult(
            success=True,
            message="Sync successful",
            feishu_id="task_12345",
            feishu_url="https://feishu.cn/task/12345"
        )
        
        assert result.success is True
        assert result.message == "Sync successful"
        assert result.feishu_id == "task_12345"
        assert result.feishu_url == "https://feishu.cn/task/12345"
        assert result.error is None
    
    def test_sync_result_failure(self):
        """Test failed sync result."""
        result = SyncResult(
            success=False,
            message="Sync failed",
            error="Network timeout"
        )
        
        assert result.success is False
        assert result.message == "Sync failed"
        assert result.error == "Network timeout"
        assert result.feishu_id is None


class TestMCPClient:
    """Test MCPClient."""
    
    @pytest.fixture
    def credentials(self):
        """Create test credentials."""
        return FeishuCredentials(
            app_id="cli_test123",
            app_secret="secret123"
        )
    
    @pytest.fixture
    def client(self, credentials):
        """Create test client."""
        return MCPClient(credentials)
    
    def test_client_initialization(self, client, credentials):
        """Test client initialization."""
        assert client.credentials == credentials
        assert client.max_retries == 3
        assert client.is_connected() is False
    
    def test_connect_success(self, client):
        """Test successful connection."""
        result = client.connect()
        
        assert result is True
        assert client.is_connected() is True
    
    def test_connect_invalid_credentials(self):
        """Test connection with invalid credentials."""
        invalid_creds = FeishuCredentials(app_id="", app_secret="")
        client = MCPClient(invalid_creds)
        
        with pytest.raises(MCPConnectionError):
            client.connect()
    
    def test_disconnect(self, client):
        """Test disconnection."""
        client.connect()
        assert client.is_connected() is True
        
        client.disconnect()
        assert client.is_connected() is False
    
    def test_create_task_not_connected(self, client):
        """Test creating task when not connected."""
        task = FeishuTask(title="Test Task")
        
        with pytest.raises(MCPConnectionError):
            client.create_task(task)
    
    @patch.object(MCPClient, '_call_api')
    def test_create_task_success(self, mock_call_api, client):
        """Test successful task creation."""
        client.connect()
        
        # Mock API response
        mock_call_api.return_value = {
            "task_id": "task_12345",
            "url": "https://feishu.cn/task/12345"
        }
        
        task = FeishuTask(
            title="Test Task",
            description="Test description"
        )
        
        result = client.create_task(task)
        
        assert result.success is True
        assert result.feishu_id == "task_12345"
        assert result.feishu_url == "https://feishu.cn/task/12345"
        assert "successfully" in result.message.lower()
        
        # Verify API was called correctly
        mock_call_api.assert_called_once()
        call_args = mock_call_api.call_args[0]
        assert call_args[0] == "create_task"
        assert call_args[1]["task"]["title"] == "Test Task"
    
    @patch.object(MCPClient, '_call_api')
    def test_create_task_with_retry(self, mock_call_api, client):
        """Test task creation with retry on failure."""
        client.connect()
        
        # Mock API to fail twice then succeed
        mock_call_api.side_effect = [
            MCPAPIError("Network timeout"),
            MCPAPIError("Network timeout"),
            {
                "task_id": "task_12345",
                "url": "https://feishu.cn/task/12345"
            }
        ]
        
        task = FeishuTask(title="Test Task")
        
        result = client.create_task(task)
        
        assert result.success is True
        assert mock_call_api.call_count == 3
    
    @patch.object(MCPClient, '_call_api')
    def test_create_task_max_retries_exceeded(self, mock_call_api, client):
        """Test task creation when max retries exceeded."""
        client.connect()
        
        # Mock API to always fail
        mock_call_api.side_effect = MCPAPIError("Network timeout")
        
        task = FeishuTask(title="Test Task")
        
        result = client.create_task(task)
        
        assert result.success is False
        assert "after 3 attempts" in result.message
        assert result.error is not None
        assert mock_call_api.call_count == 3
    
    @patch.object(MCPClient, '_call_api')
    def test_update_task_success(self, mock_call_api, client):
        """Test successful task update."""
        client.connect()
        
        mock_call_api.return_value = {
            "url": "https://feishu.cn/task/12345"
        }
        
        task = FeishuTask(
            title="Updated Task",
            status="completed"
        )
        
        result = client.update_task("task_12345", task)
        
        assert result.success is True
        assert result.feishu_id == "task_12345"
        assert "successfully" in result.message.lower()
    
    @patch.object(MCPClient, '_call_api')
    def test_get_task_success(self, mock_call_api, client):
        """Test getting a task."""
        client.connect()
        
        mock_call_api.return_value = {
            "title": "Test Task",
            "description": "Test description",
            "due_date": "2024-01-20",
            "status": "pending",
            "url": "https://feishu.cn/task/12345"
        }
        
        task = client.get_task("task_12345")
        
        assert task is not None
        assert task.title == "Test Task"
        assert task.description == "Test description"
        assert task.due_date == "2024-01-20"
        assert task.feishu_task_id == "task_12345"
    
    @patch.object(MCPClient, '_call_api')
    def test_get_task_not_found(self, mock_call_api, client):
        """Test getting a non-existent task."""
        client.connect()
        
        mock_call_api.side_effect = MCPAPIError("Task not found")
        
        task = client.get_task("task_nonexistent")
        
        assert task is None
    
    @patch.object(MCPClient, '_call_api')
    def test_create_document_success(self, mock_call_api, client):
        """Test successful document creation."""
        client.connect()
        
        mock_call_api.return_value = {
            "doc_id": "doc_12345",
            "url": "https://feishu.cn/doc/12345"
        }
        
        doc = FeishuDocument(
            title="Test Document",
            content="Test content"
        )
        
        result = client.create_document(doc)
        
        assert result.success is True
        assert result.feishu_id == "doc_12345"
        assert result.feishu_url == "https://feishu.cn/doc/12345"
    
    @patch.object(MCPClient, '_call_api')
    def test_update_document_success(self, mock_call_api, client):
        """Test successful document update."""
        client.connect()
        
        mock_call_api.return_value = {
            "url": "https://feishu.cn/doc/12345"
        }
        
        doc = FeishuDocument(
            title="Updated Document",
            content="Updated content"
        )
        
        result = client.update_document("doc_12345", doc)
        
        assert result.success is True
        assert result.feishu_id == "doc_12345"
    
    @patch.object(MCPClient, '_call_api')
    def test_upload_image_success(self, mock_call_api, client):
        """Test successful image upload."""
        client.connect()
        
        mock_call_api.return_value = {
            "url": "https://feishu.cn/images/test.png"
        }
        
        url = client.upload_image("/path/to/image.png")
        
        assert url == "https://feishu.cn/images/test.png"
    
    @patch.object(MCPClient, '_call_api')
    def test_upload_image_failure(self, mock_call_api, client):
        """Test image upload failure."""
        client.connect()
        
        mock_call_api.side_effect = MCPAPIError("Upload failed")
        
        url = client.upload_image("/path/to/image.png")
        
        assert url is None


class TestMarkdownToFeishuConverter:
    """Test MarkdownToFeishuConverter."""
    
    @pytest.fixture
    def converter(self):
        """Create converter instance."""
        return MarkdownToFeishuConverter()
    
    def test_convert_heading(self, converter):
        """Test converting headings."""
        markdown = "# Heading 1\n## Heading 2\n### Heading 3"
        
        blocks = converter.convert(markdown)
        
        assert len(blocks) == 3
        assert blocks[0]["type"] == "heading"
        assert blocks[0]["level"] == 1
        assert blocks[0]["text"] == "Heading 1"
        assert blocks[1]["level"] == 2
        assert blocks[2]["level"] == 3
    
    def test_convert_paragraph(self, converter):
        """Test converting paragraphs."""
        markdown = "This is a paragraph."
        
        blocks = converter.convert(markdown)
        
        assert len(blocks) == 1
        assert blocks[0]["type"] == "text"
        assert blocks[0]["text"] == "This is a paragraph."
    
    def test_convert_code_block(self, converter):
        """Test converting code blocks."""
        markdown = "```python\ndef hello():\n    print('Hello')\n```"
        
        blocks = converter.convert(markdown)
        
        assert len(blocks) == 1
        assert blocks[0]["type"] == "code"
        assert blocks[0]["language"] == "python"
        assert "def hello()" in blocks[0]["code"]
    
    def test_convert_task_list(self, converter):
        """Test converting task lists."""
        markdown = "- [ ] Task 1\n- [x] Task 2\n- [ ] Task 3"
        
        blocks = converter.convert(markdown)
        
        assert len(blocks) == 3
        assert blocks[0]["type"] == "task"
        assert blocks[0]["checked"] is False
        assert blocks[0]["text"] == "Task 1"
        assert blocks[1]["checked"] is True
        assert blocks[1]["text"] == "Task 2"
    
    def test_convert_unordered_list(self, converter):
        """Test converting unordered lists."""
        markdown = "- Item 1\n- Item 2\n- Item 3"
        
        blocks = converter.convert(markdown)
        
        assert len(blocks) == 1
        assert blocks[0]["type"] == "list"
        assert blocks[0]["ordered"] is False
        assert len(blocks[0]["items"]) == 3
        assert blocks[0]["items"][0] == "Item 1"
    
    def test_convert_ordered_list(self, converter):
        """Test converting ordered lists."""
        markdown = "1. First\n2. Second\n3. Third"
        
        blocks = converter.convert(markdown)
        
        assert len(blocks) == 1
        assert blocks[0]["type"] == "list"
        assert blocks[0]["ordered"] is True
        assert len(blocks[0]["items"]) == 3
        assert blocks[0]["items"][0] == "First"
    
    def test_convert_table(self, converter):
        """Test converting tables."""
        markdown = "| Name | Age |\n|------|-----|\n| Alice | 30 |\n| Bob | 25 |"
        
        blocks = converter.convert(markdown)
        
        assert len(blocks) == 1
        assert blocks[0]["type"] == "table"
        assert blocks[0]["headers"] == ["Name", "Age"]
        assert len(blocks[0]["rows"]) == 2
        assert blocks[0]["rows"][0] == ["Alice", "30"]
    
    def test_convert_bold_text(self, converter):
        """Test converting bold text."""
        markdown = "This is **bold** text"
        
        blocks = converter.convert(markdown)
        
        assert len(blocks) == 1
        assert "<b>bold</b>" in blocks[0]["text"]
    
    def test_convert_italic_text(self, converter):
        """Test converting italic text."""
        markdown = "This is *italic* text"
        
        blocks = converter.convert(markdown)
        
        assert len(blocks) == 1
        assert "<i>italic</i>" in blocks[0]["text"]
    
    def test_convert_inline_code(self, converter):
        """Test converting inline code."""
        markdown = "Use `print()` function"
        
        blocks = converter.convert(markdown)
        
        assert len(blocks) == 1
        assert "<code>print()</code>" in blocks[0]["text"]
    
    def test_convert_links(self, converter):
        """Test converting links."""
        markdown = "Visit [Google](https://google.com)"
        
        blocks = converter.convert(markdown)
        
        assert len(blocks) == 1
        assert '<a href="https://google.com">Google</a>' in blocks[0]["text"]
    
    def test_convert_images(self, converter):
        """Test converting images."""
        markdown = "![Alt text](https://example.com/image.png)"
        
        blocks = converter.convert(markdown)
        
        assert len(blocks) == 1
        assert '<img src="https://example.com/image.png" alt="Alt text">' in blocks[0]["text"]
    
    def test_convert_mixed_content(self, converter):
        """Test converting mixed content."""
        markdown = """# Title

This is a paragraph with **bold** and *italic* text.

- Item 1
- Item 2

```python
print("Hello")
```

- [ ] Task 1
- [x] Task 2
"""
        
        blocks = converter.convert(markdown)
        
        # Should have: heading, paragraph, list, code, 2 tasks
        assert len(blocks) >= 6
        assert blocks[0]["type"] == "heading"
        assert blocks[1]["type"] == "text"
        assert any(b["type"] == "list" for b in blocks)
        assert any(b["type"] == "code" for b in blocks)
        assert any(b["type"] == "task" for b in blocks)
    
    def test_convert_empty_content(self, converter):
        """Test converting empty content."""
        markdown = ""
        
        blocks = converter.convert(markdown)
        
        assert len(blocks) == 0
    
    def test_convert_only_whitespace(self, converter):
        """Test converting only whitespace."""
        markdown = "\n\n\n"
        
        blocks = converter.convert(markdown)
        
        assert len(blocks) == 0
