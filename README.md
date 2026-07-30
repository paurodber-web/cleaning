# Maid At Home

This repository contains the current Astro website for Maid At Home.

- Website source: `src/pages`, `src/layouts`, `src/components` and `src/content`
- Build command: `npm run build`
- Deployment: GitHub Actions from `main` to GitHub Pages
- Current production route structure uses clean URLs such as `/`, `/services/`, `/blog/` and `/areas-we-serve/`

The old root-level static HTML copies were removed after the Astro migration so automated reviewers and AI agents do not analyse stale duplicate pages. The generated site lives in `dist/` and is not committed.