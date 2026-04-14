import os
import re

def title_case_h2(full_text):
    # Regex to find everything between <h2> and </h2>
    # It catches attributes like <h2 class="..."> as well
    pattern = re.compile(r'(<h2[^>]*>)(.*?)(</h2>)', re.IGNORECASE | re.DOTALL)
    
    def replace_h2(match):
        opening_tag = match.group(1)
        content = match.group(2)
        closing_tag = match.group(3)
        
        # We only want to capitalize words, avoiding HTML tags inside if they exist
        # (though usually H2s are plain text or have minor spans)
        
        def capitalize_text(text):
            # Split by whitespace, capitalize first letter of each part, then join
            # This handles 'every word' regardless of length
            words = text.split()
            cap_words = [w[0].upper() + w[1:] if len(w) > 0 else w for w in words]
            return " ".join(cap_words)

        # Simple split to preserve nested tags if any (unlikely in H2s here but safer)
        # We split by <...> and capitalize only the parts outside tags
        parts = re.split(r'(<[^>]+>)', content)
        new_parts = []
        for p in parts:
            if p.startswith('<'):
                new_parts.append(p)
            else:
                new_parts.append(capitalize_text(p))
        
        return opening_tag + "".join(new_parts) + closing_tag

    return pattern.sub(replace_h2, full_text)

def main():
    root_dir = "c:\\Users\\Pau Rodriguez\\Antigravity\\Trading\\Templates\\maid_at_home_download_2"
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = title_case_h2(content)
                
                if new_content != content:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated: {path}")

if __name__ == "__main__":
    main()
