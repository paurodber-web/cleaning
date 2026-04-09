import os
import re

def main():
    with open("index.html", "r", encoding="utf-8") as f:
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
            if file.endswith(".html") and file != "index.html":
                filepath = os.path.join(d, file)
                
                is_subfolder = (d != '.')
                
                footer_to_use = master_footer
                if is_subfolder:
                    # Replace relative assets
                    footer_to_use = footer_to_use.replace('src="assets/', 'src="../assets/')
                    footer_to_use = footer_to_use.replace('href="assets/', 'href="../assets/')
                
                with open(filepath, "r", encoding="utf-8") as f:
                    file_content = f.read()
                
                # Replace the footer tag
                new_content = re.sub(r'(?s)<footer\b[^>]*>.*?</footer>', footer_to_use, file_content)
                
                if new_content != file_content:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Updated footer in {filepath}")

if __name__ == "__main__":
    main()
