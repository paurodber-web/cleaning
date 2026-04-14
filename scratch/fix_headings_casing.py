import os
import re

def title_case_heading(full_text, tag_name):
    # Improved regex to find multi-line tags and handle attributes
    pattern = re.compile(rf'(<{tag_name}[^>]*>)(.*?)(</{tag_name}>)', re.IGNORECASE | re.DOTALL)
    
    def replace_tag(match):
        opening_tag = match.group(1)
        content = match.group(2)
        closing_tag = match.group(3)
        
        def capitalize_text(text):
            # Split by whitespace, capitalize first letter, join
            # We use a regex to find words to preserve existing punctuation/spacing better
            def cap_match(m):
                word = m.group(0)
                if len(word) > 0:
                    return word[0].upper() + word[1:]
                return word
            
            # Find sequences of alphanumeric characters
            return re.sub(r'\b\w+\b', cap_match, text)

        # Split by nested tags and capitalize only text parts
        parts = re.split(r'(<[^>]+>)', content)
        new_parts = []
        for p in parts:
            if p.startswith('<'):
                new_parts.append(p)
            else:
                new_parts.append(capitalize_text(p))
        
        return opening_tag + "".join(new_parts) + closing_tag

    return pattern.sub(replace_tag, full_text)

def main():
    root_dir = "c:\\Users\\Pau Rodriguez\\Antigravity\\Trading\\Templates\\maid_at_home_download_2"
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content
                for tag in ['h1', 'h2', 'h3']:
                    new_content = title_case_heading(new_content, tag)
                
                if new_content != content:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated: {path}")

if __name__ == "__main__":
    main()
