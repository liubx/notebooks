"""飞书同步中心

集中管理和监控飞书同步状态：
- 扫描所有同步标签
- 分类同步项（待同步、已同步、失败、冲突）
- 计算统计信息
- 生成同步中心文档
"""

import re
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class SyncStatus(Enum):
    """同步状态枚举"""
    PENDING = "pending"  # 待同步
    SYNCED = "synced"    # 已同步
    ERROR = "error"      # 同步失败
    CONFLICT = "conflict"  # 同步冲突


class SyncItemType(Enum):
    """同步项类型"""
    TASK = "task"        # 任务
    DOCUMENT = "document"  # 文档


@dataclass
class SyncItem:
    """同步项"""
    file_path: str  # 文件路径（相对于 vault 根目录）
    item_type: SyncItemType  # 类型（任务/文档）
    status: SyncStatus  # 同步状态
    title: str  # 标题或内容
    feishu_id: Optional[str] = None  # 飞书 ID
    feishu_url: Optional[str] = None  # 飞书 URL
    last_sync: Optional[str] = None  # 最后同步时间
    error_message: Optional[str] = None  # 错误消息
    line_number: Optional[int] = None  # 任务所在行号（仅任务）


@dataclass
class SyncStatistics:
    """同步统计信息"""
    total: int = 0  # 总数
    pending: int = 0  # 待同步
    synced: int = 0  # 已同步
    error: int = 0  # 同步失败
    conflict: int = 0  # 同步冲突
    
    # 按类型统计
    tasks_total: int = 0  # 任务总数
    tasks_pending: int = 0  # 待同步任务
    tasks_synced: int = 0  # 已同步任务
    tasks_error: int = 0  # 失败任务
    tasks_conflict: int = 0  # 冲突任务
    
    docs_total: int = 0  # 文档总数
    docs_pending: int = 0  # 待同步文档
    docs_synced: int = 0  # 已同步文档
    docs_error: int = 0  # 失败文档
    docs_conflict: int = 0  # 冲突文档
    
    last_update: Optional[str] = None  # 最后更新时间


class SyncCenter:
    """飞书同步中心
    
    管理和监控所有飞书同步状态
    """
    
    # 同步标签模式
    SYNC_TAG_PATTERNS = {
        SyncStatus.PENDING: [
            r'#sync/feishu\b',
            r'#sync/feishu-doc\b',
            r'#sync/feishu-wiki\b',
            r'#sync/feishu-task\b'
        ],
        SyncStatus.SYNCED: [
            r'#synced/feishu\b'
        ],
        SyncStatus.ERROR: [
            r'#sync-error/feishu\b'
        ],
        SyncStatus.CONFLICT: [
            r'#sync-conflict/feishu\b'
        ]
    }
    
    def __init__(self, vault_path: str):
        """
        初始化同步中心
        
        Args:
            vault_path: Vault 根目录路径
        """
        self.vault_path = Path(vault_path)
    
    def scan_all_sync_items(self) -> List[SyncItem]:
        """
        扫描所有同步项
        
        Returns:
            同步项列表
        """
        sync_items = []
        
        # 扫描所有 Markdown 文件
        for md_file in self.vault_path.rglob("*.md"):
            # 跳过模板文件夹
            if "Templates" in md_file.parts:
                continue
            
            # 读取文件内容
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception:
                continue
            
            # 获取相对路径
            rel_path = str(md_file.relative_to(self.vault_path))
            
            # 检查文档级别的同步标签
            doc_sync_items = self._scan_document_sync(rel_path, content)
            sync_items.extend(doc_sync_items)
            
            # 检查任务级别的同步标签
            task_sync_items = self._scan_task_sync(rel_path, content)
            sync_items.extend(task_sync_items)
        
        return sync_items
    
    def _scan_document_sync(self, file_path: str, content: str) -> List[SyncItem]:
        """扫描文档级别的同步标签"""
        sync_items = []
        
        # 检查是否有文档同步标签（在 YAML front matter 或文档内容中）
        status = self._detect_document_sync_status(content)
        
        if status is None:
            return sync_items
        
        # 提取文档标题
        title = self._extract_document_title(content)
        
        # 提取同步元数据
        feishu_id, feishu_url, last_sync = self._extract_document_sync_metadata(content)
        
        # 创建同步项
        sync_item = SyncItem(
            file_path=file_path,
            item_type=SyncItemType.DOCUMENT,
            status=status,
            title=title,
            feishu_id=feishu_id,
            feishu_url=feishu_url,
            last_sync=last_sync
        )
        
        sync_items.append(sync_item)
        
        return sync_items
    
    def _detect_document_sync_status(self, content: str) -> Optional[SyncStatus]:
        """检测文档级别的同步状态（从 YAML front matter 或标签）"""
        lines = content.split('\n')
        
        # 检查 YAML front matter 中的 tags
        if lines and lines[0].strip() == '---':
            in_yaml = True
            in_tags = False
            
            for i in range(1, len(lines)):
                line = lines[i]
                
                # 检查是否到达 YAML 结束
                if line.strip() == '---':
                    break
                
                # 检查是否进入 tags 部分
                if line.strip() == 'tags:':
                    in_tags = True
                    continue
                
                # 如果在 tags 部分，检查同步标签
                if in_tags:
                    # 检查是否是标签行（以 "  - " 开头）
                    stripped = line.strip()
                    if stripped.startswith('- ') and line.startswith('  '):
                        tag = stripped[2:].strip()
                        # Add # prefix if not present for pattern matching
                        if not tag.startswith('#'):
                            tag = '#' + tag
                        status = self._detect_sync_status(tag)
                        if status:
                            return status
                    # 如果遇到非缩进行（不是标签），退出 tags 部分
                    elif line and not line.startswith(' ') and not line.startswith('\t'):
                        in_tags = False
        
        return None
    
    def _scan_task_sync(self, file_path: str, content: str) -> List[SyncItem]:
        """扫描任务级别的同步标签"""
        sync_items = []
        
        lines = content.split('\n')
        
        for i, line in enumerate(lines):
            # 检查是否是任务行
            if not self._is_task_line(line):
                continue
            
            # 检查任务是否有同步标签
            status = self._detect_sync_status(line)
            
            if status is None:
                continue
            
            # 提取任务内容
            task_content = self._extract_task_content(line)
            
            # 提取任务元数据（从后续行）
            feishu_id, feishu_url, last_sync = self._extract_task_sync_metadata(
                lines, i
            )
            
            # 创建同步项
            sync_item = SyncItem(
                file_path=file_path,
                item_type=SyncItemType.TASK,
                status=status,
                title=task_content,
                feishu_id=feishu_id,
                feishu_url=feishu_url,
                last_sync=last_sync,
                line_number=i + 1
            )
            
            sync_items.append(sync_item)
        
        return sync_items
    
    def _detect_sync_status(self, text: str) -> Optional[SyncStatus]:
        """检测同步状态"""
        for status, patterns in self.SYNC_TAG_PATTERNS.items():
            for pattern in patterns:
                if re.search(pattern, text):
                    return status
        
        return None
    
    def _is_task_line(self, line: str) -> bool:
        """判断是否是任务行"""
        stripped = line.strip()
        return bool(re.match(r'^-\s+\[([ xX])\]\s+', stripped))
    
    def _extract_task_content(self, line: str) -> str:
        """提取任务内容"""
        # 移除任务标记和标签
        match = re.match(r'^-\s+\[([ xX])\]\s+(.+)', line.strip())
        if match:
            content = match.group(2)
            # 移除标签和元数据标记
            content = re.sub(r'\s*#\S+', '', content)
            content = re.sub(r'\s*📅\s*\S+', '', content)
            content = re.sub(r'\s*@\S+', '', content)
            return content.strip()
        
        return line.strip()
    
    def _extract_document_title(self, content: str) -> str:
        """提取文档标题"""
        lines = content.split('\n')
        
        # 跳过 YAML front matter
        start_idx = 0
        if lines and lines[0].strip() == '---':
            for i in range(1, len(lines)):
                if lines[i].strip() == '---':
                    start_idx = i + 1
                    break
        
        # 查找第一个标题
        for i in range(start_idx, len(lines)):
            line = lines[i].strip()
            if line.startswith('#'):
                # 提取标题文本
                title = re.sub(r'^#+\s+', '', line)
                return title
        
        return "Untitled"
    
    def _extract_document_sync_metadata(
        self,
        content: str
    ) -> tuple[Optional[str], Optional[str], Optional[str]]:
        """从文档 YAML front matter 中提取同步元数据"""
        lines = content.split('\n')
        
        if not lines or lines[0].strip() != '---':
            return None, None, None
        
        feishu_id = None
        feishu_url = None
        last_sync = None
        
        in_feishu_sync = False
        
        for i in range(1, len(lines)):
            line = lines[i]
            
            if line.strip() == '---':
                break
            
            if line.strip() == 'feishu_sync:':
                in_feishu_sync = True
                continue
            
            if in_feishu_sync:
                # 提取 feishu_doc_id
                match = re.match(r'\s+feishu_doc_id:\s*["\']?([^"\']+)["\']?', line)
                if match:
                    feishu_id = match.group(1)
                
                # 提取 feishu_url
                match = re.match(r'\s+feishu_url:\s*["\']?([^"\']+)["\']?', line)
                if match:
                    feishu_url = match.group(1)
                
                # 提取 last_sync
                match = re.match(r'\s+last_sync:\s*(.+)', line)
                if match:
                    last_sync = match.group(1).strip()
                
                # 如果遇到非缩进行，退出 feishu_sync 部分
                if line and not line.startswith(' ') and not line.startswith('\t'):
                    in_feishu_sync = False
        
        return feishu_id, feishu_url, last_sync
    
    def _extract_task_sync_metadata(
        self,
        lines: List[str],
        task_line_idx: int
    ) -> tuple[Optional[str], Optional[str], Optional[str]]:
        """从任务后续行中提取同步元数据"""
        feishu_id = None
        feishu_url = None
        last_sync = None
        
        # 检查任务行后面的几行（只检查缩进的元数据行）
        for i in range(task_line_idx + 1, min(task_line_idx + 10, len(lines))):
            line = lines[i]
            
            # 如果是空行，继续
            if not line.strip():
                continue
            
            # 如果不是缩进的元数据行，停止
            if not line.startswith('  - '):
                break
            
            # 提取 feishu_task_id
            match = re.search(r'feishu_task_id:\s*(\S+)', line)
            if match:
                feishu_id = match.group(1)
            
            # 提取 feishu_url
            match = re.search(r'feishu_url:\s*(\S+)', line)
            if match:
                feishu_url = match.group(1)
            
            # 提取 last_sync
            match = re.search(r'last_sync:\s*(.+)', line)
            if match:
                last_sync = match.group(1).strip()
        
        return feishu_id, feishu_url, last_sync
    
    def classify_sync_items(
        self,
        sync_items: List[SyncItem]
    ) -> Dict[SyncStatus, List[SyncItem]]:
        """
        按状态分类同步项
        
        Args:
            sync_items: 同步项列表
        
        Returns:
            按状态分类的同步项字典
        """
        classified = {
            SyncStatus.PENDING: [],
            SyncStatus.SYNCED: [],
            SyncStatus.ERROR: [],
            SyncStatus.CONFLICT: []
        }
        
        for item in sync_items:
            classified[item.status].append(item)
        
        return classified
    
    def calculate_statistics(
        self,
        sync_items: List[SyncItem]
    ) -> SyncStatistics:
        """
        计算同步统计信息
        
        Args:
            sync_items: 同步项列表
        
        Returns:
            同步统计信息
        """
        stats = SyncStatistics()
        
        stats.total = len(sync_items)
        stats.last_update = datetime.now().isoformat()
        
        for item in sync_items:
            # 按状态统计
            if item.status == SyncStatus.PENDING:
                stats.pending += 1
            elif item.status == SyncStatus.SYNCED:
                stats.synced += 1
            elif item.status == SyncStatus.ERROR:
                stats.error += 1
            elif item.status == SyncStatus.CONFLICT:
                stats.conflict += 1
            
            # 按类型统计
            if item.item_type == SyncItemType.TASK:
                stats.tasks_total += 1
                if item.status == SyncStatus.PENDING:
                    stats.tasks_pending += 1
                elif item.status == SyncStatus.SYNCED:
                    stats.tasks_synced += 1
                elif item.status == SyncStatus.ERROR:
                    stats.tasks_error += 1
                elif item.status == SyncStatus.CONFLICT:
                    stats.tasks_conflict += 1
            
            elif item.item_type == SyncItemType.DOCUMENT:
                stats.docs_total += 1
                if item.status == SyncStatus.PENDING:
                    stats.docs_pending += 1
                elif item.status == SyncStatus.SYNCED:
                    stats.docs_synced += 1
                elif item.status == SyncStatus.ERROR:
                    stats.docs_error += 1
                elif item.status == SyncStatus.CONFLICT:
                    stats.docs_conflict += 1
        
        return stats
    
    def generate_sync_center_document(
        self,
        output_path: str = "飞书同步中心.md"
    ) -> str:
        """
        生成飞书同步中心文档
        
        Args:
            output_path: 输出文件路径（相对于 vault 根目录）
        
        Returns:
            生成的文档路径
        """
        # 扫描所有同步项
        sync_items = self.scan_all_sync_items()
        
        # 分类同步项
        classified = self.classify_sync_items(sync_items)
        
        # 计算统计信息
        stats = self.calculate_statistics(sync_items)
        
        # 生成文档内容
        content = self._generate_document_content(classified, stats)
        
        # 写入文件
        full_path = self.vault_path / output_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return output_path
    
    def _generate_document_content(
        self,
        classified: Dict[SyncStatus, List[SyncItem]],
        stats: SyncStatistics
    ) -> str:
        """生成同步中心文档内容"""
        lines = []
        
        # 标题
        lines.append("# 飞书同步中心\n")
        lines.append(f"*更新时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n")
        lines.append("")
        
        # 统计信息
        lines.append("## 📊 同步统计\n")
        lines.append(f"- 总同步项: {stats.total}")
        lines.append(f"- 待同步: {stats.pending}")
        lines.append(f"- 已同步: {stats.synced}")
        lines.append(f"- 同步失败: {stats.error}")
        lines.append(f"- 同步冲突: {stats.conflict}")
        lines.append("")
        
        lines.append("**任务同步:**")
        lines.append(f"- 总任务: {stats.tasks_total}")
        lines.append(f"- 待同步: {stats.tasks_pending}")
        lines.append(f"- 已同步: {stats.tasks_synced}")
        lines.append(f"- 失败: {stats.tasks_error}")
        lines.append(f"- 冲突: {stats.tasks_conflict}")
        lines.append("")
        
        lines.append("**文档同步:**")
        lines.append(f"- 总文档: {stats.docs_total}")
        lines.append(f"- 待同步: {stats.docs_pending}")
        lines.append(f"- 已同步: {stats.docs_synced}")
        lines.append(f"- 失败: {stats.docs_error}")
        lines.append(f"- 冲突: {stats.docs_conflict}")
        lines.append("")
        
        # 待同步列表
        lines.append("## ⏳ 待同步\n")
        pending_items = classified[SyncStatus.PENDING]
        if pending_items:
            # 按类型分组
            tasks = [item for item in pending_items if item.item_type == SyncItemType.TASK]
            docs = [item for item in pending_items if item.item_type == SyncItemType.DOCUMENT]
            
            if tasks:
                lines.append("### 任务\n")
                for item in tasks:
                    lines.append(self._format_sync_item(item))
                lines.append("")
            
            if docs:
                lines.append("### 文档\n")
                for item in docs:
                    lines.append(self._format_sync_item(item))
                lines.append("")
        else:
            lines.append("*暂无待同步项*\n")
        
        # 已同步列表
        lines.append("## ✅ 已同步\n")
        synced_items = classified[SyncStatus.SYNCED]
        if synced_items:
            # 按类型分组
            tasks = [item for item in synced_items if item.item_type == SyncItemType.TASK]
            docs = [item for item in synced_items if item.item_type == SyncItemType.DOCUMENT]
            
            if tasks:
                lines.append("### 任务\n")
                for item in tasks:
                    lines.append(self._format_sync_item(item))
                lines.append("")
            
            if docs:
                lines.append("### 文档\n")
                for item in docs:
                    lines.append(self._format_sync_item(item))
                lines.append("")
        else:
            lines.append("*暂无已同步项*\n")
        
        # 同步失败列表
        lines.append("## ❌ 同步失败\n")
        error_items = classified[SyncStatus.ERROR]
        if error_items:
            for item in error_items:
                lines.append(self._format_sync_item(item))
            lines.append("")
        else:
            lines.append("*暂无同步失败项*\n")
        
        # 同步冲突列表
        lines.append("## ⚠️ 同步冲突\n")
        conflict_items = classified[SyncStatus.CONFLICT]
        if conflict_items:
            for item in conflict_items:
                lines.append(self._format_sync_item(item))
            lines.append("")
        else:
            lines.append("*暂无同步冲突项*\n")
        
        return "\n".join(lines)
    
    def _format_sync_item(self, item: SyncItem) -> str:
        """格式化同步项为 Markdown 行"""
        parts = []
        
        # 类型图标
        icon = "📝" if item.item_type == SyncItemType.TASK else "📄"
        
        # 标题
        parts.append(f"- {icon} **{item.title}**")
        
        # 来源
        if item.line_number:
            parts.append(f"  - 来源: [[{item.file_path}#L{item.line_number}]]")
        else:
            parts.append(f"  - 来源: [[{item.file_path}]]")
        
        # 飞书链接
        if item.feishu_url:
            parts.append(f"  - 飞书: {item.feishu_url}")
        
        # 最后同步时间
        if item.last_sync:
            parts.append(f"  - 最后同步: {item.last_sync}")
        
        return "\n".join(parts)
