import os
import re
import json

base_path = r'c:\Users\Pau Rodriguez\Antigravity\Trading\Templates\maid_at_home_download_2\locations'
suburbs = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]

new_schema_template = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://maidathome.com.au/"},
        {"@type": "ListItem", "position": 2, "name": "Locations", "item": "https://maidathome.com.au/locations/"},
        {"@type": "ListItem", "position": 3, "name": "House Cleaning {suburb_name}", "item": "https://maidathome.com.au/locations/{folder_name}/"}
      ]
    },
    {
      "@type": "Organization",
      "@id": "https://maidathome.com.au/#organization",
      "name": "Maid at Home",
      "url": "https://maidathome.com.au/",
      "logo": "https://maidathome.com.au/assets/img/logo.webp"
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://maidathome.com.au/#localbusiness",
      "name": "Maid at Home",
      "image": "https://maidathome.com.au/assets/img/logo.webp",
      "telePhone": "+61 413 398 546",
      "priceRange": "$$",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Melbourne CBD",
        "addressLocality": "Melbourne",
        "addressRegion": "VIC",
        "postalCode": "3000",
        "addressCountry": "AU"
      },
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "reviewCount": "250"
      }
    },
    {
      "@type": "HouseCleaningService",
      "name": "House Cleaning {suburb_name}",
      "provider": { "@id": "https://maidathome.com.au/#localbusiness" },
      "areaServed": { "@type": "City", "name": "{suburb_name}" },
      "description": "Premium house cleaning services in {suburb_name}, Melbourne. We offer recurring cleans, deep cleaning, and move-out services."
    },
    {
      "@type": "FAQPage",
      "mainEntity": {faq_json}
    }
  ]
}
</script>"""

for folder in suburbs:
    file_path = os.path.join(base_path, folder, 'index.html')
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract suburb name from H1 or Title (pattern: "in Suburb Name")
    suburb_match = re.search(r'in ([\w\s]+)</h1>', content)
    if not suburb_match:
        suburb_match = re.search(r'Cleaning in ([\w\s]+) \|', content)
    
    suburb_name = suburb_match.group(1).strip() if suburb_match else folder.replace('house-cleaning-', '').replace('-', ' ').title()
    
    # Extract existing FAQs
    faq_match = re.search(r'"@type": "FAQPage",\s*"mainEntity": (\[.*?\])', content, re.DOTALL)
    if faq_match:
        faq_json = faq_match.group(1)
    else:
        # Fallback if structure is slightly different
        faq_json = "[]"
        
    # Remove ALL existing ld+json blocks
    new_content = re.sub(r'<script type="application/ld\+json">.*?</script>', '', content, flags=re.DOTALL)
    
    # Clean up empty lines left by scripts
    new_content = re.sub(r'\n\s*\n', '\n', new_content)
    
    # Inject new schema before </head>
    formatted_schema = new_schema_template.replace('{suburb_name}', suburb_name).replace('{folder_name}', folder).replace('{faq_json}', faq_json)
    
    if '</head>' in new_content:
        new_content = new_content.replace('</head>', formatted_schema + '\n</head>')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Processed: {folder}")

print("All schemas fixed successfully!")
