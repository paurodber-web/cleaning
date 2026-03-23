import os
import re
from PIL import Image

def convert_images(img_dir):
    extensions = ('.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG')
    mapping = {}
    
    for root, dirs, files in os.walk(img_dir):
        for file in files:
            if file.lower().endswith(extensions):
                old_path = os.path.join(root, file)
                name, ext = os.path.splitext(file)
                new_file = name + '.webp'
                new_path = os.path.join(root, new_file)
                
                try:
                    with Image.open(old_path) as img:
                        img.save(new_path, 'WEBP')
                    print(f"Converted: {old_path} -> {new_path}")
                    
                    # Store mapping for replacement
                    # We store both the filename and the case-insensitive version if needed
                    # but usually, we just need to replace the exact string found in files.
                    mapping[file] = new_file
                    
                    os.remove(old_path)
                    print(f"Deleted: {old_path}")
                except Exception as e:
                    print(f"Error converting {old_path}: {e}")
                    
    return mapping

def update_references(project_root, mapping):
    # Regex to match any of the old filenames
    if not mapping:
        return
    
    # Sort keys by length descending to avoid partial matches if filenames overlap
    # (though unlikely for full filenames with extensions)
    sorted_filenames = sorted(mapping.keys(), key=len, reverse=True)
    
    # We'll search for these filenames in all project files
    # extensions to search in: .html, .css, .js, .py, .txt, .json
    search_exts = ('.html', '.css', '.js', '.py', '.txt', '.json')
    
    # Build a regex pattern: (file1\.png|file2\.jpg|...)
    # We need to escape the dots in filenames
    pattern = '|'.join(re.escape(f) for f in sorted_filenames)
    # Case-insensitive if we want to be extra robust, but our mapping is based on actual files
    # However, the user said "handle cases where the extension might be capitalized"
    # so maybe the reference in HTML is "Image.webp" but the file is "Image.webp"
    # Let's use re.IGNORECASE for the match if we want, but then we need a function to replace
    
    regex = re.compile(pattern, re.IGNORECASE)

    def replace_func(match):
        matched_str = match.group(0)
        # Find which key it matches (case-insensitive)
        for key in sorted_filenames:
            if key.lower() == matched_str.lower():
                # Replace with the .webp version, keeping the base name from the mapping if possible
                # or just change the extension of the matched string.
                name, _ = os.path.splitext(matched_str)
                return name + '.webp'
        return matched_str

    for root, dirs, files in os.walk(project_root):
        # Exclude node_modules and .git
        if 'node_modules' in dirs:
            dirs.remove('node_modules')
        if '.git' in dirs:
            dirs.remove('.git')
            
        for file in files:
            if file.endswith(search_exts) and file != 'convert_and_update.py':
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    new_content, count = regex.subn(replace_func, content)
                    
                    if count > 0:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Updated {count} references in: {file_path}")
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    img_dir = 'assets/img'
    project_root = '.'
    
    print("Starting image conversion...")
    mapping = convert_images(img_dir)
    print(f"Conversion complete. {len(mapping)} images processed.")
    
    print("Updating references in project files...")
    update_references(project_root, mapping)
    print("Reference update complete.")
