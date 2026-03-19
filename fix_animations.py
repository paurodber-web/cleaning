import os
import glob
import re

html_files = glob.glob('**/*.html', recursive=True)

# We want to replace `<p class="cs_primary_color cs_primary_font mb-0">` with the animated version
# But only if it doesn't already have data-aos
pattern_p = re.compile(r'<p class="cs_primary_color cs_primary_font mb-0">\s*(?!<|.*data-aos)', re.DOTALL)
pattern_div = re.compile(r'<div class="cs_section_heading_right">\s*(?!<|.*data-aos)', re.DOTALL)

# Better yet, since we know exactly what to replace and the HTML is consistent:
p_search = '<p class="cs_primary_color cs_primary_font mb-0">'
p_replace = '<p class="cs_primary_color cs_primary_font mb-0" data-aos="fade-up" data-aos-delay="150">'

div_search = '<div class="cs_section_heading_right">'
div_replace = '<div class="cs_section_heading_right" data-aos="fade-up" data-aos-delay="150">'

changed_files = 0

for f in html_files:
    if ".antigravityignore" in f: continue
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        original_content = content
        
        # We need to make sure we don't replace ones that already have data-aos inside the tag
        # So we'll find all instances of the exact tag:
        content = content.replace(p_search, p_replace)
        content = content.replace(div_search, div_replace)
        
        # What if it was previously replaced? Like `class="..." data-aos="..."`
        # Because we only search for the exact string, it won't match if it already has data-aos.
        
        if content != original_content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            changed_files += 1
            
    except Exception as e:
        print(f"Error processing {f}: {e}")

print(f"Updated {changed_files} files.")
