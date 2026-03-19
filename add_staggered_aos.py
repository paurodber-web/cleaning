import os
import glob
import re

html_files = glob.glob('**/*.html', recursive=True)

targets = [
    '<div class="cs_iconbox_style_2 active">',
    '<div class="cs_iconbox_style_2">',
    '<div class="cs_testimonial_style_1 cs_white_bg cs_radius_16">',
    '<div class="cs_funfact_style_1 cs_center_column text-center">',
    '<div class="cs_card_style_4', # Careful with this one since it has data-src
    '<div class="accordion-item">' 
]

changed_files = 0

for f in html_files:
    if "add_staggered_aos.py" in f or ".antigravityignore" in f: continue
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        original_content = content
        
        # We will do replacement using a slightly different approach
        # For each target class string, we find all instances and sequentially add data-aos
        # However, it's easier to just use regex on the class name if it doesn't already have data-aos
        
        # 1. cs_iconbox_style_2 active
        content = re.sub(r'<div class="cs_iconbox_style_2 active"(?!.*data-aos)', '<div class="cs_iconbox_style_2 active" data-aos="fade-up" data-aos-delay="150"', content)
        
        # 2. cs_iconbox_style_2 (non-active)
        # We need staging for these because there are 3 of them consecutively
        parts = content.split('<div class="cs_iconbox_style_2">')
        if len(parts) > 1:
            new_content = parts[0]
            delay = 300 # since active is 150
            for part in parts[1:]:
                replacement = f'<div class="cs_iconbox_style_2" data-aos="fade-up" data-aos-delay="{delay}">'
                delay += 150
                if delay > 600: delay = 150
                new_content += replacement + part
            content = new_content

        # 3. cs_testimonial_style_1
        parts = content.split('<div class="cs_testimonial_style_1 cs_white_bg cs_radius_16">')
        if len(parts) > 1:
            new_content = parts[0]
            delay = 150
            for part in parts[1:]:
                replacement = f'<div class="cs_testimonial_style_1 cs_white_bg cs_radius_16" data-aos="fade-up" data-aos-delay="{delay}">'
                delay += 150
                if delay > 600: delay = 150
                new_content += replacement + part
            content = new_content
            
        # 4. cs_funfact_style_1
        parts = content.split('<div class="cs_funfact_style_1 cs_center_column text-center">')
        if len(parts) > 1:
            new_content = parts[0]
            delay = 150
            for part in parts[1:]:
                replacement = f'<div class="cs_funfact_style_1 cs_center_column text-center" data-aos="fade-up" data-aos-delay="{delay}">'
                delay += 150
                if delay > 600: delay = 150
                new_content += replacement + part
            content = new_content

        # 5. cs_card_style_4 (we just replace the prefix)
        # We can split by `<div class="cs_card_style_4`
        parts = content.split('<div class="cs_card_style_4 ')
        if len(parts) > 1:
            new_content = parts[0]
            delay = 150
            for part in parts[1:]:
                if not part.startswith('cs_bg_filed') and 'data-aos' not in part[:50]:
                    # maybe already modified or somewhat wrong format
                    replacement = '<div class="cs_card_style_4 '
                elif 'data-aos' in part[:50]:
                    replacement = '<div class="cs_card_style_4 '
                else:
                    replacement = f'<div class="cs_card_style_4 " data-aos="fade-up" data-aos-delay="{delay}" '
                    delay += 150
                    if delay > 600: delay = 150
                new_content += replacement + part
            content = new_content

        # 6. accordion-item
        parts = content.split('<div class="accordion-item">')
        if len(parts) > 1:
            new_content = parts[0]
            delay = 150
            for part in parts[1:]:
                replacement = f'<div class="accordion-item" data-aos="fade-up" data-aos-delay="{delay}">'
                delay += 150
                if delay > 600: delay = 150
                new_content += replacement + part
            content = new_content

        if content != original_content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            changed_files += 1
            
    except Exception as e:
        print(f"Error processing {f}: {e}")

print(f"Updated {changed_files} files.")
