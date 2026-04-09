import os

# CONFIGURACIÓN
TARGET_DIR = r'c:\Users\Pau Rodriguez\Antigravity\Trading\Templates\maid_at_home_download_2'
NEW_URL = 'https://mah.bookingkoala.com/booknow/home_cleaning'

# PATRONES A BUSCAR
PATTERNS = [
    'href="booking"',
    'href="booking.html"',
    'href="/booking"',
    'href="/booking.html"'
]

def update_links():
    count = 0
    for root, dirs, files in os.walk(TARGET_DIR):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    new_content = content
                    for pattern in PATTERNS:
                        replacement = f'href="{NEW_URL}"'
                        new_content = new_content.replace(pattern, replacement)
                    
                    if new_content != content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        count += 1
                        print(f"Actualizado: {file}")
                except Exception as e:
                    print(f"Error en {file}: {e}")
    
    print(f"\nTotal de archivos actualizados: {count}")

if __name__ == "__main__":
    update_links()
