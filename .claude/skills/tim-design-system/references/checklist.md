# 质量检查清单

> 做完设计后逐条对照。P0必须全过，否则打回修改。

---

## P0（必须全过）

任何一条不过就要改：

- [ ] 品牌三色使用正确（藏蓝50/暖橘30/草绿20比例）
- [ ] 没有使用禁忌清单里的任何元素（大红大紫/过量动画/花哨边框/glassmorphism/neon）
- [ ] 背景使用暖底（#f5f2ed），非纯黑纯白
- [ ] 字体用了推荐字体池里的（ZCOOL XiaoWei/Caveat/Noto Sans SC）
- [ ] 标题手写体+正文无衬线混搭
- [ ] 有响应式（至少900px断点）
- [ ] 整体干净素雅、有呼吸感
- [ ] 每个section布局形式不同
- [ ] clamp()做fluid sizing
- [ ] 没有使用任何HTML默认样式（默认blockquote、默认border-left引用、无样式ul/ol、默认table）——所有组件必须从components.md选用

---

## P1（应过）

尽量满足，提升品质：

- [ ] 留白充足，不拥挤
- [ ] 有克制的Scroll Reveal动效 + stagger延迟
- [ ] ::selection用暖橘高亮
- [ ] 卡片hover有微妙的反馈
- [ ] 色值在品牌色系内，不引入新颜色

---

## P2（加分）

锦上添花：

- [ ] 配图有暖调滤镜或自然感
- [ ] 手写装饰字（Caveat）点缀
- [ ] 装饰元素克制使用
- [ ] prefers-reduced-motion尊重
