import os
import re

root_dir = r'C:\Users\Pau Rodriguez\Antigravity\Trading\Templates\maid_at_home_download_2'

service_files = [
    'standard-clean.html',
    'deep-clean.html',
    'move-in-out-clean.html'
]

root_html_files = [
    'index.html',
    'about-us.html',
    'services.html',
    'pricing.html',
    'blog.html',
    'faqs.html',
    'contact-us.html',
    'booking.html',
    'privacy-policy.html',
    'terms-conditions.html'
]

def update_services_subdir():
    services_path = os.path.join(root_dir, 'services')
    for filename in os.listdir(services_path):
        if filename.endswith('.html'):
            path = os.path.join(services_path, filename)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 1. Update asset paths: 'assets/' -> '../assets/'
            # We look for src="assets/ or href="assets/
            content = content.replace('src="assets/', 'src="../assets/')
            content = content.replace('href="assets/', 'href="../assets/')
            
            # 2. Update navigation links to root
            for root_file in root_html_files:
                # Avoid matching things like "some-other-index.html"
                # Use regex to find href="root_file"
                pattern = f'href="{root_file}"'
                replacement = f'href="../{root_file}"'
                content = re.sub(pattern, replacement, content)
            
            # 3. Update 'suburbs/' links to '../suburbs/'
            content = content.replace('href="suburbs/', 'href="../suburbs/')
            
            # 4. Links to other services within these files are correct (already same dir)
            # But wait, if they were originally 'services/deep-clean.html' in root, 
            # and they were copied to 'services/', they might still have 'services/' prefix or not.
            # Looking at standard-clean.html, it had href="deep-clean.html" already.
            # So no change needed for those.
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {path}")

def update_root_files():
    for filename in root_html_files:
        path = os.path.join(root_dir, filename)
        if not os.path.exists(path):
            continue
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for s_file in service_files:
            # Change href="standard-clean.html" to href="services/standard-clean.html"
            pattern = f'href="{s_file}"'
            replacement = f'href="services/{s_file}"'
            content = re.sub(pattern, replacement, content)
            
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {path}")

def update_suburbs_files():
    suburbs_path = os.path.join(root_dir, 'suburbs')
    for filename in os.listdir(suburbs_path):
        if filename.endswith('.html'):
            path = os.path.join(suburbs_path, filename)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            for s_file in service_files:
                # Change href="../standard-clean.html" to href="../services/standard-clean.html"
                pattern = f'href="../{s_file}"'
                replacement = f'href="../services/{s_file}"'
                content = re.sub(pattern, replacement, content)
                
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {path}")

def update_blog_files():
    blog_path = os.path.join(root_dir, 'blog')
    for filename in os.listdir(blog_path):
        if filename.endswith('.html'):
            path = os.path.join(blog_path, filename)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            for s_file in service_files:
                # Change href="../standard-clean.html" to href="../services/standard-clean.html"
                pattern = f'href="../{s_file}"'
                replacement = f'href="../services/{s_file}"'
                content = re.sub(pattern, replacement, content)
                
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {path}")

if __name__ == "__main__":
    update_services_subdir()
    update_root_files()
    update_suburbs_files()
    update_blog_files()
