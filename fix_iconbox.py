import os
import glob
import re

html_files = glob.glob('**/*.html', recursive=True)

target = '<div class="cs_iconbox_style_1">'

changed_files = 0

for f in html_files:
    if "fix_iconbox.py" in f or ".antigravityignore" in f: continue
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        original_content = content
        
        parts = content.split(target)
        if len(parts) > 1:
            new_content = parts[0]
            delay = 150
            for part in parts[1:]:
                replacement = f'<div class="cs_iconbox_style_1" data-aos="fade-up" data-aos-delay="{delay}">'
                delay += 150
                # Reset delay after 4 items (600) to start from 150 again if there are multiple groups
                if delay > 600: 
                    delay = 150
                new_content += replacement + part
            
            if new_content != original_content:
                with open(f, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                changed_files += 1
                
    except Exception as e:
        print(f"Error processing {f}: {e}")

print(f"Updated {changed_files} files.")
