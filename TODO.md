# 莞中人飞跃手册落地 TODO

> 这份清单用于把当前架构方案真正落到仓库、网站和协作流程里。当前站点尚未真正 build / 上线 / 对外引用，旧 `docs/` 基本没有内容资产价值，所以按“绿地重建”处理：可以直接删除旧 `docs/` 并重写 `mkdocs.yml`。

## 状态说明

- `[ ]` 未开始
- `[~]` 进行中
- `[x]` 已完成
- `P0` 第一版必须完成
- `P1` 第一版上线前最好完成
- `P2` 内容规模起来后再做

## 总原则

- [x] `P0` 所有新路径统一使用英文小写 kebab-case。
- [x] `P0` 直接删除旧 `docs/`，按新架构重建。
- [x] `P0` 直接重写 `mkdocs.yml`，不做旧路径兼容。
- [x] `P0` 第一目标是把新站 build 跑通，不做旧内容迁移。
- [x] `P0` 主站是公开正本，WPS 指北保存群内敏感材料。
- [x] `P0` 公众号不作为技术模块；只在投稿说明中告知公开内容可能被莞言瓜语转载、摘编或二次传播。
- [x] `P0` 每个复杂对象优先文件夹 + `index.md`，不要为了少建目录把复杂主题压成单个 `.md`。
- [x] `P0` `mkdocs.yml` 是读者导航，不是完整文件树。
- [x] `P0` C 类个人贡献默认不逐篇进 `mkdocs.yml`，只更新所在目录的 `index.md`。
- [x] `P0` 不做登录、不做静态站密码页；不公开敏感材料。
- [ ] `P0` 真实 `docs/` 和 `mkdocs.yml` 的重建要单独 PR，避免和设计文档修改混在一起。

## Phase 0：决策确认

### 0.1 仓库与部署

- [x] `P0` 工程主仓使用 GitHub。
  - 验收：仓库、部署、评论、PR 协作均按 GitHub 设计；真实仓库创建后再把 `repo_url` / `repo_name` 填回 `mkdocs.yml`。
- [x] `P1` 暂不配置 Gitee 镜像。
  - 验收：如后续需要，只作为代码镜像，不作为 Pages 发布入口。
- [x] `P0` 第一版部署平台使用 GitHub Pages。
  - 验收：Cloudflare Pages 只作为后续备选方案。
- [ ] `P0` 确认第一版是否使用自有域名。
  - 验收：若不用，TODO 标注为后续；若用，列出域名、备案、DNS、证书责任人。
- [ ] `P1` 确认是否需要国内访问加速。
  - 验收：如果需要，单独评估 CDN / OSS / CloudBase，不阻塞第一版骨架。

### 0.2 评论系统

- [x] `P0` 第一版评论系统使用 giscus + GitHub Discussions。
- [x] `P0` GitHub 仓库开启 Discussions。
- [x] `P0` 安装 giscus app。
- [x] `P0` 创建评论分类。
  - 建议：`Comments` 或 `General`。
- [x] `P0` giscus 使用 `pathname` 映射。
  - 验收：页面标题变化不影响评论归属。
- [x] `P0` 评论默认全站开启。
- [x] `P0` 支持通过 frontmatter `comments: false` 关闭单页评论。
- [x] `P0` 明确投稿说明、隐私边界、治理规则等页面可以关闭评论。
- [x] `P0` 评论治理规则写入贡献说明或评论说明页。

### 0.3 内容语言

- [x] `P0` 主内容格式使用 Markdown。
- [x] `P0` 页面元数据使用 YAML frontmatter。
- [x] `P0` 支持 Markdown 内 LaTeX 数学公式。
- [x] `P0` 在 `mkdocs.yml` 中启用 `pymdownx.arithmatex`。
- [x] `P0` 在 `mkdocs.yml` 中引入 MathJax。
- [x] `P0` 写一个公式渲染测试页面或在首页留一个隐藏检查片段。
- [x] `P0` 不支持整篇 `.tex` 作为内容源。

### 0.4 公开边界

- [x] `P0` 确认 WPS 指北和飞跃手册主站的边界文案。
  - 验收：首页、投稿说明、案例模板里的公开/私密边界一致。
- [x] `P0` 确认公开转载告知的固定文案。
  - 建议文案：`合并到飞跃手册主站的公开内容，未来可能被莞言瓜语转载、摘编、排版或二次传播；维护者会尊重作者署名、匿名和脱敏约定。`
  - 验收：PR 模板、案例模板、投稿说明均使用同一语义。
- [x] `P0` 确认匿名作者展示格式。
  - 示例：`20xx 届 匿名校友`、`20xx 届 某理工科校友`。
  - 验收：案例模板里有明确字段。
- [x] `P0` 确认哪些信息永远不进公开仓库。
  - 至少包括：具体个人负面评价、未经证实传闻、群内敏感内幕、未授权聊天记录、隐私联系方式。

### 0.5 第一版范围

- [x] `P0` 确认第一版只做骨架 + 模板 + 少量示例，不追求全目录填满。
- [x] `P0` 确认第一版必有一级目录：
  - `start-here/`
  - `admissions/`
  - `majors/`
  - `universities/`
  - `campus-life/`
  - `pathways/`
  - `cases/`
  - `commons/`
- [x] `P0` 确认绿地重建策略：旧 `docs/` 可直接删除，不做迁移前置工作。
- [x] `P0` 确认第一版不做旧路径重定向。
  - 验收：因为尚未上线，第一版不引入 `mkdocs-redirects`。

## Phase 1：工程基础

### 1.1 Python 与依赖

- [x] `P0` 新建 `requirements.txt`。
  - 包含：`mkdocs-material`、`pymdown-extensions`。`mkdocs-git-revision-date-localized-plugin` 暂不启用，避免第一版未提交页面触发构建不稳定。
  - 验收：`pip install -r requirements.txt` 成功。
- [x] `P0` 在 README 或贡献说明中写本地启动命令。
  - Windows：`.venv\Scripts\activate`
  - macOS/Linux：`source .venv/bin/activate`
  - 通用：`mkdocs serve`
- [x] `P0` 本地跑通 `mkdocs build --strict`。
  - 验收：命令退出码为 0。
- [x] `P1` 记录 Python 版本建议。
  - 建议：Python 3.11+。
- [ ] `P1` 如果依赖版本出现不稳定，锁定主要依赖版本。

### 1.2 MkDocs 配置

- [x] `P1` 真实 GitHub 仓库创建后，更新 `mkdocs.yml` 的 `repo_url` 和 `repo_name`。
  - 验收：指向 GitHub 主仓。
- [x] `P1` 真实 GitHub 仓库创建后，更新 `edit_uri`。
  - 验收：页面上的编辑链接能打开正确仓库路径。
- [x] `P0` 设置 `theme.custom_dir: docs/overrides`。
  - 验收：giscus comments partial 能被 MkDocs Material 加载。
- [x] `P0` 将 theme palette 从默认 indigo 调整为符合 `DESIGN.md` 的暖纸色/墨蓝体系。
- [x] `P0` 保留 MkDocs Material，不引入独立前端框架。
- [x] `P0` 保留中文搜索和导航能力。
- [x] `P0` 开启或确认以下功能：
  - `navigation.sections`
  - `navigation.indexes`
  - `navigation.top`
  - `search.highlight`
  - `toc.permalink`
- [x] `P1` 评估是否需要：
  - `navigation.tabs`
  - `navigation.footer`
  - `content.action.edit`
  - `content.code.copy`
- [x] `P0` 重建 `nav`，只使用新英文目录。
  - 验收：`mkdocs.yml` 不再引用 `zhuanye/`、`yuanxiao/`、`zhiyuan/`、`zaixiao/`、`shenzao/`、`qiuzhi/`、`fulu/`。
- [x] `P0` C 类容器在 nav 中只列 `index.md`。

### 1.3 评论基础

- [x] `P0` 创建 `docs/overrides/partials/comments.html`。
- [x] `P0` comments partial 使用 giscus。
- [x] `P0` comments partial 用 `{% if page.meta.comments is not false %}` 控制显示。
- [x] `P0` giscus 配置项包括：
  - `data-repo`
  - `data-repo-id`
  - `data-category`
  - `data-category-id`
  - `data-mapping="pathname"`
  - `data-reactions-enabled="1"`
  - `data-input-position="bottom"`
  - `data-lang="zh-CN"`
- [x] `P0` 支持明暗主题切换时同步 giscus 主题。
- [x] `P0` 默认页面不需要写 `comments: true`。
- [x] `P0` 不适合评论的页面写 `comments: false`。

### 1.4 视觉基础

- [x] `P0` 新建或更新 `docs/stylesheets/extra.css`。
- [x] `P0` 实现 `DESIGN.md` 中的基础色彩：
  - `paper-bg`
  - `paper-surface`
  - `ink-main`
  - `ink-muted`
  - `ink-blue`
  - `line-warm`
  - `soft-green`
  - `soft-red`
- [x] `P0` 设置中文正文宽度和行距。
  - 验收：桌面端长文不铺满全屏；移动端不挤。
- [x] `P0` 设置链接颜色和 hover 状态。
- [x] `P0` 设置表格样式，避免默认表格太硬。
- [x] `P0` 设置 blockquote / admonition 的纸感样式。
- [x] `P0` 设置案例引用样式。
- [x] `P1` 准备 logo 或文字标识。
  - 落点：`docs/assets/logo/`。
- [ ] `P1` 准备默认 OG 图片。
  - 落点：`docs/assets/og/`。
- [x] `P1` 检查移动端显示。
  - 验收：360px 宽度下标题、导航、表格不明显溢出。

### 1.4 Git 协作设置

- [x] `P0` 新建 `CONTRIBUTING.md`。
  - 包含：投稿入口、公开转载告知、commit 规范、PR 拆分规则、脱敏规则。
- [x] `P0` 新建 PR 模板。
  - 路径：`.github/pull_request_template.md`。
- [x] `P0` PR 模板包含：
  - 改动类型
  - 涉及目录
  - 是否新增公开内容
  - 是否涉及个人经历
  - 是否已脱敏
  - 是否接受公开转载告知
  - 本地检查结果
- [x] `P0` 新建 issue 模板或投稿建议模板。
  - 路径：`.github/ISSUE_TEMPLATE/`。
- [x] `P0` 写入 commit message 规范：
  - `content(scope): summary`
  - `case(scope): summary`
  - `index(scope): summary`
  - `structure(scope): summary`
  - `style(scope): summary`
  - `fix(scope): summary`
  - `chore(scope): summary`
- [x] `P1` 评估是否要上 commitlint。
  - 第一版可以只文档约束，不强制 CI 卡住贡献者。
- [x] `P0` 明确 PR 拆分规则：
  - 内容、目录重建、样式、导航、配置尽量分开。
- [x] `P0` 明确维护者 merge 策略：
  - squash merge 还是保留 commits。
  - 验收：贡献说明里有一句话。

## Phase 2：目录骨架重建

### 2.1 直接重建

- [x] `P0` 删除旧 `docs/`。
  - 验收：旧拼音目录不再存在于新的 `docs/` 中。
- [x] `P0` 按新架构重新创建 `docs/`。
  - 验收：新 `docs/` 只包含第一版需要的英文目录。
- [x] `P0` 整体重写 `mkdocs.yml`。
  - 验收：nav 只引用新架构的第一版页面。
- [x] `P0` 不为旧路径做 redirects。
  - 验收：`mkdocs.yml` 中不需要配置旧路径重定向。

### 2.2 一级目录

- [x] `P0` 创建 `docs/start-here/index.md`。
- [x] `P0` 创建 `docs/admissions/index.md`。
- [x] `P0` 创建 `docs/majors/index.md`。
- [x] `P0` 创建 `docs/universities/index.md`。
- [x] `P0` 创建 `docs/campus-life/index.md`。
- [x] `P0` 创建 `docs/pathways/index.md`。
- [x] `P0` 创建 `docs/cases/index.md`。
- [x] `P0` 创建 `docs/commons/index.md`。
- [ ] `P0` 每个一级 `index.md` 至少回答：
  - 这个板块解决什么问题
  - 适合谁读
  - 当前有哪些入口
  - 还缺什么
  - 如何贡献

### 2.3 `start-here/`

- [x] `P0` 创建 `docs/start-here/mindsets/index.md`。
- [x] `P1` 创建 `docs/start-here/mindsets/gaokao-inertia/index.md`。
- [x] `P1` 创建 `docs/start-here/mindsets/passive-learning/index.md`。
- [x] `P1` 创建 `docs/start-here/mindsets/grade-only-thinking/index.md`。
- [x] `P1` 创建 `docs/start-here/mindsets/information-literacy/index.md`。
- [x] `P1` 创建 `docs/start-here/mindsets/asking-for-help/index.md`。
- [x] `P0` 创建 `docs/start-here/first-questions/index.md`。
- [x] `P1` 创建 `docs/start-here/reading-routes/index.md`。
- [x] `P1` 写清高中生、大一新生、转专业同学、毕业阶段同学的阅读路线。

### 2.4 `admissions/`

- [x] `P0` 创建 `docs/admissions/methodology/index.md`。
- [x] `P0` 创建 `docs/admissions/self-assessment/index.md`。
- [x] `P0` 创建 `docs/admissions/information/index.md`。
- [x] `P0` 创建 `docs/admissions/decision-models/index.md`。
- [x] `P0` 创建 `docs/admissions/workflows/index.md`。
- [x] `P0` 创建 `docs/admissions/perspectives/index.md`。
- [x] `P0` 创建 `docs/admissions/perspectives/how-to-contribute.md`。
- [x] `P1` 创建 `docs/admissions/decision-models/major-vs-school.md`。
- [x] `P1` 创建 `docs/admissions/decision-models/city-vs-ranking.md`。
- [x] `P1` 创建 `docs/admissions/decision-models/reach-match-safety.md`。
- [x] `P1` 创建 `docs/admissions/workflows/final-checklist.md`。
- [x] `P0` 明确 admissions 不维护每年会变的录取规则。

### 2.5 `majors/`

- [x] `P0` 创建 `docs/majors/methodology/index.md`。
- [x] `P0` 创建 `docs/majors/taxonomy/index.md`。
- [x] `P0` 创建 `docs/majors/domains/index.md`。
- [x] `P0` 创建 `docs/majors/perspectives/index.md`。
- [x] `P0` 创建 `docs/majors/perspectives/how-to-contribute.md`。
- [x] `P0` 创建主要学科大类入口：
  - `docs/majors/domains/engineering/index.md`
  - `docs/majors/domains/science/index.md`
  - `docs/majors/domains/medicine/index.md`
  - `docs/majors/domains/agriculture/index.md`
  - `docs/majors/domains/business-economics-management/index.md`
  - `docs/majors/domains/law-politics/index.md`
  - `docs/majors/domains/humanities/index.md`
  - `docs/majors/domains/communication-media/index.md`
  - `docs/majors/domains/education-sports/index.md`
  - `docs/majors/domains/arts-design/index.md`
  - `docs/majors/domains/interdisciplinary/index.md`
- [x] `P0` 创建 EECS 标杆骨架：
  - `docs/majors/domains/engineering/eecs/index.md`
  - `docs/majors/domains/engineering/eecs/orientation/index.md`
  - `docs/majors/domains/engineering/eecs/programs/index.md`
  - `docs/majors/domains/engineering/eecs/fields/index.md`
  - `docs/majors/domains/engineering/eecs/foundations/index.md`
  - `docs/majors/domains/engineering/eecs/outcomes/index.md`
  - `docs/majors/domains/engineering/eecs/perspectives/index.md`
  - `docs/majors/domains/engineering/eecs/perspectives/how-to-contribute.md`
- [x] `P1` 创建 EECS foundations 子目录：
  - `mathematics/`
  - `programming/`
  - `computer-systems/`
  - `electronics-signals/`
  - `tools-practices/`
- [x] `P1` 创建 EECS fields 子目录：
  - `ai-data-intelligence/`
  - `software-systems/`
  - `security-privacy/`
  - `hardware-embedded-physical/`
  - `human-media-interaction/`
  - `theory-foundations/`
  - `domain-computing/`

### 2.6 `universities/`

- [x] `P0` 创建 `docs/universities/methodology/index.md`。
- [x] `P0` 创建 `docs/universities/dimensions/index.md`。
- [x] `P0` 创建 `docs/universities/regions/index.md`。
- [x] `P0` 创建 `docs/universities/schools/index.md`。
- [x] `P0` 创建 `docs/universities/perspectives/index.md`。
- [x] `P0` 创建 `docs/universities/perspectives/how-to-contribute.md`。
- [x] `P1` 创建首批学校入口：
  - `sysu/`
  - `scut/`
  - `jnu/`
  - `scnu/`
  - `gdufs/`
  - `szu/`
- [x] `P1` 每个学校入口至少包含：
  - `index.md`
  - `perspectives/index.md`
  - `perspectives/how-to-contribute.md`
- [x] `P1` SYSU 可先做更深样板：
  - `dimensions/`
  - `programs/`
  - `admissions-context/`

### 2.7 `campus-life/`

- [x] `P0` 创建 `docs/campus-life/academic-system/index.md`。
- [x] `P0` 创建 `docs/campus-life/learning-workflow/index.md`。
- [x] `P0` 创建 `docs/campus-life/opportunities/index.md`。
- [x] `P0` 创建 `docs/campus-life/people-and-groups/index.md`。
- [x] `P0` 创建 `docs/campus-life/wellbeing-and-practical-life/index.md`。
- [x] `P0` 创建 `docs/campus-life/failure-and-reorientation/index.md`。
- [x] `P1` 不再使用 `study-methods.md`、`social.md`、`money.md` 这类扁平入口作为最终形态。

### 2.8 `pathways/`

- [x] `P0` 创建 `docs/pathways/methodology/index.md`。
- [x] `P0` 创建 `docs/pathways/further-study/index.md`。
- [x] `P0` 创建 `docs/pathways/career/index.md`。
- [x] `P0` 创建 `docs/pathways/perspectives/index.md`。
- [x] `P0` 创建 `docs/pathways/perspectives/how-to-contribute.md`。
- [x] `P1` 创建深造路径：
  - `choosing-paths/`
  - `recommendation/`
  - `entrance-exam/`
  - `overseas/`
  - `doctoral-paths/`
  - `gap-year/`
- [x] `P1` 创建 career 路径：
  - `orientation/`
  - `internship/`
  - `job-search/`
  - `application-materials/`
  - `interviews/`
  - `industries/`
  - `workplace-transition/`
- [x] `P0` 防止 pathways 和 majors/outcomes 重复。
  - 验收：通用流程在 pathways，专业特殊性在 majors/.../outcomes。

### 2.9 `cases/`

- [x] `P0` 创建 `docs/cases/index.md`。
- [x] `P0` 创建 `docs/cases/entries/index.md`。
- [x] `P0` 创建 `docs/cases/templates/case-template.md`。
- [x] `P0` 创建 `docs/cases/indexes/index.md`。
- [x] `P0` 创建人工索引入口：
  - `by-class-year.md`
  - `by-university.md`
  - `by-major.md`
  - `by-pathway.md`
  - `by-destination.md`
  - `by-keyword.md`
- [x] `P0` 案例模板包含 frontmatter：
  - `case_id`
  - `case_type`
  - `title`
  - `author_display`
  - `anonymous`
  - `dongguan_high_school_class_year`
  - `college_entry_year`
  - `undergraduate_university`
  - `undergraduate_major`
  - `pathways`
  - `destinations`
  - `keywords`
  - `status`
  - `last_updated`
- [x] `P0` 案例模板正文包含：
  - 背景
  - 关键选择
  - 时间线
  - 过程
  - 结果
  - 复盘
  - 哪些人不该照搬
  - 公开转载告知
- [ ] `P1` 准备 1-3 个脱敏示例案例或占位样例。

### 2.10 `commons/`

- [x] `P0` 创建 `docs/commons/registries/index.md`。
- [x] `P0` 创建注册表：
  - `universities.md`
  - `majors.md`
  - `pathways.md`
  - `keywords.md`
- [x] `P1` 创建 `docs/commons/resources/index.md`。
- [x] `P1` 创建 `docs/commons/stories/index.md`。
- [x] `P1` 创建 `docs/commons/contributors.md`。

## Phase 3：模板与投稿说明

### 3.1 通用模板

- [x] `P0` 创建 `docs/commons/templates/page-template.md`。
- [x] `P0` 创建 `docs/commons/templates/perspective-template.md`。
- [x] `P0` 创建 `docs/cases/templates/case-template.md`。
- [x] `P0` 模板都包含公开转载告知。
- [x] `P0` 模板都包含最后更新时间。
- [x] `P0` 模板都说明是否允许匿名。

### 3.2 `how-to-contribute.md`

- [x] `P0` 为所有 C 类容器添加 `how-to-contribute.md`。
- [x] `P0` 每个 `how-to-contribute.md` 至少包含：
  - 这个目录收什么
  - 不收什么
  - 文件如何命名
  - 是否需要 frontmatter
  - 是否需要更新 `index.md`
  - 是否需要改 `mkdocs.yml`
  - 公开转载告知
  - 脱敏提醒
- [x] `P0` C 类文件命名统一：
  - `[year]-[name-or-alias]-[topic].md`
- [x] `P0` 如果作者匿名，文件名用 alias，不用真实姓名。
- [x] `P1` 给不会 Git 的校友准备“你可以直接发给维护者的材料清单”。

### 3.3 首页与贡献入口

- [x] `P0` 重写 `docs/index.md`。
- [x] `P0` 首页首屏回答：
  - 这是什么
  - 给谁看
  - 从哪里开始读
  - 如何贡献
- [x] `P0` 首页说明主站和 WPS 指北的关系。
- [x] `P0` 首页说明公开转载告知。
- [x] `P0` 首页不要做营销落地页。
- [x] `P1` 首页提供 3-4 条阅读路线：
  - 高中生
  - 大一新生
  - 想换专业/方向的人
  - 准备升学/就业的人

## Phase 4：旧草稿清理

### 4.1 清理原则

- [x] `P0` 不把旧 `docs/` 当作迁移对象。
- [x] `P0` 不建立旧路径映射表。
- [x] `P0` 不做旧路径重定向。
- [x] `P0` 不因为旧文件存在而保留旧目录结构。
- [ ] `P1` 如果后续发现旧文件里有个别可用段落，作为普通内容 PR 手工补入新目录。

### 4.2 清理验收

- [x] `P0` 新 `docs/` 中不存在旧拼音一级目录。
- [x] `P0` `mkdocs.yml` 不引用旧拼音路径。
- [x] `P0` `mkdocs build --strict` 通过。

## Phase 5：质量检查

### 5.1 手工检查

- [x] `P0` 检查 `mkdocs.yml` 是否只引用新架构路径。
- [x] `P0` 检查所有 nav 引用的文件都存在。
- [x] `P0` 检查所有一级目录都有 `index.md`。
- [x] `P0` 检查所有 C 类容器都有 `how-to-contribute.md`。
- [x] `P0` 检查投稿说明是否包含公开转载告知。
- [x] `P0` 检查案例模板是否包含匿名、脱敏、转载告知。
- [x] `P0` 检查首页没有把公众号写成技术模块。
- [x] `P0` 检查敏感内容没有进入公开仓库。
- [x] `P0` 检查 `DESIGN.md` 和 `extra.css` 的色彩是否一致。

### 5.2 自动检查第一版

- [x] `P0` 添加 GitHub Actions：`mkdocs build --strict`。
- [x] `P0` CI 在 PR 时运行。
- [x] `P0` CI 在 main 分支 push 时运行。
- [x] `P1` 添加路径命名检查脚本。
  - 检查英文小写连字符。
  - 允许 `README.md`、`index.md`、学校缩写、课程代码等例外。
- [x] `P1` 添加关键目录检查脚本。
  - 检查一级目录 `index.md`。
  - 检查 C 类容器 `how-to-contribute.md`。
- [ ] `P2` 添加案例 frontmatter 校验。
- [ ] `P2` 添加案例索引生成脚本。

## Phase 6：部署上线

### 6.1 静态部署

- [x] `P0` 选定部署平台：GitHub Pages。
- [x] `P0` 配置 build command。
  - 命令：`mkdocs build --strict`
- [x] `P0` 配置 output directory。
  - 目录：`site`
- [x] `P0` 配置生产分支。
  - 通常：`main`
- [x] `P0` 添加 GitHub Actions Pages workflow。
  - 验收：push 到 `main` 后自动构建并发布。
- [x] `P0` 首次部署成功。
- [x] `P0` 记录线上 URL。
- [x] `P0` 从手机访问线上 URL。
- [x] `P0` 从非登录环境访问线上 URL。
- [x] `P1` 配置 404 页面。
- [x] `P1` 配置 sitemap / robots。
- [ ] `P1` 配置自有域名和 HTTPS。

### 6.2 上线前验收

- [x] `P0` 首页可读。
- [x] `P0` 搜索可用。
- [x] `P0` 左侧导航可用。
- [x] `P0` 移动端导航可用。
- [x] `P0` 至少一个案例模板页面可访问。
- [x] `P0` 至少一个投稿说明页面可访问。
- [x] `P0` 公开转载告知可在贡献路径中看到。
- [x] `P0` 默认页面能显示 giscus 评论区。
- [x] `P0` 写了 `comments: false` 的页面不显示评论区。
- [x] `P0` 页面没有大面积空白或明显样式错乱。
- [x] `P0` 没有把旧草稿目录暴露在主导航中。

## Phase 7：第一批内容

### 7.1 起步内容

- [ ] `P0` 写 `start-here/index.md` 第一版。
- [ ] `P0` 写 `admissions/index.md` 第一版。
- [ ] `P0` 写 `majors/index.md` 第一版。
- [ ] `P0` 写 `cases/index.md` 第一版。
- [ ] `P1` 写 `majors/domains/engineering/eecs/index.md` 第一版。
- [ ] `P1` 写 `campus-life/index.md` 第一版。
- [ ] `P1` 写 `pathways/index.md` 第一版。
- [ ] `P1` 写 `universities/index.md` 第一版。

### 7.2 第一批案例

- [ ] `P0` 收集 1 个完整路径样本。
- [ ] `P0` 收集 1 个关键决策样本。
- [ ] `P1` 收集 1 个失败恢复样本。
- [ ] `P1` 收集 1 个学校体验样本。
- [ ] `P1` 收集 1 个专业体验样本。
- [ ] `P0` 所有样本脱敏。
- [ ] `P0` 所有样本确认署名或匿名方式。
- [ ] `P0` 所有样本补 frontmatter。
- [ ] `P0` 所有样本加入人工索引。

### 7.3 内容缺口表

- [ ] `P1` 在 `cases/indexes/index.md` 写当前样本缺口。
- [ ] `P1` 在 `majors/domains/index.md` 写当前专业缺口。
- [ ] `P1` 在 `universities/schools/index.md` 写当前学校缺口。
- [ ] `P1` 在 `pathways/index.md` 写当前路径缺口。

## Phase 8：长期维护

### 8.1 维护节奏

- [ ] `P1` 每月检查一次 PR 和投稿池。
- [ ] `P1` 每学期整理一次新增案例。
- [ ] `P1` 每年高考季前检查 admissions 和 majors。
- [ ] `P1` 每年毕业季前检查 pathways 和 cases。
- [ ] `P1` 对过时内容标注年份，不直接删除。

### 8.2 后续自动化

- [x] `P2` 实现 `scripts/validate_architecture.py`。
- [ ] `P2` 实现 `scripts/validate_cases.py`。
- [ ] `P2` 实现 `scripts/generate_case_indexes.py`。
- [ ] `P2` 实现 `scripts/check_generated.py`。
- [ ] `P2` CI 检查索引是否过期。
- [ ] `P2` CI 只提醒，不自动提交生成结果。

## 第一版完成定义

第一版可以认为完成，必须同时满足：

- [x] `mkdocs build --strict` 通过。
- [x] `mkdocs.yml` 主导航全部指向英文路径。
- [x] 主导航不引用旧草稿目录。
- [x] 八个一级目录都有 `index.md`。
- [x] `cases/entries/`、`cases/templates/`、`cases/indexes/` 存在。
- [x] 至少一个 `how-to-contribute.md` 是完整模板，不是占位句。
- [x] PR 模板存在，并包含公开转载告知。
- [x] 案例模板存在，并包含公开转载告知。
- [x] `CONTRIBUTING.md` 存在，并包含 commit 规范。
- [x] `DESIGN.md` 存在。
- [x] `docs/stylesheets/extra.css` 存在，并体现暖纸色/墨蓝视觉基调。
- [x] 首页说明主站、WPS 指北和公开转载告知。
- [x] 线上静态站可访问。
- [x] 移动端可以正常阅读首页和至少一个二级页面。

## 建议 PR 拆分

1. `structure(docs): create English directory skeleton`
2. `chore(mkdocs): rebuild navigation for new architecture`
3. `style(design): add handbook visual baseline`
4. `content(home): rewrite landing index and start-here`
5. `case(cases): add case template and manual indexes`
6. `content(contributing): add contribution guide and PR template`
7. `chore(ci): add strict mkdocs build workflow`

## 当前不要做

- [ ] 不要实现登录系统。
- [ ] 不要实现静态站密码页。
- [ ] 不要马上写案例自动生成脚本。
- [ ] 不要马上上 commitlint 卡贡献者。
- [ ] 不要把公众号作为仓库技术模块设计。
- [ ] 不要为了上线速度把复杂目录重新压扁。
- [ ] 不要在 build 跑通前回头整理旧草稿。
