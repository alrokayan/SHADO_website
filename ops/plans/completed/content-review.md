# Review public website content before client sharing

Requested: remove the announcement banner and review every page for real, current content.

Scope: seven pages, shared navigation/footer, feature data, metadata, illustrations and screenshot captions. Preserve the approved design, genuine dark phone capture, store placeholders and dashboard link. Compare product statements with current source/SRS; distinguish implementation evidence from runtime acceptance. Remove unsupported promises rather than turn them into new product work.

## Review decisions — September 23, 2026

- Removed the announcement element and its desktop/mobile CSS.
- Replaced vague feature headings and speculative industry cards with concrete product functions and demonstration tasks.
- Removed the immediate team-rollout implication, subjective speech-quality claim and implied store release schedule. Download links remain `#`, explicitly “Not yet available.”
- Deployment copy distinguishes agent role presets from employee permissions and local inference from integrations that send data externally. No certification, zero-cost, guaranteed outcome or performance claim is made.
- About page uses the creator's statements: independent personal platform, no customers/revenue/signed commitments, current MEWA affiliation without endorsement. These are owner-confirmed statements, not independent diligence findings.
- Privacy review checked the static site's code, hosting and mobile storage implementation. Removed an unverified email-retention practice; retained a direct contact route for requests. Removed speculative future App Store contract wording from Terms.
- Reviewed screenshot and social-preview content. Product captures are genuine; corrected individual capture dates. Concept diagrams do not present execution results.

## Evidence map

Source references below are relative to the named sibling repository. Inspected SHADO commit `5509bee` and current working-tree files; source inspection establishes implemented surfaces, not a fresh full-platform acceptance test.

| Public claim | Evidence reviewed | Boundary |
|---|---|---|
| Local/cloud models, chat, sessions, presets | SHADO `ops/SRS.md`, `ops/SRS_002_chat.md`, `backend/app/domains/chat/router.py`, `backend/app/domains/cloud/` | No equivalence or benchmark guarantee |
| Host/sandbox/remote DesktopBridge | SHADO `backend/app/domains/desktop_targets/models.py`, Master SRS desktop management contract | Configured targets and permissions required |
| Android and virtual device bridge | SHADO `backend/app/domains/mobile/`, workspace SRS device operations | Not iPhone remote control |
| Arabic voice/transcription | SHADO `backend/app/domains/namma/`, `backend/app/domains/transcription/service.py` | Installed engines and recording/compute conditions |
| Files/Nextcloud | SHADO `backend/app/domains/workplace/storage_service.py` | Separate service and credentials; catalog presence is not connection |
| MCP/skills discovery and Python tools | SHADO `frontend/components/dashboard/capability-browse-panel.tsx`, `backend/app/domains/skills/router.py`, Master SRS capability contract | Third-party dependencies and permissions |
| VS Code and project context | SHADO_vscode `src/chatView.ts`, `src/workspace.ts` | Configured backend and authorized project |
| Mobile storage | SHADO_mobile `lib/core/auth/session_local_datasource.dart` | Secure storage and persisted password cookies, not zero storage |
| Website privacy | Website templates/JS; current GitHub General Privacy Statement; public DNS CNAME and NS lookup | GitHub hosting metadata distinct from site's own lack of tracking |
| Founder/commercial status | Creator's answers in this task | Owner assertions, not external verification |

External policy checked: https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement (effective April 27, 2026). Public DNS resolves shado.rv.sa to alrokayan.github.io with Cloudflare nameservers. Dashboard sign-in rendered in Chrome; no authentication attempted.

## Verification

Passed: Hugo release build with warnings treated as errors; generated-page validation; git diff whitespace check; all seven pages in real Chrome at 1440, 390 and 320 px, both locally and on https://shado.rv.sa/. Verified no announcement banner, no horizontal overflow, no broken images or script errors, working mobile navigation and placeholder store links. GitHub Pages run 35850348542 successfully deployed commit 78690d8. This is website validation and a source-grounded content review, not a new end-to-end certification of every SHADO capability.
