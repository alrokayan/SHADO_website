# SHADO website

Read `../SHADO/ops/constitution/AGENTS.md` and its required PM policy.
These scoped rules supplement the shared constitution.

## Architecture and content

- This is a Hugo site. Follow the version pinned in the existing build workflow
  and README; do not introduce a Node/Sass build pipeline without a task need.
- Edit `content/` and `data/home.yaml` for copy, `layouts/` for templates,
  `assets/css/` and `assets/js/` for appearance/behavior, `hugo.toml` for public
  configuration, and `static/images/` for image assets.
- Preserve the established brand, accessibility and reduced-motion behavior.
- Edit source rather than generated `public/` or `resources/` content.
- Verify product claims against current SHADO authority. Do not imply unavailable
  store listings, completely offline integrations, zero operating cost or
  unverified compliance. Website copy is not implementation evidence.
- Keep public product/legal copy consistent with the actual published scope.

## Validation and publication

```sh
hugo --gc --minify --panicOnWarning
python3 scripts/check-site.py
```

Visually verify affected pages and responsive states. Follow shared approval
and main-only Git rules. Publication uses the existing GitHub Actions workflow;
do not add a separate deployment mechanism.
