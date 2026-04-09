import os
import re

def main():
    with open("pruebas/footer_final.html", "r", encoding="utf-8") as f:
        content = f.read()
    
    match = re.search(r'(?s)<footer\b[^>]*>.*?</footer>', content)
    if not match:
        print("Could not find footer in pruebas/footer_final.html")
        return
        
    master_footer = match.group(0)
    # The master footer from footer_final.html has src="../assets/" everywhere.
    # So we need to adapt it. If it's a root file, replace "../assets/" with "assets/".
    # If it's a subfolder file, keep "../assets/".
    
    print("Master footer extracted from pruebas/footer_final.html.")
    
    dirs_to_search = ['.', 'locations', 'services', 'blog']
    
    for d in dirs_to_search:
        if not os.path.exists(d):
            continue
            
        for file in os.listdir(d):
            if file.endswith(".html"):
                filepath = os.path.join(d, file)
                
                is_subfolder = (d != '.')
                
                footer_to_use = master_footer
                if not is_subfolder:
                    footer_to_use = footer_to_use.replace('../assets/', 'assets/')
                
                with open(filepath, "r", encoding="utf-8") as f:
                    file_content = f.read()
                
                new_content = re.sub(r'(?s)<footer\b[^>]*>.*?</footer>', footer_to_use, file_content)
                
                if new_content != file_content:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Updated footer in {filepath}")

if __name__ == "__main__":
    main()
