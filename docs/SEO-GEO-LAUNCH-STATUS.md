# SEO, GEO and launch status

## Implemented in source

- Canonical production origin, social metadata, preview `noindex,follow`, `robots.txt`, sitemap and `llms.txt` are generated for the Astro site.
- Every indexable service, blog and approved area page has a canonical URL, structured data and internal navigation.
- Blog articles lead with a direct answer, contain an in-page index and link to indexable service or pricing pages.
- The home page uses the verified business history: **Since 2017, serving Melbourne families**. The service-response promise is **within 48 hours**.
- Only approved Google Business Profile areas are indexable and linked from the areas hub. Other generated suburb URLs remain available for direct local testing but are `noindex,follow`, are omitted from the sitemap and are not linked from indexable pages.
- The site includes an accessible mobile quick-action bar outside pricing and booking. It hides near the footer and while a form field is active. The calculator is unchanged.
- GTM receives non-PII conversion events for phone, email, WhatsApp, Google profile, Instagram, booking start and contact-form submission.

## Indexable priority service areas

Albert Park, Balwyn, Brighton, Camberwell, Collingwood, Docklands, Elwood, Hawthorn, Kew, Malvern, Melbourne CBD, Middle Park, Port Melbourne, Prahran, Richmond, South Yarra, Southbank, St Kilda and Toorak.

## Information that must be verified before it is claimed

- Review count and aggregate rating source.
- Public insurance, police-check and training claims.
- Exact business address if it is intended for display.
- Real team and in-home photographs, with consent and descriptive alt text.
- Any award, membership or third-party accreditation.

## Release validation

Run `npm run build`. It checks suburb indexability, blog answer-first content and the generated site before deployment.