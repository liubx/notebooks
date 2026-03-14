"""飞书同步引擎

管理与飞书平台的双向同步：
- 同步任务到飞书
- 同步文档到飞书
- 从飞书同步更新
- 处理同步冲突
"""

import re
from pathlib import Path
from typing import Optional, Dict, Any, List
from datetime import datetime

from ..mcp.client import MCPClient, MCPConnectionError, MCPAPIError
from ..mcp.models import FeishuTask, FeishuDocument, SyncResult
from ..mcp.converter import MarkdownToFeishuConverter
from ..tasks.models import Task


class SyncConflict(Exception):
    """同步冲突异常"""
    pass


class FeishuSyncEngine:
    """飞书同步引擎
    
    管理 Obsidian 与飞书平台之间的双向同步
    """
    
    def __init__(self, mcp_client: MCPClient, vault_path: str):
        """
        初始化同步引擎
        
        Args:
            mcp_client: MCP 客户端
            vault_path: Vault 根目录路径
        """
        self.mcp_client = mcp_client
        self.vault_path = Path(vault_path)
        self.converter = MarkdownToFeishuConverter()
    
    def sync_task_to_feishu(
        self,
        task: Task,
        tasklist_id: Optional[str] = None
    ) -> SyncResult:
        """
        同步任务到飞书
        
        Args:
            task: 任务对象
            tasklist_id: 飞书任务清单 ID（可选）
            
        Returns:
            同步结果
        """
        try:
            # 检查连接
            if not self.mcp_client.is_connected():
                self.mcp_client.connect()
            
            # 提取任务元数据
            feishu_task = self._task_to_feishu_task(task)
            
            # 检查是否已有 feishu_task_id（更新 vs 创建）
            feishu_task_id = self._extract_feishu_task_id(task)
            
            if feishu_task_id:
                # 更新现有任务
                result = self.mcp_client.update_task(feishu_task_id, feishu_task)
            else:
                # 创建新任务
                result = self.mcp_client.create_task(feishu_task, tasklist_id)
            
            if result.success:
                # 更新任务文件中的元数据
                self._update_task_metadata(
                    task,
                    result.feishu_id,
                    result.feishu_url,
                    result.sync_time
                )
                
                # 更新同步状态标签
                self._update_sync_status_tag(task, "synced")
            
            return result
        
        except MCPConnectionError as e:
            return SyncResult(
                success=False,
                message="MCP 连接失败",
                error=str(e),
                sync_time=datetime.now()
            )
        
        except MCPAPIError as e:
            return SyncResult(
                success=False,
                message="飞书 API 调用失败",
                error=str(e),
                sync_time=datetime.now()
            )
        
        except Exception as e:
            return SyncResult(
                success=False,
                message="同步失败",
                error=str(e),
                sync_time=datetime.now()
            )
    
    def _task_to_feishu_task(self, task: Task) -> FeishuTask:
        """将 Obsidian 任务转换为飞书任务"""
        # 提取优先级
        priority = None
        if "重要" in task.priority or "紧急" in task.priority:
            priority = "high"
        
        # 提取状态
        status = "completed" if task.completed else "pending"
        
        # 提取自定义分组
        custom_group = self._extract_custom_group(task)
        
        return FeishuTask(
            title=task.content,
            description=f"来源: {task.file_path}",
            due_date=task.due_date,
            assignee=task.assignee,
            priority=priority,
            status=status,
            custom_group=custom_group
        )
    
    def _extract_feishu_task_id(self, task: Task) -> Optional[str]:
        """从任务文件中提取 feishu_task_id"""
        file_path = self.vault_path / task.file_path
        
        if not file_path.exists():
            return None
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 查找任务所在行附近的 feishu_task_id
            lines = content.split('\n')
            task_line_idx = task.line_number - 1
            
            # 检查任务行后面的几行
            for i in range(task_line_idx + 1, min(task_line_idx + 5, len(lines))):
                line = lines[i]
                match = re.search(r'feishu_task_id:\s*(\S+)', line)
                if match:
                    return match.group(1)
            
            return None
        
        except Exception:
            return None
    
    def _extract_custom_group(self, task: Task) -> Optional[str]:
        """提取任务的自定义分组"""
        for tag in task.tags:
            if tag.startswith('#group/'):
                return tag.replace('#group/', '')
        return None
    
    def _update_task_metadata(
        self,
        task: Task,
        feishu_task_id: str,
        feishu_url: str,
        sync_time: datetime
    ) -> None:
        """更新任务文件中的同步元数据"""
        file_path = self.vault_path / task.file_path
        
        if not file_path.exists():
            return
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            lines = content.split('\n')
            task_line_idx = task.line_number - 1
            
            # 检查是否已有元数据
            metadata_start = task_line_idx + 1
            has_metadata = False
            
            if metadata_start < len(lines):
                next_line = lines[metadata_start].strip()
                if next_line.startswith('- feishu_task_id:'):
                    has_metadata = True
            
            # 构建元数据行
            metadata_lines = [
                f"  - feishu_task_id: {feishu_task_id}",
                f"  - feishu_url: {feishu_url}",
                f"  - last_sync: {sync_time.isoformat()}",
                f"  - sync_status: synced"
            ]
            
            if has_metadata:
                # 更新现有元数据
                # 找到元数据结束位置
                metadata_end = metadata_start
                while metadata_end < len(lines):
                    line = lines[metadata_end].strip()
                    if not line.startswith('- feishu_') and not line.startswith('- last_sync') and not line.startswith('- sync_status'):
                        break
                    metadata_end += 1
                
                # 替换元数据
                lines[metadata_start:metadata_end] = metadata_lines
            else:
                # 插入新元数据
                lines.insert(metadata_start, '\n'.join(metadata_lines))
            
            # 写回文件
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
        
        except Exception as e:
            # 记录错误但不中断流程
            print(f"Warning: Failed to update task metadata: {e}")
    
    def _update_sync_status_tag(self, task: Task, status: str) -> None:
        """更新任务的同步状态标签
        
        Args:
            task: 任务对象
            status: 状态（synced, error, conflict）
        """
        file_path = self.vault_path / task.file_path
        
        if not file_path.exists():
            return
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 替换同步标签
            # #sync/feishu -> #synced/feishu
            # #sync-error/feishu -> #synced/feishu
            # #sync-conflict/feishu -> #synced/feishu
            
            old_tags = ['#sync/feishu', '#sync-error/feishu', '#sync-conflict/feishu']
            new_tag = f'#synced/feishu' if status == 'synced' else f'#sync-{status}/feishu'
            
            for old_tag in old_tags:
                content = content.replace(old_tag, new_tag)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        
        except Exception as e:
            print(f"Warning: Failed to update sync status tag: {e}")
    
    def sync_document_to_feishu(
        self,
        file_path: str,
        doc_type: str = "doc",
        folder_path: Optional[str] = None
    ) -> SyncResult:
        """
        同步文档到飞书
        
        Args:
            file_path: 文档文件路径（相对于 vault 根目录）
            doc_type: 文档类型（doc/wiki/sheet）
            folder_path: 飞书文件夹路径（可选）
            
        Returns:
            同步结果
        """
        try:
            # 检查连接
            if not self.mcp_client.is_connected():
                self.mcp_client.connect()
            
            # 读取文档内容
            full_path = self.vault_path / file_path
            if not full_path.exists():
                return SyncResult(
                    success=False,
                    message="文档文件不存在",
                    error=f"File not found: {file_path}",
                    sync_time=datetime.now()
                )
            
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 提取标题和正文
            title, markdown_content = self._extract_title_and_content(content)
            
            # 转换 Markdown 为飞书格式
            feishu_content = self._convert_markdown_to_feishu(markdown_content, full_path.parent)
            
            # 检查是否已有 feishu_doc_id
            feishu_doc_id = self._extract_feishu_doc_id(content)
            
            # 创建飞书文档对象
            feishu_doc = FeishuDocument(
                title=title,
                content=feishu_content,
                doc_type=doc_type,
                folder_path=folder_path
            )
            
            if feishu_doc_id:
                # 更新现有文档
                result = self.mcp_client.update_document(feishu_doc_id, feishu_doc)
            else:
                # 创建新文档
                result = self.mcp_client.create_document(feishu_doc)
            
            if result.success:
                # 更新文档元数据
                self._update_document_metadata(
                    file_path,
                    result.feishu_id,
                    result.feishu_url,
                    result.sync_time,
                    doc_type,
                    folder_path
                )
                
                # 更新同步状态标签
                self._update_document_sync_tag(file_path, "synced")
            
            return result
        
        except MCPConnectionError as e:
            return SyncResult(
                success=False,
                message="MCP 连接失败",
                error=str(e),
                sync_time=datetime.now()
            )
        
        except MCPAPIError as e:
            return SyncResult(
                success=False,
                message="飞书 API 调用失败",
                error=str(e),
                sync_time=datetime.now()
            )
        
        except Exception as e:
            return SyncResult(
                success=False,
                message="同步失败",
                error=str(e),
                sync_time=datetime.now()
            )
    
    def _extract_title_and_content(self, content: str) -> tuple[str, str]:
        """从文档中提取标题和正文
        
        Returns:
            (title, content) 元组
        """
        lines = content.split('\n')
        
        # 跳过 YAML front matter
        start_idx = 0
        if lines and lines[0].strip() == '---':
            for i in range(1, len(lines)):
                if lines[i].strip() == '---':
                    start_idx = i + 1
                    break
        
        # 查找第一个标题作为文档标题
        title = "Untitled"
        content_start = start_idx
        
        for i in range(start_idx, len(lines)):
            line = lines[i].strip()
            if line.startswith('#'):
                # 提取标题文本
                title = re.sub(r'^#+\s+', '', line)
                content_start = i + 1
                break
        
        # 提取正文（从标题后开始）
        markdown_content = '\n'.join(lines[content_start:])
        
        return title, markdown_content
    
    def _convert_markdown_to_feishu(
        self,
        markdown: str,
        base_path: Path
    ) -> str:
        """转换 Markdown 为飞书格式
        
        Args:
            markdown: Markdown 内容
            base_path: 文档所在目录（用于解析相对路径）
            
        Returns:
            飞书格式内容（JSON 字符串）
        """
        # 处理图片上传
        markdown = self._process_images(markdown, base_path)
        
        # 使用转换器转换为飞书格式
        blocks = self.converter.convert(markdown)
        
        # 转换为 JSON 字符串
        import json
        return json.dumps(blocks, ensure_ascii=False)
    
    def _process_images(self, markdown: str, base_path: Path) -> str:
        """处理文档中的图片，上传到飞书并替换 URL
        
        Args:
            markdown: Markdown 内容
            base_path: 文档所在目录
            
        Returns:
            处理后的 Markdown 内容
        """
        # 查找所有图片引用
        image_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
        
        def replace_image(match):
            alt_text = match.group(1)
            image_path = match.group(2)
            
            # 跳过外部 URL
            if image_path.startswith('http://') or image_path.startswith('https://'):
                return match.group(0)
            
            # 解析相对路径
            full_image_path = base_path / image_path
            
            if not full_image_path.exists():
                # 图片不存在，保持原样
                return match.group(0)
            
            try:
                # 上传图片到飞书
                feishu_url = self.mcp_client.upload_image(str(full_image_path))
                
                if feishu_url:
                    # 替换为飞书 URL
                    return f'![{alt_text}]({feishu_url})'
                else:
                    # 上传失败，保持原样
                    return match.group(0)
            
            except Exception:
                # 上传失败，保持原样
                return match.group(0)
        
        return re.sub(image_pattern, replace_image, markdown)
    
    def _extract_feishu_doc_id(self, content: str) -> Optional[str]:
        """从文档 YAML front matter 中提取 feishu_doc_id"""
        # 查找 YAML front matter
        lines = content.split('\n')
        
        if not lines or lines[0].strip() != '---':
            return None
        
        in_yaml = True
        in_feishu_sync = False
        
        for i in range(1, len(lines)):
            line = lines[i]
            
            if line.strip() == '---':
                break
            
            # 检查是否进入 feishu_sync 部分
            if line.strip() == 'feishu_sync:':
                in_feishu_sync = True
                continue
            
            # 如果在 feishu_sync 部分，查找 feishu_doc_id
            if in_feishu_sync:
                match = re.match(r'\s+feishu_doc_id:\s*["\']?([^"\']+)["\']?', line)
                if match:
                    return match.group(1)
                
                # 如果遇到非缩进行，退出 feishu_sync 部分
                if line and not line.startswith(' ') and not line.startswith('\t'):
                    in_feishu_sync = False
        
        return None
    
    def _update_document_metadata(
        self,
        file_path: str,
        feishu_doc_id: str,
        feishu_url: str,
        sync_time: datetime,
        doc_type: str,
        folder_path: Optional[str]
    ) -> None:
        """更新文档的同步元数据"""
        full_path = self.vault_path / file_path
        
        if not full_path.exists():
            return
        
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            lines = content.split('\n')
            
            # 查找或创建 YAML front matter
            if not lines or lines[0].strip() != '---':
                # 没有 YAML front matter，创建一个
                yaml_lines = [
                    '---',
                    'feishu_sync:',
                    f'  platform: feishu',
                    f'  doc_type: {doc_type}',
                    f'  feishu_doc_id: "{feishu_doc_id}"',
                    f'  feishu_url: "{feishu_url}"',
                ]
                
                if folder_path:
                    yaml_lines.append(f'  feishu_folder: "{folder_path}"')
                
                yaml_lines.extend([
                    f'  last_sync: {sync_time.isoformat()}',
                    f'  sync_status: synced',
                    '---',
                    ''
                ])
                
                lines = yaml_lines + lines
            else:
                # 已有 YAML front matter，更新或添加 feishu_sync 部分
                yaml_end = 0
                for i in range(1, len(lines)):
                    if lines[i].strip() == '---':
                        yaml_end = i
                        break
                
                # 查找 feishu_sync 部分
                feishu_sync_start = -1
                for i in range(1, yaml_end):
                    if lines[i].strip() == 'feishu_sync:':
                        feishu_sync_start = i
                        break
                
                # 构建 feishu_sync 内容
                feishu_sync_lines = [
                    'feishu_sync:',
                    f'  platform: feishu',
                    f'  doc_type: {doc_type}',
                    f'  feishu_doc_id: "{feishu_doc_id}"',
                    f'  feishu_url: "{feishu_url}"',
                ]
                
                if folder_path:
                    feishu_sync_lines.append(f'  feishu_folder: "{folder_path}"')
                
                feishu_sync_lines.extend([
                    f'  last_sync: {sync_time.isoformat()}',
                    f'  sync_status: synced',
                ])
                
                if feishu_sync_start >= 0:
                    # 找到 feishu_sync 部分的结束位置
                    feishu_sync_end = feishu_sync_start + 1
                    while feishu_sync_end < yaml_end:
                        line = lines[feishu_sync_end]
                        if line and not line.startswith(' ') and not line.startswith('\t'):
                            break
                        feishu_sync_end += 1
                    
                    # 替换 feishu_sync 部分
                    lines[feishu_sync_start:feishu_sync_end] = feishu_sync_lines
                else:
                    # 在 YAML 结束前插入 feishu_sync 部分
                    lines[yaml_end:yaml_end] = feishu_sync_lines
            
            # 写回文件
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
        
        except Exception as e:
            print(f"Warning: Failed to update document metadata: {e}")
    
    def _update_document_sync_tag(self, file_path: str, status: str) -> None:
        """更新文档的同步状态标签"""
        full_path = self.vault_path / file_path
        
        if not full_path.exists():
            return
        
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 替换同步标签
            old_tags = ['#sync/feishu-doc', '#sync/feishu-wiki', '#sync-error/feishu', '#sync-conflict/feishu']
            new_tag = f'#synced/feishu' if status == 'synced' else f'#sync-{status}/feishu'
            
            for old_tag in old_tags:
                content = content.replace(old_tag, new_tag)
            
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
        
        except Exception as e:
            print(f"Warning: Failed to update document sync tag: {e}")
    
    def sync_from_feishu_task(self, task: Task) -> SyncResult:
        """
        从飞书同步任务更新
        
        Args:
            task: 本地任务对象
            
        Returns:
            同步结果
        """
        try:
            # 检查连接
            if not self.mcp_client.is_connected():
                self.mcp_client.connect()
            
            # 获取 feishu_task_id
            feishu_task_id = self._extract_feishu_task_id(task)
            
            if not feishu_task_id:
                return SyncResult(
                    success=False,
                    message="任务未关联飞书任务",
                    error="No feishu_task_id found",
                    sync_time=datetime.now()
                )
            
            # 从飞书获取任务
            feishu_task = self.mcp_client.get_task(feishu_task_id)
            
            if not feishu_task:
                return SyncResult(
                    success=False,
                    message="飞书任务不存在",
                    error=f"Task not found: {feishu_task_id}",
                    sync_time=datetime.now()
                )
            
            # 检查冲突
            conflict = self._detect_task_conflict(task, feishu_task)
            
            if conflict:
                # 标记冲突
                self._update_sync_status_tag(task, "conflict")
                raise SyncConflict(conflict)
            
            # 更新本地任务
            self._update_local_task(task, feishu_task)
            
            return SyncResult(
                success=True,
                message="任务已从飞书同步",
                feishu_id=feishu_task_id,
                feishu_url=feishu_task.feishu_url,
                sync_time=datetime.now()
            )
        
        except SyncConflict:
            raise
        
        except MCPConnectionError as e:
            return SyncResult(
                success=False,
                message="MCP 连接失败",
                error=str(e),
                sync_time=datetime.now()
            )
        
        except MCPAPIError as e:
            return SyncResult(
                success=False,
                message="飞书 API 调用失败",
                error=str(e),
                sync_time=datetime.now()
            )
        
        except Exception as e:
            return SyncResult(
                success=False,
                message="同步失败",
                error=str(e),
                sync_time=datetime.now()
            )
    
    def sync_from_feishu_document(self, file_path: str) -> SyncResult:
        """
        从飞书同步文档更新
        
        Args:
            file_path: 文档文件路径（相对于 vault 根目录）
            
        Returns:
            同步结果
        """
        try:
            # 检查连接
            if not self.mcp_client.is_connected():
                self.mcp_client.connect()
            
            # 读取本地文档
            full_path = self.vault_path / file_path
            if not full_path.exists():
                return SyncResult(
                    success=False,
                    message="文档文件不存在",
                    error=f"File not found: {file_path}",
                    sync_time=datetime.now()
                )
            
            with open(full_path, 'r', encoding='utf-8') as f:
                local_content = f.read()
            
            # 获取 feishu_doc_id
            feishu_doc_id = self._extract_feishu_doc_id(local_content)
            
            if not feishu_doc_id:
                return SyncResult(
                    success=False,
                    message="文档未关联飞书文档",
                    error="No feishu_doc_id found",
                    sync_time=datetime.now()
                )
            
            # 从飞书获取文档
            feishu_doc = self.mcp_client.get_document(feishu_doc_id)
            
            if not feishu_doc:
                return SyncResult(
                    success=False,
                    message="飞书文档不存在",
                    error=f"Document not found: {feishu_doc_id}",
                    sync_time=datetime.now()
                )
            
            # 检查冲突
            conflict = self._detect_document_conflict(file_path, local_content, feishu_doc)
            
            if conflict:
                # 标记冲突
                self._update_document_sync_tag(file_path, "conflict")
                raise SyncConflict(conflict)
            
            # 更新本地文档
            self._update_local_document(file_path, feishu_doc)
            
            return SyncResult(
                success=True,
                message="文档已从飞书同步",
                feishu_id=feishu_doc_id,
                feishu_url=feishu_doc.feishu_url,
                sync_time=datetime.now()
            )
        
        except SyncConflict:
            raise
        
        except MCPConnectionError as e:
            return SyncResult(
                success=False,
                message="MCP 连接失败",
                error=str(e),
                sync_time=datetime.now()
            )
        
        except MCPAPIError as e:
            return SyncResult(
                success=False,
                message="飞书 API 调用失败",
                error=str(e),
                sync_time=datetime.now()
            )
        
        except Exception as e:
            return SyncResult(
                success=False,
                message="同步失败",
                error=str(e),
                sync_time=datetime.now()
            )
    
    def _update_local_task(self, task: Task, feishu_task: FeishuTask) -> None:
        """更新本地任务内容"""
        file_path = self.vault_path / task.file_path
        
        if not file_path.exists():
            return
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            lines = content.split('\n')
            task_line_idx = task.line_number - 1
            
            # 更新任务行
            old_line = lines[task_line_idx]
            
            # 保持任务格式，只更新内容和状态
            checkbox = "[x]" if feishu_task.status == "completed" else "[ ]"
            
            # 提取原有的标签和元数据
            task_content = feishu_task.title
            
            # 重建任务行（保留原有的缩进和格式）
            indent = len(old_line) - len(old_line.lstrip())
            new_line = ' ' * indent + f"- {checkbox} {task_content}"
            
            # 保留原有的标签
            if '#' in old_line:
                tags_part = old_line[old_line.index('#'):]
                new_line += ' ' + tags_part
            
            lines[task_line_idx] = new_line
            
            # 更新元数据中的 last_sync
            metadata_start = task_line_idx + 1
            if metadata_start < len(lines):
                for i in range(metadata_start, min(metadata_start + 10, len(lines))):
                    if 'last_sync:' in lines[i]:
                        lines[i] = f"  - last_sync: {datetime.now().isoformat()}"
                        break
            
            # 写回文件
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
        
        except Exception as e:
            print(f"Warning: Failed to update local task: {e}")
    
    def _update_local_document(self, file_path: str, feishu_doc: FeishuDocument) -> None:
        """更新本地文档内容"""
        full_path = self.vault_path / file_path
        
        if not full_path.exists():
            return
        
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            lines = content.split('\n')
            
            # 保留 YAML front matter
            yaml_end = 0
            if lines and lines[0].strip() == '---':
                for i in range(1, len(lines)):
                    if lines[i].strip() == '---':
                        yaml_end = i + 1
                        break
            
            # 更新 last_sync 时间
            for i in range(yaml_end):
                if 'last_sync:' in lines[i]:
                    lines[i] = f'  last_sync: {datetime.now().isoformat()}'
                    break
            
            # 转换飞书内容为 Markdown
            # 注意：这里简化处理，实际应该有飞书格式到 Markdown 的转换器
            # 目前假设 feishu_doc.content 已经是 Markdown 格式
            markdown_content = feishu_doc.content
            
            # 重建文档：YAML front matter + 标题 + 内容
            new_lines = lines[:yaml_end]
            new_lines.append('')
            new_lines.append(f'# {feishu_doc.title}')
            new_lines.append('')
            new_lines.append(markdown_content)
            
            # 写回文件
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(new_lines))
        
        except Exception as e:
            print(f"Warning: Failed to update local document: {e}")
    
    def _detect_task_conflict(self, local_task: Task, feishu_task: FeishuTask) -> Optional[str]:
        """检测任务同步冲突
        
        Args:
            local_task: 本地任务
            feishu_task: 飞书任务
            
        Returns:
            冲突描述，如果没有冲突则返回 None
        """
        # 获取本地任务的最后同步时间
        last_sync_time = self._get_task_last_sync_time(local_task)
        
        if not last_sync_time:
            # 没有同步记录，不算冲突
            return None
        
        # 获取本地任务的修改时间
        local_modified = self._get_file_modified_time(local_task.file_path)
        
        # 只有当本地在最后同步后被修改，才检查冲突
        if not local_modified or local_modified <= last_sync_time:
            # 本地没有修改，不算冲突
            return None
        
        # 本地在最后同步后被修改，检查内容是否不同
        local_completed = local_task.completed
        feishu_completed = feishu_task.status == "completed"
        
        if local_completed != feishu_completed:
            return f"任务状态冲突：本地为 {'已完成' if local_completed else '未完成'}，飞书为 {'已完成' if feishu_completed else '未完成'}"
        
        # 检查其他字段
        if local_task.content != feishu_task.title:
            return f"任务内容冲突：本地和飞书的内容不一致"
        
        return None
    
    def _detect_document_conflict(
        self,
        file_path: str,
        local_content: str,
        feishu_doc: FeishuDocument
    ) -> Optional[str]:
        """检测文档同步冲突
        
        Args:
            file_path: 文档文件路径
            local_content: 本地文档内容
            feishu_doc: 飞书文档
            
        Returns:
            冲突描述，如果没有冲突则返回 None
        """
        # 获取最后同步时间
        last_sync_time = self._get_document_last_sync_time(local_content)
        
        if not last_sync_time:
            # 没有同步记录，不算冲突
            return None
        
        # 获取本地文档的修改时间
        local_modified = self._get_file_modified_time(file_path)
        
        # 如果本地在最后同步后被修改，且飞书文档也不同，则存在冲突
        if local_modified and local_modified > last_sync_time:
            # 简单的内容差异检测
            # 提取本地文档的正文（跳过 YAML front matter）
            _, local_markdown = self._extract_title_and_content(local_content)
            
            # 比较内容（简化版本）
            if local_markdown.strip() != feishu_doc.content.strip():
                return f"文档内容冲突：本地和飞书的内容在最后同步后都被修改"
        
        return None
    
    def _get_task_last_sync_time(self, task: Task) -> Optional[datetime]:
        """获取任务的最后同步时间"""
        file_path = self.vault_path / task.file_path
        
        if not file_path.exists():
            return None
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            lines = content.split('\n')
            task_line_idx = task.line_number - 1
            
            # 检查任务行后面的元数据
            for i in range(task_line_idx + 1, min(task_line_idx + 10, len(lines))):
                line = lines[i]
                match = re.search(r'last_sync:\s*(.+)', line)
                if match:
                    time_str = match.group(1).strip()
                    return datetime.fromisoformat(time_str)
            
            return None
        
        except Exception:
            return None
    
    def _get_document_last_sync_time(self, content: str) -> Optional[datetime]:
        """从文档内容中获取最后同步时间"""
        lines = content.split('\n')
        
        if not lines or lines[0].strip() != '---':
            return None
        
        in_feishu_sync = False
        
        for i in range(1, len(lines)):
            line = lines[i]
            
            if line.strip() == '---':
                break
            
            if line.strip() == 'feishu_sync:':
                in_feishu_sync = True
                continue
            
            if in_feishu_sync:
                match = re.match(r'\s+last_sync:\s*(.+)', line)
                if match:
                    time_str = match.group(1).strip()
                    return datetime.fromisoformat(time_str)
                
                if line and not line.startswith(' ') and not line.startswith('\t'):
                    in_feishu_sync = False
        
        return None
    
    def _get_file_modified_time(self, file_path: str) -> Optional[datetime]:
        """获取文件的修改时间"""
        full_path = self.vault_path / file_path
        
        if not full_path.exists():
            return None
        
        try:
            import os
            mtime = os.path.getmtime(full_path)
            return datetime.fromtimestamp(mtime)
        except Exception:
            return None

