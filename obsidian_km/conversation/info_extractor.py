"""信息提取模块

从用户输入中提取关键信息：
- 标题和内容
- 日期和时间
- 标签和分类
- 优先级和负责人
- 项目和领域关联
"""

import re
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Optional


@dataclass
class ExtractedInfo:
    """提取的信息"""
    title: Optional[str] = None
    content: Optional[str] = None
    date: Optional[datetime] = None
    time: Optional[str] = None
    tags: list[str] = field(default_factory=list)
    priority: list[str] = field(default_factory=list)
    assignee: Optional[str] = None
    project: Optional[str] = None
    area: Optional[str] = None
    due_date: Optional[datetime] = None


class InfoExtractor:
    """信息提取器
    
    使用正则表达式和模式匹配从用户输入中提取结构化信息
    """
    
    # 日期模式
    DATE_PATTERNS = {
        r'今天': lambda: datetime.now(),
        r'明天': lambda: datetime.now() + timedelta(days=1),
        r'后天': lambda: datetime.now() + timedelta(days=2),
        r'昨天': lambda: datetime.now() - timedelta(days=1),
        r'前天': lambda: datetime.now() - timedelta(days=2),
        r'下周一': lambda: InfoExtractor._next_weekday(0),
        r'下周二': lambda: InfoExtractor._next_weekday(1),
        r'下周三': lambda: InfoExtractor._next_weekday(2),
        r'下周四': lambda: InfoExtractor._next_weekday(3),
        r'下周五': lambda: InfoExtractor._next_weekday(4),
        r'下周六': lambda: InfoExtractor._next_weekday(5),
        r'下周日': lambda: InfoExtractor._next_weekday(6),
        r'本周五': lambda: InfoExtractor._this_weekday(4),
    }
    
    # 标签模式
    TAG_PATTERN = r'#([^\s#]+)'
    
    # 负责人模式
    ASSIGNEE_PATTERN = r'@([^\s@]+)'
    
    # 优先级关键词
    PRIORITY_KEYWORDS = {
        '重要': '#重要',
        '紧急': '#紧急',
        '高优先级': '#重要',
        '低优先级': '#低优先级',
    }
    
    # 项目标签模式
    PROJECT_TAG_PATTERN = r'#project/([^\s#]+)'
    
    # 领域标签模式
    AREA_TAG_PATTERN = r'#area/([^\s#]+)'
    
    # 截止日期关键词
    DUE_DATE_KEYWORDS = [
        '截止', '截止日期', '期限', '前', '之前', '完成'
    ]
    
    def extract(self, user_input: str) -> ExtractedInfo:
        """从用户输入中提取信息
        
        Args:
            user_input: 用户输入的文本
            
        Returns:
            提取的信息对象
        """
        info = ExtractedInfo()
        
        # 提取标题和内容
        info.title, info.content = self._extract_title_and_content(user_input)
        
        # 提取日期
        info.date = self._extract_date(user_input)
        
        # 提取时间
        info.time = self._extract_time(user_input)
        
        # 提取标签
        info.tags = self._extract_tags(user_input)
        
        # 提取优先级
        info.priority = self._extract_priority(user_input)
        
        # 提取负责人
        info.assignee = self._extract_assignee(user_input)
        
        # 提取项目
        info.project = self._extract_project(user_input)
        
        # 提取领域
        info.area = self._extract_area(user_input)
        
        # 提取截止日期
        info.due_date = self._extract_due_date(user_input)
        
        return info
    
    def _extract_title_and_content(self, text: str) -> tuple[Optional[str], Optional[str]]:
        """提取标题和内容
        
        标题通常是第一句话或冒号前的部分
        """
        # 尝试按冒号分割
        if '：' in text or ':' in text:
            parts = re.split(r'[：:]', text, maxsplit=1)
            if len(parts) == 2:
                return parts[0].strip(), parts[1].strip()
        
        # 尝试按句号分割
        if '。' in text or '.' in text:
            parts = re.split(r'[。.]', text, maxsplit=1)
            if len(parts) == 2 and len(parts[0]) < 50:
                return parts[0].strip(), parts[1].strip()
        
        # 如果文本较短，作为标题
        if len(text) < 50:
            return text.strip(), None
        
        # 否则，前50个字符作为标题
        return text[:50].strip(), text.strip()
    
    def _extract_date(self, text: str) -> Optional[datetime]:
        """提取日期"""
        # 检查相对日期关键词
        for pattern, date_func in self.DATE_PATTERNS.items():
            if re.search(pattern, text):
                return date_func()
        
        # 检查绝对日期格式：YYYY-MM-DD
        match = re.search(r'(\d{4})-(\d{1,2})-(\d{1,2})', text)
        if match:
            year, month, day = match.groups()
            return datetime(int(year), int(month), int(day))
        
        # 检查日期格式：MM月DD日 或 M月D日
        match = re.search(r'(\d{1,2})月(\d{1,2})日', text)
        if match:
            month, day = match.groups()
            year = datetime.now().year
            return datetime(year, int(month), int(day))
        
        return None
    
    def _extract_time(self, text: str) -> Optional[str]:
        """提取时间"""
        # 检查时间格式：HH:MM
        match = re.search(r'(\d{1,2}):(\d{2})', text)
        if match:
            hour, minute = match.groups()
            return f"{int(hour):02d}:{minute}"
        
        # 检查时间格式：HH点MM分
        match = re.search(r'(\d{1,2})点(\d{1,2})分', text)
        if match:
            hour, minute = match.groups()
            return f"{int(hour):02d}:{int(minute):02d}"
        
        # 检查时间格式：HH点
        match = re.search(r'(\d{1,2})点', text)
        if match:
            hour = match.group(1)
            return f"{int(hour):02d}:00"
        
        return None
    
    def _extract_tags(self, text: str) -> list[str]:
        """提取标签"""
        matches = re.findall(self.TAG_PATTERN, text)
        return [f"#{tag}" for tag in matches]
    
    def _extract_priority(self, text: str) -> list[str]:
        """提取优先级"""
        priorities = []
        for keyword, tag in self.PRIORITY_KEYWORDS.items():
            if keyword in text:
                priorities.append(tag)
        return priorities
    
    def _extract_assignee(self, text: str) -> Optional[str]:
        """提取负责人"""
        match = re.search(self.ASSIGNEE_PATTERN, text)
        if match:
            return match.group(1)
        
        # 检查"@...负责"模式（优先级最高）
        match = re.search(r'@([^\s，,。.：:]+)\s*负责', text)
        if match:
            return match.group(1)
        
        # 检查"负责人"关键词
        match = re.search(r'负责人[：:]?\s*([^\s，,。.：:]+)', text)
        if match:
            return match.group(1)
        
        # 检查"让...负责"模式
        match = re.search(r'让\s*([^\s，,。.：:]+)\s*负责', text)
        if match:
            return match.group(1)
        
        return None
    
    def _extract_project(self, text: str) -> Optional[str]:
        """提取项目"""
        match = re.search(self.PROJECT_TAG_PATTERN, text)
        if match:
            return match.group(1)
        return None
    
    def _extract_area(self, text: str) -> Optional[str]:
        """提取领域"""
        match = re.search(self.AREA_TAG_PATTERN, text)
        if match:
            return match.group(1)
        return None
    
    def _extract_due_date(self, text: str) -> Optional[datetime]:
        """提取截止日期
        
        查找截止日期关键词附近的日期表达式
        """
        # 检查是否包含截止日期关键词
        has_due_keyword = any(keyword in text for keyword in self.DUE_DATE_KEYWORDS)
        
        if not has_due_keyword:
            return None
        
        # 提取日期（复用 _extract_date 方法）
        return self._extract_date(text)
    
    @staticmethod
    def _next_weekday(weekday: int) -> datetime:
        """获取下周指定星期几的日期
        
        Args:
            weekday: 0=周一, 1=周二, ..., 6=周日
        """
        today = datetime.now()
        days_ahead = weekday - today.weekday()
        if days_ahead <= 0:  # 如果今天是或已过该星期几，则取下周
            days_ahead += 7
        return today + timedelta(days=days_ahead)
    
    @staticmethod
    def _this_weekday(weekday: int) -> datetime:
        """获取本周指定星期几的日期
        
        Args:
            weekday: 0=周一, 1=周二, ..., 6=周日
        """
        today = datetime.now()
        days_ahead = weekday - today.weekday()
        if days_ahead < 0:  # 如果已过该星期几，则取下周
            days_ahead += 7
        return today + timedelta(days=days_ahead)
