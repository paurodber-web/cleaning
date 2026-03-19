import os
import re

def process_html_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace index.html handling paths like ../index.html or ../../index.html with /
                # Except if it's already an absolute URL. GitHub Pages root is /
                content = re.sub(r'href="(?!https?://|mailto:|tel:)(?:\.\./)*index\.html(#[^"]*)?"', r'href="/\1"', content)
                
                # Replace other .html files and keep their path structure
                # e.g. href="about.html" -> href="about", href="../../services.html#prices" -> href="../../services#prices"
                content = re.sub(r'href="(?!https?://|mailto:|tel:)([^"]+?)\.html(#[^"]*)?"', r'href="\1\2"', content)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

if __name__ == "__main__":
    directory = "."
    process_html_files(directory)
