# SHADO website

A Hugo product website for https://shado.rv.sa. Original design inspired by Langflow's dark visual language; no Langflow source, assets or commercial theme included.

## Edit content

- `content/_index.md`: hero headline and introductory copy.
- `data/home.yaml`: bridge descriptions, feature cards and FAQ.
- `content/*.md`: Features, Deployment & Privacy, About & Contact, Support, Privacy Policy and Terms.
- `layouts/home.html`: remaining homepage content and structure.
- `layouts/baseof.html`, `layouts/partials/`, `layouts/page.html`: shared shell, navigation, footer and page layout.
- `assets/css/main.css`: brand colors, responsive layouts and reduced-motion styles.
- `assets/js/main.js`: accessible mobile navigation.
- `hugo.toml`: canonical URL, dashboard login URL, SEO description and public contact email.
- `static/images/`: product and brand images.

Seven English pages are published. App Store and Play Store buttons intentionally link to `#` and are labelled Coming soon. Set `dashboardURL` in `hugo.toml` to change the login destination. Store links live in `layouts/partials/downloads.html`; replace the placeholders when approved listings exist. Arabic site translation is not yet implemented.

## Local development

Install Hugo **0.166.0** (standard binary; no Node, Go toolchain or Sass dependencies required).

```sh
hugo server --bind 127.0.0.1
```

For a release build:

```sh
hugo --gc --minify --panicOnWarning
python3 scripts/check-site.py
```

Generated `public/` files are ignored by Git.

## GitHub Pages and Actions setup

1. Open the repository **Settings → Pages**.
2. Under **Build and deployment → Source**, choose **GitHub Actions**.
3. Keep **Custom domain** set to `shado.rv.sa`.
4. Cloudflare DNS should contain `CNAME shado → alrokayan.github.io`, DNS only.
5. Push to `main`. Under **Actions**, watch **Build and deploy Hugo**. It installs a pinned, checksum-verified Hugo binary, builds, checks local references, uploads `public/`, and deploys to Pages.
6. Enable **Enforce HTTPS** after GitHub has issued the domain certificate.

The workflow uses GitHub's automatic token; no deployment secret or personal access token is required. Pull requests build and validate without deploying. Use **Actions → Build and deploy Hugo → Run workflow** to redeploy manually.

## Assets and publication scope

SHADO logo/symbol/social image: owner-provided branding pack, version 1.2.0. Dashboard image: acquisition demonstration capture dated 2026-09-23. Phone image: the branding pack’s genuine dark-mode iPhone Simulator tools capture dated 2026-09-22. Images are converted to WebP with metadata omitted. Founder portrait: owner-provided acquisition materials. Diagrams are original conceptual illustrations, not screenshots or execution evidence. The contact address is the founder's public GitHub profile email.

Privacy and terms distinguish this static website from configured SHADO deployments. Reconcile these notices with the exact distributed app and enabled services before an App Store submission or managed-service launch; adding website pages alone does not implement in-app privacy links or account deletion.

Local model deployment does not imply all integrations are offline, zero operating costs, or automatic government compliance. Copy distinguishes optional external services and illustrative use cases.
