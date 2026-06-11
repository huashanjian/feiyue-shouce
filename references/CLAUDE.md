# references/ — 参考项目目录

> 25 个高校飞跃手册 & 生存指南的 Git 子模块集合，为莞中人飞跃手册的编写提供内容参考、结构参照和灵感来源。

---

## 目录

- [如何使用这些参考项目](#如何使用这些参考项目)
- [参考资料全景图](#参考资料全景图)
- [分级评估](#分级评估)
- [按主题的内容映射](#按主题的内容映射)
- [单项目详细评估](#单项目详细评估)
  - [🏛️ Top/985 高校](#-top985-高校)
  - [🏫 211 高校](#-211-高校)
  - [🎓 广东高校](#-广东高校)
  - [🏗️ 其他高校](#-其他高校)
  - [📋 综合索引 & 方法论](#-综合索引--方法论)
- [内容覆盖度分析](#内容覆盖度分析)
- [从优秀项目中学习的要点](#从优秀项目中学习的要点)
- [维护说明](#维护说明)

---

## 如何使用这些参考项目

### 使用原则

1. **参考结构，不抄内容**：学习各家如何组织章节、如何平衡客观信息和个人体验，但内容必须原创
2. **素材来源**：当需要"莞中人怎么说"板块时，可以从这些手册中找校友体验的写作风格参考
3. **查漏补缺**：对照各家手册的目录，检查我们自己的大纲是否有遗漏
4. **脱敏参照**：学习上交生存手册的"说真话但不越界"的语调

### 查阅优先级

- **首选**（S 级，结构+内容双优）：上交生存手册、上交飞跃手册、清华飞跃手册、南科大飞跃手册
- **次选**（A 级，内容扎实）：华科电气飞跃手册、河大CS生存手册、安大飞跃手册、华东理工飞跃手册
- **补充**（B 级，特定角度有价值）：复旦数院飞跃手册、华工CS保研、同济面经、深大飞跃手册
- **按需**（C 级，内容较少或过时）：西交飞跃手册(2011)、大工飞跃手册(2018)、川师大/wiki类项目

---

## 参考资料全景图

```
references/
├── CLAUDE.md              ← 本文件：参考项目使用指南
└── sources/               ← 23 个高校飞跃手册 & 生存指南（Git 子模块）
    ├── SurviveSJTUManual/     ← 🥇 最值得学习：方法论 + 生存指南的标杆
    ├── SJTU-Application/      ← 🥈 飞跃手册的结构标杆（出国+保研+考研+就业）
    ├── THU-feiyue-docs/       ← 🥉 出国深造专题的标杆
    ├── Fudan-Math-Flight/     ← 数学专业的出国飞跃手册
    ├── XJTU-feiyue/           ← 2011年老牌飞跃手册，历史参考
    ├── DUT-overseas/          ← 大工飞跃手册（含2018 PDF）
    ├── HUST-CS-career/        ← 华科CS职业规划+飞跃手册（编写中，内容少）
    ├── HUST-EE-feiyue/        ← 华科电气飞跃手册（按专业组织的标杆）
    ├── HNU-fly-book/          ← 湖大飞跃手册（GitBook）
    ├── ECUST-Leap/            ← 华东理工飞跃手册（Docusaurus，出国+保研+考研+求职）
    ├── Tongji-interview/      ← 同济各厂面经汇总（求职专题标杆）
    ├── AHU-Impart-Inherit/    ← 安大飞跃手册（docsify，文理医工全覆盖）
    ├── Hainanu-Application/   ← 海南大学飞跃手册
    ├── HFUT-baoyan/           ← 合工大保研经验
    ├── HENU-CS-Survival/      ← 河大CS生存/飞跃手册（2026版，小而精）
    ├── SHU-fly/               ← 上大溯源手册（Hugo）
    ├── CS-BAOYAN-Wiki/         ← 🥇 全国最大CS保研Wiki，按届组织经验帖
    ├── SCUT-CS-baoyan/        ← 华工CS保研经验（广东985）
    ├── cs-self-learning/       ← 🥇 CS自学指南（csdiy.wiki），MkDocs Material标杆
    ├── SUSTech-Application/   ← 南科大飞跃手册（全链路标杆）
    ├── SZU-FeiYue/            ← 深大飞跃手册（广东双非）
    ├── XJTLU-wiki/            ← 西交利物浦wiki
    ├── SICNU-wiki/            ← 川师大wiki
    ├── FLY-NJTech/            ← 南工大飞跃手册（含2021 PDF）
    └── NWU-career-plan/       ← 全国高校飞跃手册索引（发现窗口）
```

---

## 分级评估

### S 级：结构+内容双优（必读）

| 项目 | 亮点 | 对我们的价值 |
|------|------|-------------|
| **SurviveSJTUManual** | 08年写成，GitBook持续维护。立志篇 → 访谈集 → 生存技巧 → 附录，四段式结构。敢说真话（"失败的思维方式""反对PUA""悲壮的学习方式"） | 大学生存指南的直接参照；"说真话但不过界"的语调标杆 |
| **SJTU-Application** | 涵盖出国、直博、保研、考研、就业五大出路。按院系+按出路双维度组织。模板源自南科大 | 深造指南 + 求职指南的结构参照；多出路并行的组织方式 |
| **THU-feiyue-docs** | 清华出国深造专题，MkDocs Material。系统覆盖语言考试、选校、文书、签证全流程 | 出国板块的内容框架可直接参考 |
| **SUSTech-Application** | 南科大飞跃手册，连续多年维护，全链路覆盖，是很多后续手册的模板来源 | 飞跃手册的"行业标准"模板；广东高校视角 |
| **CS-BAOYAN-Wiki** | 全国最大非商业CS保研社区，QQ群数万人。按届收集保研经验帖，覆盖清北到双非各层次 | CS保研板块的最全参考；社区运营模式参考 |
| **cs-self-learning** | PKUFlyingPig 的 CS 自学指南（csdiy.wiki），50k+ stars。MkDocs Material + i18n，覆盖CS全部子领域 | EECS 课程学习板块的直接参照；MkDocs Material 最佳实践 |

### A 级：某一方面突出（重点参考对应板块）

| 项目 | 亮点 | 对我们的价值 |
|------|------|-------------|
| **HUST-EE-feiyue** | 按专业组织，电气学科留学的完整指南。编委会模式、版权声明都可借鉴 | 专业认知篇的结构参照；编委会组织形式参考 |
| **HENU-CS-Survival** | 2026版，小而精。分生存篇和飞跃篇，内容直白（"如何刷GPA""选水课"） | "敢说真话"的写作范例；小体量项目的可行性证明 |
| **ECUST-Leap** | 出国/保研/考研/求职全覆盖，Docusaurus，有 GitHub Discussions 论坛 | 四合一结构；社区讨论机制 |
| **AHU-Impart-Inherit** | docsify，文理医工多学科覆盖，有独立域名 www.ahu.wiki | 多学科覆盖的组织方式；CDN加速的部署经验 |

### B 级：特定角度有用（按需查阅）

| 项目 | 亮点 | 对我们的价值 |
|------|------|-------------|
| **Fudan-Math-Flight** | 数学专业出国，受浙大和中科大飞跃手册启发 | 基础学科专业的飞跃手册样本 |
| **Tongji-interview** | 按公司组织的面经（字节、腾讯、阿里、华为、美团等）+ 知识点汇总 | 求职指南-面试板块的内容参考 |
| **SCUT-CS-baoyan** | 华工CS保研：保研基础知识、导师选择、陶瓷经验 | 广东985视角；保研板块内容参考 |
| **SHU-fly** | 上大"溯源手册"，Hugo 构建，按届组织 | 按届组织的另一种结构思路 |
| **SZU-FeiYue** | 深大飞跃手册，广东双非视角 | 广东非985/211高校的补充视角 |

### C 级：内容较少或过时（特定场景参考）

| 项目 | 状态 | 用途 |
|------|------|------|
| **XJTU-feiyue** | 2011年版，信息严重过时 | 历史参考；了解飞跃手册的早期形态 |
| **DUT-overseas** | 2018版，单一PDF | 保留作为早期飞跃手册的样本 |
| **FLY-NJTech** | 2021第一版，PDF形式 | 双非高校飞跃手册样本 |
| **XJTLU-wiki** / **SICNU-wiki** | wiki类，内容较泛 | 中外合作/师范类视角参考 |
| **HUST-CS-career** | 编写中，内容很少 | 关注其后续更新 |
| **HFUT-baoyan** | 保研经验汇总，内容有限 | 211高校保研视角 |
| **Hainanu-Application** | 内容较简 | 211高校飞跃手册样本 |
| **HNU-fly-book** | GitBook，国内访问不稳定 | 注意部署方案选择 |

---

## 按主题的内容映射

> 将 23 个参考项目的内容对应到我们手册的六大篇章，标注参考优先级。

### 📗 专业认知篇

| 子主题 | 最佳参考 | 次选参考 |
|--------|---------|---------|
| EECS 综合 | cs-self-learning（⭐课程体系标杆）, CS-BAOYAN-Wiki（⭐保研标杆） | HUST-CS-career, SCUT-CS-baoyan |
| 软件工程 | Tongji-interview（偏就业） | cs-self-learning 软件工程章 |
| 电子信息/电气 | HUST-EE-feiyue（⭐最完整） | - |
| 数学 | Fudan-Math-Flight | cs-self-learning 数学基础章 |
| 如何读懂一个专业（方法论） | SurviveSJTUManual 立志篇 | - |

### 📘 院校选择篇

| 子主题 | 最佳参考 | 次选参考 |
|--------|---------|---------|
| 客观信息+就读体验模板 | SJTU-Application（按院系组织） | SUSTech-Application |
| 广东省内高校 | SCUT-CS-baoyan（华工）, SZU-FeiYue（深大） | - |
| 如何选择大学（方法论） | SurviveSJTUManual 立志篇 | - |

### 🧭 大学生存指南

| 子主题 | 最佳参考 | 次选参考 |
|--------|---------|---------|
| 学习方法与时间管理 | SurviveSJTUManual 生存技巧 | HENU-CS-Survival S2, cs-self-learning 必学工具 |
| 社团、社交与人际关系 | SurviveSJTUManual 访谈集-管理者的智慧 | - |
| 转专业、辅修、双学位 | SurviveSJTUManual 附录-转专业 | - |
| 钱的事（生活费、奖学金、兼职） | SurviveSJTUManual | - |
| 心理与健康 | SurviveSJTUManual 立志篇（反对PUA等） | - |

### 🚀 深造指南

| 子主题 | 最佳参考 | 次选参考 |
|--------|---------|---------|
| 考研 | SurviveSJTUManual 访谈集-考研 | HENU-CS-Survival |
| 保研 | CS-BAOYAN-Wiki（⭐CS保研全网最全）, SCUT-CS-baoyan | HFUT-baoyan, SJTU-Application |
| 出国-语言考试 | THU-feiyue-docs, HUST-EE-feiyue | SUSTech-Application |
| 出国-选校/文书/费用 | THU-feiyue-docs | SJTU-Application, SUSTech-Application |
| Gap Year | （暂无专门参考，需从各手册零星搜集） | - |

### 💼 求职指南

| 子主题 | 最佳参考 | 次选参考 |
|--------|---------|---------|
| 实习 | SJTU-Application（实习板块） | SurviveSJTUManual 附录 |
| 简历与面试 | Tongji-interview（⭐按公司组织） | - |
| 行业选择 | SurviveSJTUManual 访谈集-关于工作 | - |
| 第一份工作 | SurviveSJTUManual 附录-已工作学长经验 | - |

### 📙 附录

| 子主题 | 最佳参考 | 次选参考 |
|--------|---------|---------|
| 校友故事 | SurviveSJTUManual 访谈集 | SJTU-Application 各院系分享 |
| 常用资源 | NWU-career-plan（论坛、工具链接） | THU-feiyue-docs |
| 贡献者名单 | 各家手册的致谢/编委会页面 | - |

---

## 单项目详细评估

### 🏛️ Top/985 高校

#### SurviveSJTUManual — 上交生存手册 ⭐ S级

- **仓库**: `https://github.com/SurviveSJTU/SurviveSJTUManual`
- **年份**: 2008年原版，持续维护中
- **技术**: GitBook
- **结构**: 序 → 立志篇(11篇) → 访谈集(6大主题) → 生存技巧(5大主题) → 附录(8大主题)
- **内容规模**: 约60+篇文章
- **独特价值**:
  - 中国高校生存手册的开创者，影响了后来几乎所有飞跃手册
  - "立志篇"是这本书的灵魂——不是教你怎么做，而是教你怎么想
  - 敢写"失败的思维方式""悲壮的学习方式""反对PUA"这种标题
  - 附录涵盖转专业、实习、本科转学、社团、通识课
- **对我们项目的意义**: 大学生存指南的标杆，也是"敢说真话"的语调标杆
- **注意**: 部分内容以上海交大特定政策和环境为背景，迁移时需注意通用化

#### SJTU-Application — 上交飞跃手册 ⭐ S级

- **仓库**: `https://github.com/SurviveSJTU/SJTU-Application`
- **技术**: docsify
- **模板来源**: 南科大飞跃手册
- **结构**: 按五大出路组织（出国、直博、保研、考研、就业）+ 按院系组织
- **独特价值**:
  - "申请"的定义扩展为广义：出国+直博+保研+考研+就业
  - 按院系组织（电院、机动、密院、安泰...），有具体的专业+出路交叉内容
  - 早期保留了南科大同学的投稿作为样本（非常好的 onboarding 策略）
  - 有明确的时效性提醒（"20fall是史上最难，但21fall可能更难"）
- **对我们项目的意义**: 深造指南+求职指南的结构标杆；多出路+多院系的矩阵式组织

#### THU-feiyue-docs — 清华飞跃手册 ⭐ S级

- **仓库**: `https://github.com/THU-feiyue/docs`
- **技术**: MkDocs Material（和我们一样！）
- **结构**: 出国深造全流程：前期准备 → 语言考试 → 选校 → 文书 → 网申 → 签证 → 行前
- **独特价值**:
  - 专注出国，深度足够
  - MkDocs Material 的使用经验可直接借鉴
  - 内容质量高，清华校友撰写
- **对我们项目的意义**: 出国板块的内容框架可直接参考；MkDocs Material 部署参考

#### Fudan-Math-Flight — 复旦数院飞跃手册

- **仓库**: `https://github.com/iwannabethe/Flight-Manual-FudanSMS`
- **年份**: 受浙大和中科大飞跃手册启发
- **独特价值**: 数学专业的出国飞跃手册，展示了基础学科如何做飞跃手册
- **对我们项目的意义**: 专业认知篇中数学类专业的参考

#### HUST-CS-career — 华科CS职业规划

- **仓库**: `https://github.com/heptagonhust/career_plan`
- **状态**: 编写中，内容较少
- **结构**: 工作与实习 + 飞跃计划（出国/保研/考研）
- **对我们项目的意义**: 关注后续更新；计算机专业的框架参考

#### HUST-EE-feiyue — 华科电气飞跃手册 ⭐ A级

- **仓库**: `https://github.com/LHYi/Feiyue-for-ECE`
- **年份**: 2020
- **作者**: 华科电气学院9位16级本科生，学院支持
- **独特价值**:
  - 按学科专业组织的标杆
  - 编委会模式描述非常详细（主编、编委、特邀顾问的分工）
  - 版权声明清晰（CC + 学院授权）
  - 前言写得很好："传承是飞跃手册强大的理由"
- **对我们项目的意义**: 专业认知篇的组织形式参考；编委会运营参考

#### HNU-fly-book — 湖大飞跃手册

- **仓库**: `https://github.com/juwentao/HNU-fly-book`
- **技术**: GitBook
- **状态**: 国内访问不稳定，需刷新
- **对我们项目的意义**: GitBook 部署的经验教训（我们应避免使用国内访问不稳定的方案）

#### 同济大学

- **Tongji-interview** — 同济面经汇总 ⭐ A级（求职板块）
  - **仓库**: `https://github.com/wenjunBZ/RushForOffer`
  - **内容**: 按公司组织的面经（字节、腾讯、阿里、百度、华为、美团、网易等）+ "offer备战手册" + 知识点汇总
  - **独特价值**: 求职面试板块最系统的一个参考
  - **对我们项目的意义**: 求职指南-简历与面试板块的内容标杆

- **Tongji-baoyan** — 同济软院保研
  - **仓库**: `https://github.com/doubleZ0108/3Months-Farewell-3Years.git`
  - **状态**: ⚠️ 子模块添加失败（checkout 错误），未纳入

#### XJTU-feiyue — 西交飞跃手册

- **仓库**: `https://github.com/eeyes-net/feiyue-2011-05`
- **年份**: 2011年
- **状态**: 严重过时
- **对我们项目的意义**: 历史参考；了解中国高校飞跃手册的早期形态；编码有乱码

#### DUT-overseas — 大工飞跃手册

- **仓库**: `https://github.com/alexedinburgh/dutOverseas`
- **年份**: 2018年版
- **内容**: 2017-2018两年的飞跃手册，含PDF
- **对我们项目的意义**: 了解早期飞跃手册的形态

### 🏫 211 高校

#### ECUST-Leap — 华东理工飞跃手册 ⭐ A级

- **仓库**: `https://github.com/ECUST-Leap/ecust-leap.github.io`
- **技术**: Docusaurus
- **结构**: 出国 + 保研 + 考研 + 求职，四合一全覆盖
- **独特价值**:
  - 有 GitHub Discussions 作为社区论坛
  - Docusaurus 部署经验
- **对我们项目的意义**: 四合一结构参考；社区运营参考

#### AHU-Impart-Inherit — 安大飞跃手册 ⭐ A级

- **仓库**: `https://github.com/AHUer-LeapLap/Impart-Inherit`
- **技术**: docsify
- **域名**: www.ahu.wiki（独立域名，CDN加速）
- **独特价值**: 文理医工多学科覆盖；技术支持描述详细
- **对我们项目的意义**: 多学科覆盖的组织方式；CDN/域名部署经验

#### HENU-CS-Survival — 河大CS生存/飞跃手册 ⭐ A级

- **仓库**: `https://github.com/HENU-CS/SurvivalHandbook`
- **年份**: 2026版
- **结构**: S1 前言 → S2 生存篇（基础学习/考研/保研/FAQ）→ S3 飞跃篇（基础/硕士/博士/FAQ）
- **独特价值**:
  - 小而精（体量小但每篇都有干货）
  - 敢写"如何刷GPA""选水课""挂科重修"等实操内容
  - 用 CC BY-SA 4.0 协议，鼓励复用
  - 2026版，时效性最好
- **对我们项目的意义**: 小体量项目也能做好"敢说真话"的范例

#### SHU-fly — 上大溯源手册

- **仓库**: `https://github.com/shuosc/fly`
- **技术**: Hugo
- **独特价值**: 按届组织（不同于其他手册的按主题组织），有溯源的视角
- **对我们项目的意义**: 另一种结构思路的参考

#### HFUT-baoyan — 合工大保研经验

- **仓库**: `https://github.com/PhelixChen/baoyan`
- **内容**: 合工大校友保研经验文章
- **对我们项目的意义**: 211高校保研视角

#### Hainanu-Application — 海南大学飞跃手册

- **仓库**: `https://github.com/Hainanu-Application/Hainanu-Application.github.io`
- **状态**: 内容较简
- **对我们项目的意义**: 211高校飞跃手册的部署参考

### 🎓 广东高校

#### SCUT-CS-baoyan — 华工CS保研 ⭐ 广东重点参考

- **仓库**: `https://github.com/fjchange/SCUT_CS_baoyan`
- **内容**: 保研基础知识 + 接收函/陶瓷经验 + 导师和方向选择
- **独特价值**: 广东省内唯一985的计算机保研经验
- **对我们项目的意义**: 广东高校视角；保研板块的内容参考（莞中学生最可能去的就是广东高校）

#### SUSTech-Application — 南科大飞跃手册 ⭐ S级

- **仓库**: `https://github.com/SUSTech-Application/SUSTechapplication`
- **技术**: 自建站点（后续被多所高校手册复用模板）
- **独特价值**:
  - 连续多年维护（2019 Fall 起），每年更新
  - 全链路覆盖：申请前 → 申请中 → 申请后
  - 模板被上交、安大等多校复用，已成为事实标准
- **对我们项目的意义**: 飞跃手册的"行业标准"模板；广东高校视角

#### SZU-FeiYue — 深大飞跃手册

- **仓库**: `https://github.com/SZU-FeiYue/docs`
- **状态**: 持续更新中
- **独特价值**: 广东双非高校的飞跃手册
- **对我们项目的意义**: 莞中学生很大比例会去深大，这是最直接的参照之一

### 🏗️ 其他高校

#### XJTLU-wiki — 西交利物浦 Wiki

- **仓库**: `https://github.com/awesome-xjtlu/wiki`
- **独特价值**: 中外合作办学视角
- **对我们项目的意义**: 中外合作办学这一特殊类型的选择参考

#### SICNU-wiki — 川师大 Wiki

- **仓库**: `https://github.com/SICNU-Application/wiki-SICNU`
- **独特价值**: 师范类高校飞跃手册
- **对我们项目的意义**: 师范类高校视角

#### FLY-NJTech — 南工大飞跃手册

- **仓库**: `https://github.com/yaoshun123/FLY_NJTech`
- **年份**: 2021第一版
- **格式**: PDF
- **对我们项目的意义**: 双非高校飞跃手册样本；含工作开展文档

### 📋 综合索引 & 方法论

#### NWU-career-plan — 全国高校飞跃手册索引

- **仓库**: `https://github.com/nwuzmedoutlook/career-plan`
- **内容**: 汇总了30+所高校的飞跃手册链接 + 留学论坛/工具资源
- **独特价值**:
  - 按高校层次分类（Top/985/211/其他）
  - 收录了留学论坛（ChaseDream、一亩三分地、The GradCafe）、保研论坛、考研论坛
  - 收录了导师评价网、科研经费查询等实用工具
  - 有润学、欧洲留学、电力电子等专题资源
- **对我们项目的意义**: 发现更多参考项目的窗口；附录-常用资源的内容来源

#### CS-BAOYAN-Wiki — 全国计算机保研 Wiki ⭐ S级

- **仓库**: `https://github.com/CS-BAOYAN/CS-BAOYAN-Wiki`
- **技术**: Astro (Starlight)
- **年份**: 2024年起长期维护（前身为 CS-BAOYAN-2024/2025 系列）
- **规模**: 全国最大非商业CS保研社区，4个QQ群数万人
- **结构**: 按届组织经验帖 + 保研攻略 + 推荐资料 + 导师评价
- **独特价值**:
  - CS保研领域最系统的经验集合，覆盖从清北到双非各层次
  - 社区驱动模式成熟（QQ群 + GitHub + 网站三位一体）
  - 按届组织保证了内容时效性
- **对我们项目的意义**: EECS-深造路径/保研板块的最全参考；社区运营+内容征集模式参考

#### cs-self-learning — CS 自学指南 ⭐ S级

- **仓库**: `https://github.com/PKUFlyingPig/cs-self-learning`
- **技术**: MkDocs Material + i18n（和我们一样！）
- **域名**: csdiy.wiki
- **作者**: PKUFlyingPig（北大校友）
- **规模**: 50k+ stars，CS自学领域最具影响力的中文项目
- **结构**: 必学工具 → 数学基础 → 编程入门 → 电子基础 → 数据结构与算法 → 软件工程 → 体系结构/OS/网络/数据库/编译 → AI/ML/DL → 后记
- **独特价值**:
  - MkDocs Material 的最佳实践案例（i18n双语、search、git-revision-date、minify）
  - 每篇 = 一门世界名校CS课程的客观评价 + 学习建议，是「敢下判断」的典范
  - 有完整的贡献模板（template.md）和协作规范
  - "必学工具"章节（翻墙/Git/Vim/LaTeX/Docker等）可直接参考
- **对我们项目的意义**: EECS 课程学习/自学的直接参照；MkDocs Material 部署和配置参考；贡献模板设计参考

---

## 内容覆盖度分析

> 将 25 个参考项目的内容覆盖到我们手册七篇章，标注覆盖程度。

| 我们的篇章 | 覆盖程度 | 说明 |
|-----------|:--------:|------|
| 前言 | ⭐ | 各家前言都写得好（HUST-EE-feiyue、SJTU-Application），可学习如何写前言 |
| 专业认知 | ⭐⭐⭐⭐ | cs-self-learning（EECS课程体系标杆）、CS-BAOYAN-Wiki（CS保研标杆）、HUST-EE-feiyue（电气） |
| 院校选择 | ⭐ | 只有按"母校"组织的视角，没有跨校比较/选校方法论 |
| 志愿填报 | — | 所有参考手册都不覆盖（受众已是大学生），完全原创 |
| 在校生存 | ⭐⭐⭐ | 上交生存手册覆盖面最全，cs-self-learning 补充了工具链和学习工作流 |
| 深造 | ⭐⭐⭐⭐⭐ | 各家手册核心领域；CS-BAOYAN-Wiki 补强了CS保研板块 |
| 求职 | ⭐⭐ | 同济面经最系统，各家有零星覆盖，缺乏系统性 |
| 附录 | ⭐⭐ | 各家附录差异大，上交生存手册附录最丰富 |

### 主要缺口（需要我们原创填补）

1. **院校选择方法论**：所有手册都是"本校学生如何申请外校"，没有"高中生如何选大学"的视角
2. **跨校比较**：没有任何手册做高校之间的横向比较
3. **高中生视角**：所有手册的受众都是大学生，没有面向高中生的内容
4. **家长视角**：完全没有
5. **广东省系统性覆盖**：只有华工和深大两个点，缺少中大、暨大、华师、广外、汕大等
6. **文科专业**：绝大多数手册是理工科视角
7. **Gap Year**：几乎没有专门讨论
8. **心理与健康**：仅上交生存手册略有涉及

---

## 从优秀项目中学习的要点

### 结构设计

1. **多维度组织**（学 SJTU-Application）：按出路 × 按院系，矩阵式
2. **分层设计**（学 SurviveSJTUManual）：立志（why）→ 生存（how）→ 飞跃（where），层层递进
3. **时效性标注**（学 SJTU-Application）：在文章开篇标注"此内容适合XX届参考"
4. **下一步导航**（学各家）：每篇末尾给出"读完这篇后可以看什么"

### 内容语调

1. **敢下判断**（学 SurviveSJTUManual）：
   - ✅ "这个专业不适合数学不好的人"
   - ❌ "数学是重要的基础"
2. **说人话**（学 HENU-CS-Survival）：
   - ✅ "选水课就能把绩点保持在90分以上"
   - ❌ "建议同学们合理规划课程选择以优化绩点表现"
3. **标注不确定性**（学 SJTU-Application）：
   - "20fall是史上最难申请的一年，但21fall可能更难"

### 技术选型

1. **优先国内可访问**：避免 GitBook（湖大手册访问不稳定）；MkDocs Material（清华方案、cs-self-learning）或 docsify（上交方案）经验证
2. **MkDocs Material 参考**：cs-self-learning 提供了 i18n、search、git-revision-date、minify 等插件的最佳实践
3. **有论坛/讨论区**：华东理工用 GitHub Discussions 做社区；CS-BAOYAN-Wiki 用 QQ 群 + GitHub 三位一体
4. **独立域名 + CDN**：安大手册的 www.ahu.wiki；cs-self-learning 的 csdiy.wiki

### 协作机制

1. **编委会模式**（学 HUST-EE-feiyue）：主编 + 编委 + 特邀顾问
2. **逐年迭代**（学 SUSTech-Application）：每年 Fall 出一版，保留历史版本
3. **Onboarding 样本**（学 SJTU-Application）：早期保留其他学校投稿作为样本，降低参与门槛

### 可持续发展

1. **署名机制**（学各家）：XX届 + 名字（允许化名）
2. **过时标注而非删除**（CLAUDE.md 设计原则已覆盖）
3. **开源协议**：CC BY-SA 4.0（河大CS使用）是合适的协议

---

## 维护说明

### 更新子模块

```bash
# 更新所有子模块到最新
git submodule update --remote

# 更新单个子模块
cd references/sources/SUSTech-Application && git pull origin main
```

### 添加新参考项目

```bash
git submodule add <repo-url> references/sources/<name>
```

添加后需要更新此文档。

### 注意事项

- 这 25 个仓库是外部维护的项目，随时可能变更、归档或删除
- 如果某个仓库失效，在 `.gitmodules` 中移除，并在此文档中标注为"已失效"
- 不要直接修改 `references/sources/` 下的任何文件（它们属于各自的子模块仓库）
- 如果要基于某个参考项目做本地笔记，放在 `references/notes/` 目录下

---

*最后更新：2026-06-08*
*整理者：Claude (辅助)*
