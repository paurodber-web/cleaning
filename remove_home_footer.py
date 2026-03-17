import os
import re

def remove_home_from_footer(directory):
    # Pattern to match the <li> containing the Home link in index.html or variations
    # Targeting specifically the structure found in the footer menu
    
    # Matching: <li> and its contents that link to index.html and have text "Home"
    # Supported structures:
    # <li><a ... href="index.html">Home</a></li>
    # with optional whitespace and attributes
    
    home_li_pattern = re.compile(
        r'<li>\s*<a[^>]*href=["\'](?:(?:\.\./)*index\.html|index\.html)["\'][^>]*>\s*Home\s*</a>\s*</li>',
        re.IGNORECASE | re.DOTALL
    )

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Target only the footer section to be safe
                    # Look for cs_footer_menu ul
                    footer_menu_pattern = re.compile(r'(<ul\s+class="[^"]*cs_footer_menu[^"]*"[^>]*>)(.*?)(</ul>)', re.DOTALL)
                    
                    def replace_func(match):
                        ul_start = match.group(1)
                        ul_content = match.group(2)
                        ul_end = match.group(3)
                        
                        modified_content = home_li_pattern.sub('', ul_content)
                        return ul_start + modified_content + ul_end
                    
                    if footer_menu_pattern.search(content):
                        new_content = footer_menu_pattern.sub(replace_func, content)
                        
                        if new_content != content:
                            with open(path, 'w', encoding='utf-8') as f:
                                f.write(new_content)
                            print(f"Removed Home link from footer in: {path}")
                except Exception as e:
                    print(f"Error processing {path}: {e}")

if __name__ == "__main__":
    remove_home_from_footer(".")
