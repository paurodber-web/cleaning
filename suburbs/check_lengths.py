import os
import re

def slugify(name):
    return name.lower().replace(' ', '-')

def parse_suburbs_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    suburbs = {}
    sections = re.split(r'={20,}\s*SUBURB:\s*(.*?)\s*={20,}', content)
    for i in range(1, len(sections), 2):
        suburb_name = sections[i].strip()
        suburb_data = sections[i+1].strip()
        data = {}
        # Improved parsing: split by tags in braces
        parts = re.split(r'\{(.*?)\}', suburb_data)
        for j in range(1, len(parts), 2):
            tag = parts[j].strip()
            val = parts[j+1].strip()
            # Stop if we hit TESTIMONIAL CARDS or some other section
            val = re.split(r'\n\s*\n|TESTIMONIAL CARDS', val)[0].strip()
            data[tag] = val
        suburbs[suburb_name] = data
    return suburbs

# Targets from index.html analysis
TARGETS = {
    'meta_title': 37,
    'meta_description': 58,
    'hero_title': 29,
    'hero_description': 158,
    'standard_clean_description': 102,
    'deep_clean_description': 114,
    'move_clean_description': 116,
    'trust_section_title': 162,
    'testimonial_intro': 72,
    'process_section_title': 126
}

def analyze_lengths():
    data_path = r"C:\Users\Pau Rodriguez\Antigravity\Trading\Templates\maid_at_home_download_2\suburbs\suburbs_text"
    suburbs_data = parse_suburbs_data(data_path)
    
    sample = suburbs_data.get('Abbotsford', {})
    
    print("\n### Comparison: index.html vs suburbs_text (Abbotsford)\n")
    print("| Tag | index.html (Chars) | Suburbs_text (Chars) | Excess | Status |")
    print("| :--- | :---: | :---: | :---: | :--- |")
    
    for tag, target in TARGETS.items():
        actual_text = sample.get(tag, '')
        actual = len(actual_text)
        diff = actual - target
        status = "✅ OK"
        if diff > 0:
            status = "⚠️ TOO LONG"
        if diff > 40:
            status = "🚨 CRITICAL"
        
        print(f"| {tag} | {target} | {actual} | {diff:+} | {status} |")
    
    print("\n> [!CAUTION]")
    print("> The content provided in `suburbs_text` is significantly longer than the original template placeholders.")
    print("> If we use this text as is, the design WILL break or look cluttered.")

if __name__ == "__main__":
    analyze_lengths()
