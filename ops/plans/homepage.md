# Hugo homepage delivery

User scope: implement and deploy only the homepage in SHADO_website, using a Langflow-inspired Hugo design; configure Actions, build, commit and push.

- Original templates and styles with SHADO brand assets; no copied Langflow source or paid theme.
- Homepage sections: agent diagram, bridges, features, actual UI captures, deployment, use cases, FAQ and contact.
- GitHub Actions: pinned Hugo build, artifact validation, Pages deployment on main.
- Verify desktop and mobile layouts, navigation, FAQ, assets, reduced motion and live HTTPS page.

Evidence: Hugo 0.166.0 release build with warnings treated as errors; scripts/check-site.py validates artifact references, IDs, image alternative text and domain. Browser checks cover 1440px, 390px and 320px layouts. Deployment evidence is recorded after publishing.
