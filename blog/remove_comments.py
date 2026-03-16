import os
import re
import glob

directory = "blog"
html_files = glob.glob(os.path.join(directory, "*.html"))

pattern = re.compile(r'<div class="cs_height_50 cs_height_lg_24">\s*</div>\s*<h2 class="cs_fs_36 cs_mb_16">\s*Leave A Reply\s*</h2>.*?<form.*?</form>', re.DOTALL | re.IGNORECASE)

for filepath in html_files:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        new_content, count = pattern.subn('', content)
        
        if count > 0:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Removed comment form from: {filepath}")
        else:
            print(f"No comment form found in: {filepath} (or already removed)")
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
