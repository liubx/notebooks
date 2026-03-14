"""项目级飞书同步

管理项目级别的飞书同步配置和操作：
- 项目配置管理（.feishu-sync.json）
- 项目任务清单同步
- 任务分组同步
"""

import json
from pathlib import Path
from typing import Optional, Dict, Any, List
from datetime import datetime

from ..mcp.client import MCPClient, MCPConnectionError, MCPAPIError
from ..mcp.models import FeishuTask, SyncResult
from ..tasks.models import Task
from .feishu_sync import FeishuSyncEngine


class ProjectSyncConfig:
    """项目同步配置"""
    
    def __init__(
        self,
        project_name: str,
        feishu_tasklist_id: Optional[str] = None,
        feishu_tasklist_url: Optional[str] = None,
        sync_enabled: bool = True,
        sync_mode: str = "bidirectional",
        grouping_mode: str = "custom",
        custom_groups: Optional[List[Dict[str, str]]] = None,
        default_group: str = "未分组",
        field_mapping: Optional[Dict[str, str]] = None,
        last_sync: Optional[str] = None,
        created: Optional[str] = None
    ):
        """
        初始化项目同步配置
        
        Args:
            project_name: 项目名称
            feishu_tasklist_id: 飞书任务清单 ID
            feishu_tasklist_url: 飞书任务清单 URL
            sync_enabled: 是否启用同步
            sync_mode: 同步模式（bidirectional/obsidian_to_feishu/feishu_to_obsidian）
            grouping_mode: 分组模式（custom/none）
            custom_groups: 自定义分组列表
            default_group: 默认分组名称
            field_mapping: 字段映射
            last_sync: 最后同步时间
            created: 创建时间
        """
        self.project_name = project_name
        self.feishu_tasklist_id = feishu_tasklist_id
        self.feishu_tasklist_url = feishu_tasklist_url
        self.sync_enabled = sync_enabled
        self.sync_mode = sync_mode
        self.grouping_mode = grouping_mode
        self.custom_groups = custom_groups or []
        self.default_group = default_group
        self.field_mapping = field_mapping or {
            "title": "任务标题",
            "description": "任务描述",
            "due_date": "截止日期",
            "assignee": "负责人",
            "priority": "优先级",
            "status": "状态"
        }
        self.last_sync = last_sync
        self.created = created or datetime.now().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        return {
            "project_name": self.project_name,
            "feishu_tasklist_id": self.feishu_tasklist_id,
            "feishu_tasklist_url": self.feishu_tasklist_url,
            "sync_enabled": self.sync_enabled,
            "sync_mode": self.sync_mode,
            "grouping_mode": self.grouping_mode,
            "custom_groups": self.custom_groups,
            "default_group": self.default_group,
            "field_mapping": self.field_mapping,
            "last_sync": self.last_sync,
            "created": self.created
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ProjectSyncConfig':
        """从字典创建配置对象"""
        return cls(
            project_name=data.get("project_name", ""),
            feishu_tasklist_id=data.get("feishu_tasklist_id"),
            feishu_tasklist_url=data.get("feishu_tasklist_url"),
            sync_enabled=data.get("sync_enabled", True),
            sync_mode=data.get("sync_mode", "bidirectional"),
            grouping_mode=data.get("grouping_mode", "custom"),
            custom_groups=data.get("custom_groups", []),
            default_group=data.get("default_group", "未分组"),
            field_mapping=data.get("field_mapping"),
            last_sync=data.get("last_sync"),
            created=data.get("created")
        )


class ProjectSyncManager:
    """项目同步管理器
    
    管理项目级别的飞书同步配置和操作
    """
    
    CONFIG_FILENAME = ".feishu-sync.json"
    
    def __init__(self, mcp_client: MCPClient, vault_path: str):
        """
        初始化项目同步管理器
        
        Args:
            mcp_client: MCP 客户端
            vault_path: Vault 根目录路径
        """
        self.mcp_client = mcp_client
        self.vault_path = Path(vault_path)
        self.sync_engine = FeishuSyncEngine(mcp_client, vault_path)
    
    def create_project_config(
        self,
        project_path: str,
        project_name: str,
        **kwargs
    ) -> ProjectSyncConfig:
        """
        创建项目同步配置文件
        
        Args:
            project_path: 项目文件夹路径（相对于 vault 根目录）
            project_name: 项目名称
            **kwargs: 其他配置参数
            
        Returns:
            项目同步配置对象
        """
        config = ProjectSyncConfig(project_name=project_name, **kwargs)
        self.save_project_config(project_path, config)
        return config
    
    def load_project_config(self, project_path: str) -> Optional[ProjectSyncConfig]:
        """
        加载项目同步配置
        
        Args:
            project_path: 项目文件夹路径（相对于 vault 根目录）
            
        Returns:
            项目同步配置对象，如果不存在则返回 None
        """
        config_file = self.vault_path / project_path / self.CONFIG_FILENAME
        
        if not config_file.exists():
            return None
        
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            return ProjectSyncConfig.from_dict(data)
        
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Failed to load project config: {e}")
            return None
    
    def save_project_config(
        self,
        project_path: str,
        config: ProjectSyncConfig
    ) -> bool:
        """
        保存项目同步配置
        
        Args:
            project_path: 项目文件夹路径（相对于 vault 根目录）
            config: 项目同步配置对象
            
        Returns:
            是否保存成功
        """
        config_file = self.vault_path / project_path / self.CONFIG_FILENAME
        
        try:
            # 确保目录存在
            config_file.parent.mkdir(parents=True, exist_ok=True)
            
            # 写入配置
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(config.to_dict(), f, ensure_ascii=False, indent=2)
            
            return True
        
        except IOError as e:
            print(f"Warning: Failed to save project config: {e}")
            return False
    
    def validate_project_config(self, config: ProjectSyncConfig) -> tuple[bool, Optional[str]]:
        """
        验证项目同步配置
        
        Args:
            config: 项目同步配置对象
            
        Returns:
            (是否有效, 错误消息)
        """
        if not config.project_name:
            return False, "项目名称不能为空"
        
        if config.sync_mode not in ["bidirectional", "obsidian_to_feishu", "feishu_to_obsidian"]:
            return False, f"无效的同步模式: {config.sync_mode}"
        
        if config.grouping_mode not in ["custom", "none"]:
            return False, f"无效的分组模式: {config.grouping_mode}"
        
        # 验证自定义分组格式
        if config.grouping_mode == "custom":
            for group in config.custom_groups:
                if not isinstance(group, dict):
                    return False, "自定义分组必须是字典格式"
                if "name" not in group:
                    return False, "自定义分组必须包含 name 字段"
        
        return True, None
    
    def get_or_create_tasklist(
        self,
        project_path: str,
        project_name: str
    ) -> tuple[Optional[str], Optional[str]]:
        """
        获取或创建飞书任务清单
        
        Args:
            project_path: 项目文件夹路径
            project_name: 项目名称
            
        Returns:
            (tasklist_id, tasklist_url) 元组，失败返回 (None, None)
        """
        # 加载配置
        config = self.load_project_config(project_path)
        
        # 如果配置存在且有 tasklist_id，直接返回
        if config and config.feishu_tasklist_id:
            return config.feishu_tasklist_id, config.feishu_tasklist_url
        
        # 否则创建新的任务清单
        try:
            if not self.mcp_client.is_connected():
                self.mcp_client.connect()
            
            # 调用 MCP 创建任务清单
            # 注意：这里假设 MCP 客户端有 create_tasklist 方法
            # 实际实现中需要添加这个方法
            result = self._create_tasklist(project_name)
            
            if result:
                tasklist_id, tasklist_url = result
                
                # 更新或创建配置
                if config:
                    config.feishu_tasklist_id = tasklist_id
                    config.feishu_tasklist_url = tasklist_url
                else:
                    config = ProjectSyncConfig(
                        project_name=project_name,
                        feishu_tasklist_id=tasklist_id,
                        feishu_tasklist_url=tasklist_url
                    )
                
                self.save_project_config(project_path, config)
                return tasklist_id, tasklist_url
            
            return None, None
        
        except (MCPConnectionError, MCPAPIError) as e:
            print(f"Warning: Failed to create tasklist: {e}")
            return None, None
    
    def _create_tasklist(self, project_name: str) -> Optional[tuple[str, str]]:
        """
        创建飞书任务清单
        
        Args:
            project_name: 项目名称
            
        Returns:
            (tasklist_id, tasklist_url) 元组，失败返回 None
        """
        # 这里需要调用 MCP 客户端的 create_tasklist 方法
        # 由于当前 MCPClient 没有这个方法，我们先返回 None
        # 在实际实现中需要扩展 MCPClient
        
        # 临时实现：抛出异常表示需要 mock
        raise MCPAPIError("create_tasklist not implemented in MCPClient")
    
    def add_custom_group(
        self,
        project_path: str,
        group_name: str,
        feishu_group_id: Optional[str] = None
    ) -> bool:
        """
        添加自定义分组
        
        Args:
            project_path: 项目文件夹路径
            group_name: 分组名称
            feishu_group_id: 飞书分组 ID（可选）
            
        Returns:
            是否添加成功
        """
        config = self.load_project_config(project_path)
        
        if not config:
            return False
        
        # 检查分组是否已存在
        for group in config.custom_groups:
            if group.get("name") == group_name:
                # 更新 feishu_group_id
                if feishu_group_id:
                    group["feishu_group_id"] = feishu_group_id
                self.save_project_config(project_path, config)
                return True
        
        # 添加新分组
        new_group = {"name": group_name}
        if feishu_group_id:
            new_group["feishu_group_id"] = feishu_group_id
        
        config.custom_groups.append(new_group)
        return self.save_project_config(project_path, config)
    
    def get_group_id(self, project_path: str, group_name: str) -> Optional[str]:
        """
        获取分组的飞书 ID
        
        Args:
            project_path: 项目文件夹路径
            group_name: 分组名称
            
        Returns:
            飞书分组 ID，如果不存在则返回 None
        """
        config = self.load_project_config(project_path)
        
        if not config:
            return None
        
        for group in config.custom_groups:
            if group.get("name") == group_name:
                return group.get("feishu_group_id")
        
        return None

    
    def sync_project_tasks(
        self,
        project_path: str,
        tasks: List[Task]
    ) -> List[SyncResult]:
        """
        同步项目任务到飞书任务清单
        
        Args:
            project_path: 项目文件夹路径
            tasks: 任务列表
            
        Returns:
            同步结果列表
        """
        results = []
        
        # 加载项目配置
        config = self.load_project_config(project_path)
        
        if not config or not config.sync_enabled:
            return results
        
        # 获取或创建任务清单
        tasklist_id, _ = self.get_or_create_tasklist(
            project_path,
            config.project_name
        )
        
        if not tasklist_id:
            # 无法获取任务清单，返回失败结果
            for task in tasks:
                results.append(SyncResult(
                    success=False,
                    message="无法获取飞书任务清单",
                    error="Failed to get or create tasklist",
                    sync_time=datetime.now()
                ))
            return results
        
        # 同步每个任务
        for task in tasks:
            # 检查任务是否需要同步
            if not self._should_sync_task(task):
                continue
            
            # 提取任务的分组
            group_name = self._extract_task_group(task)
            
            # 如果有分组，确保分组存在
            if group_name and config.grouping_mode == "custom":
                self._ensure_group_exists(project_path, group_name, tasklist_id)
            
            # 同步任务
            result = self.sync_engine.sync_task_to_feishu(task, tasklist_id)
            results.append(result)
        
        # 更新配置的最后同步时间
        config.last_sync = datetime.now().isoformat()
        self.save_project_config(project_path, config)
        
        return results
    
    def _should_sync_task(self, task: Task) -> bool:
        """判断任务是否需要同步"""
        # 检查任务是否有同步标签
        sync_tags = ['#sync/feishu', '#sync/feishu-task']
        return any(tag in task.tags for tag in sync_tags)
    
    def _extract_task_group(self, task: Task) -> Optional[str]:
        """提取任务的分组名称"""
        for tag in task.tags:
            if tag.startswith('#group/'):
                return tag.replace('#group/', '')
        return None
    
    def _ensure_group_exists(
        self,
        project_path: str,
        group_name: str,
        tasklist_id: str
    ) -> Optional[str]:
        """
        确保分组存在，如果不存在则创建
        
        Args:
            project_path: 项目文件夹路径
            group_name: 分组名称
            tasklist_id: 任务清单 ID
            
        Returns:
            飞书分组 ID，失败返回 None
        """
        # 检查配置中是否已有该分组
        group_id = self.get_group_id(project_path, group_name)
        
        if group_id:
            return group_id
        
        # 创建新分组
        try:
            if not self.mcp_client.is_connected():
                self.mcp_client.connect()
            
            # 调用 MCP 创建分组
            group_id = self._create_group(tasklist_id, group_name)
            
            if group_id:
                # 添加到配置
                self.add_custom_group(project_path, group_name, group_id)
                return group_id
            
            return None
        
        except (MCPConnectionError, MCPAPIError) as e:
            print(f"Warning: Failed to create group: {e}")
            return None
    
    def _create_group(self, tasklist_id: str, group_name: str) -> Optional[str]:
        """
        在飞书任务清单中创建分组
        
        Args:
            tasklist_id: 任务清单 ID
            group_name: 分组名称
            
        Returns:
            飞书分组 ID，失败返回 None
        """
        # 这里需要调用 MCP 客户端的 create_group 方法
        # 由于当前 MCPClient 没有这个方法，我们先抛出异常
        # 在实际实现中需要扩展 MCPClient
        raise MCPAPIError("create_group not implemented in MCPClient")
    
    def sync_group_changes(
        self,
        project_path: str
    ) -> bool:
        """
        同步飞书任务清单的分组变更到 Obsidian
        
        Args:
            project_path: 项目文件夹路径
            
        Returns:
            是否同步成功
        """
        config = self.load_project_config(project_path)
        
        if not config or not config.feishu_tasklist_id:
            return False
        
        try:
            if not self.mcp_client.is_connected():
                self.mcp_client.connect()
            
            # 从飞书获取分组列表
            groups = self._get_tasklist_groups(config.feishu_tasklist_id)
            
            if groups is None:
                return False
            
            # 更新配置中的分组列表
            config.custom_groups = [
                {"name": group["name"], "feishu_group_id": group["id"]}
                for group in groups
            ]
            
            return self.save_project_config(project_path, config)
        
        except (MCPConnectionError, MCPAPIError) as e:
            print(f"Warning: Failed to sync group changes: {e}")
            return False
    
    def _get_tasklist_groups(self, tasklist_id: str) -> Optional[List[Dict[str, str]]]:
        """
        获取飞书任务清单的分组列表
        
        Args:
            tasklist_id: 任务清单 ID
            
        Returns:
            分组列表，失败返回 None
        """
        # 这里需要调用 MCP 客户端的 get_tasklist_groups 方法
        # 由于当前 MCPClient 没有这个方法，我们先抛出异常
        # 在实际实现中需要扩展 MCPClient
        raise MCPAPIError("get_tasklist_groups not implemented in MCPClient")
