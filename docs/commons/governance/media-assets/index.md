---
comments: false
---

# 图片与附件规则

## 存放原则

内容图片不要统一堆进一个大的 `docs/assets/`。图片应尽量靠近拥有它的页面，方便搬迁、审稿、删除和溯源。

## 推荐位置

- 全站视觉资产：`docs/assets/logo/`、`docs/assets/site/`，只放站点标识、主题图标、公共社交封面等。
- 文件夹页面图片：放在该页面所在目录的 `_assets/`，例如 `docs/majors/domains/engineering/eecs/_assets/field-map.webp`。
- 子方向图片：放在对应子方向目录的 `_assets/`，例如 `docs/pathways/career/interviews/technical/_assets/interview-flow.webp`。
- 案例图片：优先把案例做成文件夹页面，例如 `docs/cases/entries/2026-name-topic/index.md`，图片放在同目录 `_assets/`。
- 多页共用图片：放在最近共同父目录的 `_assets/shared/`，不要提升到全站 assets。

## 命名规则

图片文件使用英文小写连字符：`timeline-01.webp`、`course-map.png`。不要使用微信截图默认名、中文空格名或含个人隐私的文件名。

## 引用规则

Markdown 中优先使用相对路径：

```md
![课程结构图](_assets/course-map.webp)
```

不要使用本机绝对路径，也不要使用部署域名的绝对 URL。

## 隐私边界

上传前必须清理姓名、手机号、微信号、学号、准考证号、定位、证件照、聊天头像和未授权肖像。含敏感信息的原图不进入仓库。
