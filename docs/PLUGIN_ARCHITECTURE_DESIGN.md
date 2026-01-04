# Claude Code Plugin 标准架构设计方案

## 一、概述

本文档为 `happy-coding-agent` 项目提供一个标准化的 Claude Code 插件组织方案。该方案基于 Claude Code 的官方扩展机制，结合业界最佳实践，提供清晰的目录结构、组件规范和工作流程。

## 二、核心概念

### 2.1 Claude Code 扩展机制

Claude Code 支持三种主要的扩展类型：

| 类型 | 目录 | 用途 | 触发方式 |
|------|------|------|----------|
| **Commands** | `.claude/commands/` | 斜杠命令，用户主动调用 | `/command-name` |
| **Agents** | `.claude/agents/` | 子代理，处理特定类型的任务 | Task 工具自动调度 |
| **Skills** | `.claude/skills/` | 可复用的专业能力包 | Skill 工具调用 |

### 2.2 本项目的双重角色

```
┌─────────────────────────────────────────────────────────────────┐
│                   happy-coding-agent                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────────────┐    ┌───────────────────────────────┐  │
│  │   Plugin Package     │    │      Distribution CLI         │  │
│  │   (.claude/)         │    │      (hca command)            │  │
│  │                      │    │                               │  │
│  │  • agents/           │    │  • init - 部署插件            │  │
│  │  • commands/         │───▶│  • update - 更新插件          │  │
│  │  • skills/           │    │  • status - 查看状态          │  │
│  │                      │    │  • package - 打包发布         │  │
│  └──────────────────────┘    └───────────────────────────────┘  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## 三、推荐的目录结构

### 3.1 完整目录结构

```
happy-coding-agent/
│
├── 📄 CLAUDE.md                    # 项目级 Claude 指令
├── 📄 README.md                    # 项目说明文档
├── 📄 LICENSE                      # 开源许可证
├── 📄 pyproject.toml               # Python 包配置
├── 📄 manifest.json                # [新增] 插件清单文件
│
├── 📁 .claude/                     # Claude Code 插件核心目录
│   │
│   ├── 📄 settings.json            # [新增] 插件默认设置
│   │
│   ├── 📁 agents/                  # 子代理定义
│   │   ├── 📄 _index.json          # [新增] 代理索引和分类
│   │   │
│   │   ├── 📁 code/                # [新增] 代码分析类代理
│   │   │   ├── 📄 code-architect.md
│   │   │   ├── 📄 code-explorer.md
│   │   │   └── 📄 code-reviewer.md
│   │   │
│   │   ├── 📁 screenshot/          # [新增] 截图分析类代理
│   │   │   ├── 📄 ui-analyzer.md
│   │   │   ├── 📄 interaction-analyzer.md
│   │   │   ├── 📄 business-analyzer.md
│   │   │   ├── 📄 synthesizer.md
│   │   │   └── 📄 reviewer.md
│   │   │
│   │   └── 📁 test/                # [新增] 测试类代理
│   │       ├── 📄 test-generator.md
│   │       └── 📄 test-runner.md
│   │
│   ├── 📁 commands/                # 斜杠命令
│   │   ├── 📄 _index.json          # [新增] 命令索引
│   │   ├── 📄 feature-analyzer.md
│   │   ├── 📄 feature-pipeline.md
│   │   ├── 📄 feature-dev.md
│   │   └── 📄 screenshot-analyzer.md
│   │
│   ├── 📁 skills/                  # 技能包
│   │   ├── 📄 _index.json          # [新增] 技能索引
│   │   │
│   │   ├── 📁 feature-design-assistant/
│   │   │   ├── 📄 SKILL.md         # 技能主文件 (必需)
│   │   │   ├── 📁 references/      # 参考文档
│   │   │   ├── 📁 scripts/         # 可执行脚本
│   │   │   └── 📁 assets/          # 资产文件
│   │   │
│   │   ├── 📁 task-execution-engine/
│   │   │   └── ...
│   │   │
│   │   ├── 📁 screenshot-feature-extractor/
│   │   │   └── ...
│   │   │
│   │   └── 📁 skill-creation-guide/
│   │       └── ...
│   │
│   └── 📁 .hca/                    # [保留] 元数据目录
│       └── 📄 metadata.json
│
├── 📁 cli/                         # CLI 工具源码
│   ├── 📄 __init__.py
│   ├── 📄 main.py
│   │
│   ├── 📁 commands/                # CLI 命令
│   │   ├── 📄 __init__.py
│   │   ├── 📄 init.py
│   │   ├── 📄 update.py
│   │   ├── 📄 status.py
│   │   ├── 📄 package.py           # [新增] 打包命令
│   │   ├── 📄 validate.py          # [新增] 验证命令
│   │   └── 📄 list.py              # [新增] 列表命令
│   │
│   └── 📁 core/                    # 核心逻辑
│       ├── 📄 __init__.py
│       ├── 📄 config.py
│       ├── 📄 deployer.py
│       ├── 📄 git_ops.py
│       ├── 📄 validator.py         # [新增] 验证器
│       ├── 📄 packager.py          # [新增] 打包器
│       └── 📄 manifest.py          # [新增] 清单解析器
│
├── 📁 tests/                       # 测试目录
│   ├── 📄 conftest.py
│   ├── 📄 test_init_modes.py
│   ├── 📄 test_deployer.py         # [新增]
│   ├── 📄 test_validator.py        # [新增]
│   └── 📁 fixtures/                # [新增] 测试固件
│       └── ...
│
├── 📁 docs/                        # [新增] 文档目录
│   ├── 📄 PLUGIN_ARCHITECTURE_DESIGN.md  # 本文档
│   ├── 📄 CONTRIBUTING.md          # 贡献指南
│   ├── 📄 COMPONENT_SPEC.md        # 组件规范
│   └── 📄 CHANGELOG.md             # 变更日志
│
└── 📁 scripts/                     # [新增] 开发脚本
    ├── 📄 build.sh
    ├── 📄 release.sh
    └── 📄 validate-all.sh
```

### 3.2 目录职责说明

| 目录 | 职责 | 重要性 |
|------|------|--------|
| `.claude/` | Claude Code 插件内容，部署到目标项目 | 核心 |
| `cli/` | CLI 工具，用于分发和管理插件 | 核心 |
| `docs/` | 项目文档，开发者参考 | 重要 |
| `tests/` | 自动化测试，质量保证 | 重要 |
| `scripts/` | 开发和发布脚本 | 辅助 |

## 四、核心文件规范

### 4.1 manifest.json - 插件清单

```json
{
  "$schema": "https://claude.ai/schemas/plugin-manifest-v1.json",
  "name": "happy-coding-agent",
  "version": "1.0.0",
  "description": "A collection of Claude Code skills, commands, and agents for rapid product development",
  "author": "notedit",
  "license": "MIT",
  "repository": "https://github.com/notedit/happy-coding-agent",

  "claude_code": {
    "min_version": "1.0.0",
    "features": ["agents", "commands", "skills"]
  },

  "components": {
    "agents": {
      "code": {
        "description": "Code analysis and architecture agents",
        "items": ["code-architect", "code-explorer", "code-reviewer"]
      },
      "screenshot": {
        "description": "Screenshot analysis multi-agent pipeline",
        "items": ["ui-analyzer", "interaction-analyzer", "business-analyzer", "synthesizer", "reviewer"]
      },
      "test": {
        "description": "Testing automation agents",
        "items": ["test-generator", "test-runner"]
      }
    },
    "commands": {
      "items": ["feature-analyzer", "feature-pipeline", "feature-dev", "screenshot-analyzer"]
    },
    "skills": {
      "items": ["feature-design-assistant", "task-execution-engine", "screenshot-feature-extractor", "skill-creation-guide"]
    }
  },

  "dependencies": {
    "python": ">=3.8",
    "packages": ["click>=8.0", "rich>=13.0"]
  },

  "tags": ["development", "productivity", "code-review", "architecture"]
}
```

### 4.2 Agent 文件规范

```yaml
# .claude/agents/{category}/{agent-name}.md

---
# === 必需字段 ===
name: agent-name                  # 代理标识符 (kebab-case)
description: |                    # 详细描述 (用于调度决策)
  First sentence is the summary.
  Following sentences provide more detail about capabilities.

# === 可选字段 ===
tools: Glob, Grep, Read, Edit    # 允许使用的工具
model: opus | sonnet | haiku     # 推荐模型
color: green | blue | yellow     # UI 颜色标识
---

# Agent Instructions

## Core Responsibilities
- Responsibility 1
- Responsibility 2

## Process
1. Step one
2. Step two

## Output Format
Describe expected output...
```

### 4.3 Command 文件规范

```yaml
# .claude/commands/{command-name}.md

---
# === 必需字段 ===
description: "One-line description for command list"

# === 可选字段 ===
argument-hint: "Placeholder text for arguments"
allowed-tools: Read, Write, Glob, Grep, Bash
---

## Phase 1: Setup
Instructions for phase 1...

## Phase 2: Execution
Instructions for phase 2...

## Variables
- $ARGUMENTS - User-provided arguments
```

### 4.4 Skill 文件规范

```yaml
# .claude/skills/{skill-name}/SKILL.md

---
# === 必需字段 ===
name: skill-name
description: |
  What the skill does.
  When to use this skill: (1) scenario one, (2) scenario two.

# === 可选字段 ===
license: MIT | See LICENSE.txt
---

# Skill Name

## Overview
Brief overview...

## Core Workflow
1. Step one
2. Step two

## Bundled Resources

### Scripts
- `scripts/script1.py` - Description

### References
- `references/ref1.md` - Description

## Usage Examples
Example 1...
```

### 4.5 索引文件规范

```json
// .claude/agents/_index.json
{
  "version": "1.0",
  "categories": {
    "code": {
      "name": "Code Analysis",
      "description": "Agents for analyzing and architecting code",
      "agents": [
        {
          "file": "code/code-architect.md",
          "name": "code-architect",
          "summary": "Designs feature architectures"
        }
      ]
    }
  }
}
```

## 五、组件分类体系

### 5.1 Agents 分类

```
agents/
├── code/               # 代码分析类
│   ├── architect      # 架构设计
│   ├── explorer       # 代码探索
│   └── reviewer       # 代码审查
│
├── screenshot/         # 截图分析类 (多代理流水线)
│   ├── ui-analyzer           # UI 分析
│   ├── interaction-analyzer  # 交互分析
│   ├── business-analyzer     # 业务分析
│   ├── synthesizer           # 综合整理
│   └── reviewer              # 质量审查
│
├── test/               # 测试类
│   ├── generator      # 测试生成
│   └── runner         # 测试执行
│
└── workflow/           # [未来] 工作流类
    ├── planner        # 任务规划
    └── executor       # 任务执行
```

### 5.2 Commands 分类

```
commands/
├── feature-*          # 功能开发系列
│   ├── feature-analyzer     # 需求分析
│   ├── feature-dev          # 引导开发
│   └── feature-pipeline     # 任务执行
│
├── screenshot-*       # 截图分析系列
│   └── screenshot-analyzer  # 截图特征提取
│
└── [future]/          # 未来扩展
    ├── refactor-*     # 重构系列
    ├── doc-*          # 文档系列
    └── test-*         # 测试系列
```

### 5.3 Skills 分类

```
skills/
├── design/            # 设计类
│   └── feature-design-assistant/
│
├── execution/         # 执行类
│   └── task-execution-engine/
│
├── analysis/          # 分析类
│   └── screenshot-feature-extractor/
│
└── meta/              # 元技能类
    └── skill-creation-guide/
```

## 六、CLI 命令设计

### 6.1 命令概览

```bash
hca <command> [options]

Commands:
  init      Initialize .claude in current project
  update    Update deployed configurations
  status    Show deployment status
  list      List available components
  package   Package plugin for distribution
  validate  Validate plugin structure
  publish   Publish to registry (future)

Global Options:
  -v, --verbose    Enable verbose output
  --version        Show version
  --help           Show help
```

### 6.2 命令详细设计

#### `hca init`
```bash
hca init [options]

Options:
  --select           Interactive component selection
  --components       Comma-separated component list
  --mode             Deployment mode: overwrite|merge|backup
  --source           Custom source repository
  --branch           Source branch (default: main)

Examples:
  hca init                           # Deploy all components
  hca init --select                  # Interactive selection
  hca init --components agents,skills
  hca init --mode merge              # Preserve user additions
```

#### `hca list`
```bash
hca list [type] [options]

Arguments:
  type               agents|commands|skills|all (default: all)

Options:
  --remote           List from remote repository
  --json             Output as JSON
  --details          Show detailed information

Examples:
  hca list                           # List all local components
  hca list agents --details          # List agents with descriptions
  hca list --remote                  # List from source repo
```

#### `hca validate`
```bash
hca validate [path] [options]

Arguments:
  path               Path to validate (default: current directory)

Options:
  --fix              Auto-fix issues where possible
  --strict           Strict validation mode
  --report           Generate validation report

Examples:
  hca validate                       # Validate current project
  hca validate .claude/skills/       # Validate skills only
  hca validate --fix                 # Fix common issues
```

#### `hca package`
```bash
hca package [options]

Options:
  --output           Output directory
  --format           Package format: zip|tar|skill
  --include          Components to include
  --exclude          Components to exclude

Examples:
  hca package                        # Package all to ./dist
  hca package --format skill         # Create .skill files
  hca package --include skills       # Package skills only
```

## 七、验证规则

### 7.1 结构验证

| 规则 | 级别 | 描述 |
|------|------|------|
| V001 | ERROR | `SKILL.md` 必须存在于每个 skill 目录 |
| V002 | ERROR | YAML frontmatter 必须包含 `name` 和 `description` |
| V003 | WARN | Agent/Command 文件名应使用 kebab-case |
| V004 | WARN | Skill 目录名应与 `name` 字段一致 |
| V005 | INFO | 建议添加 `_index.json` 索引文件 |

### 7.2 内容验证

| 规则 | 级别 | 描述 |
|------|------|------|
| C001 | ERROR | Description 不能为空 |
| C002 | WARN | Description 应包含使用场景 |
| C003 | WARN | SKILL.md 不应超过 500 行 |
| C004 | INFO | 建议包含示例用法 |
| C005 | INFO | 脚本应有执行权限 |

### 7.3 依赖验证

| 规则 | 级别 | 描述 |
|------|------|------|
| D001 | ERROR | 引用的文件必须存在 |
| D002 | WARN | 避免循环引用 |
| D003 | INFO | 外部依赖应在 manifest 中声明 |

## 八、最佳实践

### 8.1 命名规范

```
# 文件和目录
kebab-case.md           # 文件名
kebab-case/             # 目录名

# YAML 字段
name: kebab-case        # 标识符
description: "..."       # 句子格式，首字母大写

# 变量
$ARGUMENTS              # 大写下划线
```

### 8.2 文档编写

```markdown
# 标题层级
# H1 - 仅用于文档标题
## H2 - 主要章节
### H3 - 子章节
#### H4 - 细节段落

# 列表
- 使用无序列表描述并列项
1. 使用有序列表描述步骤

# 代码
`inline code` 用于短代码
```language
code block 用于长代码
```

### 8.3 渐进式披露

```
Level 1: Metadata (始终加载)
├── name
└── description (~100 words)

Level 2: SKILL.md Body (触发时加载)
└── Main content (<500 lines)

Level 3: Resources (按需加载)
├── references/    # Claude 判断需要时读取
├── scripts/       # 执行时加载
└── assets/        # 输出时使用
```

### 8.4 测试策略

```python
# tests/test_agents.py
def test_agent_frontmatter():
    """Validate all agent files have required frontmatter."""

def test_agent_tools_valid():
    """Validate all declared tools are recognized."""

# tests/test_skills.py
def test_skill_structure():
    """Validate skill directory structure."""

def test_skill_references_exist():
    """Validate all referenced files exist."""
```

## 九、迁移计划

### 9.1 从当前结构迁移

```bash
# Phase 1: 创建分类目录结构
mkdir -p .claude/agents/{code,screenshot,test}
mkdir -p docs scripts

# Phase 2: 移动并重命名代理文件
mv .claude/agents/code-*.md .claude/agents/code/
mv .claude/agents/screenshot-*.md .claude/agents/screenshot/
mv .claude/agents/test-*.md .claude/agents/test/

# Phase 3: 创建索引文件
# 生成 _index.json

# Phase 4: 添加 manifest.json

# Phase 5: 验证和测试
hca validate --strict
```

### 9.2 兼容性考虑

| 版本 | 变更 | 兼容性 |
|------|------|--------|
| 1.x | 当前结构 | 基准 |
| 2.0 | 分类目录 | 向后兼容 (flat fallback) |
| 2.1 | manifest.json | 向后兼容 (可选) |
| 3.0 | 强制分类 | 需要迁移 |

## 十、未来扩展

### 10.1 插件注册表

```yaml
# 未来支持插件发布到中央注册表
hca publish
hca search "code review"
hca install notedit/happy-coding-agent
```

### 10.2 插件组合

```yaml
# 支持依赖其他插件
dependencies:
  plugins:
    - name: "base-tools"
      version: "^1.0"
```

### 10.3 钩子系统

```yaml
# 支持生命周期钩子
hooks:
  pre-install: "scripts/check-deps.sh"
  post-install: "scripts/setup.sh"
  pre-command: "scripts/validate-context.sh"
```

## 十一、总结

本设计方案提供了：

1. **清晰的目录结构** - 分层组织，职责明确
2. **标准化的文件规范** - 统一的格式和元数据
3. **完整的 CLI 工具** - 部署、验证、打包一体化
4. **渐进式迁移路径** - 保持向后兼容
5. **未来扩展能力** - 注册表、组合、钩子

通过遵循此方案，项目将具备：
- 更好的可维护性
- 更清晰的组件发现
- 更可靠的质量保证
- 更便捷的分发部署
