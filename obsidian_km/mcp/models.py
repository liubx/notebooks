"""Data models for MCP integration."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List, Dict, Any


@dataclass
class FeishuTask:
    """Represents a Feishu task."""
    
    title: str
    description: str = ""
    due_date: Optional[str] = None
    assignee: Optional[str] = None
    priority: Optional[str] = None
    status: str = "pending"  # pending, in_progress, completed
    feishu_task_id: Optional[str] = None
    feishu_url: Optional[str] = None
    custom_group: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for API calls."""
        data = {
            "title": self.title,
            "description": self.description,
            "status": self.status,
        }
        
        if self.due_date:
            data["due_date"] = self.due_date
        if self.assignee:
            data["assignee"] = self.assignee
        if self.priority:
            data["priority"] = self.priority
        if self.custom_group:
            data["custom_group"] = self.custom_group
            
        return data


@dataclass
class FeishuDocument:
    """Represents a Feishu document."""
    
    title: str
    content: str  # Feishu format content
    doc_type: str = "doc"  # doc, wiki, sheet
    folder_path: Optional[str] = None
    feishu_doc_id: Optional[str] = None
    feishu_url: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for API calls."""
        data = {
            "title": self.title,
            "content": self.content,
            "doc_type": self.doc_type,
        }
        
        if self.folder_path:
            data["folder_path"] = self.folder_path
            
        return data


@dataclass
class SyncResult:
    """Result of a sync operation."""
    
    success: bool
    message: str
    feishu_id: Optional[str] = None
    feishu_url: Optional[str] = None
    sync_time: datetime = field(default_factory=datetime.now)
    error: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "success": self.success,
            "message": self.message,
            "feishu_id": self.feishu_id,
            "feishu_url": self.feishu_url,
            "sync_time": self.sync_time.isoformat(),
            "error": self.error,
        }
