import os
import re

def main():
    root_dir = "."
    index_path = "index.html"
    
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    match = re.search(r'(?s)<footer\b[^>]*>.*?</footer>', content)
    if not match:
        print("Could not find footer in index.html")
        return
        
    master_footer = match.group(0)
    print("Master footer extracted from index.html.")
    
    # Base directories to search
    dirs_to_search = ['.', 'locations', 'services', 'blog']
    
    for d in dirs_to_search:
        if not os.path.exists(d):
            continue
            
        for file in os.listdir(d):
            if file.endswith(".html"):
                filepath = os.path.join(d, file)
                
                # Check if it needs relative asset paths
                needs_relative = (d != '.')
                
                footer_to_use = master_footer
                if needs_relative:
                    # Replace 'assets/' with '../assets/' but avoid '.../assets/'
                    # We can directly do a string replace of 'src="assets/' and 'href="assets/'
                    footer_to_use = footer_to_use.replace('src="assets/', 'src="../assets/')
                    footer_to_use = footer_to_use.replace('href="assets/', 'href="../assets/')
                    
                    # Also replace internal root links like href="/about-us" with href="/about-us" if necessary. 
                    # They are probably absolute /path or relative. The root uses absolute /path, so no change needed.

                with open(filepath, "r", encoding="utf-8") as f:
                    file_content = f.read()
                
                new_content = re.sub(r'(?s)<footer\b[^>]*>.*?</footer>', footer_to_use, file_content)
                
                if new_content != file_content:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Updated footer in {filepath}")

if __name__ == "__main__":
    main()
