import re
import random

def rewrite_titles(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Templates for each section title (Human-sounding, SEO & Conversion focused)
    title_templates = {
        'ABOUT_SECTION_TITLE': [
            "Dedicated to Making Your Home Shine",
            "Professional Home Cleaning You Can Trust",
            "Meet Your Local Home Cleaning Experts",
            "Quality Cleaning for Your Living Space",
            "Expert Care for Every Local Home"
        ],
        'WHY_CHOOSE_SECTION_TITLE': [
            "Why Your Neighbors Choose Our Service",
            "The Secret to a Consistently Cleaner Home",
            "What Sets Our Local Cleaning Apart",
            "Reliable Results for Your Peace of Mind",
            "Why We Are the Preferred Local Choice"
        ],
        'SERVICES_SECTION_TITLE': [
            "Flexible Cleaning for Every Need",
            "Complete Home Care Solutions for You",
            "Professional Cleaning Services We Offer",
            "From Basic Tidying to Deep Cleaning",
            "Tailored Cleaning Plans for Your Home"
        ],
        'HOW_WORKS_TITLE': [
            "Book Your Professional Clean Today",
            "Our Simple Process for a Spotless Home",
            "How to Get Your Home Glowing",
            "Three Easy Steps to a Cleaner House",
            "Getting Started With Your Local Team"
        ],
        'TESTIMONIALS_TITLE': [
            "What Local Residents Say About Us",
            "Real Reviews from Happy Homeowners",
            "Client Stories from Your Neighborhood",
            "Kind Words from Our Regular Customers",
            "Why Our Clients Love the Results"
        ],
        'BLOG_TITLE': [
            "Expert Tips for a Tidy Home",
            "Our Latest Cleaning and Care Advice",
            "Helpful Tricks for a Healthier Space",
            "Pro Insights for Maintaining Your Home",
            "Guides to Keeping Your Place Fresh"
        ],
        'FAQ_TITLE': [
            "Answers to Your Cleaning Questions",
            "Common Info About Our Services",
            "Everything You Need to Know Today",
            "Frequently Asked Home Care Questions",
            "Clear Answers for Your Peace of Mind"
        ]
    }

    def replace_suburb_titles(match):
        suburb_block = match.group(0)
        
        for tag, templates in title_templates.items():
            new_title = random.choice(templates)
            suburb_block = re.sub(rf'\[\[{tag}\]\]: .*', f'[[{tag}]]: {new_title}', suburb_block)
        
        return suburb_block

    # Regex to match each suburb block
    new_content = re.sub(r'\[.*?\]\n(?:.*?\n)+?(?=\n\[|$)', replace_suburb_titles, content, flags=re.MULTILINE)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    rewrite_titles('suburbs/suburbs_text')
    print("Section titles rewritten successfully with human-centric language.")
