# AI Job Search Assistant · AI 求职助手

> 5 步流水线完成求职调研：搜索 → 筛选 → 调研 → 匹配 → 报告

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Claude%20Code-purple)](https://claude.ai/code)

---

## 🎯 这是什么

投简历前最耗时的不是"写简历"——是**调研**。

- 在不同招聘平台搜岗位 → 跳来跳去
- 用 Excel 整理公司信息 → 碎片化严重
- 凭感觉判断"这家值不值得投" → 缺乏标准
- 针对每家改简历、准备面试 → 工作量 × N

**这个 Skill 把"从搜岗位到准备面试"的完整流程压缩成 5 步流水线**，你只需要提供目标岗位、城市偏好和简历 PDF，它帮你完成从搜索到报告的全过程。

---

## 📦 安装

### 前提条件

- 已安装 [Claude Code](https://claude.ai/code)

### 方法一：Git Clone（推荐）

**macOS / Linux：**
```bash
git clone https://github.com/MiaIria/ai-job-search-assistant-skill.git ~/.claude/skills/
```

**Windows (PowerShell)：**
```powershell
git clone https://github.com/MiaIria/ai-job-search-assistant-skill.git $env:USERPROFILE\.claude\skills\
```

### 方法二：手动下载

1. 下载 [ZIP](https://github.com/MiaIria/ai-job-search-assistant-skill/archive/refs/heads/main.zip) 并解压
2. 将解压后的文件夹重命名为 `ai-job-search-assistant-skill`
3. 放入 `~/.claude/skills/`（Windows: `C:\Users\<用户名>\.claude\skills\`）

---

## 🚀 使用方法

在 Claude Code 中输入：

```
/ai-job-search-assistant-skill
```

然后按提示提供 3 项信息：

1. **目标岗位**（如"AI 产品经理"）
2. **城市偏好**（如"北京优先，上海也可"）
3. **个人简历**（PDF 文件）

也可以一次性提供：

```
/ai-job-search-assistant-skill
岗位: AI产品经理
城市: 北京、上海
简历: [上传 PDF]
```

---

## 🏗️ 5 步流水线

```
Step 1: 搜索筛选          → 50 家公司（多渠道聚合 + 城市过滤 + 去重）
    ↓
Step 2: 简历解析 + 匹配评分 → 50 → 20-25 家（100 分量表筛选）
    ↓
Step 3: 深度调研           → 15 家（5 维框架：基础/文化/制度/薪酬/AI团队）
    ↓
Step 4: 匹配分析 + 简历优化 → 8 家优先（STAR 改写 + 面试预测题）
    ↓
Step 5: 最终报告           → 候选人画像 + 公司列表 + 深度报告 + 投递建议 + 附录
```

---

## 📊 100 分匹配量表

Step 2 使用三轴评分筛选公司（避免 LLM 凭"感觉"推荐）：

| 维度 | 分值 | 考察内容 |
|------|------|---------|
| 硬要求匹配 | 30 分 | 学历、年限、必需技能 |
| 经验相关性 | 40 分 | 行业、职能、项目经验 |
| 软性匹配 | 30 分 | 公司阶段、技术栈、成长空间 |

- ≥ 90 分 → 强烈推荐
- 75-89 分 → 推荐
- 60-74 分 → 可行
- < 60 分 → 不推荐

---

## 📂 目录结构

```
ai-job-search-assistant-skill/
├── SKILL.md                ← Skill 定义（5 步流水线完整实现）
├── references/             ← 方法论、评分量表、调研框架、信息源标准
├── scripts/                ← 公司名去重、匹配评分、来源校验辅助脚本
├── README.md               ← 本文件
└── LICENSE                 ← MIT
```

> 这是以 prompt 工程为核心的 Skill。`references/` 用于沉淀方法论，`scripts/` 用于处理去重、评分、来源校验等确定性步骤。

---

## 🧰 辅助脚本

这些脚本不会自动运行，由执行 Skill 的 agent 在合适步骤调用：

```bash
# 标准化并去重公司名单
python scripts/normalize_companies.py companies.txt

# 按 30/40/30 量表计算匹配分
python scripts/score_fit.py --hard 24 --experience 32 --soft 21

# 检查报告里是否包含可追溯来源链接
python scripts/validate_sources.py report.md
```

---

## ⚠️ 质量保证

**必须做到**：

- 信息准确、来源可追溯
- 公司名称标准化、无重复
- 严格排除用户已调研的公司
- 匹配分析客观、有证据支撑
- 简历建议具体、可执行
- 面试准备有针对性

**严禁**：

- 编造公司或招聘信息
- 推荐已排除的公司
- 推荐明显不在目标城市的岗位
- 推荐与目标岗位无关的职位
- 建议简历造假或夸大
- 只挑正面信息，报喜不报忧

---

## 💡 使用场景

- 准备跳槽，想看市场上有什么机会
- 拿到几个 offer，想系统对比
- 对某行业不熟，想快速了解有哪些公司在招 AI 岗位
- 想让简历更有针对性，针对每家偏好做 STAR 改写
- 面试前想准备"你对这家公司了解多少"的回答

---

## 🔄 增量使用

支持传入**已调研公司列表**来排除重复。几天内分多次使用不会重复劳动：

```
/ai-job-search-assistant-skill
岗位: AI产品经理
城市: 深圳
排除: [上次已调研的公司列表]
简历: [PDF]
```

---

## 📄 License

MIT © [MiaIria](https://github.com/MiaIria)
