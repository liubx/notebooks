"""意图识别模块

识别用户输入的意图，包括：
- 创建笔记意图（日常笔记、项目、会议等）
- 任务操作意图（创建、更新、查询）
- 同步操作意图
- 查询操作意图
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class IntentType(Enum):
    """意图类型枚举"""
    # 笔记创建意图
    CREATE_DAILY_NOTE = "create_daily_note"
    CREATE_PROJECT = "create_project"
    CREATE_MEETING_NOTE = "create_meeting_note"
    CREATE_KNOWLEDGE_CARD = "create_knowledge_card"
    CREATE_CODE_SNIPPET = "create_code_snippet"
    CREATE_ADR = "create_adr"
    CREATE_PROBLEM_SOLVING = "create_problem_solving"
    
    # 任务操作意图
    CREATE_TASK = "create_task"
    UPDATE_TASK = "update_task"
    QUERY_TASK = "query_task"
    COMPLETE_TASK = "complete_task"
    
    # 同步操作意图
    SYNC_TO_FEISHU = "sync_to_feishu"
    CHECK_SYNC_STATUS = "check_sync_status"
    
    # 查询操作意图
    QUERY_NOTE = "query_note"
    SEARCH_CONTENT = "search_content"
    
    # 其他操作意图
    GENERATE_REVIEW = "generate_review"
    ARCHIVE_PROJECT = "archive_project"
    UNKNOWN = "unknown"


@dataclass
class Intent:
    """识别的意图"""
    type: IntentType
    confidence: float  # 0.0 - 1.0
    note_type: Optional[str] = None  # daily, project, meeting, etc.
    task_operation: Optional[str] = None  # create, update, query, complete
    sync_target: Optional[str] = None  # feishu, etc.


class IntentRecognizer:
    """意图识别器
    
    使用关键词匹配和模式识别来识别用户意图
    """
    
    # 日常笔记关键词
    DAILY_NOTE_KEYWORDS = [
        "记录", "今天", "日常", "工作", "学习", "生活",
        "笔记", "写下", "记下"
    ]
    
    # 项目关键词
    PROJECT_KEYWORDS = [
        "项目", "新项目", "创建项目", "project"
    ]
    
    # 会议关键词
    MEETING_KEYWORDS = [
        "会议", "开会", "讨论", "meeting", "参与者", "议题"
    ]
    
    # 知识卡片关键词
    KNOWLEDGE_CARD_KEYWORDS = [
        "知识卡片", "知识点", "学习", "技术", "概念"
    ]
    
    # 代码片段关键词
    CODE_SNIPPET_KEYWORDS = [
        "代码", "代码片段", "snippet", "代码块"
    ]
    
    # ADR 关键词
    ADR_KEYWORDS = [
        "技术决策", "决策记录", "adr", "架构决策"
    ]
    
    # 问题解决关键词
    PROBLEM_SOLVING_KEYWORDS = [
        "问题", "解决", "bug", "错误", "故障"
    ]
    
    # 任务创建关键词
    TASK_CREATE_KEYWORDS = [
        "添加任务", "创建任务", "todo", "待办", "任务"
    ]
    
    # 任务更新关键词
    TASK_UPDATE_KEYWORDS = [
        "更新任务", "修改任务", "改任务"
    ]
    
    # 任务查询关键词
    TASK_QUERY_KEYWORDS = [
        "查看任务", "任务列表", "有哪些任务", "今天的任务"
    ]
    
    # 任务完成关键词
    TASK_COMPLETE_KEYWORDS = [
        "标记完成", "完成了", "做完了", "已完成"
    ]
    
    # 同步关键词
    SYNC_KEYWORDS = [
        "同步", "同步到飞书", "飞书", "feishu"
    ]
    
    # 查询关键词
    QUERY_KEYWORDS = [
        "查找", "搜索", "查询", "找", "search"
    ]
    
    # 回顾关键词
    REVIEW_KEYWORDS = [
        "回顾", "总结", "周回顾", "月回顾", "review"
    ]
    
    # 归档关键词
    ARCHIVE_KEYWORDS = [
        "归档", "archive"
    ]
    
    def recognize(self, user_input: str) -> Intent:
        """识别用户输入的意图
        
        Args:
            user_input: 用户输入的文本
            
        Returns:
            识别的意图对象
        """
        user_input_lower = user_input.lower()
        
        # 检查同步意图（优先级较高）
        if self._contains_keywords(user_input_lower, self.SYNC_KEYWORDS):
            return Intent(
                type=IntentType.SYNC_TO_FEISHU,
                confidence=0.9,
                sync_target="feishu"
            )
        
        # 检查任务完成意图
        if self._contains_keywords(user_input_lower, self.TASK_COMPLETE_KEYWORDS):
            return Intent(
                type=IntentType.COMPLETE_TASK,
                confidence=0.85,
                task_operation="complete"
            )
        
        # 检查任务更新意图
        if self._contains_keywords(user_input_lower, self.TASK_UPDATE_KEYWORDS):
            return Intent(
                type=IntentType.UPDATE_TASK,
                confidence=0.85,
                task_operation="update"
            )
        
        # 检查任务查询意图
        if self._contains_keywords(user_input_lower, self.TASK_QUERY_KEYWORDS):
            return Intent(
                type=IntentType.QUERY_TASK,
                confidence=0.85,
                task_operation="query"
            )
        
        # 检查任务创建意图
        if self._contains_keywords(user_input_lower, self.TASK_CREATE_KEYWORDS):
            return Intent(
                type=IntentType.CREATE_TASK,
                confidence=0.9,
                task_operation="create"
            )
        
        # 检查会议记录意图
        if self._contains_keywords(user_input_lower, self.MEETING_KEYWORDS):
            return Intent(
                type=IntentType.CREATE_MEETING_NOTE,
                confidence=0.9,
                note_type="meeting"
            )
        
        # 检查项目意图
        if self._contains_keywords(user_input_lower, self.PROJECT_KEYWORDS):
            return Intent(
                type=IntentType.CREATE_PROJECT,
                confidence=0.9,
                note_type="project"
            )
        
        # 检查 ADR 意图
        if self._contains_keywords(user_input_lower, self.ADR_KEYWORDS):
            return Intent(
                type=IntentType.CREATE_ADR,
                confidence=0.9,
                note_type="adr"
            )
        
        # 检查代码片段意图
        if self._contains_keywords(user_input_lower, self.CODE_SNIPPET_KEYWORDS):
            return Intent(
                type=IntentType.CREATE_CODE_SNIPPET,
                confidence=0.85,
                note_type="code_snippet"
            )
        
        # 检查问题解决意图
        if self._contains_keywords(user_input_lower, self.PROBLEM_SOLVING_KEYWORDS):
            return Intent(
                type=IntentType.CREATE_PROBLEM_SOLVING,
                confidence=0.85,
                note_type="problem_solving"
            )
        
        # 检查知识卡片意图
        if self._contains_keywords(user_input_lower, self.KNOWLEDGE_CARD_KEYWORDS):
            return Intent(
                type=IntentType.CREATE_KNOWLEDGE_CARD,
                confidence=0.85,
                note_type="knowledge_card"
            )
        
        # 检查回顾意图
        if self._contains_keywords(user_input_lower, self.REVIEW_KEYWORDS):
            return Intent(
                type=IntentType.GENERATE_REVIEW,
                confidence=0.85
            )
        
        # 检查归档意图
        if self._contains_keywords(user_input_lower, self.ARCHIVE_KEYWORDS):
            return Intent(
                type=IntentType.ARCHIVE_PROJECT,
                confidence=0.85
            )
        
        # 检查查询意图
        if self._contains_keywords(user_input_lower, self.QUERY_KEYWORDS):
            return Intent(
                type=IntentType.QUERY_NOTE,
                confidence=0.8
            )
        
        # 检查日常笔记意图（默认意图，置信度较低）
        if self._contains_keywords(user_input_lower, self.DAILY_NOTE_KEYWORDS):
            return Intent(
                type=IntentType.CREATE_DAILY_NOTE,
                confidence=0.7,
                note_type="daily"
            )
        
        # 未知意图
        return Intent(
            type=IntentType.UNKNOWN,
            confidence=0.0
        )
    
    def _contains_keywords(self, text: str, keywords: list[str]) -> bool:
        """检查文本是否包含关键词列表中的任意一个
        
        Args:
            text: 要检查的文本（已转为小写）
            keywords: 关键词列表
            
        Returns:
            是否包含关键词
        """
        return any(keyword in text for keyword in keywords)
