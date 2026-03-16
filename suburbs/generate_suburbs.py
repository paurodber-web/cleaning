import os
import re
import random

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
        # Parse tags like {tag_name}\nValue
        parts = re.split(r'\{(.*?)\}', suburb_data)
        for j in range(1, len(parts), 2):
            tag = parts[j].strip()
            value = parts[j+1].strip()
            # If there's a next tag, only take up to there
            value = value.split('\n{')[0].strip()
            data[tag] = value
            
        # Parse testimonials
        testis = []
        if "TESTIMONIAL CARDS" in suburb_data:
            testi_parts = suburb_data.split("TESTIMONIAL CARDS")[1]
            matches = re.findall(r'Testimonial \d+ Text: "(.*?)"\s*Name: (.*?)\s*Suburb: (.*?)\s*Rating: (\d+)', testi_parts, re.DOTALL)
            for m in matches:
                testis.append({
                    'text': m[0].strip(),
                    'name': m[1].strip(),
                    'suburb': m[2].strip(),
                    'rating': m[3].strip()
                })
        data['testimonials'] = testis
        suburbs[suburb_name] = data
        
    return suburbs

def generate_suburb_pages():
    base_dir = r"C:\Users\Pau Rodriguez\antigravity\trading\templates\maid_at_home_download_2"
    suburbs_dir = os.path.join(base_dir, "suburbs")
    template_path = os.path.join(suburbs_dir, "template.html")
    data_path = os.path.join(suburbs_dir, "suburbs_text")
    
    suburbs_data = parse_suburbs_data(data_path)
    suburb_names = sorted(list(suburbs_data.keys()))
    
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()

    # Create the footer links once
    footer_links_html = ""
    for s_name in suburb_names:
        slug = slugify(s_name)
        footer_links_html += f'              <div class="cs_suburb_item"><a href="{slug}.html">{s_name}</a></div>\n'

    for suburb_name, data in suburbs_data.items():
        content = template_content
        
        # Nearby Suburbs Logic
        nearby_candidates = [s for s in suburb_names if s != suburb_name]
        random.seed(suburb_name) # Deterministic for each suburb
        nearby_selection = random.sample(nearby_candidates, min(5, len(nearby_candidates)))
            
        nearby_links_html = ""
        for ns in nearby_selection:
            ns_slug = slugify(ns)
            nearby_links_html += f'            <li><a href="{ns_slug}.html">{ns}</a></li>\n'

        # Mapping markers to data, with fallbacks for dynamic sections
        replacements = {
            '[[META_TITLE]]': data.get('meta_title', f"Professional Cleaning in {suburb_name} | Maid At Home"),
            '[[META_DESCRIPTION]]': data.get('meta_description', f"Expert home cleaning services in {suburb_name}. Trusted local team delivering premium results."),
            '[[HERO_TITLE]]': data.get('hero_title', f"Trusted professional cleaning in {suburb_name}"),
            '[[HERO_DESCRIPTION]]': data.get('hero_description', f"Experience a premium residential cleaning service in {suburb_name}. Our professional team provides reliable solutions tailored to your unique home."),
            
            # About Section
            '[[ABOUT_SECTION_TITLE]]': data.get('about_title', f"Preferred by hundreds of {suburb_name} residents"),
            '[[ABOUT_DESC]]': data.get('trust_section_title', data.get('about_desc', f"We deliver professional results for {suburb_name} residents through premium techniques.")),
            
            # Services
            '[[STANDARD_CLEAN_DESCRIPTION]]': data.get('standard_clean_description', f"A reliable house cleaning in {suburb_name} that covers all the basics."),
            '[[DEEP_CLEAN_DESCRIPTION]]': data.get('deep_clean_description', f"We handle the real heavy lifting for your {suburb_name} home with a thorough scrub."),
            '[[MOVE_CLEAN_DESCRIPTION]]': data.get('move_clean_description', f"Take the stress out of your {suburb_name} move with a full property clean."),
            '[[PROCESS_SECTION_TITLE]]': data.get('process_section_title', f"We’ve refined our {suburb_name} cleaning process to be as efficient as possible."),
            
            # Why Choose Us
            '[[WHY_CHOOSE_SECTION_TITLE]]': data.get('why_title', f"Why we are the most reliable choice for you in {suburb_name}"),
            '[[WHY_CHOOSE_US_DESC]]': data.get('why_desc', f"Discover a higher standard of home care with professional cleaning plans tailored specifically for your {suburb_name} lifestyle."),
            
            # Services Titles
            '[[SERVICES_TITLE]]': data.get('services_title', f"Our {suburb_name} cleaning services"),
            '[[SERVICES_DESC]]': data.get('services_desc', f"From a quick refresh to a deep scrub down, we have the right service to keep your {suburb_name} home feeling fresh."),
            
            # How It Works
            '[[HOW_WORKS_TITLE]]': data.get('how_title', f"A simpler way to a clean home in {suburb_name}"),
            
            # Testimonials section title
            '[[TESTIMONIALS_TITLE]]': data.get('testi_title', f"Why our {suburb_name} clients trust us"),
            '[[TESTIMONIALS_DESC]]': data.get('testimonial_intro', data.get('testi_desc', f"Honest feedback from local {suburb_name} families who enjoy a cleaner home.")),
            
            # FAQ
            '[[FAQ_TITLE]]': data.get('faq_title', f"Common questions about {suburb_name} cleaning"),
            '[[FAQ_DESC]]': data.get('faq_desc', f"Find everything you need to know about our services in {suburb_name}."),
            
            # Blog
            '[[BLOG_TITLE]]': data.get('blog_title', f"From Our {suburb_name} Cleaning Experts"),
            '[[BLOG_DESC]]': data.get('blog_desc', f"Tips and tricks to maintain a fresher {suburb_name} home."),

            # Nearby Suburbs
            '[[NEARBY_SUBURBS_LINKS]]': nearby_links_html,
        }
        
        # Testimonials
        for i in range(1, 4):
            if len(data.get('testimonials', [])) >= i:
                t = data['testimonials'][i-1]
                replacements[f'[[TESTIMONIAL_{i}_TEXT]]'] = t['text']
                replacements[f'[[TESTIMONIAL_{i}_NAME]]'] = t['name']

        # Names cleanup
        content = content.replace('Amanda Rivera', replacements.get('[[TESTIMONIAL_1_NAME]]', 'Amanda Rivera'))
        content = content.replace('Daniel Wright', replacements.get('[[TESTIMONIAL_2_NAME]]', 'Daniel Wright'))
        content = content.replace('Rachel Bennett', replacements.get('[[TESTIMONIAL_3_NAME]]', 'Rachel Bennett'))
        
        # Apply all replacements
        for marker, val in replacements.items():
            content = content.replace(marker, val)
            
        # Global Suburb replacement
        content = content.replace('{{suburb}}', suburb_name)
        
        # Suburbs Footer
        content = re.sub(r'<div class="cs_footer_suburbs_grid cs_primary_font">.*?</div>', f'<div class="cs_footer_suburbs_grid cs_primary_font">\n{footer_links_html}            </div>', content, flags=re.DOTALL)

        # Save file (Only if you want to generate)
        # file_name = f"{slugify(suburb_name)}.html"
        # save_path = os.path.join(suburbs_dir, file_name)
        # with open(save_path, 'w', encoding='utf-8') as f:
        #     f.write(content)

    print("Script updated with correct About/Mission mappings and Nearby Suburbs logic.")

if __name__ == "__main__":
    generate_suburb_pages()
