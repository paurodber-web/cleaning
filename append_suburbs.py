import json
import sys
import os

def check_lengths(data):
    limits = {
        "[[META_TITLE]]": (1, 60),
        "[[META_DESCRIPTION]]": (140, 165),
        "[[HERO_DESCRIPTION]]": (130, 160),
        "[[ABOUT_SECTION_TITLE]]": (35, 45),
        "[[ABOUT_DESC]]": (140, 170),
        "[[WHY_CHOOSE_SECTION_TITLE]]": (35, 45),
        "[[WHY_CHOOSE_US_DESC]]": (120, 140),
        "[[SERVICES_SECTION_TITLE]]": (20, 30),
        "[[SERVICES_DESC]]": (130, 160),
        "[[STANDARD_CLEAN_DESCRIPTION]]": (90, 110),
        "[[DEEP_CLEAN_DESCRIPTION]]": (100, 120),
        "[[MOVE_CLEAN_DESCRIPTION]]": (110, 130),
        "[[HOW_WORKS_TITLE]]": (25, 35),
        "[[PROCESS_SECTION_TITLE]]": (110, 130),
        "[[TESTIMONIALS_TITLE]]": (20, 30),
        "[[TESTIMONIALS_DESC]]": (60, 80),
        "[[TESTIMONIAL_1_TEXT]]": (120, 150),
        "[[TESTIMONIAL_2_TEXT]]": (120, 150),
        "[[TESTIMONIAL_3_TEXT]]": (120, 150),
        "[[FAQ_TITLE]]": (20, 30),
        "[[FAQ_DESC]]": (90, 120),
        "[[BLOG_TITLE]]": (20, 30),
        "[[BLOG_DESC]]": (50, 70),
    }

    errors = []
    for tag, (min_len, max_len) in limits.items():
        val = data.get(tag, "")
        length = len(val)
        if length < min_len or length > max_len:
            errors.append(f"{tag} length is {length}, expected {min_len}-{max_len}. Text: '{val}'")
            
    # Check hyphens
    for tag, val in data.items():
        if tag not in ["[[NEARBY_SUBURBS_LINKS]]", "name"]:
            if "-" in val:
                errors.append(f"Hyphen found in {tag}: {val}")
    
    # Check H1 exclusivity
    h1_phrase = f"House cleaning in {data['name']}".lower()
    for tag, val in data.items():
        if tag not in ["name", "[[NEARBY_SUBURBS_LINKS]]"]:
            if h1_phrase in val.lower():
                errors.append(f"H1 phrase found in {tag}")

    if errors:
        for e in errors:
            print(e)
        return False
    return True

file_path = "c:\\Users\\Pau Rodriguez\\Antigravity\\Trading\\Templates\\maid_at_home_download_2\\suburbs\\suburbs_text"

with open("batch.json", "r", encoding="utf-8") as f:
    batch = json.load(f)

success = True
for item in batch:
    print(f"Checking {item['name']}...")
    if not check_lengths(item):
        print(f"Failed length checks for {item['name']}")
        success = False

if not success:
    sys.exit(1)

with open(file_path, "a", encoding="utf-8") as f:
    for item in batch:
        f.write(f"\n[{item['name']}]\n")
        f.write(f"[[META_TITLE]]: {item['[[META_TITLE]]']}\n")
        f.write(f"[[META_DESCRIPTION]]: {item['[[META_DESCRIPTION]]']}\n")
        f.write(f"[[HERO_TITLE]]: House cleaning in {item['name']}\n")
        f.write(f"[[HERO_DESCRIPTION]]: {item['[[HERO_DESCRIPTION]]']}\n")
        f.write(f"[[ABOUT_SECTION_TITLE]]: {item['[[ABOUT_SECTION_TITLE]]']}\n")
        f.write(f"[[ABOUT_DESC]]: {item['[[ABOUT_DESC]]']}\n")
        f.write(f"[[WHY_CHOOSE_SECTION_TITLE]]: {item['[[WHY_CHOOSE_SECTION_TITLE]]']}\n")
        f.write(f"[[WHY_CHOOSE_US_DESC]]: {item['[[WHY_CHOOSE_US_DESC]]']}\n")
        f.write(f"[[SERVICES_SECTION_TITLE]]: {item['[[SERVICES_SECTION_TITLE]]']}\n")
        f.write(f"[[SERVICES_DESC]]: {item['[[SERVICES_DESC]]']}\n")
        f.write(f"[[STANDARD_CLEAN_DESCRIPTION]]: {item['[[STANDARD_CLEAN_DESCRIPTION]]']}\n")
        f.write(f"[[DEEP_CLEAN_DESCRIPTION]]: {item['[[DEEP_CLEAN_DESCRIPTION]]']}\n")
        f.write(f"[[MOVE_CLEAN_DESCRIPTION]]: {item['[[MOVE_CLEAN_DESCRIPTION]]']}\n")
        f.write(f"[[HOW_WORKS_TITLE]]: {item['[[HOW_WORKS_TITLE]]']}\n")
        f.write(f"[[PROCESS_SECTION_TITLE]]: {item['[[PROCESS_SECTION_TITLE]]']}\n")
        f.write(f"[[TESTIMONIALS_TITLE]]: {item['[[TESTIMONIALS_TITLE]]']}\n")
        f.write(f"[[TESTIMONIALS_DESC]]: {item['[[TESTIMONIALS_DESC]]']}\n")
        f.write(f"[[TESTIMONIAL_1_TEXT]]: {item['[[TESTIMONIAL_1_TEXT]]']}\n")
        f.write(f"[[TESTIMONIAL_2_TEXT]]: {item['[[TESTIMONIAL_2_TEXT]]']}\n")
        f.write(f"[[TESTIMONIAL_3_TEXT]]: {item['[[TESTIMONIAL_3_TEXT]]']}\n")
        f.write(f"[[TESTIMONIAL_1_NAME]]: {item.get('[[TESTIMONIAL_1_NAME]]', 'Sarah L.')}\n")
        f.write(f"[[TESTIMONIAL_2_NAME]]: {item.get('[[TESTIMONIAL_2_NAME]]', 'Mark D.')}\n")
        f.write(f"[[TESTIMONIAL_3_NAME]]: {item.get('[[TESTIMONIAL_3_NAME]]', 'Emma C.')}\n")
        f.write(f"[[TESTIMONIAL_4_NAME]]: {item.get('[[TESTIMONIAL_4_NAME]]', 'Paul F.')}\n")
        f.write(f"[[FAQ_TITLE]]: {item['[[FAQ_TITLE]]']}\n")
        f.write(f"[[FAQ_DESC]]: {item['[[FAQ_DESC]]']}\n")
        f.write(f"[[BLOG_TITLE]]: {item['[[BLOG_TITLE]]']}\n")
        f.write(f"[[BLOG_DESC]]: {item['[[BLOG_DESC]]']}\n")
        f.write(f"[[NEARBY_SUBURBS_LINKS]]: {item['[[NEARBY_SUBURBS_LINKS]]']}\n")

print("Successfully appended!")
