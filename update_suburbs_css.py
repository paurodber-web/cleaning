import os

def update_css():
    directory = 'suburbs'
    old_string = """    @media (max-width: 991px) {
      .cs_hero_calc { margin-bottom: 30px !important; }
    }"""
    new_string = """    @media (max-width: 991px) {
      .cs_hero_style_1 { border-radius: 0 !important; }
      .cs_hero_calc { margin-bottom: 30px !important; }
    }"""

    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if old_string in content:
                new_content = content.replace(old_string, new_string)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filepath}")
            else:
                print(f"Pattern not found in {filepath}")

if __name__ == "__main__":
    update_css()
