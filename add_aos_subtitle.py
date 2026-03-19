import os
import re

def process_html_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Function to add data-aos="fade-down" to subtitles
                def replace_subtitle(match):
                    tag = match.group(0)
                    if 'data-aos=' not in tag:
                        if tag.endswith('/>'):
                            return tag[:-2] + ' data-aos="fade-down" data-aos-duration="600"/>'
                        else:
                            return tag[:-1] + ' data-aos="fade-down" data-aos-duration="600">'
                    return tag

                # Apply to subtitules
                content_new = re.sub(r'<[^>]+class="[^"]*cs_section_subtitle[^"]*"[^>]*>', replace_subtitle, content)
                
                # Function to delay titles so they appear smoothly AFTER the subtitle
                def replace_title(match):
                    tag = match.group(0)
                    if 'data-aos=' in tag and 'data-aos-delay' not in tag:
                        if tag.endswith('/>'):
                            return tag[:-2] + ' data-aos-delay="150"/>'
                        else:
                            return tag[:-1] + ' data-aos-delay="150">'
                    return tag

                content_new = re.sub(r'<[^>]+class="[^"]*cs_section_title[^"]*"[^>]*>', replace_title, content_new)

                if content_new != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content_new)
                    print(f"Updated {filepath}")

if __name__ == "__main__":
    process_html_files(".")
