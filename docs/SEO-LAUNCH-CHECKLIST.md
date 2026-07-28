# Maid At Home SEO launch checklist

The website implementation is complete without these credentials. The actions below must be performed in the corresponding business accounts after the production domain is deployed.

## Before public launch

- Point `maidathome.com.au` to the production build and force HTTPS.
- Confirm only one hostname resolves publicly. Redirect `www` to the non-`www` canonical host in one hop.
- Add `PUBLIC_GA4_ID` to the production environment when the GA4 property is ready.
- Complete one test booking and confirm the booking provider still receives the submitted details.
- Confirm the real business email, prices, discounts, service areas and policies with the operations team.

## Google Search Console

1. Create a Domain property for `maidathome.com.au` using DNS verification.
2. Submit `https://maidathome.com.au/sitemap.xml`.
3. Inspect the homepage, Regular House Cleaning, Pricing, Areas We Serve and the five published suburb URLs.
4. Request indexing only after the production checks pass.
5. Review Page indexing, HTTPS, Core Web Vitals and Enhancements weekly for the first eight weeks.

## Google Business Profile

- Use exactly the same business name and website domain as the site.
- Select the most accurate primary category; do not add categories for services not genuinely provided.
- Configure the real service area rather than publishing a fabricated office address.
- Add service entries for Regular, Deep, End of Lease, Move In, Hourly, Carpet and Oven Cleaning.
- Link the main website with `?utm_source=google&utm_medium=organic&utm_campaign=gbp`.
- Link the booking action with `?utm_source=google&utm_medium=organic&utm_campaign=gbp_booking` when the profile supports it.
- Upload current team/work photos that the business owns and can verify.
- Ask real customers for honest reviews after completed services. Never pre-write the review or offer an incentive.
- Reply to reviews with specific, privacy-safe context and no keyword stuffing.

## Bing and Apple

- Verify Bing Webmaster Tools and submit the same sitemap.
- Claim or update Apple Business Connect with the same name, website, email and service area.
- Check important Australian directories for duplicate or outdated records before adding new citations.

## Analytics acceptance test

Use GA4 DebugView or Tag Assistant and verify these events where the relevant action exists:

- `email_click`
- `phone_click`
- `booking_start`
- `booking_complete` (depends on the BookingKoala iframe posting a completion message)
- `calculator_start`
- `calculator_complete`
- `quote_start` and `quote_complete` when a separate quote form is introduced

Mark completed booking or quote events as key events in GA4. Because the booking form is cross-domain, also configure BookingKoala's native GA4 or webhook integration if it does not expose a completion message to the parent page.

## Monitoring rhythm

- Weekly for eight weeks: coverage, sitemap processing, query impressions, broken URLs and conversion events.
- Monthly: rankings and landing-page conversions for `house cleaning services Melbourne`, `regular house cleaning Melbourne`, `house cleaning prices Melbourne`, service terms and the five initial suburbs.
- Every quarter: validate prices, policy wording, service areas, author/reviewer details and article dates.
- Publish additional suburb pages only after operational coverage and unique local information have been reviewed. The build blocks thin or highly duplicated published suburb content.

## Realistic expectations

- Technical discovery and first impressions can appear within days to three weeks after Search Console submission.
- Long-tail article and suburb movement commonly begins in four to twelve weeks.
- Competitive service terms often need three to six months of consistent indexing, reviews, links and conversion improvements.
- Meaningful visibility for the primary Melbourne term commonly takes six to twelve months for a new domain, depending on authority and local reputation.
