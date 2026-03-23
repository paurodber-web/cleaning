import os

root_dir = r"c:\Users\Pau Rodriguez\Antigravity\Trading\Templates\maid_at_home_download_2"
new_phone_display = "0413 398 546"
new_phone_intl = "+61 413 398 546"
new_phone_clean = "61413398546"

# Variants to hunt for
placeholders = [
    "+61 3 0000 0000",
    "+613 0000 0000",
    "03 0000 0000",
    "(03) 0000 0000",
    "0000 0000"
]

for root, dirs, files in os.walk(root_dir):
    for f in files:
        if f.endswith(".html"):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8") as file:
                content = file.read()
            
            updated = content
            for p in placeholders:
                # If it's tel: or wa.me we need the clean version
                # But usually schema uses "telephone": "+61..."
                updated = updated.replace(p, new_phone_intl)
            
            if updated != content:
                with open(path, "w", encoding="utf-8") as file:
                    file.write(updated)
                print(f"Updated {path}")

print("Comprehensive phone number update completed.")
