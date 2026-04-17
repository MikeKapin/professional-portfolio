# mikekapin.com

Personal single-page site for Mike Kapin.

Plain static HTML + inline CSS, no build step. Deploys to Netlify via GitHub continuous deployment (site id `b5f8f9f3-8f8b-49fb-87af-dab84f5db8d0`).

## Files

- `index.html` — entire site
- `sitemap.xml`, `robots.txt` — SEO
- `images/` — unused by current build, retained for potential future use

## Deploy

Continuous deployment from `main` via the Netlify GitHub integration. To push a manual deploy:

```
NETLIFY_AUTH_TOKEN=<token> npx netlify-cli deploy --prod --dir=. --site=b5f8f9f3-8f8b-49fb-87af-dab84f5db8d0
```

## History

Prior versions of this site (with consulting content, HVAC/EdTech framing, and `lark-labs.html`) are preserved on the `archive/pre-coi-consulting-site-2026-04-16` branch.
