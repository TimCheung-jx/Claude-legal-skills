# Claude Legal Skills | Claude 法律技能集

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://openclaw.ai)
[![Hermes](https://img.shields.io/badge/Hermes-Compatible-green)](https://github.com/TimCheung-jx)

> **English**: A collection of Claude's standard legal skills, adapted for Chinese legal practice, compliance with Chinese laws and regulations, and suitable for Chinese legal research and retrieval.
>
> **中文**: 基于 Claude 标准法律技能改造的技能集合，适用于中国法律法规、中国律师执业规则，适合中国法律研究和检索，可被 OpenClaw 和 Hermes 等 Agent 安装使用。

---

## Overview | 概述

This repository contains a curated collection of legal skills originally developed by [Anthropic's Claude for Legal](https://github.com/anthropics/claude-for-legal), adapted and localized for Chinese legal practice.

本仓库包含一系列基于 [Anthropic Claude for Legal](https://github.com/anthropics/claude-for-legal) 开发的法律技能，经过本土化改造，适用于中国法律实践。

### Key Adaptations | 关键改造

- **Legal Framework | 法律框架**: Adapted from US/Common Law to Chinese Civil Law system | 从英美法系适配到中国民法体系
- **Regulatory Compliance | 监管合规**: Aligned with Chinese regulations and industry standards | 符合中国监管规定和行业标准
- **Practice Rules | 执业规则**: Conforms to Chinese lawyer practice norms | 符合中国律师执业规范
- **Research Methods | 研究方法**: Optimized for Chinese legal research and case retrieval | 针对中国法律研究和案例检索优化
- **Language | 语言**: Bilingual Chinese-English support | 中英双语支持

---

## Skills Included | 包含技能

### Core Legal Skills | 核心法律技能

| Skill | Description | 描述 |
|-------|-------------|------|
| **law-overview-chart** | Legal research framework and methodology | 法律研究框架与方法论 |
| **client-intake** | Client intake and case onboarding | 客户接待与案件受理 |
| **client-letter** | Legal correspondence drafting | 法律函件起草 |
| **client-comms-log** | Client communication tracking | 客户沟通记录 |
| **research-start** | Legal research initiation | 法律研究启动 |
| **memo** | Legal memo drafting | 法律备忘录撰写 |
| **draft** | Document drafting assistant | 文书起草助手 |
| **deadlines** | Case deadline management | 案件期限管理 |
| **status** | Case status tracking | 案件状态跟踪 |
| **supervisor-review-queue** | Work product review workflow | 工作成果审核流程 |
| **semester-handoff** | Case handover protocols | 案件交接协议 |
| **cold-start-interview** | Initial client interview | 初次客户访谈 |
| **ramp** | New matter ramp-up | 新事项启动 |
| **build-guide** | Legal work product standards | 法律工作成果标准 |
| **customize** | Skill customization guide | 技能定制指南 |

### Specialized Skills | 专业技能

| Skill | Description | 描述 |
|-------|-------------|------|
| **law-overview-chart** | Visual legal framework mapping | 可视化法律框架图谱 |

---

## Installation | 安装

### For OpenClaw | OpenClaw 安装

```bash
# Install entire skill collection
openclaw skills install TimCheung-jx/Claude-legal-skills

# Or install individual skills
openclaw skills install TimCheung-jx/Claude-legal-skills/client-intake
openclaw skills install TimCheung-jx/Claude-legal-skills/legal-memo
```

### For Hermes | Hermes 安装

```bash
# Clone the repository
git clone https://github.com/TimCheung-jx/Claude-legal-skills.git

# Copy skills to Hermes skills directory
cp -r Claude-legal-skills/.claude/skills/* ~/.hermes/skills/
```

### Manual Installation | 手动安装

```bash
# Clone repository
git clone https://github.com/TimCheung-jx/Claude-legal-skills.git

# Copy to your agent's skills directory
cp -r Claude-legal-skills/.claude/skills/* ~/.openclaw/workspace/skills/
```

---

## Usage | 使用

Each skill follows the standard Claude skill format with Chinese localization:

每个技能遵循标准 Claude 技能格式，并进行中文本地化：

```yaml
---
name: skill-name
description: |
  中文描述：说明技能用途
  English: Description of skill purpose
---

# Skill content in bilingual format | 双语格式的技能内容
```

### Example | 示例

**Input | 输入:**
```
/client-intake
客户：张三
案件类型：合同纠纷
争议金额：100万元
```

**Output | 输出:**
```
【案件受理记录】

客户信息：张三
案件类型：合同纠纷
争议标的：100万元

【初步分析】
根据《民法典》合同编相关规定...

【下一步行动】
1. 收集合同文本及相关证据
2. 分析违约事实及责任
3. 评估诉讼/仲裁可行性
```

---

## Skill Structure | 技能结构

```
Claude-legal-skills/
├── .claude/
│   └── skills/
│       ├── client-intake/          # 客户接待
│       ├── client-letter/          # 法律函件
│       ├── client-comms-log/       # 沟通记录
│       ├── research-start/         # 研究启动
│       ├── memo/                   # 法律备忘录
│       ├── draft/                  # 文书起草
│       ├── deadlines/              # 期限管理
│       ├── status/                 # 状态跟踪
│       ├── supervisor-review-queue/# 审核流程
│       ├── semester-handoff/       # 案件交接
│       ├── cold-start-interview/   # 初次访谈
│       ├── ramp/                   # 事项启动
│       ├── build-guide/            # 成果标准
│       ├── customize/              # 定制指南
│       └── law-overview-chart/     # 法律框架
├── README.md
└── LICENSE
```

---

## Localization Notes | 本地化说明

### Legal Framework Adaptation | 法律框架适配

| Original (US) | Adapted (China) | 说明 |
|--------------|-----------------|------|
| Case Law | Guiding Cases | 指导性案例 |
| Statutory Law | Laws & Regulations | 法律法规 |
| Federal/State | Central/Local | 中央/地方 |
| Bar Association | 律师协会 | All-China Lawyers Association |
| Attorney-Client Privilege | 律师保密义务 | 律师法第38条 |

### Research Sources | 研究来源

- **Laws | 法律**: 国家法律法规数据库 (https://flk.npc.gov.cn)
- **Cases | 案例**: 中国裁判文书网 (https://wenshu.court.gov.cn)
- **Regulations | 法规**: 国家市场监督管理总局 (https://www.samr.gov.cn)
- **Industry Rules | 行业规范**: 各行业协会规定

---

## Compatibility | 兼容性

| Platform | Status | Notes |
|----------|--------|-------|
| **OpenClaw** | ✅ Fully Supported | Native skill format |
| **Hermes** | ✅ Compatible | Standard skill structure |
| **Claude Desktop** | ⚠️ Partial | May require manual setup |
| **Claude Code** | ⚠️ Partial | CLI commands need adaptation |

---

## Contributing | 贡献

We welcome contributions to improve Chinese legal practice support:

欢迎贡献以改进中国法律实践支持：

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

### Contribution Areas | 贡献领域

- Additional legal skills | 增加法律技能
- Improved localization | 改进本地化
- Case study examples | 案例研究示例
- Documentation translation | 文档翻译

---

## Acknowledgments | 致谢

- Original skills by [Anthropic's Claude for Legal](https://github.com/anthropics/claude-for-legal)
- Adapted for Chinese legal practice by TimCheung-jx
- Inspired by the legal AI community

---

## License | 许可证

MIT License - see [LICENSE](LICENSE) file for details.

---

## Author | 作者

**TimCheung-jx** - [GitHub](https://github.com/TimCheung-jx)

---

## Related Repositories | 相关仓库

| Repository | Description | 描述 |
|------------|-------------|------|
| [ad-compliance-review](https://github.com/TimCheung-jx/ad-compliance-review) | Ad compliance review | 广告合规审查 |
| [trademark-preexam](https://github.com/TimCheung-jx/trademark-preexam) | Trademark pre-examination | 商标预审 |
| [trademark-invalidity-defense](https://github.com/TimCheung-jx/trademark-invalidity-defense) | Trademark invalidity defense | 商标无效答辩 |
| [ecommerce-compliance-guide](https://github.com/TimCheung-jx/ecommerce-compliance-guide) | E-commerce compliance | 电商合规指南 |

---

**Disclaimer | 免责声明**

These skills are for educational and productivity purposes only. They do not constitute legal advice. Always consult qualified legal professionals for specific legal matters.

本技能仅供教育和提高工作效率使用，不构成法律意见。具体法律事务请咨询专业律师。
