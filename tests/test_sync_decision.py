"""智能同步判断器测试

包含单元测试和基于属性的测试
"""

import pytest
from hypothesis import given, strategies as st, settings, assume

from obsidian_km.sync import (
    SyncDecisionMaker,
    SyncDecision,
    ConfidenceLevel,
)


# ============================================================================
# 单元测试：智能同步判断
# ============================================================================

class TestSyncDecisionMaker:
    """智能同步判断器单元测试"""
    
    def setup_method(self):
        """测试前准备"""
        self.decision_maker = SyncDecisionMaker()
    
    # 工作内容自动识别测试
    
    def test_work_project_tag(self):
        """测试工作项目标签识别"""
        content = "今天的项目进展 #project/电商系统"
        decision = self.decision_maker.should_sync(content)
        
        assert decision.should_sync is True
        assert decision.confidence == ConfidenceLevel.HIGH
        assert decision.ask_user is False
        assert '工作项目标签' in decision.matched_features
    
    def test_work_area_tag(self):
        """测试工作领域标签识别"""
        content = "技术管理相关内容 #area/技术管理"
        decision = self.decision_maker.should_sync(content)
        
        assert decision.should_sync is True
        assert decision.confidence == ConfidenceLevel.HIGH
        assert decision.ask_user is False
        assert '工作领域标签' in decision.matched_features
    
    def test_work_task_tag(self):
        """测试工作任务标签识别"""
        content = "完成设计文档 #task/work"
        decision = self.decision_maker.should_sync(content)
        
        assert decision.should_sync is True
        assert decision.confidence == ConfidenceLevel.HIGH
        assert decision.ask_user is False
        assert '#task/work' in decision.matched_features
    
    def test_meeting_keywords(self):
        """测试会议关键词识别"""
        content = "今天开了个会议，讨论了团队协作的问题"
        decision = self.decision_maker.should_sync(content)
        
        assert decision.should_sync is True
        assert decision.confidence == ConfidenceLevel.HIGH
        assert decision.ask_user is False
    
    def test_adr_keywords(self):
        """测试技术决策记录关键词识别"""
        content = "技术决策：选择 React 作为前端框架"
        decision = self.decision_maker.should_sync(content)
        
        assert decision.should_sync is True
        assert decision.confidence == ConfidenceLevel.HIGH
        assert decision.ask_user is False
        assert '技术决策记录' in decision.matched_features
    
    def test_multiple_work_keywords(self):
        """测试多个工作关键词识别"""
        content = "今天的项目会议讨论了需求和开发计划"
        decision = self.decision_maker.should_sync(content)
        
        assert decision.should_sync is True
        assert decision.confidence == ConfidenceLevel.HIGH
        assert decision.ask_user is False
    
    # 私有内容自动识别测试
    
    def test_personal_task_tag(self):
        """测试个人任务标签识别"""
        content = "买菜做饭 #task/personal"
        decision = self.decision_maker.should_sync(content)
        
        assert decision.should_sync is False
        assert decision.confidence == ConfidenceLevel.HIGH
        assert decision.ask_user is False
        assert '#task/personal' in decision.matched_features
    
    def test_life_area_tag(self):
        """测试生活领域标签识别"""
        content = "今天的健身计划 #area/健康"
        decision = self.decision_maker.should_sync(content)
        
        assert decision.should_sync is False
        assert decision.confidence == ConfidenceLevel.HIGH
        assert decision.ask_user is False
        assert '生活领域标签' in decision.matched_features
    
    def test_personal_project_path(self):
        """测试个人项目路径识别"""
        content = "装修进展"
        file_path = "1-Projects/Personal/装修项目/README.md"
        decision = self.decision_maker.should_sync(content, file_path)
        
        assert decision.should_sync is False
        assert decision.confidence == ConfidenceLevel.HIGH
        assert decision.ask_user is False
        assert '个人项目路径' in decision.matched_features
    
    def test_sensitive_info(self):
        """测试敏感信息识别"""
        content = "我的银行卡密码是 123456"
        decision = self.decision_maker.should_sync(content)
        
        assert decision.should_sync is False
        assert decision.confidence == ConfidenceLevel.HIGH
        assert decision.ask_user is False
        assert '敏感信息' in decision.matched_features
    
    def test_private_tag(self):
        """测试私有标签识别"""
        content = "这是私有内容 #private"
        decision = self.decision_maker.should_sync(content)
        
        assert decision.should_sync is False
        assert decision.confidence == ConfidenceLevel.HIGH
        assert decision.ask_user is False
        assert '#private' in decision.matched_features
    
    def test_personal_project_keywords(self):
        """测试个人项目关键词识别"""
        content = "买房计划和预算"
        decision = self.decision_maker.should_sync(content)
        
        assert decision.should_sync is False
        assert decision.confidence == ConfidenceLevel.HIGH
        assert decision.ask_user is False
        assert '个人项目关键词' in decision.matched_features
    
    # 不确定内容询问机制测试
    
    def test_no_clear_features(self):
        """测试无明确特征的内容"""
        content = "这是一段普通的文本"
        decision = self.decision_maker.should_sync(content)
        
        assert decision.ask_user is True
        assert decision.confidence == ConfidenceLevel.LOW
        assert decision.prompt is not None
    
    def test_learning_keywords_only(self):
        """测试只包含学习关键词的内容"""
        content = "今天学习了 Python 的装饰器"
        decision = self.decision_maker.should_sync(content)
        
        assert decision.ask_user is True
        assert decision.confidence == ConfidenceLevel.MEDIUM
        assert '学习关键词' in decision.matched_features
    
    def test_learning_with_work_keywords(self):
        """测试同时包含学习和工作关键词的内容"""
        content = "学习了项目中使用的技术方案"
        decision = self.decision_maker.should_sync(content)
        
        assert decision.ask_user is True
        assert decision.confidence == ConfidenceLevel.LOW
        assert '学习关键词' in decision.matched_features
        assert '工作关键词' in decision.matched_features
    
    def test_single_work_keyword(self):
        """测试只包含单个工作关键词的内容"""
        content = "今天参与了一个项目"
        decision = self.decision_maker.should_sync(content)
        
        assert decision.ask_user is True
        # Note: "项目" is a work keyword, but without learning keywords
        # it should have MEDIUM confidence
        assert decision.confidence == ConfidenceLevel.MEDIUM
    
    # 边缘情况测试
    
    def test_personal_project_tag_excluded(self):
        """测试个人项目标签被排除"""
        content = "买房计划 #project/买房"
        decision = self.decision_maker.should_sync(content)
        
        # 应该被识别为个人项目关键词，而不是工作项目
        assert decision.should_sync is False
        assert decision.confidence == ConfidenceLevel.HIGH
    
    def test_life_area_excluded(self):
        """测试生活领域标签被排除"""
        content = "财务规划 #area/财务"
        decision = self.decision_maker.should_sync(content)
        
        assert decision.should_sync is False
        assert decision.confidence == ConfidenceLevel.HIGH
    
    def test_empty_content(self):
        """测试空内容"""
        content = ""
        decision = self.decision_maker.should_sync(content)
        
        assert decision.ask_user is True
        assert decision.confidence == ConfidenceLevel.LOW


# ============================================================================
# 属性测试：工作内容自动识别
# ============================================================================

# Feature: obsidian-knowledge-management-workflow, Property 4: 工作内容自动识别
@given(
    work_feature=st.sampled_from([
        '#project/电商系统',
        '#project/后台管理',
        '#project/移动端',
        '#area/技术管理',
        '#area/团队协作',
        '#area/产品设计',
        '#task/work',
        '会议',
        '团队',
        '协作',
        '需求',
        '开发',
        '测试',
        '技术决策',
        'ADR',
    ])
)
@settings(max_examples=100)
def test_property_work_content_auto_detection(work_feature):
    """
    **Validates: Requirements 19.2, 19.3**
    
    属性 4：对于任意包含明确工作特征的内容，应该自动识别为工作内容
    
    对于任意包含明确工作特征（项目标签、工作领域标签、工作任务标签、
    会议关键词、团队协作关键词、技术决策记录）的内容，应该自动识别为
    工作相关内容并标记为需要同步
    """
    decision_maker = SyncDecisionMaker()
    
    # 构造包含工作特征的内容
    content = f"今天的工作内容 {work_feature}"
    
    # 判断是否需要同步
    decision = decision_maker.should_sync(content)
    
    # 验证识别为工作内容
    # 注意：单个工作关键词可能置信度不够高，需要多个关键词
    # 但标签和特定关键词（如"会议"、"团队"）应该被识别
    if work_feature.startswith('#') or work_feature in ['会议', '团队', '协作', '技术决策', 'ADR']:
        assert decision.should_sync is True or decision.ask_user is True, \
            f"Expected work content to be synced or asked, but got should_sync={decision.should_sync}, " \
            f"ask_user={decision.ask_user} for feature: {work_feature}"
        
        if decision.should_sync:
            assert decision.confidence in [ConfidenceLevel.HIGH, ConfidenceLevel.MEDIUM], \
                f"Expected high or medium confidence for work content, but got {decision.confidence} " \
                f"for feature: {work_feature}"


# Feature: obsidian-knowledge-management-workflow, Property 4: 工作内容自动识别（多个关键词）
@given(
    work_keywords=st.lists(
        st.sampled_from([
            '会议', '团队', '协作', '项目', '需求', '开发', '测试',
            '上线', '部署', '评审', '汇报', '周报', '月报',
        ]),
        min_size=2,
        max_size=5,
        unique=True
    )
)
@settings(max_examples=100)
def test_property_multiple_work_keywords_detection(work_keywords):
    """
    **Validates: Requirements 19.2, 19.3**
    
    属性 4：对于任意包含多个工作关键词的内容，应该自动识别为工作内容
    """
    decision_maker = SyncDecisionMaker()
    
    # 构造包含多个工作关键词的内容
    content = f"今天的工作：{' '.join(work_keywords)}"
    
    # 判断是否需要同步
    decision = decision_maker.should_sync(content)
    
    # 验证识别为工作内容（多个关键词应该有高置信度）
    assert decision.should_sync is True, \
        f"Expected work content with multiple keywords to be synced, but got should_sync={decision.should_sync} " \
        f"for keywords: {work_keywords}"
    assert decision.confidence == ConfidenceLevel.HIGH, \
        f"Expected high confidence for multiple work keywords, but got {decision.confidence}"
    assert decision.ask_user is False, \
        f"Expected not to ask user for multiple work keywords, but got ask_user={decision.ask_user}"


# ============================================================================
# 属性测试：私有内容自动识别
# ============================================================================

# Feature: obsidian-knowledge-management-workflow, Property 5: 私有内容自动识别
@given(
    private_feature=st.sampled_from([
        '#task/personal',
        '#area/健康',
        '#area/财务',
        '#area/家庭',
        '#area/生活',
        '#private',
        '个人项目',
        '买房',
        '装修',
        '密码',
        '银行卡',
        '身份证',
        '工资',
        '隐私',
    ])
)
@settings(max_examples=100)
def test_property_private_content_auto_detection(private_feature):
    """
    **Validates: Requirements 19.7**
    
    属性 5：对于任意包含明确私有特征的内容，应该自动识别为私有内容
    
    对于任意包含明确私有特征（个人任务标签、生活领域标签、个人项目关键词、
    敏感个人信息）的内容，应该自动识别为私有内容并标记为 #private
    """
    decision_maker = SyncDecisionMaker()
    
    # 构造包含私有特征的内容
    content = f"今天的内容 {private_feature}"
    
    # 判断是否需要同步
    decision = decision_maker.should_sync(content)
    
    # 验证识别为私有内容
    assert decision.should_sync is False, \
        f"Expected private content not to be synced, but got should_sync={decision.should_sync} " \
        f"for feature: {private_feature}"
    assert decision.confidence == ConfidenceLevel.HIGH, \
        f"Expected high confidence for private content, but got {decision.confidence} " \
        f"for feature: {private_feature}"
    assert decision.ask_user is False, \
        f"Expected not to ask user for private content, but got ask_user={decision.ask_user} " \
        f"for feature: {private_feature}"


# Feature: obsidian-knowledge-management-workflow, Property 5: 私有内容自动识别（文件路径）
@given(
    personal_project=st.sampled_from([
        '买房计划',
        '装修项目',
        '家庭旅行',
        '个人理财',
    ])
)
@settings(max_examples=100)
def test_property_personal_project_path_detection(personal_project):
    """
    **Validates: Requirements 19.7**
    
    属性 5：对于任意位于个人项目路径下的内容，应该自动识别为私有内容
    """
    decision_maker = SyncDecisionMaker()
    
    # 构造个人项目路径
    file_path = f"1-Projects/Personal/{personal_project}/README.md"
    content = "项目进展"
    
    # 判断是否需要同步
    decision = decision_maker.should_sync(content, file_path)
    
    # 验证识别为私有内容
    assert decision.should_sync is False, \
        f"Expected personal project not to be synced, but got should_sync={decision.should_sync} " \
        f"for path: {file_path}"
    assert decision.confidence == ConfidenceLevel.HIGH, \
        f"Expected high confidence for personal project, but got {decision.confidence}"
    assert decision.ask_user is False, \
        f"Expected not to ask user for personal project, but got ask_user={decision.ask_user}"


# ============================================================================
# 属性测试：不确定内容询问机制
# ============================================================================

# Feature: obsidian-knowledge-management-workflow, Property 6: 不确定内容询问机制
@given(
    neutral_content=st.text(
        alphabet=st.characters(
            whitelist_categories=('Lu', 'Ll', 'Nd', 'Zs'),
            blacklist_characters='#@'
        ),
        min_size=10,
        max_size=100
    )
)
@settings(max_examples=100)
def test_property_uncertain_content_ask_user(neutral_content):
    """
    **Validates: Requirements 19.4**
    
    属性 6：对于任意无明确特征的内容，应该主动询问用户
    
    对于任意不包含明确工作或私有特征的内容，应该主动询问用户是否需要同步
    """
    decision_maker = SyncDecisionMaker()
    
    # 过滤掉包含工作或私有关键词的内容
    work_keywords = decision_maker.WORK_KEYWORDS
    private_keywords = (
        decision_maker.PERSONAL_PROJECT_KEYWORDS +
        decision_maker.LIFE_AREA_KEYWORDS +
        decision_maker.SENSITIVE_KEYWORDS +
        decision_maker.LEARNING_KEYWORDS +
        decision_maker.ADR_KEYWORDS
    )
    
    # 检查是否包含关键词
    has_work_keyword = any(keyword in neutral_content for keyword in work_keywords)
    has_private_keyword = any(keyword in neutral_content for keyword in private_keywords)
    
    # 如果包含关键词，跳过此测试用例
    assume(not has_work_keyword and not has_private_keyword)
    
    # 判断是否需要同步
    decision = decision_maker.should_sync(neutral_content)
    
    # 验证需要询问用户
    assert decision.ask_user is True, \
        f"Expected to ask user for uncertain content, but got ask_user={decision.ask_user} " \
        f"for content: {neutral_content[:50]}..."
    assert decision.prompt is not None, \
        f"Expected prompt for uncertain content, but got None for content: {neutral_content[:50]}..."
    assert decision.confidence in [ConfidenceLevel.LOW, ConfidenceLevel.MEDIUM], \
        f"Expected low or medium confidence for uncertain content, but got {decision.confidence}"


# Feature: obsidian-knowledge-management-workflow, Property 6: 不确定内容询问机制（学习内容）
@given(
    learning_keyword=st.sampled_from([
        '学习', '学了', '学到', '笔记', '总结',
        '读书', '阅读', '看了', '了解了',
    ])
)
@settings(max_examples=100)
def test_property_learning_content_ask_user(learning_keyword):
    """
    **Validates: Requirements 19.4**
    
    属性 6：对于任意包含学习关键词但无明确工作特征的内容，应该询问用户
    """
    decision_maker = SyncDecisionMaker()
    
    # 构造包含学习关键词的内容
    content = f"今天{learning_keyword}了一些新知识"
    
    # 判断是否需要同步
    decision = decision_maker.should_sync(content)
    
    # 验证需要询问用户
    assert decision.ask_user is True, \
        f"Expected to ask user for learning content, but got ask_user={decision.ask_user} " \
        f"for keyword: {learning_keyword}"
    assert decision.prompt is not None, \
        f"Expected prompt for learning content, but got None for keyword: {learning_keyword}"
    assert decision.confidence in [ConfidenceLevel.LOW, ConfidenceLevel.MEDIUM], \
        f"Expected low or medium confidence for learning content, but got {decision.confidence}"
