# Suburb page content guide

Create each page as `src/content/suburbs/suburb-slug.md`. The public URL will be `/areas-we-serve/suburb-slug/`.

The build publishes a page only when both `draft: false` and `seoReview.reviewed: true` are present. It checks for at least 550 meaningful words across the complete landing page, with at least 75% differentiation from every other published suburb page. Keep every visible section short; uniqueness should come from specific details across the whole page, not from one long editorial block.

## Frontmatter template

```yaml
---
suburb: "Suburb Name"
postcode: "3000"
region: "inner"
regionLabel: "Inner Melbourne"
title: "House Cleaning Suburb Name | Maid At Home"
description: "Write a unique 120–160 character description that explains the local service and gives a useful reason to visit or book."
heroIntro: "Write at least two genuinely local sentences. Mention relevant housing, access or household patterns only when they have been checked."
summary: "Summarise what makes cleaning in this suburb different and how the page will help the resident choose an appropriate service."
localSectionTitle: "Write a locally specific heading for the main editorial section."
servicesIntro: "Explain which services are most relevant locally and why."
recurringIntro: "Explain how local household and property conditions affect a sensible cleaning frequency."
recurringRecommendation: "Give an original, qualified recommendation for weekly, fortnightly or longer rhythms."
carpetTitle: "Write a short local heading for the dedicated carpet-cleaning section."
carpetIntro: "Explain briefly why carpet cleaning may be relevant to homes in this suburb."
carpetImage: "https://example.com/relevant-carpeted-home-image.webp"
carpetImageAlt: "Accurate description of the carpet-cleaning section image"
whyImage: "https://example.com/relevant-cleaner-or-home-image.webp"
whyImageAlt: "Accurate description of the Why Maid At Home section image"
nearbyIntro: "A short local introduction connecting this suburb with its ten surrounding service areas."
faqIntro: "Introduce the genuinely local questions answered on this page."
image: "https://example.com/relevant-local-or-home-image.webp"
imageAlt: "Accurate description of the image, written for accessibility"
imageWidth: 1600
imageHeight: 1067
ctaImage: "https://example.com/suburb-or-locally-relevant-home-image.webp"
ctaImageAlt: "Accurate description of the image used behind the final CTA"
localHighlights:
  - title: "A local consideration"
    text: "At least 50 characters describing a verified issue that changes cleaning, access or scheduling in this suburb."
  - title: "A second consideration"
    text: "Use specific, useful information rather than replacing the suburb name in a generic paragraph."
  - title: "A third consideration"
    text: "Explain how the local housing or household context affects the recommended cleaning approach."
homeTypes:
  - "Apartments"
  - "Terrace homes"
accessNotes:
  - "A checked, suburb-relevant note about parking, lifts, keys or building access."
  - "A second practical note residents should provide before the booking."
services:
  - "standard-clean"
  - "deep-clean"
  - "hourly-clean"
nearbySuburbs:
  # Add exactly 10 genuinely nearby suburbs.
  - name: "Nearby Suburb 1"
    slug: "nearby-suburb-1"
  - name: "Nearby Suburb 2"
    slug: "nearby-suburb-2"
  # Continue until Nearby Suburb 10.
faqs:
  - question: "A genuine question residents in this suburb may have?"
    answer: "Write a complete, locally useful answer of at least 80 characters."
  - question: "A question about property access or parking?"
    answer: "Answer using checked information and ask customers to confirm address-specific details."
  - question: "A question about choosing a suitable service?"
    answer: "Explain the decision without repeating the same answer used on another suburb page."
  - question: "A question about recurring cleaning?"
    answer: "Connect frequency and savings to the local household or property context."
  - question: "Another suburb-specific booking question?"
    answer: "Provide useful information without inventing availability, testimonials or a local office."
publishedAt: 2026-07-16
updatedAt: 2026-07-16
seoReview:
  reviewed: false
  uniqueContentEstimate: 75
  localFactsCheckedAt: 2026-07-16
draft: true
---
```

## Required landing-page structure

The frontmatter fields, local highlights and FAQs collectively form the unique content. Do not add a long Markdown article beneath the frontmatter. The result should read like a direct service landing page made from short, scannable sections.

- Explain only the suburb details that change cleaning requirements, service choice, access or scheduling.
- Describe cleaning priorities that follow from local property types and conditions.
- Keep local highlight copy to one concise paragraph per card.
- Write at least five unique FAQs for the suburb; both the questions and answers must be locally useful.
- Write unique introductions for services and recurring discounts rather than relying only on shared labels.
- Treat oven cleaning as an optional extra, not a suburb-page service card.
- Do not include Carpet Clean in the main service-card list. Give it a separate local section because it has distinct search intent.
- Add relevant hero, carpet and CTA images with accurate alt text.
- Add a relevant image for the open two-column Why Maid At Home section.
- Add exactly 10 genuinely nearby suburbs.
- Avoid demographics, landmarks, transport claims or parking advice unless verified from a reliable source.
- Do not reuse testimonials across suburb pages or invent local customer claims.
- Do not add an address or claim a Maid At Home office exists in the suburb.
- Keep repeated service descriptions in the template; do not copy the same long paragraphs into every Markdown file.

Some section titles may be reused, but their short descriptions, recommendations and local evidence should be independently written.

## Testimonial rotation

Keep approved customer reviews in `src/data/testimonials.ts`, not inside individual suburb Markdown files. Each suburb page selects three reviews from that shared bank using its slug, so a set of 13–14 testimonials will rotate consistently across the published pages.

- Store only approved, accurately attributed testimonials.
- Preserve the original wording unless the customer has approved an edited version.
- Include the service context and review source when known.
- Do not change the suburb mentioned by a reviewer to make a testimonial appear local.
