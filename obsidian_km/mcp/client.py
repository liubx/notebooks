"""MCP client wrapper for Feishu API access."""

import time
from typing import Optional, Dict, Any, List
from datetime import datetime

from ..config import FeishuCredentials
from .models import FeishuTask, FeishuDocument, SyncResult


class MCPConnectionError(Exception):
    """Raised when MCP connection fails."""
    pass


class MCPAPIError(Exception):
    """Raised when MCP API call fails."""
    pass


class MCPClient:
    """
    MCP client wrapper for Feishu API access.
    
    This client wraps the lark-mcp service to provide a clean interface
    for Feishu API operations. In production, this would connect to an
    actual MCP server. For testing, this can be mocked.
    """
    
    def __init__(self, credentials: FeishuCredentials, max_retries: int = 3):
        """
        Initialize MCP client.
        
        Args:
            credentials: Feishu API credentials
            max_retries: Maximum number of retries for failed requests
        """
        self.credentials = credentials
        self.max_retries = max_retries
        self._connected = False
    
    def connect(self) -> bool:
        """
        Connect to MCP service.
        
        Returns:
            True if connection successful
            
        Raises:
            MCPConnectionError: If connection fails
        """
        # In production, this would establish connection to lark-mcp service
        # For now, we just validate credentials
        if not self.credentials.app_id or not self.credentials.app_secret:
            raise MCPConnectionError("Invalid credentials: app_id and app_secret required")
        
        self._connected = True
        return True
    
    def is_connected(self) -> bool:
        """Check if client is connected."""
        return self._connected
    
    def disconnect(self) -> None:
        """Disconnect from MCP service."""
        self._connected = False
    
    def create_task(
        self,
        task: FeishuTask,
        tasklist_id: Optional[str] = None
    ) -> SyncResult:
        """
        Create a task in Feishu.
        
        Args:
            task: FeishuTask object
            tasklist_id: Optional tasklist ID to add task to
            
        Returns:
            SyncResult with task ID and URL
            
        Raises:
            MCPConnectionError: If not connected
            MCPAPIError: If API call fails
        """
        if not self._connected:
            raise MCPConnectionError("Not connected to MCP service")
        
        # Retry logic
        last_error = None
        for attempt in range(self.max_retries):
            try:
                # In production, this would call lark-mcp API
                # For now, simulate API call
                result = self._call_api(
                    "create_task",
                    {
                        "task": task.to_dict(),
                        "tasklist_id": tasklist_id
                    }
                )
                
                return SyncResult(
                    success=True,
                    message="Task created successfully",
                    feishu_id=result.get("task_id"),
                    feishu_url=result.get("url"),
                    sync_time=datetime.now()
                )
            
            except MCPAPIError as e:
                last_error = e
                if attempt < self.max_retries - 1:
                    # Wait before retry (exponential backoff)
                    time.sleep(2 ** attempt)
                    continue
                break
        
        return SyncResult(
            success=False,
            message=f"Failed to create task after {self.max_retries} attempts",
            error=str(last_error),
            sync_time=datetime.now()
        )
    
    def update_task(
        self,
        task_id: str,
        task: FeishuTask
    ) -> SyncResult:
        """
        Update a task in Feishu.
        
        Args:
            task_id: Feishu task ID
            task: Updated FeishuTask object
            
        Returns:
            SyncResult
            
        Raises:
            MCPConnectionError: If not connected
            MCPAPIError: If API call fails
        """
        if not self._connected:
            raise MCPConnectionError("Not connected to MCP service")
        
        last_error = None
        for attempt in range(self.max_retries):
            try:
                result = self._call_api(
                    "update_task",
                    {
                        "task_id": task_id,
                        "task": task.to_dict()
                    }
                )
                
                return SyncResult(
                    success=True,
                    message="Task updated successfully",
                    feishu_id=task_id,
                    feishu_url=result.get("url"),
                    sync_time=datetime.now()
                )
            
            except MCPAPIError as e:
                last_error = e
                if attempt < self.max_retries - 1:
                    time.sleep(2 ** attempt)
                    continue
                break
        
        return SyncResult(
            success=False,
            message=f"Failed to update task after {self.max_retries} attempts",
            error=str(last_error),
            sync_time=datetime.now()
        )
    
    def get_task(self, task_id: str) -> Optional[FeishuTask]:
        """
        Get a task from Feishu.
        
        Args:
            task_id: Feishu task ID
            
        Returns:
            FeishuTask object or None if not found
            
        Raises:
            MCPConnectionError: If not connected
            MCPAPIError: If API call fails
        """
        if not self._connected:
            raise MCPConnectionError("Not connected to MCP service")
        
        try:
            result = self._call_api("get_task", {"task_id": task_id})
            
            return FeishuTask(
                title=result.get("title", ""),
                description=result.get("description", ""),
                due_date=result.get("due_date"),
                assignee=result.get("assignee"),
                priority=result.get("priority"),
                status=result.get("status", "pending"),
                feishu_task_id=task_id,
                feishu_url=result.get("url")
            )
        
        except MCPAPIError:
            return None
    
    def create_document(
        self,
        document: FeishuDocument
    ) -> SyncResult:
        """
        Create a document in Feishu.
        
        Args:
            document: FeishuDocument object
            
        Returns:
            SyncResult with document ID and URL
            
        Raises:
            MCPConnectionError: If not connected
            MCPAPIError: If API call fails
        """
        if not self._connected:
            raise MCPConnectionError("Not connected to MCP service")
        
        last_error = None
        for attempt in range(self.max_retries):
            try:
                result = self._call_api(
                    "create_document",
                    {"document": document.to_dict()}
                )
                
                return SyncResult(
                    success=True,
                    message="Document created successfully",
                    feishu_id=result.get("doc_id"),
                    feishu_url=result.get("url"),
                    sync_time=datetime.now()
                )
            
            except MCPAPIError as e:
                last_error = e
                if attempt < self.max_retries - 1:
                    time.sleep(2 ** attempt)
                    continue
                break
        
        return SyncResult(
            success=False,
            message=f"Failed to create document after {self.max_retries} attempts",
            error=str(last_error),
            sync_time=datetime.now()
        )
    
    def update_document(
        self,
        doc_id: str,
        document: FeishuDocument
    ) -> SyncResult:
        """
        Update a document in Feishu.
        
        Args:
            doc_id: Feishu document ID
            document: Updated FeishuDocument object
            
        Returns:
            SyncResult
            
        Raises:
            MCPConnectionError: If not connected
            MCPAPIError: If API call fails
        """
        if not self._connected:
            raise MCPConnectionError("Not connected to MCP service")
        
        last_error = None
        for attempt in range(self.max_retries):
            try:
                result = self._call_api(
                    "update_document",
                    {
                        "doc_id": doc_id,
                        "document": document.to_dict()
                    }
                )
                
                return SyncResult(
                    success=True,
                    message="Document updated successfully",
                    feishu_id=doc_id,
                    feishu_url=result.get("url"),
                    sync_time=datetime.now()
                )
            
            except MCPAPIError as e:
                last_error = e
                if attempt < self.max_retries - 1:
                    time.sleep(2 ** attempt)
                    continue
                break
        
        return SyncResult(
            success=False,
            message=f"Failed to update document after {self.max_retries} attempts",
            error=str(last_error),
            sync_time=datetime.now()
        )
    
    def get_document(self, doc_id: str) -> Optional[FeishuDocument]:
        """
        Get a document from Feishu.
        
        Args:
            doc_id: Feishu document ID
            
        Returns:
            FeishuDocument object or None if not found
            
        Raises:
            MCPConnectionError: If not connected
            MCPAPIError: If API call fails
        """
        if not self._connected:
            raise MCPConnectionError("Not connected to MCP service")
        
        try:
            result = self._call_api("get_document", {"doc_id": doc_id})
            
            return FeishuDocument(
                title=result.get("title", ""),
                content=result.get("content", ""),
                doc_type=result.get("doc_type", "doc"),
                folder_path=result.get("folder_path"),
                feishu_doc_id=doc_id,
                feishu_url=result.get("url")
            )
        
        except MCPAPIError:
            return None
    
    def upload_image(self, image_path: str) -> Optional[str]:
        """
        Upload an image to Feishu.
        
        Args:
            image_path: Path to image file
            
        Returns:
            Feishu image URL or None if upload fails
            
        Raises:
            MCPConnectionError: If not connected
            MCPAPIError: If API call fails
        """
        if not self._connected:
            raise MCPConnectionError("Not connected to MCP service")
        
        try:
            result = self._call_api(
                "upload_image",
                {"image_path": image_path}
            )
            return result.get("url")
        
        except MCPAPIError:
            return None
    
    def _call_api(self, method: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Call MCP API method.
        
        This is a placeholder that would be replaced with actual MCP calls
        in production. For testing, this can be mocked.
        
        Args:
            method: API method name
            params: Method parameters
            
        Returns:
            API response data
            
        Raises:
            MCPAPIError: If API call fails
        """
        # In production, this would make actual MCP calls
        # For now, raise an error to indicate this needs to be mocked in tests
        raise MCPAPIError(f"MCP API call not implemented: {method}")
