# 莞中人飞跃手册（暂定名）

> 东莞中学校友共建的大学公开指南。从东正路62号到更远的地方。

## 项目身份

- **名称**：莞中人飞跃手册（暂定，待更好的名字）
- **对标**：上交生存手册（结构化方法论）+ 清华/上交飞跃手册（按主题组织）
- **受众**：莞中在校生 + 莞中校友 + 莞中教师 （不包含莞中家长）
- **品牌关系**：与"莞中人指北"（WPS 共享文档）是兄弟产品。指北放群内敏感内容，飞跃手册放公网结构化内容

## 与莞中人指北的分工

| | 莞中人指北（WPS） | 莞中人飞跃手册（公网主站） |
|---|---|---|
| 受众 | 莞中校友群内 | 全网公开 |
| 内容基调 | 真实、敢说、不装 | 客观、结构化、可传播 |
| 专业评价 | 有内幕、有吐槽 | 客观分析优缺点 |
| 编辑方式 | 微信打开就写 | Git PR → review → merge |
| 品牌曝光 | 仅群内传播 | 搜索引擎可收录 |

## 公开内容与转载告知

飞跃手册不是公众号文章合集，也不是把 WPS 原文搬到公网。它应该是一个长期内容母库：主站负责保存结构化、可检索、可维护的正文；WPS 指北继续承载群内才适合看的真实材料。

| 渠道 | 角色 | 可以放什么 | 不应该放什么 |
|---|---|---|---|
| WPS 指北 | 原始材料池 / 群内讨论场 | 群内经验、未脱敏反馈、征集草稿、敏感但有价值的提醒 | 直接面向公网的定稿 |
| 飞跃手册主站 | 公开母库 / 长期正本 | 结构化指南、案例正本、索引、专业/学校/路径页面 | 未脱敏材料、纯宣传稿、每年需要人工追最新的具体政策清单 |

飞跃手册由"莞言瓜语"维护。贡献者提交 PR、commit、issue、案例素材或经维护者整理入库的公开内容时，应默认理解为：这些公开内容未来可能被莞言瓜语在公众号或其他公开渠道中转载、摘编、排版或二次传播。维护者应在投稿说明里提前写清楚这一点。

转载告知的边界：

- 只针对已经进入飞跃手册主站、并且适合公开传播的内容。
- 保持作者约定的署名、届别、匿名方式和脱敏边界。
- 可以做排版、摘要和语言调整，但不能改变作者原意或制造不真实背书。
- 敏感内容、未授权材料、只适合群内的 WPS 指北内容，不因为公众号需要而进入公网。

## 设计原则

1. **结构化优先**：每篇有清晰的目录层次，适合系统阅读，不是碎片化的帖子
2. **敢说真话但不过界**：可以客观分析"这个专业不适合什么样的人"，但不放针对具体个人的吐槽
3. **长期可维护**：内容过时标注而非删除，保持手册的历史感
4. **署名但不强求**：默认署 XX届+名字，允许化名

## 目录结构

> **文件夹/文件决策规则**：需要容纳多个人独立贡献的，就是文件夹；内容整合为单一权威口径的，就是文件。
>
> **三类文件**：
> - **A 类（index.md）**：索引 + 链接，谁加新文章谁来加一行
> - **B 类（固定名）**：整合后的权威口径，多人编辑同一篇，读起来像一个声音
> - **C 类（自由命名）**：个人署名，格式 `[year]-[name-or-alias]-[topic].md`，零冲突；页面标题和署名可用中文
>
> **深度来源**：参考 SurviveSJTUManual 的“先改变看法，再给技巧”、THU-feiyue-docs 的“按真实申请时间线做深”、SJTU-Application / SUSTech-Application / SZU-FeiYue 的“案例库是核心资产”、cs-self-learning 的“领域地图必须表达学习顺序和先修关系”。
>
> **空文件夹不冗余**：每个 C 类容器目录标配 `index.md` + `how-to-contribute.md`。后者教会贡献者三步走——怎么命名文件、怎么创建子文件夹、怎么更新索引。有了它，"空文件夹"就不再是空壳，而是等着人来填的脚手架。
>
> **路径命名规范**：文件夹和文件统一使用英文小写连字符（如 `campus-life/`、`major-vs-school.md`），导航标题和页面标题使用中文。学校缩写、课程代码、专业缩写可保留常见英文缩写（如 `sysu/`、`cs61a.md`、`eecs/`）。
>
> **图片与附件存放规范**：内容图片不统一堆进一个大的 `docs/assets/`。全站视觉资产只放 `docs/assets/logo/`、`docs/assets/site/`；正文图片放在拥有它的页面目录下的 `_assets/`，例如 `docs/majors/domains/engineering/eecs/_assets/field-map.webp`。具体子方向、学校、路径、案例的图片放在对应子目录自己的 `_assets/`；多页共用图片放最近共同父目录的 `_assets/shared/`。案例如果需要多张图，优先采用文件夹页面 `cases/entries/[case-id]/index.md`，图片放 `cases/entries/[case-id]/_assets/`。详见 `commons/governance/media-assets/`。
>
> **专业覆盖原则**：`majors/domains/` 下先把主要学科大类和专业群入口列全，保证读者能找到位置；不要求每个入口立刻写深。入口页可以先是索引和征稿说明，等有内容后再展开具体专业、资源、科研、实习和去向路径。
>
> **反过度扁平化原则**：不要把复杂概念压成一排 `.md` 文件。凡是内部天然包含子问题、子能力、相邻方向比较、资源路线或多人贡献空间的对象，都应优先设计成文件夹，用 `index.md` 承担总览，用子目录承载层级。
>
> **案例库优先原则**：带有具体人、具体背景、具体选择、具体过程和具体结果的莞中人样本不是附录，而是手册的核心资产。这类样本优先进入 `cases/entries/`，再由专业、学校、路径页面引用或索引；局部观点、短方法、尚未形成样本的主题补充才放在对应目录的 `perspectives/`。

```
docs/
├── index.md                                  ← 前言/主页
│
├── start-here/                               ← 心智转换型：从高中生到大学生，先学会怎么看问题
│   ├── index.md                              ← 开始阅读：这本手册不是替你做决定
│   ├── mindsets/                             ← 莞中人进入大学后最常见的思维惯性
│   │   ├── index.md
│   │   ├── gaokao-inertia/                   ← 高考惯性：只会等题、等标准答案、等排名
│   │   ├── passive-learning/                 ← 被安排惯性：不会主动找资源、找人、找机会
│   │   ├── grade-only-thinking/              ← 只看绩点：把大学压缩成第二次高考
│   │   ├── information-literacy/             ← 信息素养：如何查证、筛选和使用信息
│   │   └── asking-for-help/                  ← 如何向老师、同学、校友提问
│   ├── first-questions/                      ← 读手册前先问自己的问题
│   │   ├── index.md
│   │   ├── what-do-i-want/
│   │   ├── what-can-i-try-now/
│   │   ├── what-should-i-stop-doing/
│   │   └── how-to-use-alumni-advice/
│   └── reading-routes/                       ← 不同读者的阅读路线
│       ├── index.md
│       ├── high-school-students/
│       ├── college-freshmen/
│       ├── major-switchers/
│       └── graduating-students/
│
├── admissions/                               ← 决策流程型：高考后的第一组选择
│   ├── index.md                              ← 志愿填报总览（B 类）
│   ├── methodology/                          ← 如何做志愿决策
│   │   ├── index.md
│   │   └── principles.md
│   │
│   ├── self-assessment/                      ← 先判断自己是什么样的人
│   │   ├── index.md
│   │   ├── priorities.md                     ← 专业/学校/城市/家庭/经济/性格排序
│   │   ├── constraints.md                    ← 家庭、地域、学费、身体条件等硬约束
│   │   └── risk-tolerance.md                 ← 能不能接受调剂、冷门专业、复读风险
│   │
│   ├── information/                          ← 怎么获得和判断信息
│   │   ├── index.md
│   │   ├── official-sources.md               ← 去哪里核对最新信息，不维护具体规则
│   │   ├── score-rank.md                     ← 分数、排位、线差怎么看
│   │   └── alumni-signals.md                 ← 校友信息怎么听，哪些话可信/不可信
│   │
│   ├── decision-models/                      ← 核心决策模型
│   │   ├── index.md
│   │   ├── major-vs-school.md                ← 专业优先还是学校优先
│   │   ├── city-vs-ranking.md                ← 城市、地域与学校名气怎么权衡
│   │   ├── reach-match-safety.md             ← 冲稳保策略
│   │   ├── major-reassignment.md             ← 调剂、转专业风险
│   │   └── hidden-costs.md                   ← 隐性成本：实习城市、读研路径、转专业难度等
│   │
│   ├── workflows/                            ← 填报阶段的操作流程
│   │   ├── index.md
│   │   ├── before-score.md                   ← 出分前做什么
│   │   ├── after-score.md                    ← 出分后怎么缩小范围
│   │   ├── final-checklist.md                ← 最终提交前检查
│   │   └── family-discussion.md              ← 怎么和家里讨论
│   │
│   └── perspectives/                         ← 署名个人视角：经验复盘或个人方法论（C 类容器）
│       ├── index.md
│       ├── how-to-contribute.md
│       └── ...
│
├── majors/                                   ← 认知对象型：专业世界
│   ├── index.md                              ← 专业认知总览（B 类）
│   │
│   ├── methodology/                          ← 如何读懂一个专业
│   │   ├── index.md
│   │   ├── what-to-ask.md                     ← 读懂专业时必须问的问题
│   │   ├── evidence-sources.md               ← 专业信息来源怎么判断
│   │   └── comparison-methods.md             ← 如何比较相邻专业
│   │
│   ├── taxonomy/                             ← 专业世界的分类地图
│   │   ├── index.md
│   │   ├── disciplines-map.md                ← 学科大类总图
│   │   ├── major-groups.md                   ← 专业群如何形成
│   │   └── naming-traps.md                   ← 学校命名/专业名的坑
│   │
│   ├── domains/                              ← 具体学科大类、专业群、专业
│   │   ├── index.md
│   │
│   │   ├── engineering/                      ← 工科：工程实现、系统建造、项目交付
│   │   │   ├── index.md                      ← 工科总览：工科和理科的区别、内部分支、适合谁（B 类）
│   │   │   ├── map/                          ← 工科分类地图，不写成 map.md
│   │   │   │   ├── index.md
│   │   │   │   ├── information-computing/
│   │   │   │   ├── mechanical-energy/
│   │   │   │   ├── civil-environment/
│   │   │   │   └── materials-chemical/
│   │   │   ├── fit/                          ← 什么样的人适合工科
│   │   │   │   ├── index.md
│   │   │   │   ├── strengths/
│   │   │   │   └── risk-signals/
│   │   │   ├── misconceptions/               ← 高中生对工科的常见误解
│   │   │   │   ├── index.md
│   │   │   │   └── ...
│   │   │
│   │   │   ├── eecs/                         ← 电子信息与计算机专业群
│   │   │   │   ├── index.md                  ← 专业群总览：这个专业群是什么、适合谁（B 类）
│   │   │   │   ├── orientation/              ← 看懂这个专业群
│   │   │   │   │   ├── index.md
│   │   │   │   │   ├── map/
│   │   │   │   │   ├── comparisons/
│   │   │   │   │   ├── curriculum/
│   │   │   │   │   └── misconceptions/
│   │   │   │   ├── programs/                 ← 具体专业入口
│   │   │   │   │   ├── index.md
│   │   │   │   │   ├── computer-science/
│   │   │   │   │   ├── software-engineering/
│   │   │   │   │   ├── electronic-information/
│   │   │   │   │   └── artificial-intelligence/
│   │   │   │   ├── fields/                   ← 方向生态图：技术/研究/行业方向
│   │   │   │   │   ├── index.md
│   │   │   │   │   ├── how-to-contribute.md
│   │   │   │   │   ├── ai-data-intelligence/
│   │   │   │   │   ├── software-systems/
│   │   │   │   │   ├── security-privacy/
│   │   │   │   │   ├── hardware-embedded-physical/
│   │   │   │   │   ├── human-media-interaction/
│   │   │   │   │   ├── theory-foundations/
│   │   │   │   │   └── domain-computing/
│   │   │   │   ├── foundations/              ← 专业群所需基础能力结构，不讲通用学习方法
│   │   │   │   │   ├── index.md
│   │   │   │   │   ├── mathematics/
│   │   │   │   │   ├── programming/
│   │   │   │   │   ├── computer-systems/
│   │   │   │   │   ├── electronics-signals/
│   │   │   │   │   └── tools-practices/
│   │   │   │   ├── outcomes/                 ← 专业语境下的去向，不重复 pathways/
│   │   │   │   │   ├── index.md
│   │   │   │   │   ├── industry-roles/
│   │   │   │   │   ├── graduate-study/
│   │   │   │   │   └── research-paths/
│   │   │   │   └── perspectives/             ← 署名个人视角
│   │   │   │       ├── index.md
│   │   │   │       ├── how-to-contribute.md
│   │   │   │       └── ...
│   │   │
│   │   │   ├── mechanical-automation/
│   │   │   ├── energy-power/
│   │   │   ├── materials/
│   │   │   ├── chemical-pharmaceutical/
│   │   │   ├── civil-architecture/
│   │   │   ├── water-environment-safety/
│   │   │   ├── transportation/
│   │   │   ├── aerospace-marine/
│   │   │   ├── geoscience-mining/
│   │   │   ├── biomedical-engineering/
│   │   │   └── industrial-systems/
│   │   │
│   │   ├── science/
│   │   ├── medicine/
│   │   ├── agriculture/
│   │   ├── business-economics-management/
│   │   ├── law-politics/
│   │   ├── humanities/
│   │   ├── communication-media/
│   │   ├── education-sports/
│   │   ├── arts-design/
│   │   └── interdisciplinary/
│   │
│   └── perspectives/                         ← 专业选择的个人视角（C 类容器）
│       ├── index.md
│       ├── how-to-contribute.md
│       └── ...
│
├── universities/                             ← 认知对象型：大学世界
│   ├── index.md                              ← 院校认知总览（B 类）
│   │
│   ├── methodology/                          ← 如何读懂一所大学
│   │   ├── index.md
│   │   ├── what-to-ask.md
│   │   ├── evidence-sources.md
│   │   └── comparison-methods.md
│   │
│   ├── dimensions/                           ← 判断一所大学的维度
│   │   ├── index.md
│   │   ├── city-and-region/
│   │   ├── academic-ecosystem/
│   │   ├── peer-group/
│   │   ├── campus-life/
│   │   ├── career-resources/
│   │   └── further-study-resources/
│   │
│   ├── regions/                              ← 区域视角，不维护实时排名
│   │   ├── index.md
│   │   ├── greater-bay-area/
│   │   ├── yangtze-river-delta/
│   │   ├── beijing-tianjin/
│   │   └── overseas/
│   │
│   ├── schools/                              ← 具体学校
│   │   ├── index.md
│   │   ├── sysu/
│   │   │   ├── index.md
│   │   │   ├── dimensions/
│   │   │   ├── programs/
│   │   │   ├── admissions-context/
│   │   │   └── perspectives/
│   │   ├── scut/
│   │   ├── jnu/
│   │   ├── scnu/
│   │   ├── gdufs/
│   │   └── szu/
│   │
│   └── perspectives/                         ← 院校选择与就读体验的个人视角
│       ├── index.md
│       ├── how-to-contribute.md
│       └── ...
│
├── campus-life/                              ← 在校生存：进入大学后怎么长期运行
│   ├── index.md                              ← 大学生存总览：大学不是第二个高中（B 类）
│   │
│   ├── academic-system/                      ← 读懂大学的学业制度
│   │   ├── index.md
│   │   ├── course-selection/                 ← 选课、退课、先修、课程信息差
│   │   ├── gpa-and-ranking/                  ← GPA、排名、奖学金、保研资格如何影响选择
│   │   ├── exams-and-recovery/               ← 考试、挂科、重修、补救
│   │   ├── transfer-minor-double-degree/     ← 转专业、辅修、双学位
│   │   └── graduation-requirements/          ← 毕业要求、培养方案、学分结构
│   │
│   ├── learning-workflow/                    ← 大学学习方式
│   │   ├── index.md
│   │   ├── self-learning/                    ← 不等老师讲完，自己搭学习路线
│   │   ├── note-and-review/                  ← 笔记、复习、资料管理
│   │   ├── time-and-energy/                  ← 时间、精力、ddl、长期项目
│   │   ├── information-search/               ← 找资料、找课程、找机会
│   │   └── tools/                            ← 工具链：Git、Markdown、AI、文献/资料管理等
│   │
│   ├── opportunities/                        ← 大学里的机会如何出现
│   │   ├── index.md
│   │   ├── research-projects/                ← 科研、课题组、实验室、导师
│   │   ├── competitions/                     ← 竞赛、项目、作品
│   │   ├── internships-and-practice/         ← 实习、社会实践、兼职
│   │   ├── exchange-and-summer-programs/     ← 交换、暑校、暑研
│   │   └── scholarships-and-funding/         ← 奖学金、资助、项目经费
│   │
│   ├── people-and-groups/                    ← 人、组织与合作
│   │   ├── index.md
│   │   ├── classmates-and-roommates/
│   │   ├── clubs-and-student-organizations/
│   │   ├── mentors-and-seniors/
│   │   ├── teamwork-and-conflict/
│   │   └── asking-for-help/
│   │
│   ├── wellbeing-and-practical-life/         ← 身心和现实生活
│   │   ├── index.md
│   │   ├── mental-health/
│   │   ├── money/
│   │   ├── housing-and-campus-services/
│   │   ├── health-and-safety/
│   │   └── family-communication/
│   │
│   └── failure-and-reorientation/            ← 失误、停滞和重新选择
│       ├── index.md
│       ├── falling-behind/
│       ├── burnout/
│       ├── wrong-major-or-school/
│       ├── failed-application-or-job-search/
│       └── rebuilding-a-plan/
│
├── pathways/                                 ← 行动路径型：毕业/升学/就业的下一站选择
│   ├── index.md
│   ├── methodology/                          ← 如何规划下一站
│   │   ├── index.md
│   │   ├── self-positioning/                 ← 先判断自己处在什么位置
│   │   ├── timeline/                         ← 大一到大四的准备节奏
│   │   ├── tradeoffs/                        ← 稳定/成长/收入/自由/风险的权衡
│   │   └── decision-points/                  ← 什么时候必须做选择，什么时候还可以观望
│   │
│   ├── further-study/                        ← 深造路径
│   │   ├── index.md
│   │   ├── choosing-paths/                   ← 先选路径：保研/考研/出国/直博/gap
│   │   │   ├── index.md
│   │   │   ├── recommendation-vs-exam/
│   │   │   ├── domestic-vs-overseas/
│   │   │   ├── master-vs-phd/
│   │   │   └── costs-and-risks/
│   │   ├── recommendation/                   ← 保研路径
│   │   │   ├── index.md
│   │   │   ├── eligibility/
│   │   │   ├── preparation/
│   │   │   ├── summer-camps/
│   │   │   ├── school-selection/
│   │   │   ├── interviews/
│   │   │   ├── documents/
│   │   │   └── perspectives/
│   │   ├── entrance-exam/                    ← 考研路径
│   │   │   ├── index.md
│   │   │   ├── target-selection/
│   │   │   ├── exam-subjects/
│   │   │   ├── preparation-timeline/
│   │   │   ├── retake-and-adjustment/
│   │   │   ├── reexamination/
│   │   │   └── perspectives/
│   │   ├── overseas/                         ← 境外申请路径
│   │   │   ├── index.md
│   │   │   ├── regions/
│   │   │   ├── program-types/
│   │   │   ├── application-materials/
│   │   │   ├── funding/
│   │   │   ├── timeline/
│   │   │   └── perspectives/
│   │   ├── doctoral-paths/                   ← 博士路径，不只放在出国或保研下面
│   │   │   ├── index.md
│   │   │   ├── direct-phd/
│   │   │   ├── master-to-phd/
│   │   │   ├── supervisors/
│   │   │   └── research-fit/
│   │   └── gap-year/                         ← 延迟一年再申请/考试/工作
│   │       ├── index.md
│   │       ├── reasons/
│   │       ├── planning/
│   │       ├── risks/
│   │       └── perspectives/
│   │
│   ├── career/                               ← 求职路径
│   │   ├── index.md
│   │   ├── orientation/                      ← 要不要先就业，适合什么就业节奏
│   │   │   ├── index.md
│   │   │   ├── choosing-work/
│   │   │   ├── industry-map/
│   │   │   ├── timing/
│   │   │   └── constraints/
│   │   ├── internship/                       ← 实习路径
│   │   │   ├── index.md
│   │   │   ├── first-internship/
│   │   │   ├── daily-internship/
│   │   │   ├── summer-internship/
│   │   │   ├── return-offer/
│   │   │   └── perspectives/
│   │   ├── job-search/                       ← 正式求职制度
│   │   │   ├── index.md
│   │   │   ├── campus-recruiting/
│   │   │   ├── social-recruiting/
│   │   │   ├── state-owned-and-public/
│   │   │   ├── civil-service/
│   │   │   └── overseas-job-search/
│   │   ├── application-materials/            ← 通用材料骨架；专业化写法回到 majors/
│   │   │   ├── index.md
│   │   │   ├── resume/
│   │   │   ├── portfolio/
│   │   │   ├── cover-letter/
│   │   │   └── online-assessment/
│   │   ├── interviews/                       ← 通用筛选形式；专业题型回到 majors/
│   │   │   ├── index.md
│   │   │   ├── behavioral/
│   │   │   ├── group-interview/
│   │   │   ├── case/
│   │   │   └── technical/
│   │   ├── industries/                       ← 行业入口；岗位生态特殊性回到专业 outcomes/
│   │   │   ├── index.md
│   │   │   ├── technology-internet/
│   │   │   ├── finance-consulting/
│   │   │   ├── public-sector/
│   │   │   ├── education-media/
│   │   │   ├── manufacturing-energy/
│   │   │   └── healthcare-biotech/
│   │   ├── workplace-transition/             ← 拿到 offer 之后
│   │   │   ├── index.md
│   │   │   ├── offer-negotiation/
│   │   │   ├── onboarding/
│   │   │   └── first-year/
│   │   └── perspectives/
│   │
│   └── perspectives/                         ← 下一站路径的局部观点和短经验
│       ├── index.md
│       ├── how-to-contribute.md
│       └── ...
│
├── cases/                                    ← 样本索引型：莞中人的真实样本库，核心资产
│   ├── index.md                              ← 案例库总览：按届别、大学、专业、路径、去向交叉索引
│   ├── how-to-contribute.md                  ← 如何提交一篇带背景和结果的莞中人样本
│   ├── entries/                              ← 样本正本：完整路径、关键选择、重要片段都可入库
│   │   ├── index.md
│   │   └── 2024-zhang-san-sysu-eecs-recommendation.md
│   ├── indexes/                              ← 索引页，不重复正文，只链接 entries
│   │   ├── index.md
│   │   ├── by-class-year/                    ← 按莞中届别
│   │   ├── by-university/                    ← 按本科/研究生学校
│   │   ├── by-major/                         ← 按专业/专业群
│   │   ├── by-pathway/                       ← 按保研、考研、出国、就业、转专业等路径
│   │   ├── by-destination/                   ← 按最终去向
│   │   └── by-keywords/                      ← 关键词：跨专业、gap、转码、低绩点、家庭约束等
│   └── templates/                            ← 案例模板
│       ├── index.md
│       ├── full-path-case.md
│       └── interview-style-case.md
│
└── commons/                                  ← 共同体型：资源、故事、贡献与治理
    ├── stories/                              ← 非路径型故事：人物、群体、活动、共同体记忆
    │   ├── index.md
    │   └── how-to-contribute.md
    ├── resources/
    │   ├── index.md
    │   └── ...
    ├── registries/                           ← 术语注册表：统一代码和命名，服务案例索引
    │   ├── index.md
    │   ├── universities.md                   ← 学校代码，如 sysu/scut/szu
    │   ├── majors.md                         ← 专业/专业群代码，如 eecs/clinical-medicine
    │   ├── pathways.md                       ← 路径代码，如 recommendation/career/overseas
    │   └── keywords.md                       ← 关键词规范，避免同义词把索引打散
    ├── contributors.md
    └── governance/
        ├── index.md
        └── contribution-rules.md
```

## 架构说明

### 文件分类（A / B / C）

手册里只有三种文件，没有"编委会文件"和"个人文件"的二分法——任何文件都是大家来写，但写入方式不同：

| | A 类：索引 | B 类：权威口径 | C 类：个人署名 |
|---|---|---|---|
| **文件名** | 固定 `index.md` | 固定名 | 自由命名，格式 `[year]-[name-or-alias]-[topic].md` |
| **产出** | 链接列表 | 一篇整合过的文章，读起来像一个声音 | 每个人自己的视角 |
| **多人参与** | 谁加新内容谁来加一行 | 多人编辑同一篇，内容融合进正文 | 各写各的文件，零冲突 |
| **类比** | 目录页 | 维基百科词条 | 论坛帖子 |
| **示例** | `majors/domains/engineering/eecs/fields/index.md` | `majors/domains/engineering/eecs/index.md`（专业群概览） | `cases/entries/2026-zhang-san-eecs-major-choice.md` |
| **核心约束** | 保持链接最新 | 不能"你一嘴我一嘴"，观点必须融合 | 署名，为自己说的话负责 |

**编委会不是"唯一能写 B 类的人"**——B 类的意思是产出形态是整合的，不是作者是内定的。任何人只要有能力综合多方信息、写出统一口径的文章，都可以 PR B 类文件。

### 顶层目录的知识类型

每个顶层目录必须先声明自己属于哪一种知识类型，再决定内部结构。不要把所有栏目都做成同一种“文章列表”。

| 知识类型 | 顶层目录 | 组织方式 | 核心问题 |
|---|---|---|---|
| 心智转换型 | `start-here/` | 按高中惯性、大学新问题、阅读路线组织 | 我该如何开始理解大学和选择？ |
| 决策流程型 | `admissions/` | 按自我评估、信息判断、决策模型、执行流程组织 | 我现在该怎么做选择？ |
| 认知对象型 | `majors/`、`universities/` | 按方法论、分类/维度、具体对象、个人视角组织 | 我选择的对象到底是什么？ |
| 行动场景型 | `campus-life/` | 按大学内的长期行动场景组织 | 进入大学以后怎么运行？ |
| 行动路径型 | `pathways/` | 按下一站目标、准备、执行、复盘组织 | 毕业/升学/就业要走向哪里？ |
| 样本索引型 | `cases/` | 按样本正本 + 多维索引组织 | 莞中人真实经历了哪些选择、阶段和结果？ |
| 共同体型 | `commons/` | 按资源、故事、贡献规则、治理组织 | 莞中共同体如何沉淀和维护经验？ |

**关键边界**：顶层行动目录讲“通用行动方法”，认知对象目录讲“这个对象的结构、差异和特殊性”。例如 `pathways/career/` 讲怎么找实习，`majors/domains/engineering/eecs/outcomes/industry-roles/` 只讲 EECS 岗位生态和技术面特殊性。`cases/` 不承担通用解释，而是保存带背景、过程和结果的真实样本；主干页需要案例时引用它，不复制它。

### 从参考项目学到的架构原则

参考项目不能只拿来抄栏目名，要学它们为什么能长出来。

| 参考项目 | 真正值得学的地方 | 落到本手册的规则 |
|---|---|---|
| SurviveSJTUManual | 先处理学生怎么看大学、失败、主动性、工作和研究，再写生存技巧 | 新增 `start-here/`，把高考惯性、被安排惯性、信息素养和提问能力放到入口 |
| THU-feiyue-docs | 单一路径按真实时间线做深：前期判断、准备、材料、网申、面试、录取后 | `pathways/` 每条稳定路径都要有阶段结构，不能只列材料名 |
| SJTU-Application / SUSTech-Application | 经验帖不是附属内容，而是读者最想看的真实样本 | 新增 `cases/`，把完整路径、关键选择、重要片段集中入库，再被各主干页索引 |
| SZU-FeiYue / AHU-Impart-Inherit | 素材密度不均匀时，按路径、专业、学院、年份聚合案例，比强行写全主干更能启动 | 允许 `cases/` 先长起来；主干页可以从案例中逐步提炼 |
| cs-self-learning | 领域地图要表达先修关系和学习顺序，不只是方向清单 | `majors/.../foundations/` 和 `fields/` 必须写清能力顺序、相邻方向和错误路线 |

### start-here/ 边界

`start-here/` 是读者进入手册前的入口，不是鸡汤区，也不是所有方法论的总仓库。它只回答三个问题：

1. 我从莞中进入大学后，哪些高中阶段有效的习惯会失效？
2. 我该如何读这本手册，如何判断一条校友建议是否适合我？
3. 我现在该先问什么问题、看什么页面、做什么低成本尝试？

`start-here/` 应该写：

- 高考惯性、被安排惯性、只看绩点、害怕试错、不会问问题、不会查信息
- 不同读者的阅读路线，例如高中生、大一新生、想转专业的人、临近毕业的人
- 如何使用案例：看背景、看限制条件、看失败和转向，而不是只看结果
- 如何从“求标准答案”转向“建立自己的判断”

`start-here/` 不应该写：

- 具体志愿填报策略；这属于 `admissions/`
- 具体专业、学校评价；这属于 `majors/` 和 `universities/`
- 大学里的具体生存技巧；这属于 `campus-life/`
- 保研、考研、出国、求职流程；这属于 `pathways/`
- 抒情式鼓励文章；除非它能转化成清楚的判断或行动

### campus-life/ 深度模型

`campus-life/` 不是大学生活杂项，也不是“学习/社交/心理”的文章夹。它学习 SurviveSJTUManual 的方式：把大学看成一个需要读懂的运行系统，帮助读者识别制度、机会、人际、失败和恢复机制。

每个 `campus-life/` 子目录至少要回答：

- 这个场景背后的大学制度或隐性规则是什么
- 莞中人常见误解是什么
- 什么选择会带来长期后果，什么只是短期波动
- 遇到问题时可以找哪些人、查哪些文件、走哪些流程
- 什么情况下应该停止硬扛，重新调整路径

`campus-life/` 与 `start-here/` 的区别：`start-here/` 讲“你该如何开始看大学”；`campus-life/` 讲“进入大学后具体系统如何运转”。例如“不要只用高考思维理解 GPA”放 `start-here/mindsets/grade-only-thinking/`；“GPA、排名、奖学金、保研资格如何互相影响”放 `campus-life/academic-system/gpa-and-ranking/`。

### cases/ 元数据与正文规则

`cases/` 学习 SUSTech-Application 的元数据规则和 SZU-FeiYue 的案例正文骨架。元数据负责索引，正文负责让人读懂一个真实的人如何经历一个选择、一段路径或一次转向。

每篇样本必须有 frontmatter：

```yaml
---
case_id: 2024-zhang-san-sysu-eecs-recommendation
case_type: full-path
title: "张三：从莞中到中大 EECS，再到保研"
author_display: "张三"
anonymous: false
dongguan_high_school_class_year: 2020
college_entry_year: 2020
undergraduate_university: sysu
undergraduate_major: eecs
pathways: [recommendation]
destinations: ["清华深圳-计算机技术硕士"]
status: completed
keywords: [eecs, recommendation, research, gpa, summer-camp]
related_majors: [majors/domains/engineering/eecs/]
related_universities: [universities/schools/sysu/]
related_pathways: [pathways/further-study/recommendation/]
last_updated: 2026-06-09
---
```

必填字段：

- `case_id`：和文件名一致，英文小写连字符
- `case_type`：样本类型，见下方说明
- `title`：页面标题，可以中文
- `author_display`：展示名，可以是真名、化名或“匿名”
- `anonymous`：是否匿名
- `dongguan_high_school_class_year`：莞中届别或毕业年份
- `college_entry_year`：大学入学年份
- `undergraduate_university`：本科院校代码
- `undergraduate_major`：本科专业或专业群代码
- `pathways`：经历涉及的路径，如 `admissions`、`transfer`、`recommendation`、`entrance-exam`、`overseas`、`career`、`gap-year`
- `destinations`：最终去向，可以是学校、项目、公司、行业或“仍在探索”
- `keywords`：用于索引的关键词
- `last_updated`：最后更新时间

`case_type` 可选值：

- `full-path`：完整路径复盘，例如从本科选择到保研/考研/出国/就业结果
- `decision`：一次关键选择，例如专业优先还是学校优先、要不要转专业、要不要 gap
- `episode`：一个重要阶段或事件，例如第一次实习、一次夏令营、一次科研经历
- `failure-recovery`：失败与恢复，例如 GPA 崩盘、保研失败、求职受挫后如何重建
- `object-experience`：对某个专业、学校、项目、行业的具体体验样本

可选字段：

- `graduate_university`
- `graduate_major`
- `employer`
- `regions`
- `constraints`：如家庭经济、地域、低绩点、跨专业、身体条件、gap
- `contact`：邮箱、微信、GitHub 等，允许留空

每篇样本正文建议使用这个骨架。`full-path` 可以写得完整一些；`decision`、`episode`、`failure-recovery` 可以聚焦一个片段，但仍要交代背景、过程和结果。

```markdown
# 标题
> 一句话摘要：这篇案例最值得读者学到什么

## 背景
莞中届别、本科院校、专业、成绩/经历/家庭或地域约束、当时的选择处境。

## 关键选择
当时面临哪些选项，为什么选了这条路，放弃了什么。

## 时间线 / 关键节点
按大一到毕业、申请/求职阶段，或这次事件的发生顺序写清楚关键节点。

## 过程
具体做了什么，遇到什么坑，哪些信息来源有用，哪些判断后来被证明不对。

## 结果
申请/求职/转向结果是什么；如果失败，也写清失败在哪里。

## 现在回看
哪些建议仍然成立，哪些只适用于当时的年份、学校、专业或个人条件。

## 适合谁 / 不适合谁
读者在什么处境下可以参考，什么处境下不应照搬。

## 联系方式（可选）
```

`cases/indexes/` 的规则：

- 索引页只链接 `entries/`，不复制正文
- 每篇案例至少进入 `by-class-year/`、`by-university/`、`by-major/`、`by-pathway/` 四类索引
- 主干页引用案例时，只写一句“相关案例：...”并链接，不把案例拆散搬运
- 如果一篇文章虽短，但有明确背景、过程、结果和可供比较的限制条件，仍可进入 `cases/entries/`
- 如果一篇文章只是观点、提醒、方法补充或没有完整背景和结果，放对应 `perspectives/`

### 信息架构层级

自动化虽然暂不实现，但内容从一开始就要按“正本、索引、导航、词表”分层。这样手工维护也不会乱，未来要自动化时也有清楚的源数据。

```
内容正本层     → 真正写文章的地方
索引生成层     → 按元数据把正本重新组织
导航展示层     → 读者看到的少数入口和阅读路线
术语注册层     → 学校、专业、路径、关键词的统一命名
```

对应到本项目：

| 层级 | 目录/文件 | 规则 |
|---|---|---|
| 内容正本层 | `cases/entries/`、各主干页、局部 `perspectives/` | 真正写正文；同一篇莞中人样本只能有一个正本 |
| 索引生成层 | `cases/indexes/` | 只做链接、摘要和分组，不写新的经验正文 |
| 导航展示层 | `mkdocs.yml` nav、各顶层 `index.md` | 导航不是文件树复刻，只暴露少数阅读入口 |
| 术语注册层 | `commons/registries/` | 统一学校、专业、路径、关键词代码，避免同义词把索引打散 |

硬规则：

- **正本只能有一个**：一个莞中人样本只写在 `cases/entries/`；专业页、学校页、路径页只引用它。
- **索引不是内容**：`cases/indexes/` 只放链接、一句话摘要、分组说明，不写新的经验。
- **导航不是目录结构**：`docs/` 可以很深，`mkdocs.yml` 必须克制；复杂索引用页面消化，不全部暴露到 nav。
- **代码必须注册**：frontmatter 里的 `undergraduate_university`、`undergraduate_major`、`pathways`、`keywords` 应优先使用 `commons/registries/` 中已有写法；新增代码时先更新注册表。
- **主干页服务案例阅读**：`majors/`、`universities/`、`pathways/` 的主干页不是为了覆盖所有情况，而是帮助读者读懂、比较和正确使用 `cases/`。

### 生长型页面规则

这套规则只适用于“会持续吸收多人贡献、从案例中提炼判断”的页面，不是所有页面都要套。不要把每篇文章都写成“已有内容/缺口/征稿方向”，那会让读者烦，也会让操作指南变得不清楚。

**适用页面**：

- 顶层或二级 `index.md`，如 `majors/index.md`、`universities/index.md`、`campus-life/index.md`、`pathways/index.md`
- 学科大类、专业群、具体专业的入口页，如 `majors/domains/engineering/index.md`、`majors/domains/engineering/eecs/index.md`
- 学校、学院、项目入口页，如 `universities/schools/sysu/index.md`、`universities/schools/sysu/programs/*/index.md`
- 路径总览页，如 `pathways/further-study/recommendation/index.md`、`pathways/career/internship/index.md`
- 大学生存的长期场景页，如 `campus-life/academic-system/index.md`、`campus-life/opportunities/index.md`
- 案例库和索引页，如 `cases/index.md`、`cases/indexes/*/index.md`

这些页面应该回答：

- 这个目录解决什么问题
- 现在已有的主干判断是什么
- 已有哪些案例、局部经验或资源
- 目前缺什么方向、样本或反例
- 贡献者可以怎样补

**不适用页面**：

- 具体操作指南、清单、规则页，如 `admissions/workflows/final-checklist.md`、`commons/governance/contribution-rules.md`
- 注册表页，如 `commons/registries/*.md`
- 莞中人样本正本，如 `cases/entries/*.md`
- 单点方法页，如简历写法、SOP 写法、某个材料说明、某个面试形式说明
- `start-here/` 下的具体心智转换文章，除非它本身是一个长期入口页

这些页面应该追求清楚、完整、可执行，不需要写“目前缺什么”。

**页面成熟度只用于生长型页面**：

```
stub          只有入口、问题清单和征稿说明
seeded        已有少量案例或局部经验，但还没有稳定判断
mapped        已经能整理出分类、差异和常见路径
synthesized   已经有较成熟的主干判断，并能解释案例之间的差异
maintained    有维护者持续更新、合并新经验、标注过时内容
```

成熟度是维护者的内部判断，不必用生硬标签展示给读者。对读者更友好的写法是：

```markdown
目前本页已有 3 篇莞中人案例，主要集中在 EECS 和经管方向；医学、法学和文科样本仍较少。阅读时请注意这些样本边界。
```

**核心原则**：

- 如果页面负责“收集和组织多个贡献”，用生长型页面规则。
- 如果页面负责“讲清一个具体问题”，不用。
- `index.md` 不只是链接列表，它也是收束页：既告诉读者“现在我们知道什么”，也告诉贡献者“下一步可以补什么”。

### 五层内容深度

本手册的内容全部由莞中人共建，但不是所有内容都应该写成同一种“经验贴”。每个核心页面都要尽量把同一件事拆成五层：

```
资料整理     → 我们整理了什么事实
解释框架     → 我们如何理解这些事实
亲历经验     → 莞中人的经历如何修正或补充理解
适用处境     → 这对不同莞中人分别意味着什么
下一步验证   → 读者接下来应该查什么、问谁、尝试什么
```

这五层不是要求每篇文章机械套五个标题，而是要求写作者知道自己在补哪一层。一个页面如果只有资料整理，会像百科；只有亲历经验，会像散乱帖子；只有解释框架，会像空泛建议；没有适用处境，就容易把个人经验误当标准答案；没有下一步验证，读者读完仍然不知道怎么行动。

**第一层：资料整理**

资料整理负责把事实、规则、流程、课程、路径、时间线说清楚。它可以来自公开资料，也可以来自校友整理，但必须尽量可核对。

应该写：

- 这个专业/学校/路径的基本事实是什么
- 关键流程、时间线、材料、课程或组织结构是什么
- 哪些信息每年可能变化，读者应该去哪里核对
- 哪些事实已经过时，是否需要标注年份

不应该写：

- 不标年份地维护每年变化的招生政策、分数线、项目名单
- 把单个校友的经历包装成普遍事实
- 只复制官网介绍，不解释它对读者有什么意义

**第二层：解释框架**

解释框架负责告诉读者“这些事实该怎么看”。它是手册区别于资料汇总的核心。

应该写：

- 读这个对象时应该问哪些问题
- 这个主题有哪些关键维度和权衡
- 相邻专业、学校、路径之间的真实差别是什么
- 哪些指标有用，哪些指标容易误导

不应该写：

- 只给结论，不说明判断依据
- 把复杂选择简化成排名、分数、薪资、名气单一维度
- 用过度绝对的语气替读者做决定

**第三层：亲历经验**

亲历经验负责把莞中人的真实经历放进来，补充和修正前两层。带有背景、选择、过程、结果和限制条件的样本进入 `cases/entries/`；局部观点、短方法或尚未形成样本的主题补充进入对应目录的 `perspectives/`；主干页可以引用二者，但不要复制完整正文。

应该写：

- 当事人的届别、背景、选择处境和时间
- 这段经历验证了什么，也反驳了什么
- 经验中的限制条件，例如学校、专业、年份、家庭、成绩、城市
- 失败、后悔、转向和反例

不应该写：

- 脱离背景引用一句“我觉得很好/很坑”
- 用单个成功案例推出普遍路径
- 放未经证实的传言、针对具体个人的负面评价

**第四层：适用处境**

适用处境负责提醒读者：同一条建议对不同人不一定成立。它把经验重新放回莞中学生可能面对的差异里。

应该写：

- 什么样的人适合，什么样的人需要谨慎
- 成绩、性格、家庭经济、城市偏好、风险承受力、专业背景如何改变结论
- 哪些前提变了，建议就不成立
- 哪些问题需要和家人、老师、学长学姐进一步确认

不应该写：

- 把“适合我”写成“适合所有莞中人”
- 回避代价、风险和不适合人群
- 用“看个人”结束，不给任何具体判断维度

**第五层：下一步验证**

下一步验证负责把阅读转化成行动。手册不替读者做决定，而是告诉他下一步该如何自己确认。

应该写：

- 下一步该看哪些页面、资料、课程、项目或案例
- 应该问谁，问什么问题
- 可以做什么低成本尝试，例如旁听课程、做小项目、联系校友、查培养方案
- 到哪个时间点应该重新评估

不应该写：

- 只说“多了解”“多问问”这种空话
- 不区分短期行动和长期准备
- 让读者以为读完一篇文章就完成了决策

**不同目录的五层侧重点**：

| 顶层目录 | 更重的层 | 说明 |
|---|---|---|
| `start-here/` | 解释框架、适用处境、下一步验证 | 入口页要先帮助读者摆脱高中惯性，学会使用手册 |
| `admissions/` | 解释框架、适用处境、下一步验证 | 志愿填报变化快，不维护实时政策，重点教判断和验证 |
| `majors/` | 解释框架、亲历经验、适用处境 | 专业认知要解释能力结构、路径分化和适合人群 |
| `universities/` | 资料整理、亲历经验、适用处境 | 学校/城市/学院生态需要事实和校友体验互相校正 |
| `campus-life/` | 资料整理、解释框架、亲历经验、下一步验证 | 大学生存要读懂制度、机会、人际和失败恢复机制，不做生活建议杂烩 |
| `pathways/` | 资料整理、解释框架、下一步验证 | 路径页要讲清机制、时间线、材料和执行检查点 |
| `cases/` | 亲历经验、适用处境 | 案例库保存莞中人样本，重点写清背景、选择、过程、结果和限制条件 |
| `commons/` | 资源、治理规则 | 共同体内容重在沉淀资源、贡献秩序和非路径型故事 |

### how-to-contribute.md 规范

**每个 C 类容器目录标配两件套：`index.md` + `how-to-contribute.md`。** 前者解释"这里放什么"（B 类整合口径），后者教会贡献者"怎么往里放东西"（B 类操作指南）。有了它，空文件夹不再冗余——它把「这个目录等着你来填」变成了「照着这三步就能填」。

**必须覆盖的七个问题**：

1. **这个目录放什么** — 一句话说清楚这个容器收什么类型的文章，给一两个具体例子
2. **文件命名规则** — 格式 + 示例（如 `2024-zhang-san-tencent-backend-internship.md`）
3. **文章模板** — 可直接复制粘贴的 markdown 骨架，含必填署名格式
4. **如何创建新文件夹** — 如果需要新建子分类，命名规则是什么、子文件夹里的 `index.md` 怎么写、父级 `index.md` 怎么加链接。**这是关键：让贡献者知道怎么"建造"还不存在的目录结构**
5. **如何更新 index.md** — A 类索引页的链接格式、加在哪个位置
6. **要不要改 mkdocs.yml** — **绝大多数情况下不需要**。C 类文件不逐一列入导航栏。只有当新增**顶级栏目**或**新的专业/学校入口**时才需要 PR mkdocs.yml
7. **提交流程** — fork → branch → commit → PR → review，一图流或三句话

**几种典型 how-to-contribute.md 的区别**：

| 容器类型 | 特殊说明 |
|----------|----------|
| `majors/domains/engineering/eecs/foundations/how-to-contribute.md` | 重点教：如何补充能力基础、课程/书/项目路线；如果能力分类不存在，怎么创建 `category/index.md` |
| `majors/domains/engineering/eecs/fields/how-to-contribute.md` | 重点教：如何判断一篇内容放 `perspectives/`，还是创建新的细分方向文件夹 |
| `universities/schools/sysu/perspectives/how-to-contribute.md` | 文件名格式 `[year]-[name-or-alias]-[campus-or-topic].md`；一个校区可多人写 |
| `universities/schools/sysu/programs/how-to-contribute.md` | **重点教文件夹创建**：如果要评价的学院/专业还没有文件夹，如何创建并命名（如 `computer-science/`），如何在 `programs/index.md` 加链接 |
| `universities/schools/sysu/admissions-context/how-to-contribute.md` | 文件名格式 `[year]-[name-or-alias]-[batch-type].md`；强调写明年份因为分数线每年变 |
| `admissions/perspectives/how-to-contribute.md` | 文件名格式 `[year]-[name-or-alias]-[topic].md`；可写个人复盘，也可写成体系的个人方法论 |
| `cases/how-to-contribute.md` | 重点教：莞中人样本如何写元信息、样本类型、背景、选择、过程、结果、限制条件，并更新多维索引 |
| `commons/stories/how-to-contribute.md` | 非路径型故事；文件名 `[year]-[name-or-alias]-[story-topic].md` |
| 其他专业容器（临床/金融/法学） | 参照 EECS 同位置 how-to-contribute.md，调整专业语境 |

**通用模板骨架**（每个 how-to-contribute.md 在此基础上改）：

```markdown
# 如何投稿：[栏目名称]

## 这个栏目放什么
（一句话，举两个具体例子）

## 命名规则
文件名：`[格式].md`
例如：`2024-zhang-san-tencent-backend-internship.md`

## 文章模板
复制下面的骨架开始写：

[markdown 模板，含署名区]

## 如何创建新文件夹（如果需要）
如果你要写的内容属于一个还不存在的子分类：
1. 创建文件夹，命名规则：[规则]
2. 在文件夹里创建 `index.md`：[模板]
3. 在父级 `index.md` 里加链接：[格式]

## 如何更新 index.md
在 `index.md` 的对应位置添加：
`- [你的标题](./你的文件名.md) — XX届 名字`

## 需要改 mkdocs.yml 吗？
不需要。C 类文件不逐一列入导航栏。
只有当你要新增**顶级栏目**或**新的专业/学校入口**时，才需要 PR mkdocs.yml。

## 提交流程
1. Fork 本仓库
2. 创建你的文章文件（和文件夹，如果需要）
3. 更新 index.md 加链接
4. 提交 PR，等待 review
```

### 三层归属模型

手册的核心逻辑：**路径机制归通用页，专业/学校特殊性归对象页，带背景和结果的莞中人样本归 `cases/`，局部观点和短方法归 `perspectives/`**。同一个问题可以在多个目录被提到，但每个目录只承担自己的那一层，不互相抢正文。

```
第一层：通用方法论     → 不假设读者学什么专业，讲清楚「怎么做」（B 类为主）
第二层：大类特殊性     → 假设读者已读过通用方法论，只写本专业的特殊性（B + C）
第三层：个人经验       → 有背景、过程、结果的样本进 cases/entries/；局部视角进对应 perspectives/（C 类）
```

**通用页的底线**：即使以链接为主，每个通用页必须有 200-500 字的核心方法论，不能让读者点进去只看到链接。

### majors/ 专业认知深度模型

`majors/` 的深度不靠把所有专业名无限铺开，而靠每一级目录承担不同认知任务：

```
学科大类页     → 讲清楚这个大类的气质、内部分支、适合谁、常见误解
专业群页       → 横向比较相邻专业，解释课程分化、能力门槛、路径差异
具体专业页     → 讲清楚这个专业学什么、怎么读、适合/不适合谁、出路是什么
署名观点页     → 保留个人经验、选择复盘和成体系但非共识的个人方法论
```

**学科大类页**（如 `majors/domains/engineering/index.md`）至少回答：

- 这个大类和相邻大类有什么本质区别（如工科 vs 理科、医学 vs 生物）
- 这个大类内部有哪些主要专业群，它们如何分布在理论/实践、软/硬、实验/项目等维度上
- 什么样的人适合进入这个大类，什么样的人需要谨慎
- 高中生最容易误解什么

**专业群页**（如 `majors/domains/engineering/eecs/index.md`）至少回答：

- 这个专业群包含哪些具体专业，为什么它们应该放在一起理解
- 相邻专业之间的区别是什么，哪些差异是真差异，哪些只是学校命名差异
- 共同课程、分化课程和核心能力门槛是什么
- 这个专业群的求职、科研、保研、考研、出国路径如何分化
- 哪些内容适合进入主干页，哪些应保留在 `perspectives/`

**具体专业页**（如 `majors/domains/medicine/clinical-medicine/index.md`）至少回答：

- 这个专业到底学什么，不只是专业介绍里的套话
- 大学几年会怎么过，最难的门槛是什么
- 适合什么样的人，不适合什么样的人
- 和相邻专业有什么区别
- 常见出路、路径风险和学校差异是什么
- 莞中人真实经验如何补充或修正主干判断

**perspectives/** 是署名个人视角区。它承载局部观点、短方法、个人判断框架或某个主题的补充；如果文章有具体背景、选择、过程、结果和限制条件，即使只是一段经历，也应进入 `cases/entries/`，专业页只做链接或摘要。只要还没有被整理成共识，就不强行揉进主干页；编委会可以从中提炼观点进入 B 类页面，但原文保留署名。

### fields/ 方向文件夹创建规则

`fields/` 用来承载“方向生态图”，不是把所有可能方向预先铺成空文件夹。规则是：**一级稳定方向预建，二级细分方向由内容触发创建。**

以 `majors/domains/engineering/eecs/fields/` 为例，预建的一级方向是：

```
ai-data-intelligence/
software-systems/
security-privacy/
hardware-embedded-physical/
human-media-interaction/
theory-foundations/
domain-computing/
```

每个一级方向的 `index.md` 负责列出方向地图、已有内容、缺口和征稿方向。细分方向先写在 `index.md` 的方向地图里，不默认建文件夹。

**先不要创建新文件夹的情况**：

- 只有一篇个人经历、个人观点或选择复盘
- 只是想补充一句“我做过这个方向”
- 方向边界还不清楚，和已有方向高度重叠
- 内容主要是主观叙述，没有资源、路径、比较或长期维护价值

这类内容优先放入对应一级方向的 `perspectives/`，文件名用：

```text
[year]-[name-or-alias]-[topic].md
```

**可以创建细分方向文件夹的情况**：

- 已经有多篇内容需要归档到同一方向
- 需要维护这个方向的资源、路线、岗位/研究入口或相邻方向比较
- 这个方向是长期稳定存在的认知入口，而不是一次性话题
- 上级 `index.md` 已经写不下，需要独立页面承载结构

**创建新细分方向文件夹的步骤**：

1. 在上级 `index.md` 检查是否已有相近方向，避免重复命名。
2. 用英文小写连字符命名，如 `generative-ai-llm/`、`cryptography/`、`distributed-systems/`。
3. 新文件夹至少包含 `index.md`；如果允许个人投稿，再包含 `perspectives/index.md` 和 `perspectives/how-to-contribute.md`。
4. 在上级 `index.md` 的方向地图中加链接，并写一句话说明这个方向解决什么问题。
5. 如果新增的是长期入口，而不是单篇个人文章，才考虑是否需要改 `mkdocs.yml`；默认不改。

**新方向 `index.md` 至少回答**：

- 这个方向解决什么问题
- 和相邻方向有什么区别
- 入门需要哪些基础能力
- 本科生可以从什么课程、项目或论文开始
- 典型研究问题、行业岗位或应用场景是什么
- 目前已有莞中人经验有哪些，缺什么

### 深度从哪来

手册的深度不从"预设所有主题"来，而从**层级化的分类容器**来：

- **知识分类深度**（借鉴 cs-self-learning）：`resources/programming-language/python/cs61a.md` — 大类 / 子类 / 具体资源，每个分类层级有 `index.md`
- **学科分类深度**：`majors/domains/engineering/eecs/programs/computer-science/` — 学科大类 / 专业群 / 具体专业，避免把临床医学、金融学、EECS 这类不同层级的对象并列
- **个人贡献深度**（借鉴 SJTU-Application / SUSTech-Application / SZU-FeiYue）：`cases/entries/2024-zhang-san-sysu-eecs-recommendation.md` — 莞中人样本集中入库，再被专业、学校、路径页面索引
- **机构深度**（借鉴 CS-BAOYAN-Wiki）：`universities/schools/sysu/programs/clinical-medicine/` — 一个学院可能是多个人贡献的入口

### 文件夹/文件决策规则

**需要容纳多个人独立贡献的，就是文件夹。内容整合为单一权威口径的，就是文件。**

额外硬约束：**不要为了“少建目录”而把复杂对象写成单个 `.md`。** 扁平文件只适合边界清楚、内容可被一篇整合文章讲完的主题；如果一个主题天然能继续拆出稳定子结构，就必须先考虑文件夹。

| 实体 | 决策 | 理由 |
|------|------|------|
| 学科大类（工科/理科/医学/经管等） | 文件夹 | 讲清楚大类气质、内部分支、适合谁，不直接承载个人经验 |
| 专业群（EECS/材料化工/法政等） | 文件夹 | 多个专业共享 orientation、programs、fields、foundations、outcomes 等专业语境 |
| 具体专业（临床医学/金融学/法学等） | 文件夹 | 讲清楚这个专业学什么、适合谁、常见误解和出路 |
| 学校（中大/华工/暨大） | 文件夹 | 多人写：整体体验、各学院评价、报考建议 |
| 学校的学院（中山医/岭院/计院） | 文件夹 | 可能多个人写同一个学院 |
| 知识分类（Python/ML/系统） | 文件夹 | 下面还有多门具体资源 |
| 样本库（cases/entries/） | 文件夹 | 带背景、过程、结果和限制条件的莞中人样本正本库，可多维索引 |
| 局部个人视角（perspectives/） | 文件夹 | 主题内的短观点、局部方法、尚未形成样本的补充，容器 = index.md + how-to-contribute.md |
| 具体资源推荐（CS61A, CS229） | 文件 | 一个人推荐一门课，后来者可改进正文 |
| 志愿填报/在校生存子主题 | 文件或文件夹 | 方法论用文件；可继续扩展、可容纳多人经验的主题用文件夹 |
| 通用路径主题（保研流程/简历写法/面试形式） | 文件夹或文件 | 简单流程可用文件；一旦包含材料、时间线、案例、专业差异链接，就必须用文件夹 |

**必须升格为文件夹的情况**：

- 主题内部包含多个稳定子能力或子方向，例如 `mathematics/` 下面应有 `linear-algebra/`、`probability-statistics/`，不能写成 `math.md`
- 主题需要承载路线、资源、案例、观点或长期更新，例如 `fields/theory-foundations/` 不能只写成一篇 `theory.md`
- 主题有横向比较任务，例如一个专业群内的相邻专业、一个方向内的相邻技术路线
- 主题未来可能容纳多人署名内容，需要 `perspectives/` 或 `how-to-contribute.md`
- 主题名本身是大类词、能力域词或生态词，例如 `foundations`、`systems`、`mathematics`、`pathways`、`research-paths`

**可以保持为单个 `.md` 的情况**：

- 它是一篇边界明确的 B 类整合文章，例如 `methodology.md`、`misconceptions.md`、`final-checklist.md`
- 它只是一个单点判断或单一流程，不需要承载子资源和多人贡献
- 它在上级目录中只是一个解释性页面，不承担“容器”职责

**判断顺序**：

1. 先问这个对象是不是“容器”。如果是，建文件夹。
2. 再问它是否包含稳定二级结构。如果包含，建文件夹。
3. 再问未来是否会有多人贡献或多篇内容。如果会，建文件夹并配 `index.md` / `how-to-contribute.md`。
4. 只有以上都否，才使用单个 `.md`。

### 跨目录归属规则

手册里很多主题天然会跨目录：简历、SOP、保研、考研、技术面试、案例面试、医学生规培、某个学校的保研氛围，都可能同时牵涉路径、专业、学校和个人经验。归属规则不是看关键词，而是看这篇内容主要回答什么问题。

**第一判断：这篇内容主要在讲什么？**

| 主要问题 | 归属目录 | 写法 |
|---|---|---|
| 这条路径怎么运作？ | `pathways/` | 写制度、时间线、材料、流程、检查点、常见坑 |
| 这个专业走这条路径有什么特殊性？ | `majors/.../outcomes/` | 写专业导致的差异：能力结构、评价标准、岗位/研究方向、材料写法 |
| 这所学校/学院提供了什么条件？ | `universities/schools/.../` | 写学校环境、学院资源、同伴氛围、政策语境、城市条件 |
| 大学期间怎么为它做日常准备？ | `campus-life/` | 写在校运行系统：学业制度、学习工作流、机会获取、人际协作、现实生活和失败恢复 |
| 某个人经历了一个有背景、过程和结果的选择/阶段/转向？ | `cases/entries/` | 保留样本完整性，不强行拆散；之后可以被专业、学校、路径主干页引用或提炼 |
| 某个人只想补充一个局部观点或方法？ | 最近的 `perspectives/` | 只承载短观点、局部方法、主题补充，不替代样本库 |

**第二判断：如果一个主题横跨多个目录，谁做主干？**

| 主题 | 主干放哪里 | 特殊性放哪里 | 个人经历放哪里 |
|---|---|---|---|
| 简历 | `pathways/career/application-materials/resume/` | 各专业 `outcomes/industry-roles/` 下写专业化简历，例如 EECS 项目经历、商科实习叙述、设计作品集 | 求职复盘、简历修改前后带结果的样本进 `cases/entries/`；单个简历观点进相关 `perspectives/` |
| SOP / PS / 文书 | `pathways/further-study/overseas/application-materials/` | 各专业 `outcomes/graduate-study/` 下写专业化叙事，例如理工科研究动机、文科问题意识、商科职业叙事 | 申请复盘、文书策略带背景和结果的样本进 `cases/entries/`；单个文书心得进相关 `perspectives/` |
| 保研 | `pathways/further-study/recommendation/` | 各专业 `outcomes/graduate-study/` 写夏令营偏好、面试题型、科研门槛 | 保研复盘、夏令营经历、失败恢复等样本进 `cases/entries/`；局部面试技巧进相关 `perspectives/` |
| 考研 | `pathways/further-study/entrance-exam/` | 各专业 `outcomes/graduate-study/` 写科目差异、复试方式、院校选择逻辑 | 考研复盘、跨考选择、复试经历等样本进 `cases/entries/`；单个科目心得进相关 `perspectives/` |
| 技术面试 | `pathways/career/interviews/technical/` 只写通用筛选形式 | EECS 等专业的 `outcomes/industry-roles/` 写具体题型、准备路线、岗位差异 | 求职复盘或单场面试带背景和结果的样本进 `cases/entries/`；题型总结进相关 `perspectives/` |
| 案例面试 | `pathways/career/interviews/case/` 只写通用形式 | 经管、咨询、金融等专业页写行业题型和训练方式 | 求职复盘或单场案例面试样本进 `cases/entries/`；训练方法进相关 `perspectives/` |
| 医学生规培/专培/执业路径 | 不强行放入通用 `career/` | `majors/domains/medicine/.../outcomes/` 作为主干，因为这是医学制度的一部分 | 医学路径、轮转、规培选择等样本进 `cases/entries/` |
| 学校保研资源 | `pathways/` 不维护某校细节 | `universities/schools/.../further-study-resources/` 或具体学院页 | 带背景和结果的个人样本进 `cases/entries/`；学校局部体验进学校 `perspectives/` |

**第三判断：通用页写到什么程度？**

通用页不能写得太空，也不能冒充专业页。它应该写清楚所有专业都会遇到的结构，但在关键位置提醒“不同专业差异很大”，并链接到专业页。

通用页应该写：

- 这个流程有哪些阶段
- 每个阶段读者要准备什么
- 哪些材料、时间线、筛选形式是跨专业都存在的
- 哪些地方一定要回到专业、学校或个人处境判断

通用页不应该写：

- 直接给所有专业统一模板
- 把 EECS、医学、文科、商科的材料写法混在一起
- 用一个人的成功路径代表所有专业
- 维护每年会变化的具体政策、项目名单或录取规则

**第四判断：专业页写到什么程度？**

专业页不是重写一遍通用流程，而是解释“为什么这个专业在这条路径上不一样”。例如普通简历页讲结构、阅读顺序和常见错误；EECS 简历页讲项目经历、技术栈、代码能力、算法/系统/AI 岗位差异；商科简历页讲实习叙述、量化结果、行业项目；医学页讲考试、轮转、规培和医院体系。

专业页应该写：

- 这个专业的评价标准是什么
- 哪些材料、经历或能力在本专业特别重要
- 和相邻专业相比，路径差异在哪里
- 这个专业的莞中人有哪些真实样本，样本之间有什么差异

专业页不应该写：

- 重复通用页已经讲清楚的流程
- 只说“本专业也要写简历/也要面试/也要科研”
- 只按单个学校或单个年份经验下结论

### 面经归属

| 面经类型 | 归属 | 理由 |
|----------|------|------|
| 行为面（自我介绍/优缺点/行为问题） | 通用求职页 `pathways/career/interviews/behavioral/` | 不分专业，但可链接到行业或专业特殊版本 |
| 技术面（coding/system design） | EECS 的 `outcomes/industry-roles/` 讲岗位差异；个人面经放 `perspectives/` | 专业语境，不重写通用求职方法 |
| 案例面（case interview） | 金融的 `outcomes/industry-roles/` 讲岗位差异；个人面经放 `perspectives/` | 专业语境，不重写通用求职方法 |
| 保研面经 | 通用流程归 `pathways/further-study/`；专业特殊性归 `outcomes/graduate-study/`；个人面经放 `perspectives/` | 隔行如隔山，但不重复通用流程 |
| 考研复试面经 | 同上 | 同上 |

### EECS 而非 CS/SE/EE 分列

计算机科学、软件工程、电子信息工程在课程上有差异，但在求职、科研、深造路径上高度重叠。按 EECS 大类组织，用一个概览页讲清楚三个专业的差异，子页则共享。对高中生来说，先理解"这个大类适不适合我"比纠结"CS 和 SE 选哪个"更有意义。

### 贡献模型

手册的贡献入口不在首页的"我要投稿"，而**分散嵌入在每个 C 类容器的 `how-to-contribute.md` 里**。这意味着：
- 贡献者浏览到感兴趣的区域（比如看到 EECS fields 或 perspectives），当场就知道怎么投稿
- 每个栏目的投稿指南是定制化的（命名规则、模板、文件夹创建方式各不相同）
- 维护工作量分散：每个 how-to-contribute.md 只覆盖它所在目录的规则，不需要一个巨大的统一投稿指南

但现实里不能假设所有人都会主动 fork、建目录、写 frontmatter。落地时要同时保留两条入口：

- **会 Git 的贡献者**：直接 PR 到对应目录，按 `how-to-contribute.md` 命名和更新索引。
- **不会 Git 或只愿意随手写的人**：先通过 WPS、问卷、微信群收集成原始材料，由维护者判断它属于案例、观点、主干页素材，还是只适合留在指北。

换句话说，目录结构是最终入库规则，不是要求每个贡献者一开始就懂的操作门槛。

**校友投稿型**（以 C 类文件为主，一人一个文件，零冲突）：
- 莞中人样本 — `cases/entries/` 接收带背景、选择、过程、结果和限制条件的样本，可以是完整路径、一次关键选择、一个阶段、一场失败恢复；`cases/indexes/` 只做索引，不复制正文
- 志愿填报 — `admissions/perspectives/` 接收署名个人视角；可以是一次决策复盘，也可以是一套完整方法论
- 专业认知 — 局部专业观点放 `perspectives/`；如果有具体背景、过程和结果，正本放 `cases/entries/`，专业页只索引
- 院校选择 — 局部就读观点放 `universities/schools/*/perspectives/`；带背景、过程和结果的学校体验样本放 `cases/entries/`
- 共同体故事 — `commons/stories/` 收非路径型故事，例如人物、群体、活动、共同体记忆

**编委会整合型**（以 B 类文件为主，多人编辑同一篇）：
- 开始阅读 — `start-here/` 整合莞中人进入大学后常见的思维惯性、信息素养问题和阅读路线
- 志愿填报主干页 — 任何人都可以 PR，但合并后必须变成统一口径；个人叙述保留在 `admissions/perspectives/`
- 在校生存 — 借鉴参考手册，编委会写 + 校友经验征集的引文
- 下一站路径 — `pathways/` 下整合深造、求职、gap year 等路径机制；专业特殊性只做链接，不抢专业页正文
- 各专业的 index.md — 专业概览、研究版图等（B 类整合）
- 案例索引 — `cases/indexes/` 由维护者或贡献者更新链接，按届别、大学、专业、路径、去向建立多维入口

**所谓"编委会"不是一个封闭的团队**——任何人都可以 PR B 类文件，只要遵循"整合而非堆砌"的规则。

### 内容落地闭环

飞跃手册真正能运转，靠的不是一次性把所有目录填满，而是让内容不断进入、被整理、被索引、被传播、再吸引新内容回来。

**最小闭环**：

1. 收集：通过 Git PR、WPS、问卷、微信群、私聊等方式收集原始材料。
2. 分流：维护者判断材料进入 `cases/entries/`、局部 `perspectives/`、B 类主干页，或保留在 WPS 指北。
3. 整理：按公开标准脱敏、补背景、补限制条件，必要时向作者追问。
4. 入库：放到主站对应目录，更新局部 `index.md`；案例同时补 frontmatter。
5. 索引：案例进入 `cases/indexes/`，主干页引用典型案例，避免正文重复。
6. 发布：MkDocs 站点生成公开版本，读者通过导航、搜索和索引阅读。
7. 告知：投稿说明写清楚公开贡献可能被莞言瓜语转载、摘编或二次传播。
8. 回流：校友群、线下沟通和公开页面继续征集缺口，让新作者补齐专业、学校、路径和案例。

**第一版不要追求全量覆盖**。第一版只需要证明这套闭环跑得通：

- 主站有清晰首页和导航，直接按新英文目录重建，不做旧路径兼容。
- 每个一级目录至少有 `index.md`，读者知道这个板块解决什么问题。
- C 类容器有 `how-to-contribute.md`，作者知道怎么投稿。
- `cases/entries/` 有模板，`cases/indexes/` 有人工维护的多维入口。
- 投稿说明提前告知：公开贡献可能被莞言瓜语在公众号或其他公开渠道转载、摘编或二次传播。

### mkdocs.yml 冲突预防

最容易冲突的不是内容文件，而是 `mkdocs.yml` 的 nav 部分。缓解策略：
- 每个 section 预留 "更多" 占位，新内容优先填进已有目录
- 不同 section 的贡献者改不同区域，天然不冲突（EECS 的人不改临床的 nav）
- 想新增 section 级别的条目，走 PR 由维护者合并
- **C 类文件的容器目录在 nav 中只列 `index.md`，不逐一列出 C 类文件**（减少 nav 改动频率）。`how-to-contribute.md` 中也明确告诉贡献者：你不需要改 mkdocs.yml

### 参考手册的结构借鉴

| 参考项目 | 借鉴点 |
|---------|--------|
| SurviveSJTUManual | 递进式分层（立志→访谈→生存→附录）；"敢说真话"的语调 |
| SJTU-Application | 出路×院系矩阵；广义申请定义（出国/直博/保研/考研/就业） |
| THU-feiyue-docs | 单一路径按真实申请时间线做深：前期判断、准备、材料、网申、面试、录取后 |
| SUSTech-Application / SZU-FeiYue | 案例库是核心资产，按路径、专业、年份、去向索引 |
| cs-self-learning | MkDocs Material 最佳实践；课程/领域地图体现学习顺序和先修关系 |
| HENU-CS-Survival | 小而精；生存篇+飞跃篇两段式 |
| HUST-EE-feiyue | 编委会模式；"传承是飞跃手册强大的理由" |

25 个参考项目的详细分析见 `references/CLAUDE.md`。

## 内容规范

### 每篇文章的结构

下面是通用骨架，实际页面不必机械使用同样标题，但至少要能对应“五层内容深度”里的若干层。短页面可以合并标题，长页面应该拆成子目录。

```
# 标题
> 一句话摘要

## 这是什么 / 这件事为什么重要
（资料整理：一句话说清楚对象、范围、适用年份或背景）

## 怎么看
（解释框架：关键维度、常见误区、相邻对象差异、判断依据）

## 莞中人怎么说
（亲历经验：精选 1-3 条校友真实体验，脱敏，署名，写清背景）

## 适合谁 / 不适合谁
（适用处境：哪些条件会改变结论，哪些读者需要谨慎）

## 下一步
（下一步验证：读完后可以看什么、问谁、查什么、试什么）

---
*最后更新：YYYY-MM-DD*
*贡献者：XX届 名字*
```

### 文风要求
- 说人话，不写百度百科体
- 可以口语化，但不碎片化
- 敢下判断："这个专业不适合数学不好的人"比"数学是重要的基础"有价值
- 控制篇幅：单篇 1000-3000 字，超过就拆成多篇

### 脱敏规则
从 WPS 校友经验中提取素材时：
- 保留：客观事实、通用经验、方法论
- 删除：针对具体个人的负面评价、未经证实的传言、群内才适合说的内幕
- 改写：把"我室友说这个老师很水"改成"部分课程教学质量参差不齐"

## 技术落地方案

这套方案的目标不是做一个复杂 CMS，而是把"校友愿意写一点"和"读者能长期找到东西"接起来。第一版优先选择低维护、可迁移、能被普通贡献者理解的技术栈。

### 一句话架构

```text
校友投稿 / WPS 原始材料 / 微信征集
        ↓
维护者分流、脱敏、补元数据
        ↓
Git 仓库中的 Markdown 正文
        ↓
MkDocs Material 构建公开主站
        ↓
静态站点部署 + 搜索引擎收录
        ↓
投稿说明告知公开转载边界
        ↓
新一轮校友投稿回流
```

### 技术选型

| 层 | 第一版选择 | 原因 | 暂不选择 |
|---|---|---|---|
| 内容格式 | Markdown + YAML frontmatter + LaTeX 数学公式 | 容易 PR、容易迁移、适合长期版本管理；公式用 MathJax 渲染 | 数据库 CMS、Notion/WPS 直接做公网正本；整篇 `.tex` 作为内容源 |
| 静态站 | MkDocs Material | 中文搜索、导航、移动端、部署成熟，适合知识库 | GitBook 作为主站、从零写前端 |
| 仓库正本 | Git 仓库 | 保留历史、方便 review、方便自动构建 | 微信群文件、WPS 文档作为正本 |
| 投稿入口 | Git PR + WPS/问卷/微信收稿 | 同时照顾会 Git 和不会 Git 的校友 | 只允许 PR |
| 发布方式 | GitHub Pages 第一版部署，Cloudflare Pages 备选 | 主仓、CI、评论都在 GitHub，第一版心智最简单 | 依赖 Gitee Pages 或自建服务器 |
| 评论系统 | giscus + GitHub Discussions | 免费、开源、无后端，csdiy 和清华飞跃都采用同类方案 | 自建评论系统、匿名评论、微信评论 |
| 私密内容 | 留在 WPS 指北 | 真正区分公开内容和群内内容 | 给静态站做伪登录 |

### 仓库与部署建议

第一版建议采用：

- **主仓**：GitHub 作为工程主仓，使用 GitHub Actions 构建和检查。
- **国内镜像**：第一版不必做；如后续需要，再把 Gitee 作为代码镜像，不作为 Pages 发布依赖。
- **主站部署**：第一版使用 GitHub Pages。它和 GitHub Actions、giscus、Discussions 在同一平台，维护成本最低；如果后续国内访问体验不稳定，再切到 Cloudflare Pages 或其他静态托管。
- **域名策略**：第一版可先用平台默认域名；如果要使用自有域名并接入国内 CDN，再单独处理备案、证书和 CDN 成本。
- **评论系统**：使用 giscus，把评论存到 GitHub Discussions；默认全站开启，页面可用 frontmatter `comments: false` 关闭。

这样做的原因是：MkDocs 生成的是普通静态文件，发布层可替换；第一版先减少外部平台数量。GitHub Pages 足够跑通主站，giscus 足够跑通评论。如果以后访问速度或域名需求变化，再迁移到 Cloudflare Pages，不影响内容结构。

### 本地开发与构建

第一版需要新增或整理：

```text
requirements.txt
docs/
mkdocs.yml
docs/stylesheets/extra.css
docs/assets/
```

建议依赖：

```text
mkdocs-material
mkdocs-git-revision-date-localized-plugin
pymdown-extensions
```

基础命令：

```bash
python -m venv .venv
source .venv/bin/activate  # Windows 使用 .venv\Scripts\activate
pip install -r requirements.txt
mkdocs serve
mkdocs build --strict
```

Markdown 是唯一主内容格式。允许在 Markdown 中写 LaTeX 数学公式：

- 行内公式：`$a^2 + b^2 = c^2$`
- 块级公式：

```text
$$
\int_a^b f(x)\,dx
$$
```

第一版只支持数学公式渲染，不支持把完整 `.tex` 文件作为网页内容源。

第一版 CI 只做三件事：

- `mkdocs build --strict`：确保导航、链接、Markdown 扩展不炸。
- 检查文件路径：英文小写连字符，不再新增拼音目录。
- 检查关键目录：一级目录和 C 类容器必须有 `index.md`，投稿容器必须有 `how-to-contribute.md`。

复杂的案例索引生成、frontmatter 全量校验、自动更新目录，先放在后续阶段。

### 内容进入系统的流程

**会 Git 的贡献者**：

1. 阅读对应目录的 `how-to-contribute.md`。
2. 在对应目录新建 Markdown 文件或子文件夹。
3. 补 frontmatter。
4. 更新局部 `index.md`。
5. 提 PR，维护者 review 后合并。

**不会 Git 的贡献者**：

1. 通过 WPS、问卷、微信群、私聊提交原始经验。
2. 维护者判断是否适合公开。
3. 适合公开的内容脱敏、补背景、补限制条件。
4. 维护者代入库，并在页面注明作者展示名或匿名。
5. 投稿说明提前告知：公开内容未来可能被莞言瓜语转载、摘编或二次传播。

不建议把未脱敏材料放进仓库，即使是 private repo 也不建议把它当作长期敏感信息库。

### Commit 与 PR 规范

公开仓库里的 commit 是协作记录，也可能成为后续转载、鸣谢和追溯作者贡献的依据。提交规范要服务三件事：看得懂、好 review、好追溯。

**commit message 格式**：

```text
type(scope): summary
```

常用 `type`：

- `content`：新增或大幅改写正文内容
- `case`：新增或修改莞中人样本
- `index`：更新索引页、目录页、链接列表
- `structure`：调整目录结构、移动页面、补 `index.md`
- `style`：视觉、CSS、排版，不改变内容含义
- `fix`：修错别字、坏链接、格式错误、事实错误
- `chore`：工具、依赖、配置、维护性改动

常用 `scope`：

- 一级目录：`start-here`、`admissions`、`majors`、`universities`、`campus-life`、`pathways`、`cases`、`commons`
- 具体对象：`eecs`、`sysu`、`recommendation`、`resume`
- 全局配置：`mkdocs`、`design`、`ci`

示例：

```text
case(cases): add anonymous sysu eecs recommendation sample
content(admissions): refine major-vs-school decision model
index(majors): add engineering domain entry links
structure(campus-life): add academic-system container
style(design): tune paper background and link colors
fix(universities): repair sysu perspective link
chore(mkdocs): rebuild navigation for English paths
```

**PR 拆分规则**：

- 一个 PR 尽量只做一类事情：新增案例、调整结构、修链接、改视觉，不要混在一起。
- 新增个人经验时，优先一个人一篇，避免多人共改同一个长文件。
- 改 `mkdocs.yml` 要谨慎；C 类个人文章默认不进主导航，只更新对应 `index.md`。
- 大规模重建目录时，PR 描述必须写清楚删除旧 `docs/`、新建目录范围和 `mkdocs.yml` 变化。

**公开转载告知**：

在 PR 模板、`how-to-contribute.md`、案例模板里都要写明：合并到飞跃手册主站的公开内容，可能被莞言瓜语转载、摘编、排版或二次传播；维护者会尊重作者署名、匿名和脱敏约定。

### 评论系统

第一版使用 giscus 接入 GitHub Discussions。评论是公开内容，不能当作私信、投稿箱或敏感信息收集入口。

落地方式：

- 在 GitHub 仓库开启 Discussions。
- 安装 giscus app。
- 新建评论分类，例如 `Comments` 或 `General`。
- 添加 `docs/overrides/partials/comments.html`。
- 在 `mkdocs.yml` 中设置 `theme.custom_dir: docs/overrides`。
- 默认全站开启评论；如果某页不适合评论，在 frontmatter 中写 `comments: false`。

评论默认开启范围：全站页面。

需要显式关闭评论的页面：

- 投稿说明、隐私边界、治理规则等不适合讨论分叉的页面
- 作者明确不希望开放讨论的个人案例
- 任何可能诱导读者留下隐私信息的页面

giscus 配置建议：

- `data-mapping="pathname"`：按页面路径绑定讨论，避免标题改动导致评论漂移。
- `data-input-position="bottom"`：评论框放在已有讨论之后，降低随手灌水。
- `data-reactions-enabled="1"`：允许轻量反馈。
- `data-lang="zh-CN"`。
- 跟随 MkDocs 明暗主题切换。
- `repo_id` / `category_id` 必须来自真实 GitHub 仓库和真实 Discussions 分类；仓库还没创建或当前账号不可见时，保持为空，不要编造。

评论治理：

- 评论区只用于公开补充、纠错、提问和资源补充。
- 不接受个人隐私、具体负面爆料、未经证实传闻。
- 维护者可以隐藏、删除或转移不适合公开的评论。
- 重要评论如果形成长期价值，应整理进正文或 `perspectives/`，不要让知识只留在评论区。

### 内容元数据

所有页面不强制同一套 frontmatter，但案例、个人观点、主干页应该有最小元数据，方便后续自动化。

案例页：

```yaml
case_id:
case_type:
title:
author_display:
anonymous:
dongguan_high_school_class_year:
college_entry_year:
undergraduate_university:
undergraduate_major:
pathways:
destinations:
keywords:
status: published
last_updated:
```

观点页：

```yaml
title:
author_display:
anonymous:
topic:
related_cases:
status: published
last_updated:
```

主干页：

```yaml
title:
owners:
status: seeded
last_updated:
```

`status` 只服务维护，不要在读者界面里机械展示。读者看到的应该是自然边界说明，例如"目前样本主要来自 EECS 和经管，医学和文科样本仍在征集"。

### 视觉风格

视觉上可以借鉴 Kami 和 open-design，但不要照搬。

**借鉴 Kami**：

- 纸感背景，不用纯白；页面应该像"值得保存的纸"，不是普通后台。
- 克制配色，以温暖中性色和深墨蓝作为主色。
- 强调中文长文可读性，减少炫技动画和大面积渐变。
- 让内容有编辑感：标题、引言、边注、表格、案例卡片都要像经过排版。

**借鉴 open-design**：

- 建一个项目自己的 `DESIGN.md`，把颜色、字体、组件、页面气质写成明确契约。
- 所有后续页面、投稿模板和公开转载物料都从同一套视觉原则出发。
- 设计资产应该能被人和 agent 共同理解，不依赖某个设计师的口头记忆。

**第一版视觉方向**：

```text
气质：克制、温暖、校友手册、编辑部感
背景：暖纸色，不用纯白
主色：深墨蓝，用于链接、重点和导航
辅助色：低饱和松绿或朱砂红，只用于少量状态和提示
字体：正文优先中文可读性，标题可使用更有书卷气的 serif
组件：少卡片、多正文层级；案例和索引可以使用轻边框列表
动效：只保留导航、搜索、目录展开等必要交互
```

落地文件：

```text
DESIGN.md
docs/stylesheets/extra.css
docs/assets/logo/
docs/assets/og/
```

注意：Kami 的部分字体有授权边界，不能直接照搬字体方案。第一版优先使用开源或系统字体，例如 Noto Serif SC、Noto Sans SC、Source Han Serif / Sans、LXGW WenKai 等，再按实际显示效果取舍。

### 资源型页面的组织方式

`build-your-own-x` 可以借鉴的不是视觉，而是"长期收集型目录"的组织方式：大类清楚、条目轻、链接稳定、贡献门槛低。

飞跃手册里适合采用这种模式的页面包括：

- `commons/resources/`：通用资源索引
- `campus-life/learning-workflow/tools/`：工具链资源
- `majors/.../foundations/`：课程、教材、项目资源
- `pathways/.../application-materials/`：模板、案例、参考材料

这类页面不要写成长文章，而应像"可维护目录"：

```text
方向说明
适合谁
入门顺序
推荐资源列表
莞中人补充说明
如何贡献新资源
```

### 公开转载告知

公众号和其他公开渠道由莞言瓜语统一维护，飞跃手册技术方案不设计它们的选题、排版或运营流程。仓库只需要保证贡献者在提交前知道：合并到主站的公开内容，未来可能被莞言瓜语转载、摘编或二次传播。

需要落到这些位置：

- PR 模板
- 案例模板
- 各 `how-to-contribute.md`
- 首页或贡献说明页

告知文字应清楚但不吓人：贡献者保留约定的署名、匿名和脱敏边界；维护者可以为了公开传播做摘要、排版和轻度改写，但不能改变原意。

### 权限与隐私

第一版不做登录，也不做静态站密码页。

原因很简单：静态站的前端密码不是真权限系统；真正登录会引入账号、权限、服务器和隐私责任，和公开手册第一版目标不匹配。

边界规则：

- 公开、可传播、已脱敏：进入飞跃手册主站。
- 真实但敏感、只适合群内：留在 WPS 指北。
- 未整理、未确认、未授权：不进入仓库。

### 第一版交付清单

真正开始落地时，第一版应完成这些文件和能力：

```text
requirements.txt
mkdocs.yml
DESIGN.md
docs/index.md
docs/stylesheets/extra.css
docs/start-here/index.md
docs/admissions/index.md
docs/majors/index.md
docs/universities/index.md
docs/campus-life/index.md
docs/pathways/index.md
docs/cases/index.md
docs/cases/entries/index.md
docs/cases/templates/index.md
docs/cases/indexes/index.md
docs/commons/registries/index.md
```

以及：

- 新导航使用英文路径；当前站点尚未上线，旧 `docs/` 可以直接删除后重建。
- 首页解释主站、WPS 指北和公开转载告知的关系。
- 每个 C 类容器有投稿说明。
- 投稿模板写清楚：公开贡献可能被莞言瓜语转载、摘编或二次传播。

### 分期实施

**第 0 阶段：技术确认**

- GitHub 主仓、GitHub Pages 第一版部署、giscus 评论系统已确定；Cloudflare Pages 只作为后续备选。
- 本地跑通 `mkdocs serve` 和 `mkdocs build --strict`。
- 确认 `DESIGN.md` 和 `extra.css` 的视觉基调。

**第 1 阶段：主站骨架**

- 按新架构创建英文目录。
- 重建 `mkdocs.yml`，只展示读者需要的主导航。
- 搭好案例模板、投稿模板、注册表入口。
- 直接删除旧 `docs/` 并重建，不做旧路径兼容、旧内容迁移和重定向。

**第 2 阶段：内容闭环**

- 先整理 3-5 个真实或半真实的样本，验证案例模板是否好用。
- 写 2-3 个主干页，例如 `start-here/`、`admissions/`、`majors/domains/engineering/eecs/`。
- 在投稿说明、案例模板和首页里补齐公开转载告知。

**第 3 阶段：轻自动化**

- 增加案例 frontmatter 校验。
- 生成 `cases/indexes/`。
- 检查目录命名和缺失 `index.md`。
- CI 提醒，不自动替贡献者改内容。

**第 4 阶段：长期维护**

- 每年高考季前做一次重点页面复核。
- 每学期整理一次新增案例、索引和公开页面缺口。
- 对过时内容标注年份和适用边界，不轻易删除。

### 自动化备忘（暂不实现）

`cases/` 的长期维护不应该完全依赖人工更新索引。当前阶段先手工维护，等真实案例数量起来后，再考虑设计脚本和 CI。

未来可设计的脚本：

- `scripts/generate_case_indexes.py`：扫描 `docs/cases/entries/` 的 frontmatter，生成 `cases/indexes/` 下的按届别、大学、专业、路径、去向、关键词索引
- `scripts/validate_cases.py`：检查样本是否包含必填 frontmatter，检查 `case_id` 是否和文件名一致
- `scripts/validate_architecture.py`：检查目录命名、复杂对象是否被过度扁平化、关键目录是否有 `index.md`
- `scripts/check_generated.py`：重新生成索引并检查是否有未提交差异，用于 CI 提醒贡献者更新索引

触发方式备忘：

- 本地手动：贡献者运行生成脚本
- 提交前：可选 pre-commit 钩子做校验
- PR / CI：检查案例元数据和索引是否最新

原则：生成索引可以进入仓库，但初期不要让机器人自动提交改动；CI 只提醒，不替贡献者改文件。

## 实施路径

### Phase 0：跑通最小闭环（当前先确认）
- [x] 选定 GitHub 主仓、GitHub Pages 第一版部署、giscus 评论系统
- [ ] 确认主站、WPS 指北和公开转载告知的边界
- [ ] 确认不会 Git 的校友也能通过 WPS / 问卷 / 微信提供材料
- [ ] 确认 PR 模板、案例模板和投稿说明都写明公开转载告知

### Phase 1：搭骨架（当前）
- [x] 确定目录结构和导航
- [x] 创建 MkDocs 项目骨架
- [x] 收集 25 个参考项目
- [ ] 写前言
- [ ] 按新架构创建目录结构和占位文件
- [ ] 更新 mkdocs.yml 导航
- [ ] 建好投稿模板、案例模板和公开转载告知

### Phase 2：填内容（持续）
- [ ] 开始阅读：先填 `start-here/` 的高考惯性、信息素养、提问方式和不同读者阅读路线
- [ ] 案例库：优先搭好 `cases/entries/` 模板和 `cases/indexes/` 多维索引，先让莞中人真实样本流动起来
- [ ] 决策流程：先填 `admissions/` 的自我评估、信息判断、决策模型、执行流程
- [ ] 专业世界：`majors/domains/engineering/eecs/` 作为标杆首批做深；其他学科大类先保留入口和征稿说明
- [ ] 大学世界：`universities/schools/` 先覆盖广东省内 6 所高校；方法论和维度页由编委会整合
- [ ] 大学行动：`campus-life/` 借鉴上交生存手册，写清学业制度、学习工作流、机会、人和组织、现实生活、失败后重建
- [ ] 下一站路径：`pathways/` 做深保研、考研、出国、博士、实习、求职等真实路径；专业特殊性回到各专业 `outcomes/`

### Phase 3：发布推广
- [ ] 静态站点上线
- [ ] 校友群推广
- [ ] 每年高考季重点推广

## 当前状态

- [x] 架构讨论完成（见本文档目录结构）
- [x] MkDocs 基础配置就绪（mkdocs.yml）
- [x] 参考项目已收集（25 个，见 references/sources/）
- [ ] 目录结构和占位文件待按新架构创建
- [ ] mkdocs.yml 导航待重建
- [ ] 前言待编写

## 参考项目

- 上交生存手册：`references/sources/SurviveSJTUManual/`
- 清华飞跃手册：`references/sources/THU-feiyue-docs/`
- 上交飞跃手册：`references/sources/SJTU-Application/`
- CS 保研 Wiki：`references/sources/CS-BAOYAN-Wiki/`
- CS 自学指南：`references/sources/cs-self-learning/`
- 全部 25 个参考项目分析：`references/CLAUDE.md`
- 莞中人指北（WPS 侧）：`../莞中人指北/`

