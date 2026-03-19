import os
import glob
import re

html_files = glob.glob('**/*.html', recursive=True)

target_p = '<p class="cs_primary_color cs_primary_font mb-0">'
target_div = '<div class="cs_section_heading_right">'

p_matches = 0
div_matches = 0

for f in html_files:
    if "check_classes.py" in f or ".antigravityignore" in f: continue
    try:
        content = open(f, 'r', encoding='utf-8').read()
        p_matches += content.count(target_p)
        div_matches += content.count(target_div)
    except:
        pass

print(f"p matches: {p_matches}")
print(f"div matches: {div_matches}")
