---
comments: false
---

# 评论规则

评论区使用 giscus，把页面讨论保存到 GitHub Discussions。评论是公开内容，不是私信、投稿箱或敏感信息收集入口。

## 接入步骤

1. 创建或确认 GitHub 仓库：`huashanjian/feiyue-shouce`。
2. 确认仓库为 public，并在仓库设置中开启 Discussions。
3. 安装 giscus GitHub App，并允许访问该仓库。
4. 使用讨论分类。当前第一版使用 GitHub 默认分类 `General`；如后续在网页端新建 `Comments` 分类，需要同步更新 `mkdocs.yml` 的 `category` 与 `category_id`。
5. 从 giscus 配置页或 GitHub API 取得 `repo_id` 与 `category_id`。
6. 填入 `mkdocs.yml` 的 `extra.giscus`。

仓库还没有创建或当前账号不可见时，不要编造 `repo_id` / `category_id`。保持为空，页面会显示接入状态；等仓库、Discussions 和分类都准备好后再填。

可用 GitHub CLI 查询 ID：

```bash
gh api graphql \
  -F owner=huashanjian \
  -F name=feiyue-shouce \
  -f query='
query($owner: String!, $name: String!) {
  repository(owner: $owner, name: $name) {
    id
    discussionCategories(first: 20) {
      nodes {
        id
        name
      }
    }
  }
}'
```

## 配置约定

- `mapping: pathname`：按页面路径绑定讨论，标题调整不影响原评论。
- `input_position: bottom`：先看已有讨论，再发言。
- `loading: lazy`：评论区懒加载，减少页面首屏负担。
- `reactions_enabled: "1"`：允许对主讨论做表情反馈。
- `repo_id` / `category_id`：必须来自真实 GitHub 仓库和真实 Discussions 分类。

## 关闭评论

默认全站开启评论。不适合评论的页面，在 frontmatter 中写：

```yaml
---
comments: false
---
```

治理规则、投稿模板、隐私边界页，以及作者明确不希望开放讨论的案例页，应关闭评论。

## 讨论边界

评论区适合：

- 公开纠错
- 补充资源
- 提问和追问
- 说明某段内容的适用边界

评论区不适合：

- 发布私人联系方式
- 透露未脱敏经历
- 评价具体个人
- 发表未经核实的负面信息
- 提交只适合非公开讨论的材料

有长期价值的评论，应由维护者整理进正文、索引页或经验文章。评论区负责承接讨论，不负责保存最终知识。
