# SyncVoice Landing Page 设计文档

**日期**：2025-01-03
**状态**：已确认

---

## 概述

### 产品信息
- **产品名称**：SyncVoice
- **Tagline**：实时 AI 同声传译，让沟通零距离
- **产品类型**：AI 实时翻译工具
- **目标用户**：企业客户（需要国际会议、商务谈判翻译的企业）
- **页面目标**：获取注册/试用

### 核心差异化优势
1. 超低延迟 - 毫秒级响应，接近实时的翻译体验
2. 高精准度 - 基于大语言模型，专业术语翻译准确
3. 多语言支持 - 支持 50+ 语言，开箱即用
4. 企业级安全 - 数据加密、SOC2/GDPR 合规

---

## 品牌定义

### 视觉风格
- **主色调**：深灰 `#1a1a1a` + 纯白 `#ffffff`
- **强调色**：亮绿 `#22c55e`
- **字体**：Inter（英文）+ 系统中文字体
- **设计语言**：大量留白、清晰层次、无装饰元素

### 情绪板关键词
清晰、高效、专业、现代

---

## 页面结构

```
┌─────────────────────────────────────┐
│  Navigation (固定顶部)              │
├─────────────────────────────────────┤
│  Hero Section                       │
├─────────────────────────────────────┤
│  Trust Bar (客户 Logo 墙)           │
├─────────────────────────────────────┤
│  Features (4个核心功能卡片)         │
├─────────────────────────────────────┤
│  How It Works (3步流程)             │
├─────────────────────────────────────┤
│  Testimonials (客户评价轮播)        │
├─────────────────────────────────────┤
│  Pricing (3个定价方案)              │
├─────────────────────────────────────┤
│  CTA Section (最终转化)             │
├─────────────────────────────────────┤
│  Footer                             │
└─────────────────────────────────────┘
```

---

## 组件详细设计

### 1. Navigation

固定顶部导航栏：
- 左侧：Logo (SyncVoice)
- 右侧：功能 | 价格 | 案例 | [免费试用] 按钮
- 滚动时添加背景模糊效果

### 2. Hero Section

**布局**：左文右图，桌面端 50/50，移动端上下堆叠

**左侧内容**：
```
[小标签] AI 驱动的企业级翻译

# 实时同传，毫秒响应
## 让每一场国际会议都畅通无阻

SyncVoice 为企业提供 AI 实时翻译，支持 50+ 语言，
延迟低于 500ms，专业术语准确率达 98%。

[████ 免费试用 14 天 ████]   [观看演示 ▶]

✓ 无需信用卡  ✓ 5分钟完成部署  ✓ 企业级数据安全
```

**右侧**：产品演示 UI 模拟
- 音频波形 + 原文显示
- 翻译结果带打字机动画
- 语言切换器

### 3. Trust Bar

灰色背景条，展示客户 Logo：
```
已服务 500+ 企业 | [Logo] [Logo] [Logo] [Logo] [Logo] [Logo]
```
- 6-8 个企业 Logo，灰色处理
- Hover 时恢复彩色

### 4. Features Section

**标题**：为什么选择 SyncVoice？

**4 个功能卡片** (2x2 网格)：

| 图标 | 标题 | 描述 |
|------|------|------|
| ⚡ | 超低延迟 | <500ms 端到端延迟，让对话自然流畅 |
| 🎯 | 专业级精准 | 98% 专业术语准确率，垂直领域深度优化 |
| 🌍 | 50+ 语言支持 | 覆盖全球主流语言，开箱即用 |
| 🔒 | 企业级安全 | 端到端加密、SOC2 认证、GDPR 合规 |

**卡片样式**：
- 白色背景 + 细边框 `border: 1px solid #e5e5e5`
- Hover 时上浮 + 阴影加深

### 5. How It Works

**标题**：3 步开始使用

水平时间线，三个步骤：
1. **注册账号** - 填写企业信息，获取 API 密钥
2. **接入会议** - 支持 Zoom、Teams 或自有系统
3. **实时翻译** - 参会者选择语言，即刻开始

移动端改为垂直布局。

### 6. Testimonials

**标题**：客户怎么说

3 张评价卡片，可滑动：
- 大引号装饰背景
- 评价内容居中
- 头像 + 姓名 + 职位公司
- 分页指示器

### 7. Pricing

**标题**：选择适合你的方案

| Starter | Pro (推荐) | Enterprise |
|---------|-----------|------------|
| ¥999/月 | ¥2,999/月 | 联系我们 |
| 10 小时/月 | 50 小时/月 | 无限时长 |
| 10 种语言 | 50+ 语言 | 全部语言 |
| 邮件支持 | 优先支持 | 专属客服 |
| 基础 API | 完整 API + 录制 | 私有化部署 |

Pro 方案突出显示：绿色边框 + "最受欢迎" 标签

### 8. CTA Section

深色背景 (`#1a1a1a`)：
```
准备好让沟通跨越语言障碍了吗？
免费试用 14 天，无需信用卡
[立即开始]
```

### 9. Footer

4 列布局：
- 品牌信息 + 版权
- 产品：功能介绍、价格方案、客户案例
- 资源：帮助中心、API 文档、状态页
- 公司：关于、博客、联系
- 社交媒体图标

---

## 技术方案

### 技术栈
| 层面 | 选型 |
|------|------|
| 框架 | Next.js 14 (App Router) |
| 样式 | Tailwind CSS + CSS Variables |
| 动画 | Framer Motion |
| 图标 | Lucide Icons |
| 字体 | Inter (Google Fonts) |
| 部署 | Vercel |

### 项目结构
```
src/
├── app/
│   ├── layout.tsx
│   ├── page.tsx
│   └── globals.css
├── components/
│   ├── Navbar.tsx
│   ├── Hero.tsx
│   ├── TrustBar.tsx
│   ├── Features.tsx
│   ├── HowItWorks.tsx
│   ├── Testimonials.tsx
│   ├── Pricing.tsx
│   ├── CTA.tsx
│   └── Footer.tsx
└── lib/
    └── constants.ts
```

---

## Implementation Tasks

- [ ] **初始化 Next.js 项目** `priority:1` `phase:setup` `time:10min`
  - files: package.json, tailwind.config.ts, src/app/layout.tsx, src/app/globals.css
  - [ ] Step 1: 运行 create-next-app 初始化项目
  - [ ] Step 2: 配置 Tailwind CSS 主题色和字体
  - [ ] Step 3: 安装 framer-motion 和 lucide-react
  - [ ] Step 4: 验证开发服务器运行正常
  - [ ] Step 5: Commit

- [ ] **创建常量和类型定义** `priority:2` `phase:setup` `time:5min`
  - files: src/lib/constants.ts
  - [ ] Step 1: 定义颜色、导航链接、功能列表等常量
  - [ ] Step 2: 验证 TypeScript 类型正确
  - [ ] Step 3: Commit

- [ ] **实现 Navbar 组件** `priority:3` `phase:ui` `time:15min`
  - files: src/components/Navbar.tsx
  - [ ] Step 1: 创建基础导航栏结构
  - [ ] Step 2: 添加 Logo 和导航链接
  - [ ] Step 3: 实现固定定位和滚动模糊效果
  - [ ] Step 4: 添加移动端汉堡菜单
  - [ ] Step 5: Commit

- [ ] **实现 Hero 组件** `priority:4` `phase:ui` `time:20min`
  - files: src/components/Hero.tsx
  - [ ] Step 1: 创建左右分栏布局
  - [ ] Step 2: 实现左侧文案和 CTA 按钮
  - [ ] Step 3: 创建右侧产品演示模拟 UI
  - [ ] Step 4: 添加打字机动画效果
  - [ ] Step 5: 实现响应式布局
  - [ ] Step 6: Commit

- [ ] **实现 TrustBar 组件** `priority:5` `phase:ui` `time:10min`
  - files: src/components/TrustBar.tsx
  - [ ] Step 1: 创建灰色背景条布局
  - [ ] Step 2: 添加占位 Logo 图标
  - [ ] Step 3: 实现 hover 彩色效果
  - [ ] Step 4: Commit

- [ ] **实现 Features 组件** `priority:6` `phase:ui` `time:15min`
  - files: src/components/Features.tsx
  - [ ] Step 1: 创建标题区域
  - [ ] Step 2: 实现 2x2 网格卡片布局
  - [ ] Step 3: 添加图标和内容
  - [ ] Step 4: 实现 hover 动效
  - [ ] Step 5: Commit

- [ ] **实现 HowItWorks 组件** `priority:7` `phase:ui` `time:15min`
  - files: src/components/HowItWorks.tsx
  - [ ] Step 1: 创建标题区域
  - [ ] Step 2: 实现水平时间线布局
  - [ ] Step 3: 添加三个步骤内容
  - [ ] Step 4: 实现移动端垂直布局
  - [ ] Step 5: Commit

- [ ] **实现 Testimonials 组件** `priority:8` `phase:ui` `time:15min`
  - files: src/components/Testimonials.tsx
  - [ ] Step 1: 创建评价卡片组件
  - [ ] Step 2: 实现轮播/滑动功能
  - [ ] Step 3: 添加分页指示器
  - [ ] Step 4: Commit

- [ ] **实现 Pricing 组件** `priority:9` `phase:ui` `time:20min`
  - files: src/components/Pricing.tsx
  - [ ] Step 1: 创建三列定价卡片布局
  - [ ] Step 2: 实现 Pro 方案高亮样式
  - [ ] Step 3: 添加功能列表和 CTA 按钮
  - [ ] Step 4: 实现响应式堆叠布局
  - [ ] Step 5: Commit

- [ ] **实现 CTA 组件** `priority:10` `phase:ui` `time:10min`
  - files: src/components/CTA.tsx
  - [ ] Step 1: 创建深色背景区块
  - [ ] Step 2: 添加文案和按钮
  - [ ] Step 3: 实现 hover 效果
  - [ ] Step 4: Commit

- [ ] **实现 Footer 组件** `priority:11` `phase:ui` `time:15min`
  - files: src/components/Footer.tsx
  - [ ] Step 1: 创建四列布局
  - [ ] Step 2: 添加链接和社交图标
  - [ ] Step 3: 实现响应式布局
  - [ ] Step 4: Commit

- [ ] **组装首页** `priority:12` `phase:ui` `time:10min`
  - files: src/app/page.tsx
  - [ ] Step 1: 导入所有组件
  - [ ] Step 2: 按顺序组装页面
  - [ ] Step 3: 验证整体效果
  - [ ] Step 4: Commit

- [ ] **添加页面动画** `priority:13` `phase:ui` `time:15min`
  - files: src/components/*.tsx
  - [ ] Step 1: 添加滚动进入动画
  - [ ] Step 2: 优化各组件过渡效果
  - [ ] Step 3: 验证动画性能
  - [ ] Step 4: Commit

- [ ] **SEO 和元数据优化** `priority:14` `phase:docs` `time:10min`
  - files: src/app/layout.tsx, src/app/page.tsx
  - [ ] Step 1: 添加 metadata 配置
  - [ ] Step 2: 添加 Open Graph 标签
  - [ ] Step 3: Commit
