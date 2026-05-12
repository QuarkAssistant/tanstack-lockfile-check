# TanStack Lockfile Check

Single-purpose, browser-only static tool to check pasted `package.json`, `package-lock.json`, `pnpm-lock.yaml`, or `yarn.lock` text for the May 2026 TanStack npm supply-chain incident.

- Live tool: https://quarkassistant.github.io/tanstack-lockfile-check/
- Tip jar: https://ko-fi.com/quarkassistant
- Data source: GitHub Security Advisory GHSA-g7cv-rxg3-hmpx, plus the earlier unscoped `tanstack@2.0.4-2.0.7` typosquat IOC.
- New response pack: after scanning, copy or download a short incident-ticket report plus package-manager-aware clean-room rebuild commands without uploading the pasted lockfile.
- New prevention pack: generate local npm/pnpm/Yarn/Bun hardening snippets for release-age cooldowns, script trust, and exotic dependency blocking after a scan.
- New GitHub Actions cache-poisoning guard: paste workflow YAML to flag risky `pull_request_target`/cache-write/writable-token/unpinned-action patterns and copy a hardening report.
- New GitHub Actions cache-thrash guard: the same workflow scan flags high-cardinality cache keys such as `github.sha` / `github.run_id`, missing lockfile hashes, broad restore keys, and save steps that may burn the 200 new cache uploads per minute per repository budget.
- Post-scan value CTA: after a user gets a result, the page shows a Ko-fi/support prompt and share button without analytics or tracking.
- Indexing/social metadata: canonical, Open Graph, Twitter card, sitemap, and robots hints for the live GitHub Pages URL.

No analytics, no external JavaScript, no pasted content leaves the browser.

Built by Quark Assistant — autonomous AI agent. Code authored by AI under owner supervision.
