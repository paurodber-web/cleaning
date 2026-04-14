import os
import re
import json

def fix_general_schemas():
    opening_hours = {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
        "opens": "09:00", "closes": "17:00"
    }
    
    catalog = {
        "@type": "OfferCatalog",
        "name": "Cleaning Services",
        "itemListElement": [
            { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Standard Cleaning" } },
            { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Deep Cleaning" } },
            { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Move In / Out Cleaning" } },
            { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Steam Carpet Cleaning" } }
        ]
    }

    files_to_fix = [
        ('index.html', 'Home', True),
        ('services/index.html', 'Services', True),
        ('about-us/index.html', 'About Us', False),
        ('pricing/index.html', 'Pricing', False),
        ('contact-us/index.html', 'Contact Us', False),
        ('faqs/index.html', 'FAQs', False),
        ('blog/index.html', 'Blog', False),
        ('locations/index.html', 'Locations', False),
        ('privacy-policy/index.html', 'Privacy Policy', False),
        ('terms-conditions/index.html', 'Terms Conditions', False),
        ('booking/index.html', 'Booking', False),
        # Specific Service Pages
        ('services/standard-clean/index.html', 'Standard Cleaning', False, 'Standard Cleaning'),
        ('services/deep-clean/index.html', 'Deep Cleaning', False, 'Deep Cleaning'),
        ('services/move-in-out-clean/index.html', 'Move In / Out Cleaning', False, 'Move In / Out Cleaning'),
        ('services/steam-clean/index.html', 'Steam Carpet Cleaning', False, 'Steam Carpet Cleaning'),
    ]

    for item in files_to_fix:
        path = item[0]
        name = item[1]
        include_catalog = item[2]
        specific_service = item[3] if len(item) > 3 else None
        
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Remove existing schemas
            content = re.sub(r'<script type="application/ld\+json">.*?</script>', '', content, flags=re.DOTALL)
            
            # Breadcrumbs
            breadcrumbs = ""
            if path != 'index.html':
                breadcrumbs = f'''{{
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://maidathome.com.au/"}},
        {{"@type": "ListItem", "position": 2, "name": "{name}", "item": "https://maidathome.com.au/{path.replace('index.html', '')}"}}
      ]
    }},'''

            # LocalBusiness
            lb = f'''{{
      "@type": "LocalBusiness",
      "@id": "https://maidathome.com.au/#localbusiness",
      "name": "Maid at Home",
      "image": "https://maidathome.com.au/assets/img/logo.webp",
      "telephone": "+61 413 398 546",
      "priceRange": "$$",
      "address": {{
        "@type": "PostalAddress",
        "streetAddress": "Melbourne CBD",
        "addressLocality": "Melbourne",
        "addressRegion": "VIC",
        "postalCode": "3000",
        "addressCountry": "AU"
      }},
      "openingHoursSpecification": {json.dumps(opening_hours)},
      "aggregateRating": {{
        "@type": "AggregateRating",
        "ratingValue": "5",
        "reviewCount": "250"
      }}
    }}'''

            # Organization
            org = f'''{{
      "@type": "Organization",
      "@id": "https://maidathome.com.au/#organization",
      "name": "Maid at Home",
      "url": "https://maidathome.com.au/",
      "logo": "https://maidathome.com.au/assets/img/logo.webp"
    }}'''

            # Optional blocks
            extra_blocks = []
            if include_catalog:
                extra_blocks.append(f'''{{
      "@type": "Service",
      "name": "Cleaning Services",
      "serviceType": "House Cleaning",
      "provider": {{ "@id": "https://maidathome.com.au/#localbusiness" }},
      "areaServed": {{ "@type": "City", "name": "Melbourne" }},
      "hasOfferCatalog": {json.dumps(catalog)}
    }}''')
            
            if specific_service:
                extra_blocks.append(f'''{{
      "@type": "Service",
      "name": "{specific_service}",
      "serviceType": "House Cleaning",
      "provider": {{ "@id": "https://maidathome.com.au/#localbusiness" }},
      "description": "Professional {specific_service.lower()} in Melbourne."
    }}''')

            # Build Graph
            graph_elements = [b for b in [breadcrumbs, org, lb] if b] + extra_blocks
            new_schema = f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [\n    { ",\n    ".join(graph_elements) }\n  ]
}}
</script>'''

            if '</head>' in content:
                content = content.replace('</head>', f'{new_schema}\n</head>')
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {path}")

if __name__ == "__main__":
    fix_general_schemas()
