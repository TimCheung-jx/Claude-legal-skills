---
name: law-overview-chart
description: "Generate a visual overview chart for Chinese laws and regulations. Trigger this skill when the user wants to: create a summary/overview chart of a law (法律法规概览图), visualize law structure by chapters and articles, make a law cheat sheet, or when they mention any Chinese law name like 《广告法》《消费者权益保护法》《网络安全法》《劳动法》etc. Also trigger when user pastes full text of a law and asks for visualization, summary by chapters, or structural overview."
---

# 法律法规概览图生成

## 目标
将一部法律法规转化为一张结构清晰、视觉美观的概览图（HTML 页面），方便用户浏览、截图保存或打印。

## 输入方式
用户可能以两种方式提供法律：
1. **只给法律名称**（如「帮我做张《广告法》概览图」）
2. **粘贴全文**（如「这是《XX法》全文，帮我做概览图」+ 大段文本）

## 工作流

### Step 1: 获取法律全文
- 如果用户已贴全文 → 直接跳到 Step 2
- 如果只给名称 → 使用 WebSearch 搜索该法律的完整条文
  - 搜索关键词：`《法律名称》全文 site:gov.cn` 或 `《法律名称》全文`
  - 优先使用国家法律法规数据库（flk.npc.gov.cn）或北大法宝等权威来源
  - 获取到全文后，继续 Step 2

### Step 2: 解析法律结构
从全文中提取以下信息，整理为 JSON 格式：

```json
{
  "law_name": "广告法",
  "chapters": [
    {
      "title": "第一章 总则",
      "articles": [
        {"number": 1, "topic": "立法目的", "highlight": false},
        {"number": 2, "topic": "适用范围", "highlight": false},
        {"number": 3, "topic": "广告定义", "highlight": false}
      ]
    },
    {
      "title": "第二章 广告内容准则",
      "articles": [
        {"number": 8, "topic": "基本要求", "highlight": false},
        {"number": 9, "topic": "禁止性规定", "highlight": true},
        {"number": 10, "topic": "未成年人保护", "highlight": false}
      ]
    }
  ]
}
```

**解析规则：**
- 识别 `第[一二三四五六七八九十百千]+章` 或 `第\d+章` 作为章节分隔
- 识别 `第\d+条` 作为条款
- 每条提取「条号」和「核心主题词」（2-6 个汉字，概括该条核心内容）
- 如果某条内容明显是「禁止/不得/严禁」→ `highlight: true`
- 如果某条是「法律责任/处罚/罚款」→ `highlight: true`
- 如果某条是「应当/必须/义务」→ `highlight: true`（也可视情况设为次重点，由脚本处理）

### Step 3: 生成概览图 HTML
调用配套脚本生成 HTML 文件：

```bash
python /Users/timcheung/.myagents/projects/Nikita/.claude/skills/law-overview-chart/scripts/generate_chart.py <input_json> <output_html>
```

脚本会自动：
- 按章节分区，每章一个色块区域
- 每条一个圆角卡片，显示「条号 + 主题词」
- 重点条款（highlight=true）用红色卡片
- 计算布局，确保美观均衡
- 添加打印优化 CSS（适合 A4 / 横屏截图）

### Step 4: 交付
- 告知用户 HTML 文件路径
- 提示：「用浏览器打开后，可按 Ctrl+P 打印为 PDF，或用系统截图工具保存为图片」
- 如果用户需要调整（如改颜色、加条款），直接修改 JSON 重新生成

## HTML 设计规范

### 配色方案（参考《广告法》概览图）
- **页面背景**：浅蓝渐变 `#e3f2fd → #bbdefb`
- **章节区域背景**：白色半透明 `rgba(255,255,255,0.7)` + 轻微阴影
- **普通卡片**：白色 `#ffffff`，深色文字 `#2c3e50`
- **重点卡片（禁止/处罚）**：红色 `#e74c3c`，白色文字
- **次重点卡片（义务/应当）**：橙色 `#e67e22`，白色文字
- **章节标题**：深蓝 `#1565c0`，加粗

### 布局规则
- 每章一个区域（section），区域内用 CSS Grid 排列卡片
- 卡片大小：根据每章条款数量自动调整列数
  - ≤6 条：3 列
  - 7-12 条：4 列
  - 13-20 条：5 列
  - >20 条：6 列
- 卡片间距：12px
- 区域间距：24px
- 页面最大宽度：1400px，居中

### 字体
- 标题：系统默认无衬线字体，加粗
- 卡片文字：14px，居中
- 条号：12px，半透明

## 示例

**用户输入：**
> 帮我做一张《广告法》概览图

**执行过程：**
1. WebSearch 搜索「《广告法》全文」
2. 解析出 6 章 74 条的结构
3. 标记第 9 条（禁止性规定）、第 15 条（禁售商品）、第 34 条（审核责任）等为重点
4. 生成 `广告法概览图.html`

**输出：**
> 已生成《广告法》概览图：`/path/to/广告法概览图.html`
> 
> 用浏览器打开后可直接截图保存。重点条款已用红色标出（禁止性规定、法律责任等）。

## 注意事项
- 如果法律条文过长（如超过 200 条），建议只展示「章 + 重点条」，避免页面过长
- 如果某些章节条款极少（如附则只有 2 条），可与其他小章节合并显示
- 主题词尽量简洁，如果某条内容复杂，可提取多个关键词用顿号分隔（如「虚假广告/赔偿责任」）
