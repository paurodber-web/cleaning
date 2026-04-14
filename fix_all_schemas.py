import os
import re
import json

def fix_location_schemas():
    locations_dir = 'locations'
    
    # Opening Hours Template
    opening_hours = {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday"
        ],
        "opens": "09:00",
        "closes": "17:00"
    }

    for folder in os.listdir(locations_dir):
        folder_path = os.path.join(locations_dir, folder)
        if os.path.isdir(folder_path):
            index_path = os.path.join(folder_path, 'index.html')
            if os.path.exists(index_path):
                with open(index_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Extract suburb name from title
                # <title>House Cleaning in Burnley | Trusted Local Cleaners</title>
                title_match = re.search(r'<title>(.*?) in (.*?) \|', content)
                suburb = "Melbourne"
                if title_match:
                    suburb = title_match.group(2).strip()
                elif "house-cleaning-" in folder:
                    suburb = folder.replace("house-cleaning-", "").replace("-", " ").title()

                # Extract existing FAQs if possible, otherwise use generic ones
                faq_match = re.search(r'"@type": "FAQPage",\s*"mainEntity": \[(.*?)\]', content, re.DOTALL)
                faqs_json = ""
                if faq_match:
                    faqs_json = faq_match.group(1).strip()
                else:
                    # Fallback generic local FAQs
                    faqs_json = f'''
    {{
      "@type": "Question",
      "name": "What types of cleaning services do you offer in {suburb}?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "We offer a range of services, including residential cleaning, deep cleaning, move-in/move-out cleaning, and seasonal deep cleaning."
      }}
    }},
    {{
      "@type": "Question",
      "name": "Do I need to be home during the cleaning?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "No, you don’t have to be home. Many of our clients provide us with access instructions so we can clean while they’re away."
      }}
    }},
    {{
      "@type": "Question",
      "name": "What if I\'m not satisfied with the cleaning?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "Your satisfaction is our priority. If you’re not happy with the service, please let us know within 24 hours, and we’ll arrange a re-clean at no extra cost."
      }}
    }}'''

                # Clean up existing schemas
                content = re.sub(r'<script type="application/ld\+json">.*?</script>', '', content, flags=re.DOTALL)
                
                # Construct new schema
                new_schema = f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://maidathome.com.au/"}},
        {{"@type": "ListItem", "position": 2, "name": "Locations", "item": "https://maidathome.com.au/locations/"}},
        {{"@type": "ListItem", "position": 3, "name": "House Cleaning {suburb}", "item": "https://maidathome.com.au/locations/{folder}/"}}
      ]
    }},
    {{
      "@type": "Organization",
      "@id": "https://maidathome.com.au/#organization",
      "name": "Maid at Home",
      "url": "https://maidathome.com.au/",
      "logo": "https://maidathome.com.au/assets/img/logo.webp"
    }},
    {{
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
    }},
    {{
      "@type": "HouseCleaningService",
      "name": "House Cleaning {suburb}",
      "provider": {{ "@id": "https://maidathome.com.au/#localbusiness" }},
      "areaServed": {{ "@type": "City", "name": "{suburb}" }},
      "description": "Premium house cleaning services in {suburb}, Melbourne. We offer recurring cleans, deep cleaning, and move-out services."
    }},
    {{
      "@type": "FAQPage",
      "mainEntity": [{faqs_json}]
    }}
  ]
}}
</script>'''

                # Inject before </head>
                if '</head>' in content:
                    content = content.replace('</head>', f'{new_schema}\n</head>')
                
                with open(index_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated {folder}")

if __name__ == "__main__":
    fix_location_schemas()
