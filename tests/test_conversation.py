"""对话理解引擎测试

包含单元测试和基于属性的测试
"""

import pytest
from datetime import datetime, timedelta
from hypothesis import given, strategies as st, settings, assume

from obsidian_km.conversation import (
    IntentRecognizer,
    Intent,
    IntentType,
    InfoExtractor,
    ExtractedInfo,
)


# ============================================================================
# 单元测试：意图识别
# ============================================================================

class TestIntentRecognizer:
    """意图识别器单元测试"""
    
    def setup_method(self):
        """测试前准备"""
        self.recognizer = IntentRecognizer()
    
    def test_recognize_create_daily_note(self):
        """测试识别创建日常笔记意图"""
        user_input = "记录一下今天的工作进展"
        intent = self.recognizer.recognize(user_input)
        
        assert intent.type == IntentType.CREATE_DAILY_NOTE
        assert intent.note_type == "daily"
        assert intent.confidence > 0.5
    
    def test_recognize_create_meeting_note(self):
        """测试识别创建会议记录意图"""
        user_input = "今天开了个会，讨论了新项目的技术方案"
        intent = self.recognizer.recognize(user_input)
        
        assert intent.type == IntentType.CREATE_MEETING_NOTE
        assert intent.note_type == "meeting"
        assert intent.confidence > 0.8
    
    def test_recognize_create_project(self):
        """测试识别创建项目意图"""
        user_input = "创建一个新项目：电商系统"
        intent = self.recognizer.recognize(user_input)
        
        assert intent.type == IntentType.CREATE_PROJECT
        assert intent.note_type == "project"
        assert intent.confidence > 0.8
    
    def test_recognize_create_task(self):
        """测试识别创建任务意图"""
        user_input = "添加任务：完成设计文档"
        intent = self.recognizer.recognize(user_input)
        
        assert intent.type == IntentType.CREATE_TASK
        assert intent.task_operation == "create"
        assert intent.confidence > 0.8
    
    def test_recognize_query_task(self):
        """测试识别查询任务意图"""
        user_input = "今天有哪些任务？"
        intent = self.recognizer.recognize(user_input)
        
        assert intent.type == IntentType.QUERY_TASK
        assert intent.task_operation == "query"
        assert intent.confidence > 0.8
    
    def test_recognize_complete_task(self):
        """测试识别完成任务意图"""
        user_input = "把这个任务标记完成"
        intent = self.recognizer.recognize(user_input)
        
        assert intent.type == IntentType.COMPLETE_TASK
        assert intent.task_operation == "complete"
        assert intent.confidence > 0.8
    
    def test_recognize_sync_to_feishu(self):
        """测试识别同步到飞书意图"""
        user_input = "这个需要同步到飞书"
        intent = self.recognizer.recognize(user_input)
        
        assert intent.type == IntentType.SYNC_TO_FEISHU
        assert intent.sync_target == "feishu"
        assert intent.confidence > 0.8
    
    def test_recognize_query_note(self):
        """测试识别查询笔记意图"""
        user_input = "查找关于 React 的笔记"
        intent = self.recognizer.recognize(user_input)
        
        assert intent.type == IntentType.QUERY_NOTE
        assert intent.confidence > 0.5
    
    def test_recognize_unknown_intent(self):
        """测试识别未知意图"""
        user_input = "这是一段随机的文本，没有明确意图"
        intent = self.recognizer.recognize(user_input)
        
        assert intent.type == IntentType.UNKNOWN
        assert intent.confidence == 0.0


# ============================================================================
# 单元测试：信息提取
# ============================================================================

class TestInfoExtractor:
    """信息提取器单元测试"""
    
    def setup_method(self):
        """测试前准备"""
        self.extractor = InfoExtractor()
    
    def test_extract_title_and_content_with_colon(self):
        """测试提取标题和内容（冒号分隔）"""
        user_input = "会议记录：讨论了新项目的技术方案"
        info = self.extractor.extract(user_input)
        
        assert info.title == "会议记录"
        assert info.content == "讨论了新项目的技术方案"
    
    def test_extract_title_short_text(self):
        """测试提取标题（短文本）"""
        user_input = "完成设计文档"
        info = self.extractor.extract(user_input)
        
        assert info.title == "完成设计文档"
    
    def test_extract_date_today(self):
        """测试提取日期：今天"""
        user_input = "今天的工作进展"
        info = self.extractor.extract(user_input)
        
        assert info.date is not None
        assert info.date.date() == datetime.now().date()
    
    def test_extract_date_tomorrow(self):
        """测试提取日期：明天"""
        user_input = "明天的会议"
        info = self.extractor.extract(user_input)
        
        assert info.date is not None
        expected_date = (datetime.now() + timedelta(days=1)).date()
        assert info.date.date() == expected_date
    
    def test_extract_date_absolute(self):
        """测试提取日期：绝对日期"""
        user_input = "2024-01-15 的会议记录"
        info = self.extractor.extract(user_input)
        
        assert info.date is not None
        assert info.date.year == 2024
        assert info.date.month == 1
        assert info.date.day == 15
    
    def test_extract_time(self):
        """测试提取时间"""
        user_input = "14:30 的会议"
        info = self.extractor.extract(user_input)
        
        assert info.time == "14:30"
    
    def test_extract_tags(self):
        """测试提取标签"""
        user_input = "这是一个 #技术 #重要 的笔记"
        info = self.extractor.extract(user_input)
        
        assert "#技术" in info.tags
        assert "#重要" in info.tags
    
    def test_extract_priority(self):
        """测试提取优先级"""
        user_input = "这是一个重要且紧急的任务"
        info = self.extractor.extract(user_input)
        
        assert "#重要" in info.priority
        assert "#紧急" in info.priority
    
    def test_extract_assignee_with_at_symbol(self):
        """测试提取负责人（@符号）"""
        user_input = "这个任务由 @张三 负责"
        info = self.extractor.extract(user_input)
        
        assert info.assignee == "张三"
    
    def test_extract_assignee_with_keyword(self):
        """测试提取负责人（关键词）"""
        user_input = "负责人：李四"
        info = self.extractor.extract(user_input)
        
        assert info.assignee == "李四"
    
    def test_extract_project(self):
        """测试提取项目"""
        user_input = "这是 #project/电商系统 的任务"
        info = self.extractor.extract(user_input)
        
        assert info.project == "电商系统"
    
    def test_extract_area(self):
        """测试提取领域"""
        user_input = "这是 #area/技术管理 的内容"
        info = self.extractor.extract(user_input)
        
        assert info.area == "技术管理"
    
    def test_extract_due_date(self):
        """测试提取截止日期"""
        user_input = "这个任务截止日期是下周五"
        info = self.extractor.extract(user_input)
        
        assert info.due_date is not None
    
    def test_extract_multiple_info(self):
        """测试提取多个信息"""
        user_input = "添加任务：完成设计文档，下周五前，@张三 负责，重要 #project/电商系统"
        info = self.extractor.extract(user_input)
        
        assert info.title is not None
        assert info.assignee == "张三"
        assert "#重要" in info.priority
        assert info.project == "电商系统"
        assert info.due_date is not None


# ============================================================================
# 属性测试：AI 意图识别准确性
# ============================================================================

# Feature: obsidian-knowledge-management-workflow, Property 1: AI 意图识别准确性
@given(
    intent_keyword=st.sampled_from([
        ("记录", IntentType.CREATE_DAILY_NOTE),
        ("今天", IntentType.CREATE_DAILY_NOTE),
        ("会议", IntentType.CREATE_MEETING_NOTE),
        ("开会", IntentType.CREATE_MEETING_NOTE),
        ("项目", IntentType.CREATE_PROJECT),
        ("新项目", IntentType.CREATE_PROJECT),
        ("添加任务", IntentType.CREATE_TASK),
        ("创建任务", IntentType.CREATE_TASK),
        ("查看任务", IntentType.QUERY_TASK),
        ("有哪些任务", IntentType.QUERY_TASK),
        ("标记完成", IntentType.COMPLETE_TASK),
        ("完成了", IntentType.COMPLETE_TASK),
        ("同步", IntentType.SYNC_TO_FEISHU),
        ("同步到飞书", IntentType.SYNC_TO_FEISHU),
        ("查找", IntentType.QUERY_NOTE),
        ("搜索", IntentType.QUERY_NOTE),
    ])
)
@settings(max_examples=100)
def test_property_intent_recognition_accuracy(intent_keyword):
    """
    **Validates: Requirements 18.1, 18.2**
    
    属性 1：对于任意包含明确操作意图的用户输入，AI 应该正确识别意图
    
    对于任意包含明确意图关键词的用户输入，意图识别器应该正确识别对应的意图类型
    """
    keyword, expected_intent = intent_keyword
    recognizer = IntentRecognizer()
    
    # 构造包含关键词的用户输入
    user_input = f"{keyword}一些内容"
    
    # 识别意图
    intent = recognizer.recognize(user_input)
    
    # 验证识别的意图类型正确
    assert intent.type == expected_intent, \
        f"Expected intent {expected_intent}, but got {intent.type} for input: {user_input}"


# ============================================================================
# 属性测试：关键信息提取完整性
# ============================================================================

# Feature: obsidian-knowledge-management-workflow, Property 3: 关键信息提取完整性
@given(
    has_title=st.booleans(),
    has_date=st.booleans(),
    has_tag=st.booleans(),
    has_assignee=st.booleans(),
    has_priority=st.booleans(),
)
@settings(max_examples=100)
def test_property_info_extraction_completeness(
    has_title, has_date, has_tag, has_assignee, has_priority
):
    """
    **Validates: Requirements 18.4**
    
    属性 3：对于任意包含结构化信息的用户输入，AI 应该正确提取所有关键信息
    
    对于任意包含明确结构化信息的用户输入，信息提取器应该正确提取所有明确提及的信息
    """
    # 至少包含一个信息
    assume(has_title or has_date or has_tag or has_assignee or has_priority)
    
    extractor = InfoExtractor()
    
    # 构造包含指定信息的用户输入
    parts = []
    
    if has_title:
        parts.append("完成设计文档")
    
    if has_date:
        parts.append("明天")
    
    if has_tag:
        parts.append("#技术")
    
    if has_assignee:
        parts.append("@张三")
    
    if has_priority:
        parts.append("重要")
    
    user_input = " ".join(parts)
    
    # 提取信息
    info = extractor.extract(user_input)
    
    # 验证提取的信息完整性
    if has_title:
        assert info.title is not None, f"Failed to extract title from: {user_input}"
    
    if has_date:
        assert info.date is not None, f"Failed to extract date from: {user_input}"
    
    if has_tag:
        assert len(info.tags) > 0, f"Failed to extract tags from: {user_input}"
        assert "#技术" in info.tags, f"Failed to extract correct tag from: {user_input}"
    
    if has_assignee:
        assert info.assignee is not None, f"Failed to extract assignee from: {user_input}"
        assert info.assignee == "张三", f"Failed to extract correct assignee from: {user_input}"
    
    if has_priority:
        assert len(info.priority) > 0, f"Failed to extract priority from: {user_input}"
        assert "#重要" in info.priority, f"Failed to extract correct priority from: {user_input}"


# Feature: obsidian-knowledge-management-workflow, Property 3: 关键信息提取完整性（日期格式）
@given(
    date_format=st.sampled_from([
        ("今天", 0),
        ("明天", 1),
        ("后天", 2),
        ("昨天", -1),
        ("前天", -2),
    ])
)
@settings(max_examples=100)
def test_property_date_extraction_relative(date_format):
    """
    **Validates: Requirements 18.4**
    
    属性 3：对于任意相对日期表达式，应该正确提取对应的日期
    """
    keyword, days_offset = date_format
    extractor = InfoExtractor()
    
    user_input = f"{keyword}的会议"
    info = extractor.extract(user_input)
    
    # 验证提取的日期正确
    assert info.date is not None, f"Failed to extract date from: {user_input}"
    
    expected_date = (datetime.now() + timedelta(days=days_offset)).date()
    assert info.date.date() == expected_date, \
        f"Expected date {expected_date}, but got {info.date.date()} for input: {user_input}"


# Feature: obsidian-knowledge-management-workflow, Property 3: 关键信息提取完整性（标签提取）
@given(
    tags=st.lists(
        st.text(
            alphabet=st.characters(whitelist_categories=('Lu', 'Ll', 'Nd')),
            min_size=1,
            max_size=10
        ),
        min_size=1,
        max_size=5
    )
)
@settings(max_examples=100)
def test_property_tag_extraction(tags):
    """
    **Validates: Requirements 18.4**
    
    属性 3：对于任意包含标签的用户输入，应该正确提取所有标签
    """
    extractor = InfoExtractor()
    
    # 构造包含标签的用户输入
    tag_strings = [f"#{tag}" for tag in tags]
    user_input = f"这是一个笔记 {' '.join(tag_strings)}"
    
    # 提取信息
    info = extractor.extract(user_input)
    
    # 验证提取的标签完整性
    assert len(info.tags) == len(tags), \
        f"Expected {len(tags)} tags, but got {len(info.tags)} for input: {user_input}"
    
    for tag_string in tag_strings:
        assert tag_string in info.tags, \
            f"Expected tag {tag_string} not found in extracted tags: {info.tags}"


# Feature: obsidian-knowledge-management-workflow, Property 3: 关键信息提取完整性（时间提取）
@given(
    hour=st.integers(min_value=0, max_value=23),
    minute=st.integers(min_value=0, max_value=59),
)
@settings(max_examples=100)
def test_property_time_extraction(hour, minute):
    """
    **Validates: Requirements 18.4**
    
    属性 3：对于任意时间表达式，应该正确提取时间
    """
    extractor = InfoExtractor()
    
    # 构造包含时间的用户输入
    user_input = f"{hour}:{minute:02d} 的会议"
    
    # 提取信息
    info = extractor.extract(user_input)
    
    # 验证提取的时间正确
    assert info.time is not None, f"Failed to extract time from: {user_input}"
    assert info.time == f"{hour:02d}:{minute:02d}", \
        f"Expected time {hour:02d}:{minute:02d}, but got {info.time} for input: {user_input}"
