import os

def main():
    old_slug = "carpet-steam-cleaning-melbourne"
    new_slug = "steam-clean"
    
    # Old label in footer
    old_label = "Carpet Steam Clean"
    new_label = "Steam Clean"
    
    dirs_to_search = ['.', 'locations', 'services', 'blog']
    
    for d in dirs_to_search:
        if not os.path.exists(d):
            continue
            
        for file in os.listdir(d):
            if file.endswith((".html", ".xml", ".js")):
                filepath = os.path.join(d, file)
                
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                
                new_content = content.replace(old_slug, new_slug)
                new_content = new_content.replace(old_label, new_label)
                
                if new_content != content:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Updated links/labels in {filepath}")

if __name__ == "__main__":
    main()
