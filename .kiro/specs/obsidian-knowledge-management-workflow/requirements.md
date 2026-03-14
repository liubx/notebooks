# 需求文档

## 简介

本文档定义了一个基于 Obsidian 的知识管理工作流程系统，采用 PARA + Zettelkasten 混合方法。PARA 方法负责结构组织（Projects/Areas/Resources/Archives），Zettelkasten 方法负责知识网络构建（原子化笔记 + 双向链接）。该系统专为程序员设计，支持技术知识管理、项目管理、日常记录和生活管理的统一工作流程。

系统通过 AI 对话驱动笔记记录和飞书同步，用户通过与 AI 助手对话即可完成笔记创建、内容记录和飞书平台同步，无需手动操作或运行脚本。AI 助手能够智能识别工作相关内容并自动同步到飞书，对于不确定的内容会主动询问用户确认。本系统可以与任何支持 Skills 系统和 MCP（Model Context Protocol）集成的 AI 工具配合使用。

## 术语表

- **知识管理系统 (Knowledge_Management_System)**: 基于 Obsidian 的 PARA + Zettelkasten 混合工作流程系统
- **PARA结构 (PARA_Structure)**: 包含 Projects、Areas、Resources、Archives 四个顶层文件夹的组织结构
- **项目 (Project)**: 有明确截止日期和目标的短期任务集合，分为工作项目和个人项目
- **领域 (Area)**: 需要持续关注的责任范围，分为工作领域和生活领域
- **资源 (Resource)**: 长期参考的知识库，分为技术知识库和生活知识库
- **归档 (Archive)**: 已完成或不再活跃的项目和内容
- **日常笔记 (Daily_Note)**: 统一的每日记录入口，包含工作、学习、生活三个板块
- **知识卡片 (Knowledge_Card)**: 原子化的知识单元，遵循 Zettelkasten 方法
- **双向链接 (Bidirectional_Link)**: 连接笔记的链接，用于构建知识网络
- **标签系统 (Tag_System)**: 多维度分类机制，包含主题、状态、优先级、项目和领域标签
- **技术决策记录 (ADR)**: Architecture Decision Record，记录技术决策的文档
- **笔记模板 (Note_Template)**: 预定义的笔记结构，用于快速创建特定类型的笔记
- **知识流转 (Knowledge_Flow)**: 从日常笔记提炼到知识卡片再到知识网络的过程
- **任务中心 (Task_Center)**: 集中展示和管理所有任务的中心文档
- **飞书同步 (Feishu_Sync)**: Obsidian 与飞书平台之间的双向数据同步机制，通过 AI 对话驱动
- **同步冲突 (Sync_Conflict)**: 当 Obsidian 和飞书的内容同时被修改时产生的冲突状态
- **任务分类 (Task_Category)**: 将任务划分为个人任务、工作任务和项目任务的分类机制
- **同步元数据 (Sync_Metadata)**: 记录同步状态、同步时间、远程ID等同步相关信息的数据
- **飞书同步中心 (Feishu_Sync_Center)**: 集中管理和监控飞书同步状态的中心文档
- **飞书任务清单 (Feishu_Tasklist)**: 飞书平台中的任务列表或多维表格，用于集中管理项目任务
- **AI助手 (AI_Assistant)**: 基于 Skills 系统和 MCP 集成的智能助手，负责理解用户对话、创建笔记和执行飞书同步
- **对话驱动 (Conversation_Driven)**: 通过自然语言对话完成笔记记录和同步操作的交互模式
- **智能同步判断 (Smart_Sync_Decision)**: AI 助手根据内容特征自动判断是否需要同步到飞书的能力
- **Skills系统 (Skills_System)**: AI 工具的技能扩展系统，提供笔记操作和工作流程自动化能力
- **MCP集成 (MCP_Integration)**: Model Context Protocol 集成，提供外部平台（如飞书）的 API 访问能力
- **lark-mcp**: 飞书平台的 MCP 服务器实现，提供飞书 API 访问能力

## 需求

### 需求 1: PARA 文件夹结构

**用户故事:** 作为用户，我希望使用 PARA 方法组织文件夹结构，以便清晰地区分项目、领域、资源和归档内容。

#### 验收标准

1. THE Knowledge_Management_System SHALL 创建包含以下顶层文件夹的 PARA 结构：0-Daily、1-Projects、2-Areas、3-Resources、4-Archives
2. THE PARA_Structure SHALL 在 1-Projects 文件夹下包含两个子文件夹：Work（工作项目）和 Personal（个人项目，如买房、装修等有明确截止日期的事项）
3. THE PARA_Structure SHALL 在 2-Areas 文件夹下包含两个子文件夹：Work（工作领域，如技术管理、团队协作）和 Life（生活领域，如健康、财务）
4. THE PARA_Structure SHALL 在 3-Resources 文件夹下包含两个子文件夹：Tech（技术知识库）和 Life（生活知识库）
5. THE PARA_Structure SHALL 在 0-Daily 文件夹下按年月组织日常笔记（格式：YYYY/MM）

### 需求 2: 统一日常笔记系统

**用户故事:** 作为用户，我希望使用统一的日常笔记记录完整的一天，以便在一个地方管理工作、学习和生活内容。

#### 验收标准

1. WHEN 用户创建日常笔记时，THE Knowledge_Management_System SHALL 创建以当前日期命名的笔记（格式：YYYY-MM-DD）并存储在 0-Daily/YYYY/MM 文件夹中
2. THE Daily_Note SHALL 包含三个主要板块：工作板块、学习板块、生活板块
3. THE Daily_Note SHALL 在工作板块中包含以下字段：今日任务、会议记录、工作进展、问题记录
4. THE Daily_Note SHALL 在学习板块中包含以下字段：学习内容、技术笔记、阅读记录
5. THE Daily_Note SHALL 在生活板块中包含以下字段：个人事项、健康记录、心情感悟
6. THE Daily_Note SHALL 包含指向前一天和后一天笔记的导航链接
7. THE Daily_Note SHALL 使用项目标签（#project/项目名）和领域标签（#area/领域名）关联相关内容

### 需求 3: 项目和领域分离机制

**用户故事:** 作为用户，我希望通过文件夹和标签分离项目和领域内容，以便在日常笔记中统一记录的同时保持内容的组织性。

#### 验收标准

1. WHEN 用户在日常笔记中记录项目相关内容时，THE Knowledge_Management_System SHALL 支持使用 #project/项目名 标签标记内容
2. WHEN 用户在日常笔记中记录领域相关内容时，THE Knowledge_Management_System SHALL 支持使用 #area/领域名 标签标记内容
3. THE Knowledge_Management_System SHALL 支持通过标签搜索查看特定项目或领域的所有相关日常记录
4. THE Knowledge_Management_System SHALL 在 1-Projects 文件夹中为每个项目创建独立的项目文件夹
5. THE Knowledge_Management_System SHALL 在 2-Areas 文件夹中为每个领域创建独立的领域文件夹
6. THE Knowledge_Management_System SHALL 支持从日常笔记中使用双向链接指向项目文件夹或领域文件夹中的详细文档

### 需求 4: 技术知识卡片系统

**用户故事:** 作为程序员，我希望创建原子化的技术知识卡片，以便构建可重用的技术知识单元并促进知识的组合与创新。

#### 验收标准

1. THE Knowledge_Management_System SHALL 在 3-Resources/Tech 文件夹下创建 Knowledge-Cards 子文件夹用于存储技术知识卡片
2. THE Knowledge_Card SHALL 专注于单一技术概念或想法
3. THE Knowledge_Card SHALL 使用描述性标题而非编号（例如："React Hooks 闭包陷阱"而非"卡片001"）
4. THE Knowledge_Card SHALL 包含以下元数据：创建日期、来源、相关标签
5. THE Knowledge_Card SHALL 支持通过双向链接与其他知识卡片建立关联
6. THE Knowledge_Card SHALL 使用 #技术 主题标签和具体的技术子标签（如 #技术/前端/React）

### 需求 5: 代码片段管理

**用户故事:** 作为程序员，我希望管理常用的代码片段，以便快速查找和复用代码。

#### 验收标准

1. THE Knowledge_Management_System SHALL 在 3-Resources/Tech 文件夹下创建 Code-Snippets 子文件夹
2. THE Knowledge_Management_System SHALL 为每个代码片段创建独立的笔记文件
3. THE Knowledge_Management_System SHALL 在代码片段笔记中包含以下字段：代码语言、代码内容、使用场景、相关链接
4. THE Knowledge_Management_System SHALL 支持使用标签标记代码片段的编程语言和用途
5. THE Knowledge_Management_System SHALL 支持在代码片段中使用 Markdown 代码块语法高亮显示代码

### 需求 6: 技术决策记录（ADR）

**用户故事:** 作为程序员，我希望记录技术决策及其背景和理由，以便团队成员理解技术选型和架构演进。

#### 验收标准

1. THE Knowledge_Management_System SHALL 在 3-Resources/Tech 文件夹下创建 ADR 子文件夹
2. THE Knowledge_Management_System SHALL 为每个技术决策创建独立的 ADR 文档
3. THE Knowledge_Management_System SHALL 在 ADR 文档中包含以下字段：决策标题、状态（提议/已接受/已废弃）、背景、决策内容、后果、替代方案
4. THE Knowledge_Management_System SHALL 为 ADR 文档使用编号命名（格式：ADR-NNNN-决策标题）
5. THE Knowledge_Management_System SHALL 支持在 ADR 文档之间使用双向链接建立关联

### 需求 7: 项目管理模板

**用户故事:** 作为用户，我希望使用项目管理模板快速创建项目文档，以便统一管理项目信息和跟踪项目进度。

#### 验收标准

1. THE Knowledge_Management_System SHALL 提供项目管理模板，包含以下字段：项目名称、项目类型（工作/个人）、项目目标、开始日期、截止日期、当前状态、里程碑、任务列表、相关资源、项目日志
2. WHEN 用户在 1-Projects 文件夹中创建新项目时，THE Knowledge_Management_System SHALL 允许用户应用项目管理模板
3. THE Knowledge_Management_System SHALL 在项目模板中自动生成项目标签（#project/项目名）
4. THE Knowledge_Management_System SHALL 在项目模板中包含指向相关日常笔记的查询链接
5. THE Knowledge_Management_System SHALL 支持在项目文档中使用任务列表语法（- [ ] 任务内容）跟踪任务

### 需求 8: 会议记录模板

**用户故事:** 作为用户，我希望使用会议记录模板快速记录会议内容，以便保持会议记录的一致性和完整性。

#### 验收标准

1. THE Knowledge_Management_System SHALL 提供会议记录模板，包含以下字段：会议标题、会议时间、参与者、会议议题、讨论内容、决策事项、行动项、下次会议时间
2. THE Knowledge_Management_System SHALL 在会议记录模板中自动插入当前日期和时间
3. THE Knowledge_Management_System SHALL 支持在会议记录中使用任务列表语法标记行动项
4. THE Knowledge_Management_System SHALL 支持在会议记录中使用双向链接关联相关项目或领域文档
5. THE Knowledge_Management_System SHALL 支持将会议记录存储在日常笔记中或项目文件夹中

### 需求 9: 问题解决记录模板

**用户故事:** 作为程序员，我希望记录问题解决过程，以便积累经验和帮助他人解决类似问题。

#### 验收标准

1. THE Knowledge_Management_System SHALL 提供问题解决记录模板，包含以下字段：问题描述、问题环境、错误信息、解决方案、根本原因、相关资源
2. THE Knowledge_Management_System SHALL 在 3-Resources/Tech 文件夹下创建 Problem-Solving 子文件夹
3. THE Knowledge_Management_System SHALL 支持在问题解决记录中使用代码块展示错误信息和解决方案
4. THE Knowledge_Management_System SHALL 支持使用标签标记问题类型和技术栈
5. THE Knowledge_Management_System SHALL 支持在问题解决记录中使用双向链接关联相关技术知识卡片

### 需求 10: 多维度标签系统

**用户故事:** 作为用户，我希望使用多维度标签对笔记进行分类，以便从不同角度检索和组织信息。

#### 验收标准

1. THE Tag_System SHALL 支持以下主题标签：#技术、#工作、#生活、#学习
2. THE Tag_System SHALL 支持以下状态标签：#进行中、#已完成、#待办
3. THE Tag_System SHALL 支持以下优先级标签：#重要、#紧急
4. THE Tag_System SHALL 支持项目标签格式：#project/项目名
5. THE Tag_System SHALL 支持领域标签格式：#area/领域名
6. THE Tag_System SHALL 支持嵌套标签（例如：#技术/前端/React）
7. THE Tag_System SHALL 允许在单个笔记中使用多个不同维度的标签
8. WHEN 用户点击标签时，THE Knowledge_Management_System SHALL 显示所有包含该标签的笔记列表

### 需求 11: 知识流转工作流程

**用户故事:** 作为用户，我希望将日常笔记中的内容提炼为知识卡片，以便构建长期的知识网络。

#### 验收标准

1. WHEN 用户在日常笔记中发现值得保留的知识点时，THE Knowledge_Management_System SHALL 支持快速创建知识卡片并建立双向链接
2. THE Knowledge_Management_System SHALL 支持从日常笔记中复制内容到知识卡片
3. THE Knowledge_Management_System SHALL 在知识卡片中自动记录来源日常笔记的链接
4. THE Knowledge_Management_System SHALL 支持在知识卡片之间建立双向链接以形成知识网络
5. THE Knowledge_Management_System SHALL 提供图形视图展示知识卡片之间的链接关系

### 需求 12: 周期性回顾机制

**用户故事:** 作为用户，我希望定期回顾和总结我的工作和生活，以便巩固知识并反思个人成长。

#### 验收标准

1. THE Knowledge_Management_System SHALL 提供周回顾模板，包含两个部分：工作总结（本周完成项目、技术学习、工作反思）和生活总结（个人事项、健康状况、生活感悟）
2. THE Knowledge_Management_System SHALL 提供月回顾模板，包含两个部分：工作总结（本月目标达成、重要项目、技术成长）和生活总结（个人目标、重要事件、下月计划）
3. THE Knowledge_Management_System SHALL 在周回顾模板中自动嵌入本周所有日常笔记的链接
4. THE Knowledge_Management_System SHALL 在月回顾模板中自动嵌入本月所有周回顾的链接
5. THE Knowledge_Management_System SHALL 将周回顾和月回顾存储在 0-Daily 文件夹的相应年月子文件夹中

### 需求 13: 项目归档机制

**用户故事:** 作为用户，我希望将已完成的项目归档，以便保持活跃项目列表的清晰性同时保留历史记录。

#### 验收标准

1. WHEN 项目状态标记为已完成时，THE Knowledge_Management_System SHALL 支持将项目文件夹移动到 4-Archives 文件夹
2. THE Knowledge_Management_System SHALL 在归档项目时保留所有双向链接和标签
3. THE Knowledge_Management_System SHALL 在归档项目文件夹中添加归档日期元数据
4. THE Knowledge_Management_System SHALL 支持在 4-Archives 文件夹中按年份组织归档项目
5. THE Knowledge_Management_System SHALL 支持搜索和访问归档项目的内容

### 需求 14: 双向链接和知识网络

**用户故事:** 作为用户，我希望通过双向链接建立笔记之间的关联，以便构建知识网络并发现知识之间的联系。

#### 验收标准

1. THE Knowledge_Management_System SHALL 支持使用 [[笔记名称]] 语法创建双向链接
2. WHEN 用户创建指向不存在笔记的链接时，THE Knowledge_Management_System SHALL 允许快速创建该笔记
3. THE Knowledge_Management_System SHALL 在笔记中显示所有反向链接（引用当前笔记的其他笔记）
4. THE Knowledge_Management_System SHALL 提供图形视图展示笔记之间的链接关系
5. THE Knowledge_Management_System SHALL 在图形视图中使用不同颜色或形状区分不同类型的笔记（日常笔记、项目、领域、知识卡片）

### 需求 15: 搜索和检索功能

**用户故事:** 作为用户，我希望能够快速搜索和定位笔记内容，以便高效地找到所需信息。

#### 验收标准

1. THE Knowledge_Management_System SHALL 支持全文搜索功能，搜索所有笔记的标题和内容
2. THE Knowledge_Management_System SHALL 支持按标签筛选搜索结果
3. THE Knowledge_Management_System SHALL 支持按文件夹（Projects/Areas/Resources/Archives）筛选搜索结果
4. THE Knowledge_Management_System SHALL 支持按创建日期或修改日期筛选搜索结果
5. WHEN 搜索返回结果时，THE Knowledge_Management_System SHALL 高亮显示匹配的关键词
6. THE Knowledge_Management_System SHALL 支持使用正则表达式进行高级搜索

### 需求 16: 附件和资源管理

**用户故事:** 作为用户，我希望有效管理笔记中的图片、PDF 和其他附件，以便保持笔记库的整洁和可维护性。

#### 验收标准

1. THE Knowledge_Management_System SHALL 创建顶层 Attachments 文件夹用于存储所有附件
2. WHEN 用户在笔记中插入图片或文件时，THE Knowledge_Management_System SHALL 自动将附件复制到 Attachments 文件夹
3. THE Knowledge_Management_System SHALL 支持在 Attachments 文件夹下按项目或主题创建子文件夹组织附件
4. THE Knowledge_Management_System SHALL 支持在笔记中嵌入和预览图片、PDF 文件
5. THE Knowledge_Management_System SHALL 为附件使用描述性文件名而非随机字符串

### 需求 17: 分类任务管理系统

**用户故事:** 作为用户，我希望按照任务类型对任务进行分类管理，以便清晰地区分个人任务、工作任务和项目任务。

#### 验收标准

1. THE Task_Category SHALL 支持三种任务类型：个人任务（#task/personal）、工作任务（#task/work）、项目任务（#task/project/项目名）
2. WHEN 用户创建个人任务时，THE Knowledge_Management_System SHALL 支持将任务存储在 0-Daily 文件夹或 1-Projects/Personal 文件夹中
3. WHEN 用户创建工作任务时，THE Knowledge_Management_System SHALL 支持将任务存储在 0-Daily 文件夹或 2-Areas/Work 文件夹中
4. WHEN 用户创建项目任务时，THE Knowledge_Management_System SHALL 支持将任务存储在 1-Projects/Work/项目名 文件夹或 1-Projects/Personal/项目名 文件夹中
5. THE Knowledge_Management_System SHALL 在根目录创建任务中心文档
6. THE Task_Center SHALL 按任务类型分组显示：工作任务、项目任务、个人任务
7. THE Task_Center SHALL 显示今日任务、本周任务、重要紧急任务
8. THE Task_Center SHALL 显示任务统计信息：今日完成数、本周完成数、进行中任务数
9. THE Task_Center SHALL 支持快速创建新任务的功能
10. THE Knowledge_Management_System SHALL 支持为任务添加以下属性：截止日期（📅 YYYY-MM-DD）、负责人（@姓名）、优先级（#重要、#紧急）、项目关联（#project/项目名）

### 需求 18: AI 对话驱动的笔记记录

**用户故事:** 作为用户，我希望通过与 AI 助手对话来记录生活和工作的一切，以便自然、高效地创建和管理笔记。

#### 验收标准

1. THE AI_Assistant SHALL 理解用户的自然语言输入并识别用户意图（创建笔记、记录任务、更新项目等）
2. WHEN 用户描述需要记录的内容时，THE AI_Assistant SHALL 自动判断内容类型（日常笔记、项目任务、会议记录、技术笔记等）
3. WHEN 用户描述需要记录的内容时，THE AI_Assistant SHALL 自动选择合适的笔记模板和存储位置
4. THE AI_Assistant SHALL 根据对话内容自动提取关键信息：标题、日期、标签、优先级、负责人等
5. THE AI_Assistant SHALL 支持在对话中创建多种类型的笔记：日常笔记、项目文档、会议记录、技术知识卡片、问题解决记录
6. WHEN 用户提供的信息不完整时，THE AI_Assistant SHALL 主动询问缺失的关键信息
7. THE AI_Assistant SHALL 在创建笔记后向用户确认笔记内容和位置
8. THE AI_Assistant SHALL 支持在对话中修改已创建的笔记内容
9. THE AI_Assistant SHALL 支持通过对话查询和检索已有笔记
10. THE AI_Assistant SHALL 自动为笔记添加合适的标签和双向链接

### 需求 19: AI 智能同步判断

**用户故事:** 作为用户，我希望 AI 助手能够智能判断哪些内容需要同步到飞书，以便自动化同步流程并减少手动操作。

#### 验收标准

1. THE AI_Assistant SHALL 分析笔记内容特征以判断是否为工作相关内容
2. THE Smart_Sync_Decision SHALL 基于以下特征识别工作相关内容：项目标签（#project/工作项目名）、工作领域标签（#area/工作领域）、工作任务标签（#task/work）、会议记录关键词、团队协作关键词、技术决策记录
3. WHEN AI 助手识别到明确的工作相关内容时，THE AI_Assistant SHALL 自动标记内容为需要同步（#sync/feishu 或 #sync/feishu-doc）
4. WHEN AI 助手无法确定内容是否为工作相关时，THE AI_Assistant SHALL 主动询问用户："这个内容是否需要同步到飞书？"
5. WHEN 用户确认需要同步时，THE AI_Assistant SHALL 标记内容为需要同步并执行同步操作
6. WHEN 用户确认不需要同步时，THE AI_Assistant SHALL 标记内容为私有（#private）
7. THE AI_Assistant SHALL 识别以下内容为私有内容并自动标记为 #private：个人任务（#task/personal）、生活领域内容（#area/生活领域）、个人项目（1-Projects/Personal 路径下）、包含敏感个人信息的内容
8. THE AI_Assistant SHALL 在对话过程中学习用户的同步偏好，提高判断准确性
9. THE AI_Assistant SHALL 支持用户通过对话修改已有笔记的同步设置
10. THE AI_Assistant SHALL 在执行同步前向用户说明将要同步的内容和目标位置

### 需求 20: 基于 Skills 系统和 MCP 集成的飞书同步

**用户故事:** 作为用户，我希望通过 AI 工具的 Skills 系统和 MCP 集成实现飞书同步，以便在 AI 对话过程中无缝完成同步操作。

#### 验收标准

1. THE AI_Assistant SHALL 使用 Skills_System 访问和操作 Obsidian 笔记文件
2. THE AI_Assistant SHALL 使用 MCP_Integration（通过 lark-mcp 服务器）访问飞书 API 进行任务和文档操作
3. WHEN 笔记标记为需要同步时，THE AI_Assistant SHALL 在对话过程中自动执行同步操作
4. THE Feishu_Sync SHALL 支持同步任务到飞书任务清单，包含以下内容：任务标题、任务描述、截止日期、负责人、优先级、完成状态
5. THE Feishu_Sync SHALL 支持同步文档到飞书文档或知识库，包含以下内容：Markdown 正文、标题层级、列表、任务列表、代码块、表格、图片、链接
6. THE AI_Assistant SHALL 在同步完成后更新笔记的同步元数据：feishu_task_id 或 feishu_doc_id、last_sync、sync_status、feishu_url
7. THE AI_Assistant SHALL 将同步状态标签从 #sync/feishu 更新为 #synced/feishu
8. WHEN 同步失败时，THE AI_Assistant SHALL 标记内容为 #sync-error/feishu 并向用户说明失败原因
9. THE AI_Assistant SHALL 支持在对话中手动触发同步操作
10. THE AI_Assistant SHALL 支持在对话中查询同步状态和历史记录

### 需求 21: 飞书任务双向同步

**用户故事:** 作为用户，我希望 Obsidian 中的任务与飞书任务保持双向同步，以便在两个平台上保持任务信息的一致性。

#### 验收标准

1. THE AI_Assistant SHALL 支持双向同步模式：Obsidian 到飞书和飞书到 Obsidian
2. WHEN Obsidian 中的任务更新时，THE AI_Assistant SHALL 在对话过程中检测变更并自动更新对应的飞书任务
3. WHEN 用户询问飞书任务状态时，THE AI_Assistant SHALL 通过 MCP_Integration 查询飞书任务并同步更新到 Obsidian
4. THE AI_Assistant SHALL 在任务中记录以下同步元数据：feishu_task_id（飞书任务ID）、last_sync（最后同步时间）、sync_status（同步状态）、feishu_url（飞书任务链接）
5. THE AI_Assistant SHALL 支持在项目文件夹中创建 .feishu-sync.json 配置文件
6. THE AI_Assistant SHALL 通过 .feishu-sync.json 配置文件定义项目级同步规则和映射关系
7. WHEN 用户创建新项目并确认需要飞书同步时，THE AI_Assistant SHALL 在飞书中创建对应的任务清单
8. THE AI_Assistant SHALL 在项目配置文件（.feishu-sync.json）中记录飞书任务清单ID（feishu_tasklist_id）
9. WHEN 项目任务需要同步时，THE AI_Assistant SHALL 将任务同步到项目对应的飞书任务清单
10. THE AI_Assistant SHALL 确保同一项目的所有任务同步到同一个飞书任务清单
11. THE AI_Assistant SHALL 在任务同步时保持任务在项目中的顺序
12. THE AI_Assistant SHALL 支持用户通过对话指定任务的自定义分组
13. WHEN 用户指定任务分组时，THE AI_Assistant SHALL 在飞书任务清单中创建对应的自定义分组（如果不存在）
14. THE AI_Assistant SHALL 使用特殊标签（#group/分组名）标记任务所属的自定义分组
15. WHEN 用户查询飞书任务清单变更时，THE AI_Assistant SHALL 同步飞书中的分组变更到 Obsidian

### 需求 22: 飞书文档双向同步

**用户故事:** 作为用户，我希望 Obsidian 笔记与飞书文档保持双向同步，以便在团队协作时保持文档内容的一致性。

#### 验收标准

1. THE AI_Assistant SHALL 支持同步笔记到飞书文档（#sync/feishu-doc）或飞书知识库（#sync/feishu-wiki）
2. THE AI_Assistant SHALL 同步以下内容：Markdown 正文、标题层级、列表（有序/无序）、任务列表、代码块、表格、图片、链接
3. WHEN 同步图片时，THE AI_Assistant SHALL 通过 MCP_Integration 将图片上传到飞书平台
4. THE AI_Assistant SHALL 将 [[内部链接]] 转换为飞书文档链接（如果目标文档已同步）
5. THE AI_Assistant SHALL 将 #标签 转换为飞书标签
6. THE AI_Assistant SHALL 将 @提及 转换为飞书 @提及
7. THE AI_Assistant SHALL 在文档的 YAML front matter 中配置同步信息，包含以下字段：platform（平台）、doc_type（文档类型：doc/wiki/sheet）、feishu_doc_id（飞书文档ID）、feishu_folder（飞书文件夹路径）、sync_mode（同步模式）、auto_sync（自动同步开关）、last_sync（最后同步时间）、sync_status（同步状态）
8. THE AI_Assistant SHALL 支持三种同步模式：bidirectional（双向同步）、obsidian_to_feishu（仅 Obsidian 到飞书）、feishu_to_obsidian（仅飞书到 Obsidian）
9. WHEN 用户询问飞书文档更新时，THE AI_Assistant SHALL 通过 MCP_Integration 检查飞书文档变更
10. WHEN 检测到同步冲突时，THE AI_Assistant SHALL 比较 Obsidian 和飞书的修改时间和内容差异
11. WHEN 检测到同步冲突时，THE AI_Assistant SHALL 询问用户选择：保留 Obsidian 版本、保留飞书版本、手动合并
12. WHEN 检测到同步冲突时，THE AI_Assistant SHALL 使用 #sync-conflict/feishu 标记冲突文档并暂停自动同步

### 需求 23: 飞书同步中心

**用户故事:** 作为用户，我希望在一个集中的位置查看和管理所有飞书同步状态，以便监控同步进度和处理同步问题。

#### 验收标准

1. THE Knowledge_Management_System SHALL 在根目录创建飞书同步中心文档
2. THE Feishu_Sync_Center SHALL 显示任务同步状态和文档同步状态
3. THE Feishu_Sync_Center SHALL 显示待同步列表，包含所有标记为 #sync/feishu、#sync/feishu-doc、#sync/feishu-wiki 的内容
4. THE Feishu_Sync_Center SHALL 显示已同步列表，包含所有标记为 #synced/feishu 的内容
5. THE Feishu_Sync_Center SHALL 显示同步失败列表，包含所有标记为 #sync-error/feishu 或 #sync-conflict/feishu 的内容
6. THE Feishu_Sync_Center SHALL 显示同步统计信息：待同步数量、已同步数量、同步失败数量、最后同步时间
7. THE Feishu_Sync_Center SHALL 支持按同步状态筛选和搜索内容
8. THE AI_Assistant SHALL 支持通过对话查询飞书同步中心的状态信息
9. THE AI_Assistant SHALL 支持通过对话触发批量同步操作
10. THE AI_Assistant SHALL 支持通过对话处理同步失败和冲突的内容

### 需求 24: AI 自我改进机制

**用户故事:** 作为用户，我希望 AI 助手能够学习和记住我的偏好和纠正，以便在后续使用中按照我期望的方式工作。

#### 验收标准

1. THE AI_Assistant SHALL 支持用户通过对话指出问题或提供正确做法
2. WHEN 用户指出 AI 的错误或不当行为时，THE AI_Assistant SHALL 记录问题描述和正确做法
3. WHEN 用户提供偏好设置时，THE AI_Assistant SHALL 记录用户偏好
4. THE AI_Assistant SHALL 将改进记录存储在 `.kiro/steering/obsidian-km-improvements.md` 文件中
5. THE AI_Assistant SHALL 在后续操作中参考改进记录，避免重复相同错误
6. THE AI_Assistant SHALL 支持以下类型的改进记录：同步判断偏好、笔记创建习惯、标签使用规范、任务管理偏好、知识提炼偏好
7. WHEN 用户提供改进建议时，THE AI_Assistant SHALL 确认理解并说明将如何应用
8. THE AI_Assistant SHALL 支持用户查询当前的改进记录
9. THE AI_Assistant SHALL 支持用户修改或删除特定的改进记录
10. THE AI_Assistant SHALL 在改进记录中包含以下信息：日期、问题描述、正确做法、适用场景、示例

## 附加说明

本需求文档定义了一个完整的 PARA + Zettelkasten 混合知识管理工作流程，专为程序员设计，并通过 AI 对话驱动实现自然、高效的笔记记录和飞书同步。实施时应注意：

- PARA 结构提供清晰的组织框架，但应保持灵活性，允许用户根据个人需求调整子文件夹
- 日常笔记作为统一入口，通过标签和链接与项目、领域内容关联，避免内容分散
- 知识卡片系统遵循 Zettelkasten 原则，强调原子化和链接，而非层级分类
- 标签系统应简洁明了，避免过度分类导致管理负担
- 模板作为起点，用户可以根据实际使用情况进行定制
- 工作流程支持渐进式采用，用户可以从基础功能开始逐步扩展
- 技术特性（ADR、代码片段、问题解决记录）专为程序员日常工作设计
- 周期性回顾机制帮助用户从日常记录中提炼长期价值
- 分类任务管理系统提供清晰的任务组织方式，支持个人、工作和项目任务的分离管理
- AI 对话驱动的笔记记录使用户能够通过自然语言快速创建和管理笔记，无需手动操作文件系统
- AI 智能同步判断能够自动识别工作相关内容并同步到飞书，对于不确定的内容会主动询问用户
- 飞书同步通过 AI 工具的 Skills 系统和 MCP 集成在对话过程中自动完成，无需运行独立的同步脚本
- 本系统设计为平台无关，可以与任何支持 Skills 扩展和 MCP 协议的 AI 工具配合使用（如 Kiro、Claude Desktop 等）
- 同步冲突处理机制确保数据安全，AI 助手会在检测到冲突时主动询问用户处理方式
- 飞书同步中心提供统一的同步管理界面，可通过 AI 对话查询和操作
- 整个工作流程强调对话式交互，用户只需描述需求，AI 助手负责执行具体操作
- AI 自我改进机制使系统能够学习用户偏好，随着使用时间增长而变得更加个性化和智能
