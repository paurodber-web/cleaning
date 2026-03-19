import os
import glob
import re

html_files = glob.glob('**/*.html', recursive=True)

changed_files = 0

for f in html_files:
    if "fix_misc.py" in f or ".antigravityignore" in f: continue
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        original_content = content
        
        # 1. FAQs: we'll split by `<div class="cs_accordian cs_style_1 `
        # Then reassemble with staggered delays
        parts = content.split('<div class="cs_accordian cs_style_1 ')
        if len(parts) > 1:
            new_content = parts[0]
            delay = 150
            for part in parts[1:]:
                # Check if it doesn't already have data-aos.
                # Usually part starts with `cs_gray_bg1 cs_radius_12">`
                if 'data-aos=' not in part[:100]:
                    # We inject before cs_gray_bg1 ... wait, we can just inject into the class!
                    # Actually, we split before the class ends, so we can just append it before `cs_gray_bg1`
                    # The split removed '<div class="cs_accordian cs_style_1 '
                    replacement = f'<div class="cs_accordian cs_style_1 " data-aos="fade-up" data-aos-delay="{delay}" '
                    delay += 150
                    if delay > 600: delay = 150
                else:
                    replacement = '<div class="cs_accordian cs_style_1 '
                new_content += replacement + part
            content = new_content

        # 2. Blogs Section (in the inline JS script)
        # Search for: <article class="cs_post_style_1 cs_gray_bg1 cs_radius_16 h-100 mb-0">
        if '<article class="cs_post_style_1 ' in content and 'data-aos="fade-up"' not in content[content.find('<article class="cs_post_style_1 '):content.find('<article class="cs_post_style_1 ')+100]:
             content = content.replace(
                '<article class="cs_post_style_1 cs_gray_bg1 cs_radius_16 h-100 mb-0">',
                '<article class="cs_post_style_1 cs_gray_bg1 cs_radius_16 h-100 mb-0" data-aos="fade-up" data-aos-delay="150">'
             )
        
        if '<article class="cs_post_style_2 ' in content and 'data-aos="fade-up"' not in content[content.find('<article class="cs_post_style_2 '):content.find('<article class="cs_post_style_2 ')+100]:
             content = content.replace(
                '<article class="cs_post_style_2 cs_gray_bg1 cs_radius_16">',
                '<article class="cs_post_style_2 cs_gray_bg1 cs_radius_16" data-aos="fade-up" data-aos-delay="300">'
             )
             
        # 3. CTA section
        if 'class="cs_cta_style_1 cs_blue_bg1' in content and 'data-aos="zoom-in"' not in content:
             content = content.replace('class="cs_cta_style_1 cs_blue_bg1', 'data-aos="zoom-in" class="cs_cta_style_1 cs_blue_bg1')
        
        if content != original_content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            changed_files += 1
            
    except Exception as e:
        print(f"Error processing {f}: {e}")

print(f"Updated {changed_files} files.")
