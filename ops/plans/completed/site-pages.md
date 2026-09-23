# Complete the SHADO website pages

User scope: dark phone preview; Features, Deployment & Privacy, About & Contact, Support, Privacy Policy and Terms; placeholder App Store and Play Store links; real dashboard login link; publish through existing GitHub Pages workflow.

Reuse the original homepage styling and extract shared page structure. Use an existing genuine dark-mode iPhone Simulator capture. Keep operational instructions and privacy statements grounded in actual hosting and deployment boundaries. Verify all generated routes, links, mobile layouts and the live deployment.

## Verification

- Hugo 0.166.0 release build passes with warnings treated as errors.
- Artifact checker covers all seven pages, local resources, cross-page anchors, headings, image alternative text, store placeholders and dashboard URL.
- Real Chrome: seven pages at 1440, 390 and 320 px; no horizontal overflow, broken images, failed assets or JavaScript errors. Mobile navigation, FAQ and reduced motion checked.
- Dark phone: genuine 2026-09-22 iPhone Simulator tools capture from owner-provided branding pack.
- Dashboard destination: https://shado-host.golden-alpha.ts.net/login, confirmed HTTP 200 and title Sign in. A completed unauthenticated Chrome probe rendered the password sign-in form and backend/frontend/Tailscale/host status. No credentials were entered.
- Privacy content distinguishes website hosting, direct inquiries and configured deployments; store links remain Not yet available placeholders.

- Published HTTPS verification passed for all seven routes at three viewport widths after the content review; GitHub Pages run 35850348542 succeeded.
