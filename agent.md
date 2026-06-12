# Agent Instructions

## School Identity

The school behind this handbook is 东莞中学, English name Dongguan High School. Do not write 东华中学, Donghua High School, GZ, gz, or any other mistaken or ambiguous school name. Use 莞中 only as an informal Chinese shorthand when the surrounding context is already clear.

## Architecture First

This project is a public guide built as a structured knowledge base, not a flat article collection. When editing `CLAUDE.md`, `mkdocs.yml`, or files under `docs/`, preserve the intended hierarchy before adding content.

## Reference Lessons

The reference projects are not just sources of topic names:

- SurviveSJTUManual: put mindset and judgment before practical tips.
- THU-feiyue-docs: make each stable path follow the real timeline a student experiences.
- SJTU-Application, SUSTech-Application, and SZU-FeiYue: treat complete alumni cases as a core asset, not an appendix.
- cs-self-learning: make field maps express prerequisites, sequence, and neighboring areas, not just labels.

Use these lessons when revising the architecture.

## Do Not Over-Flatten

Do not compress complex concepts into a row of `.md` files. If a topic naturally contains subtopics, capabilities, comparisons, resources, paths, or multiple contributors, make it a folder with an `index.md`.

Bad patterns:

```text
foundations/
├── math.md
├── programming.md
└── systems.md
```

Better pattern:

```text
foundations/
├── index.md
├── mathematics/
├── programming/
└── computer-systems/
```

## Folder vs File Rule

Use a folder when:

- The topic is a container, category, capability domain, professional field, school, major group, or recurring contribution area.
- The topic can be split into stable subtopics.
- The topic may need resources, routes, comparisons, cases, or perspectives.
- The topic may receive multiple independent contributions.

Use a single `.md` file only when:

- The topic is a bounded integrated article.
- It can be explained as one authoritative page.
- It does not need child pages or future contribution containers.

Default decision order:

1. Is this a container? If yes, create a folder.
2. Does it have stable substructure? If yes, create a folder.
3. Will multiple people contribute to it? If yes, create a folder with `index.md` and usually `how-to-contribute.md`.
4. Only then consider a single `.md` file.

## Pathways Depth

Treat `pathways/` as a real action-path system, not as a loose collection of articles. Further study and career topics should usually have nested structure for path selection, timelines, materials, screening stages, risks, and personal perspectives.

For example, do not leave:

```text
further-study/
├── recommendation/
├── entrance-exam/
└── overseas/
```

as the final shape. Each stable path should be able to grow its own `index.md`, preparation stages, materials, interviews or assessments, plus links to `cases/entries/` for complete alumni paths and local `perspectives/` for partial viewpoints.

## Start Here

`start-here/` is the entry for mindset transition from high school to university. It should cover common Dongguan High School student inertia such as gaokao-style thinking, passive learning, grade-only thinking, weak information literacy, and not knowing how to ask alumni or teachers for help.

Do not turn `start-here/` into motivational essays. It should help readers understand how to use the handbook and how to start asking better questions.

## Campus Life

Treat `campus-life/` as a map of how university actually operates, not a miscellaneous life-advice section. It should cover academic systems, learning workflows, opportunities, people and groups, practical life, and recovery from failure or wrong turns.

Use SurviveSJTUManual as the reference spirit: identify common wrong assumptions, explain the underlying system, and give concrete ways to verify, recover, or act. Do not flatten it into `learning.md`, `social.md`, and `mental-health.md`.

## Cases as Core Asset

Dongguan High School alumni samples belong in `cases/entries/` when they have a concrete person, background, choice or event, process, result, and limits. A sample can be a full path, a key decision, an important episode, a failure-and-recovery story, or a concrete experience of a major, school, project, or industry.

Use local `perspectives/` folders only for short topic-specific viewpoints, methods, or partial notes that do not yet have enough background and result to be a sample. If a contribution has background, process, result, and reflection, move it to `cases/entries/` and index it from the relevant major, university, pathway, or campus-life page.

Each case should have frontmatter with at least:

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
last_updated:
```

The body should preserve readability with sections like background, key choices, timeline, process, result, reflection, and who should or should not copy this path.

Use `case_type` values such as `full-path`, `decision`, `episode`, `failure-recovery`, or `object-experience`.

## Automation Backlog

Case index generation and validation scripts are currently a design memo, not an implementation task. Do not create scripts, CI, or pre-commit hooks unless the user explicitly asks to implement automation.

Future automation may include generating `cases/indexes/` from case frontmatter, validating required case metadata, checking architecture naming rules, and CI checks for stale generated indexes.

## Information Layers

Keep source content, indexes, navigation, and registries separate:

- Source content: Dongguan High School alumni samples live once in `cases/entries/`; main pages and local `perspectives/` contain their own scoped writing.
- Indexes: `cases/indexes/` only links, summarizes, and groups entries. Do not write new experience content there.
- Navigation: `mkdocs.yml` is a reader-facing route, not a mirror of every folder.
- Registries: `commons/registries/` should define stable codes for universities, majors, pathways, and keywords. Frontmatter should use registered codes when possible.

Main pages in `majors/`, `universities/`, and `pathways/` should help readers interpret cases, not try to cover every possible life path themselves.

## Growth Pages

Use growth-page rules only for container pages that collect and organize many contributions, such as major, school, pathway, campus-life scenario, and case index `index.md` pages.

Growth pages should state what the page is for, what is currently known, what cases or perspectives exist, what is missing, and how contributors can help. Mature status is an internal maintenance concept; expose it to readers as plain-language boundaries like "current examples mainly come from EECS and business; medicine and humanities samples are still limited."

Do not apply this pattern to concrete guides, checklists, registries, governance rules, or complete case entries. Those pages should be clear, complete, and actionable.

## Cross-Directory Ownership

When a topic could fit several places, choose ownership by the main question:

- `pathways/`: how a path works in general, including process, timeline, materials, and checkpoints.
- `majors/.../outcomes/`: how a major or discipline changes that path.
- `universities/schools/.../`: how a school, college, region, or campus environment changes that path.
- `campus-life/`: what a student does during college to prepare or survive.
- `cases/entries/`: one person's concrete sample with background, process, result, and limits.
- `perspectives/`: short local viewpoints, methods, or partial notes under a specific topic.

Do not duplicate the same full guide in multiple directories. Link across directories instead: the general resume page belongs under `pathways/career/application-materials/resume/`, while EECS-specific resume advice belongs under the EECS outcomes area.

## Contribution Containers

For C-class personal contributions, use a container with:

```text
index.md
how-to-contribute.md
```

For signed personal writing, use `cases/entries/` when it has enough background, process, result, and limits to be a sample, and use local `perspectives/` when it is a short topic-specific viewpoint or method note. A single personal article should not force a new topic folder. Create a new subfolder only when the direction needs multiple pages, resources, routes, or long-term maintenance.

## Landing Model

Do not assume every contributor will use Git correctly. The directory architecture is the final storage and publishing structure, not the only intake path. Keep two contribution routes alive:

- Git-capable contributors can submit PRs directly to the right folder.
- Casual contributors may send raw material through forms, WeChat groups, or private messages; maintainers then route it into cases, perspectives, main-page material, or the non-public material pool.

The first launch should prove the loop works: collect material, route it, desensitize it, publish it on the MkDocs site, index it, and tell contributors clearly that public merged content may be republished or excerpted by "莞言瓜语".

## Public Reposting Notice

Do not design WeChat official-account operations as part of the handbook technical architecture. "莞言瓜语" maintains those channels separately.

The repository only needs a clear contributor notice: once public content is merged into the handbook, it may later be republished, excerpted, reformatted, or lightly edited for public distribution by "莞言瓜语". Respect the agreed author display name, anonymity, and desensitization boundary.

Put this notice in PR templates, case templates, `how-to-contribute.md`, and the contribution page or homepage. Do not put sensitive non-public material into public reposting.

## Commit Standards

Use readable, traceable commit messages:

```text
type(scope): summary
```

Recommended types: `content`, `case`, `index`, `structure`, `style`, `fix`, `chore`.

Recommended scopes: top-level directories such as `start-here`, `admissions`, `majors`, `universities`, `campus-life`, `pathways`, `cases`, `commons`, or implementation scopes such as `mkdocs`, `design`, `ci`.

Keep PRs focused. Do not mix directory migration, visual styling, case content, and navigation rewrites in one PR unless the user explicitly asks for a combined landing PR.

## Deployment

Keep MkDocs Material as the static-site implementation unless the user explicitly changes direction. The repository is GitHub-first. Use GitHub Pages for the first public deployment because it keeps the repository, Actions, Discussions, and giscus comments in one platform. Keep Cloudflare Pages as a later fallback if access speed, domain, or CDN needs justify the extra platform. Do not recommend Gitee Pages as a default deployment target.

## Comments

Use giscus with GitHub Discussions for first-version comments. Implement it through `docs/overrides/partials/comments.html` and `theme.custom_dir: docs/overrides`.

Comments are enabled by default across the site. Disable comments per page with frontmatter:

```yaml
comments: false
```

Comments are public and must not be used for sensitive non-public material, private contact information, or unverified negative claims. Disable comments on pages such as contribution rules, privacy boundaries, governance rules, or any author-specific case page where the author does not want discussion.

Do not invent giscus IDs. Keep `extra.giscus.repo_id` and `extra.giscus.category_id` empty until the real public GitHub repository, Discussions feature, giscus app installation, and discussion category exist. Once they exist, fill the IDs from giscus or GitHub GraphQL. Use `mapping: pathname`, `input_position: bottom`, lazy loading, and theme syncing in the comments partial.

## Content Language

Use Markdown as the main content format, with YAML frontmatter for metadata. Support LaTeX-style math inside Markdown via MathJax and `pymdownx.arithmatex`, including inline `$...$` and block `$$...$$` formulas. Do not use full `.tex` files as first-version content sources.

## Visual System

Use `DESIGN.md` as the visual contract for the public handbook, contribution templates, and future CSS work. The intended tone is restrained, warm, paper-like, editorial, and readable for long Chinese text.

Borrow the spirit of Kami and open-design: a clear design system, paper-like warmth, ink-blue restraint, and reusable constraints that both humans and agents can follow. Do not copy proprietary or license-sensitive font choices. Prefer open or system fonts such as Noto Serif SC, Noto Sans SC, Source Han Serif/Sans, and LXGW WenKai after checking actual rendering.

When implementing the theme, start with MkDocs Material configuration and `docs/stylesheets/extra.css`. Do not replace MkDocs Material templates or add a separate frontend framework unless the user explicitly chooses a custom frontend.

## Naming

Use English lowercase kebab-case for paths:

```text
major-vs-school.md
theory-foundations/
generative-ai-llm/
```

Use Chinese for navigation labels and page titles.

## Media Assets

Do not place all content images in one global `docs/assets/` bucket. Use ownership-based media folders:

- Site-wide visual assets only: `docs/assets/logo/` and `docs/assets/site/`.
- Page or section images: the owning folder's `_assets/`, for example `docs/majors/domains/engineering/eecs/_assets/field-map.webp`.
- Shared images used by several pages: the nearest common parent folder's `_assets/shared/`.
- Case images: prefer folder-based cases such as `docs/cases/entries/2026-name-topic/index.md` with images in `docs/cases/entries/2026-name-topic/_assets/`.

Use relative Markdown paths such as `![](_assets/course-map.webp)`. Never link local absolute paths, WeChat temporary paths, or production-domain absolute URLs inside Markdown.

