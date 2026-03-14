# Obsidian 知识管理工作流程 - Spec 文档

这是一个基于 Obsidian 的智能知识管理系统的完整规格说明。

## 📁 文档结构

```
.kiro/specs/obsidian-knowledge-management-workflow/
├── README.md                      # 本文件
├── requirements.md                # 需求文档（24 个需求）
├── design.md                      # 设计文档（架构、组件、数据模型）
├── tasks.md                       # 实施任务列表（23 个主任务）
├── user-guide.md                  # 用户使用指南
├── steering-workflow.md           # AI 助手主流程指导文件（待部署）
└── docs/
    └── improvements-reference.md  # 改进记录示例参考
```

## 📋 核心文档

### 1. requirements.md
定义了系统的 24 个需求，包括：
- PARA 文件夹结构
- 日常笔记系统
- 项目和任务管理
- 知识卡片系统
- AI 对话驱动
- 飞书双向同步
- **自我改进机制**（需求 24）

### 2. design.md
详细的设计文档，包括：
- 系统架构（4 层架构）
- 8 个核心组件（含自我改进管理器）
- 数据模型（文件夹结构、YAML 规范、标签系统）
- 28 个正确性属性
- 测试策略

### 3. tasks.md
可执行的实施任务列表：
- 23 个主任务
- 包含子任务和可选测试任务
- 每个任务引用具体需求
- 包含检查点确保质量

### 4. user-guide.md
面向最终用户的使用指南：
- 快速开始
- 4 个核心工作流程（含流程图）
- 4 个实际使用示例
- 最佳实践
- 11 个常见问题
- 6 个进阶技巧（含自我改进）

### 5. steering-workflow.md
AI 助手的主流程指导文件：
- 系统概述和核心原则
- PARA 结构规范
- 8 个核心工作流程详解
- 标签系统规范
- 交互规范
- 自我改进机制
- 快速参考

## 🚀 部署说明

### Steering 文件部署

系统使用两个 steering 文件：

1. **主流程文件**（需要部署）：
   ```
   源文件：steering-workflow.md
   目标位置：.kiro/steering/obsidian-km-workflow.md
   ```
   
2. **改进记录文件**（自动创建）：
   ```
   目标位置：.kiro/steering/obsidian-km-improvements.md
   创建时机：用户首次提供改进建议时
   ```

### 部署步骤

1. 将 `steering-workflow.md` 复制到 `.kiro/steering/obsidian-km-workflow.md`
2. AI 助手会自动读取该文件
3. 当用户提供改进建议时，AI 会自动创建 `obsidian-km-improvements.md`
4. 主流程文件通过 `#[[file:...]]` 引用改进记录文件

## 🎯 系统特点

### 核心特性

1. **对话驱动**：所有操作通过自然语言对话完成
2. **智能判断**：AI 自动识别内容类型和同步需求
3. **PARA 组织**：清晰的文件夹结构
4. **知识网络**：通过双向链接构建知识图谱
5. **飞书集成**：双向同步工作内容
6. **自我学习**：记住用户偏好，持续改进

### 技术栈

- **笔记编辑器**：Obsidian
- **AI 工具**：支持 Skills 和 MCP 的 AI 工具（如 Kiro、Claude Desktop）
- **Skills**：obsidian-markdown、json-canvas
- **MCP**：lark-mcp（飞书集成）
- **实施语言**：Python 3.9+
- **测试框架**：pytest + Hypothesis

## 📊 实施进度

### 需求阶段
- ✅ 需求文档完成（24 个需求）
- ✅ 设计文档完成（8 个组件）
- ✅ 任务列表完成（23 个任务）
- ✅ 用户指南完成
- ✅ Steering 文件完成

### 实施阶段
- ⏳ 待开始（参考 tasks.md）

## 🔗 相关资源

### 外部依赖

- **Obsidian**：https://obsidian.md
- **obsidian-markdown skill**：GitHub
- **json-canvas skill**：GitHub
- **lark-mcp**：飞书官方 MCP 服务器

### 参考文档

- **PARA 方法**：Tiago Forte 的生产力系统
- **Zettelkasten 方法**：卡片盒笔记法
- **MCP 协议**：Model Context Protocol

## 💡 使用建议

### 开始实施

1. 阅读 `requirements.md` 了解系统需求
2. 阅读 `design.md` 了解系统架构
3. 按照 `tasks.md` 的顺序实施
4. 参考 `user-guide.md` 了解用户体验

### 测试系统

1. 初始化 PARA 文件夹结构
2. 创建第一篇日常笔记
3. 测试 AI 对话交互
4. 测试飞书同步（如果配置了 lark-mcp）
5. 测试自我改进机制

### 自定义系统

1. 修改模板文件（Templates 文件夹）
2. 调整 PARA 结构（根据个人需求）
3. 配置飞书同步规则
4. 教 AI 学习你的习惯

## 📝 更新日志

### 2024-01-22
- ✅ 添加需求 24：AI 自我改进机制
- ✅ 添加组件 8：自我改进管理器
- ✅ 添加任务 23：实现自我改进管理器
- ✅ 创建 steering-workflow.md 主流程文件
- ✅ 创建 improvements-reference.md 示例文档
- ✅ 更新用户指南，添加自我改进说明

### 2024-01-15
- ✅ 完成初始需求文档（23 个需求）
- ✅ 完成设计文档（7 个组件）
- ✅ 完成任务列表（22 个任务）
- ✅ 完成用户指南

## 🤝 贡献

如果你有改进建议或发现问题，欢迎：
1. 更新需求文档
2. 完善设计文档
3. 补充使用示例
4. 分享最佳实践

## 📄 许可

本规格文档遵循项目许可协议。

---

**开始使用**：阅读 `user-guide.md` 快速上手！
