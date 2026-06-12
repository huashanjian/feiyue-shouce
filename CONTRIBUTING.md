# 贡献指南

飞跃手册第一版以 Markdown 为主，使用 YAML frontmatter 记录元数据。当前阶段优先搭好公开内容骨架，不要求贡献者一次写成长文。

## 投稿入口

- 完整经历：[如何提交案例](docs/cases/how-to-contribute.md)
- 案例格式：[案例模板](docs/cases/templates/case-template.md)
- 局部经验：进入对应板块的 `perspectives/` 目录，先阅读该目录的 `how-to-contribute.md`
- 通用模板：[投稿模板](docs/commons/templates/index.md)
- 注册表：[共用注册表](docs/commons/registries/index.md)
- 贡献规则：[治理说明](docs/commons/governance/contribution-rules.md)

## 文件命名

个人观点、经验复盘和署名材料统一使用：

```text
[year]-[name-or-alias]-[topic].md
```

如果作者匿名，文件名使用化名或主题，不使用真实姓名。复杂案例可以使用文件夹页面，例如 `docs/cases/entries/[case-id]/index.md`。

## 语言和公式

- 正文：Markdown
- 元数据：YAML frontmatter
- 行内公式：`$a^2+b^2=c^2$`
- 块级公式：`$$E = mc^2$$`

第一版不把完整 `.tex` 文件作为内容源。

## 提交流程

1. 找到最接近的目录；不确定时先放到 `cases/` 或对应 `perspectives/`。
2. 复制合适模板，补齐 frontmatter 和基本段落。
3. 更新所在目录的 `index.md`，让读者能找到新页面。
4. 提交 PR，并在 PR 模板里确认脱敏、署名和公开转载边界。

## Commit 规范

使用 `type(scope): summary`：

- `content`：新增或大幅改写正文内容
- `case`：新增或修改莞中人样本
- `index`：更新索引页、目录页、链接列表
- `structure`：调整目录结构
- `style`：视觉、CSS、排版
- `fix`：修错别字、坏链接、格式错误或事实错误
- `chore`：工具、依赖、配置、维护性改动

## PR 拆分和合并

请尽量把内容、目录结构、视觉样式、导航配置分成不同 PR。维护者默认使用 squash merge，让主分支历史保持为一组清晰的主题提交；如果某个 PR 本身需要保留多个有意义的提交，请在 PR 描述中说明。

第一版暂不上 commitlint，先用文档约束 commit message，避免把外部贡献者挡在工具链外。

## 公开转载

合并到飞跃手册主站的公开内容，未来可能被莞言瓜语转载、摘编、排版或二次传播；维护者会尊重作者署名、匿名和脱敏约定。
