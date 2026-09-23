# Hugo homepage delivery

User scope: implement and deploy only the homepage in SHADO_website, using a Langflow-inspired Hugo design; configure Actions, build, commit and push.

- Original templates and styles with SHADO brand assets; no copied Langflow source or paid theme.
- Homepage sections: agent diagram, bridges, features, actual UI captures, deployment, use cases, FAQ and contact.
- GitHub Actions: pinned Hugo build, artifact validation, Pages deployment on main.
- Verify desktop and mobile layouts, navigation, FAQ, assets, reduced motion and live HTTPS page.

Evidence: Hugo 0.166.0 release build with warnings treated as errors; scripts/check-site.py validates artifact references, IDs, image alternative text and domain. Browser checks cover 1440px, 390px and 320px layouts. Deployment evidence is recorded after publishing.

## Delivery evidence — 2026-09-23

- Initial implementation: `0aa7054`. GitHub Actions run 35847643014 built and deployed successfully.
- Live HTTP page returned 200. Chrome checks passed at 1440, 390 and 320 px: no horizontal overflow, broken images, failed assets or JavaScript errors; mobile menu, FAQ and reduced-motion handling passed.
- Public DNS targets alrokayan.github.io. GitHub Pages source is workflow; custom domain remains shado.rv.sa.
- HTTPS initially waited for certificate issuance. GitHub subsequently approved the certificate for shado.rv.sa; HTTPS enforcement is now enabled and a certificate-verified HTTPS request returned 200. No TLS verification bypass was used.
- Authenticated SSH was used to push because the existing HTTPS OAuth token lacks workflow scope. No credentials or Git configuration were changed.
- Updated actions to current verified releases after the first deployment reported the Node 20 deprecation warning.
