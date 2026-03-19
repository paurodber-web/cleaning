import os
import glob
import re

html_files = glob.glob('**/*.html', recursive=True)

changed_files = 0
# Regex to match the broken tag
# We look for: <div class="cs_card_style_4 " data-aos="fade-up" data-aos-delay="150" cs_bg_filed cs_radius_16" data-src="...">
pattern = re.compile(r'<div class="cs_card_style_4 "\s*data-aos="([^"]+)"\s*data-aos-delay="([^"]+)"\s*cs_bg_filed cs_radius_16"\s*data-src="([^"]+)">')

for f in html_files:
    if "fix_card_classes.py" in f or ".antigravityignore" in f: continue
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        original_content = content
        
        # Replace the broken string with the correct one
        # new: <div class="cs_card_style_4 cs_bg_filed cs_radius_16" data-aos="\1" data-aos-delay="\2" data-src="\3">
        content = pattern.sub(r'<div class="cs_card_style_4 cs_bg_filed cs_radius_16" data-aos="\1" data-aos-delay="\2" data-src="\3">', content)
        
        if content != original_content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            changed_files += 1
            
    except Exception as e:
        print(f"Error processing {f}: {e}")

print(f"Updated {changed_files} files.")
