"""智能同步判断器

分析笔记内容特征，判断是否需要同步到飞书：
- 识别工作相关特征（项目标签、工作领域、会议关键词等）
- 识别私有内容特征（个人任务、生活领域、敏感信息等）
- 计算判断置信度
- 生成询问提示
"""

import re
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class ConfidenceLevel(Enum):
    """置信度级别"""
    HIGH = "high"      # 高置信度：自动判断
    MEDIUM = "medium"  # 中等置信度：可能需要询问
    LOW = "low"        # 低置信度：需要询问用户


@dataclass
class SyncDecision:
    """同步决策结果"""
    should_sync: bool                    # 是否应该同步
    confidence: ConfidenceLevel          # 置信度级别
    reason: str                          # 判断理由
    matched_features: list[str]          # 匹配的特征列表
    ask_user: bool = False               # 是否需要询问用户
    prompt: Optional[str] = None         # 询问用户的提示语


class SyncDecisionMaker:
    """智能同步判断器
    
    根据内容特征自动判断是否需要同步到飞书
    """
    
    # 工作相关特征
    WORK_PROJECT_TAG_PATTERN = r'#project/(?!.*个人|.*买房|.*装修|.*家庭)'  # 排除个人项目
    WORK_AREA_TAG_PATTERN = r'#area/(?!.*生活|.*健康|.*财务|.*家庭)'  # 排除生活领域
    WORK_TASK_TAG = '#task/work'
    
    WORK_KEYWORDS = [
        '会议', '团队', '协作', '项目', '需求', '开发', '测试',
        '上线', '部署', '评审', '汇报', '周报', '月报',
        '技术方案', '架构', '设计文档', '接口文档',
        '客户', '产品', '运营', '市场',
    ]
    
    # 私有内容特征
    PERSONAL_PROJECT_KEYWORDS = ['个人项目', '买房', '装修', '家庭']
    LIFE_AREA_KEYWORDS = ['生活', '健康', '财务', '家庭', '个人']
    PERSONAL_TASK_TAG = '#task/personal'
    PRIVATE_TAG = '#private'
    
    SENSITIVE_KEYWORDS = [
        '密码', '账号', '身份证', '银行卡', '工资', '薪资',
        '隐私', '私密', '个人信息', '家庭住址',
    ]
    
    # 学习相关关键词（通常是私有内容）
    LEARNING_KEYWORDS = [
        '学习', '学了', '学到', '笔记', '总结', '心得',
        '读书', '阅读', '看了', '了解了',
    ]
    
    # 技术决策记录（通常是工作内容）
    ADR_KEYWORDS = ['技术决策', 'ADR', '架构决策', '决策记录']
    
    def should_sync(self, content: str, file_path: Optional[str] = None) -> SyncDecision:
        """判断内容是否应该同步到飞书
        
        Args:
            content: 笔记内容
            file_path: 文件路径（可选，用于路径判断）
            
        Returns:
            同步决策结果
        """
        matched_features = []
        
        # 1. 检查是否已标记为私有
        if self.PRIVATE_TAG in content:
            return SyncDecision(
                should_sync=False,
                confidence=ConfidenceLevel.HIGH,
                reason="已标记为私有内容",
                matched_features=['#private'],
                ask_user=False
            )
        
        # 2. 检查敏感信息（最高优先级）
        if self._contains_sensitive_info(content):
            matched_features.append('敏感信息')
            return SyncDecision(
                should_sync=False,
                confidence=ConfidenceLevel.HIGH,
                reason="包含敏感个人信息",
                matched_features=matched_features,
                ask_user=False
            )
        
        # 3. 检查文件路径（如果提供）
        if file_path:
            if '1-Projects/Personal' in file_path:
                matched_features.append('个人项目路径')
                return SyncDecision(
                    should_sync=False,
                    confidence=ConfidenceLevel.HIGH,
                    reason="位于个人项目文件夹",
                    matched_features=matched_features,
                    ask_user=False
                )
        
        # 4. 检查个人任务标签
        if self.PERSONAL_TASK_TAG in content:
            matched_features.append('#task/personal')
            return SyncDecision(
                should_sync=False,
                confidence=ConfidenceLevel.HIGH,
                reason="标记为个人任务",
                matched_features=matched_features,
                ask_user=False
            )
        
        # 5. 检查生活领域标签
        if self._contains_life_area(content):
            matched_features.append('生活领域标签')
            return SyncDecision(
                should_sync=False,
                confidence=ConfidenceLevel.HIGH,
                reason="包含生活领域标签",
                matched_features=matched_features,
                ask_user=False
            )
        
        # 6. 检查个人项目关键词
        if self._contains_personal_project(content):
            matched_features.append('个人项目关键词')
            return SyncDecision(
                should_sync=False,
                confidence=ConfidenceLevel.HIGH,
                reason="包含个人项目关键词",
                matched_features=matched_features,
                ask_user=False
            )
        
        # 7. 检查工作任务标签
        if self.WORK_TASK_TAG in content:
            matched_features.append('#task/work')
            return SyncDecision(
                should_sync=True,
                confidence=ConfidenceLevel.HIGH,
                reason="标记为工作任务",
                matched_features=matched_features,
                ask_user=False
            )
        
        # 8. 检查工作项目标签
        if self._contains_work_project(content):
            matched_features.append('工作项目标签')
            return SyncDecision(
                should_sync=True,
                confidence=ConfidenceLevel.HIGH,
                reason="包含工作项目标签",
                matched_features=matched_features,
                ask_user=False
            )
        
        # 9. 检查工作领域标签
        if self._contains_work_area(content):
            matched_features.append('工作领域标签')
            return SyncDecision(
                should_sync=True,
                confidence=ConfidenceLevel.HIGH,
                reason="包含工作领域标签",
                matched_features=matched_features,
                ask_user=False
            )
        
        # 10. 检查技术决策记录
        if self._contains_adr_keywords(content):
            matched_features.append('技术决策记录')
            return SyncDecision(
                should_sync=True,
                confidence=ConfidenceLevel.HIGH,
                reason="技术决策记录通常是工作内容",
                matched_features=matched_features,
                ask_user=False
            )
        
        # 11. 检查学习关键词（需要在工作关键词之前检查）
        has_learning_keywords = self._contains_learning_keywords(content)
        work_keyword_count = self._count_work_keywords(content)
        
        if has_learning_keywords:
            # 如果同时包含工作关键词，则需要询问
            if work_keyword_count > 0:
                matched_features.extend(['学习关键词', '工作关键词'])
                return SyncDecision(
                    should_sync=False,
                    confidence=ConfidenceLevel.LOW,
                    reason="包含学习和工作关键词，无法确定",
                    matched_features=matched_features,
                    ask_user=True,
                    prompt="这个内容是否需要同步到飞书？"
                )
            else:
                matched_features.append('学习关键词')
                return SyncDecision(
                    should_sync=False,
                    confidence=ConfidenceLevel.MEDIUM,
                    reason="包含学习关键词，可能是个人学习",
                    matched_features=matched_features,
                    ask_user=True,
                    prompt="这个学习内容是否需要同步到飞书？"
                )
        
        # 12. 检查工作关键词
        if work_keyword_count >= 2:
            matched_features.append(f'工作关键词({work_keyword_count}个)')
            return SyncDecision(
                should_sync=True,
                confidence=ConfidenceLevel.HIGH,
                reason="包含多个工作相关关键词",
                matched_features=matched_features,
                ask_user=False
            )
        
        # 13. 单个工作关键词，置信度中等
        if work_keyword_count == 1:
            matched_features.append('工作关键词(1个)')
            return SyncDecision(
                should_sync=False,
                confidence=ConfidenceLevel.MEDIUM,
                reason="只包含少量工作关键词，无法确定",
                matched_features=matched_features,
                ask_user=True,
                prompt="这个内容是否需要同步到飞书？"
            )
        
        # 14. 无明确特征，需要询问用户
        return SyncDecision(
            should_sync=False,
            confidence=ConfidenceLevel.LOW,
            reason="无明确工作或私有特征",
            matched_features=[],
            ask_user=True,
            prompt="这个内容是否需要同步到飞书？"
        )
    
    def _contains_sensitive_info(self, content: str) -> bool:
        """检查是否包含敏感信息"""
        return any(keyword in content for keyword in self.SENSITIVE_KEYWORDS)
    
    def _contains_work_project(self, content: str) -> bool:
        """检查是否包含工作项目标签"""
        # 匹配 #project/xxx，但排除个人项目关键词
        matches = re.findall(r'#project/([^\s#]+)', content)
        for match in matches:
            if not any(keyword in match for keyword in self.PERSONAL_PROJECT_KEYWORDS):
                return True
        return False
    
    def _contains_work_area(self, content: str) -> bool:
        """检查是否包含工作领域标签"""
        # 匹配 #area/xxx，但排除生活领域关键词
        matches = re.findall(r'#area/([^\s#]+)', content)
        for match in matches:
            if not any(keyword in match for keyword in self.LIFE_AREA_KEYWORDS):
                return True
        return False
    
    def _contains_life_area(self, content: str) -> bool:
        """检查是否包含生活领域标签"""
        matches = re.findall(r'#area/([^\s#]+)', content)
        for match in matches:
            if any(keyword in match for keyword in self.LIFE_AREA_KEYWORDS):
                return True
        return False
    
    def _contains_personal_project(self, content: str) -> bool:
        """检查是否包含个人项目关键词"""
        return any(keyword in content for keyword in self.PERSONAL_PROJECT_KEYWORDS)
    
    def _contains_adr_keywords(self, content: str) -> bool:
        """检查是否包含技术决策记录关键词"""
        return any(keyword in content for keyword in self.ADR_KEYWORDS)
    
    def _contains_learning_keywords(self, content: str) -> bool:
        """检查是否包含学习关键词"""
        return any(keyword in content for keyword in self.LEARNING_KEYWORDS)
    
    def _count_work_keywords(self, content: str) -> int:
        """统计工作关键词数量"""
        count = 0
        for keyword in self.WORK_KEYWORDS:
            if keyword in content:
                count += 1
        return count
