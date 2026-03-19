import glob

html_files = glob.glob('**/*.html', recursive=True)

# Target modal string:
# We need to find the popup-discount-final modal and replace its attributes to make it responsive.
old_str_1 = 'class="modal-dialog modal-dialog-bottom m-4 position-fixed bottom-0 end-0"\n      style="width: 380px; z-index: 1060;"'
new_str_1 = 'class="modal-dialog position-fixed bottom-0 end-0 m-3 m-md-4"\n      style="width: 380px; max-width: calc(100% - 2rem); z-index: 1060;"'

old_str_2 = 'style="border: 2px dashed #cbd5e1; padding: 12px 24px; border-radius: 12px; background: #f8fafc; font-weight: 800; font-size: 22px; color: #0E1109; letter-spacing: 2px; text-align: center; display: flex; align-items: center; justify-content: center;"'
new_str_2 = 'style="border: 2px dashed #cbd5e1; padding: 10px 12px; border-radius: 12px; background: #f8fafc; font-weight: 800; font-size: 18px; color: #0E1109; letter-spacing: 2px; text-align: center; display: flex; align-items: center; justify-content: center;"'

old_str_3 = '<button class="cs_btn_snap cs_blue_bg1 cs_white_color cs_radius_16 px-3"'
new_str_3 = '<button class="cs_btn_snap cs_accent_bg cs_primary_color cs_radius_16 px-3"'

# Handle cases where formatting might be on same line or slightly different
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    orig = content
    # Handle spacing variations for old_str_1
    import re
    # 1. Update modal-dialog positioning and width
    content = re.sub(
        r'class="modal-dialog[^"]*m-4 position-fixed bottom-0 end-0"\s*style="width: 380px; z-index: 1060;"',
        'class="modal-dialog position-fixed bottom-0 end-0 m-3 m-sm-4"\n      style="width: 380px; max-width: calc(100vw - 2rem); z-index: 1060;"',
        content
    )
    
    # 2. Update the dashed box padding and font-size
    content = re.sub(
        r'style="border: 2px dashed #cbd5e1; padding: 12px 24px; border-radius: 12px; background: #f8fafc; font-weight: 800; font-size: 22px; color: #0E1109; letter-spacing: 2px; text-align: center; display: flex; align-items: center; justify-content: center;"',
        'style="border: 2px dashed #cbd5e1; padding: 10px 15px; border-radius: 12px; background: #f8fafc; font-weight: 800; font-size: 20px; color: #0E1109; letter-spacing: 1px; text-align: center; display: flex; align-items: center; justify-content: center;"',
        content
    )
    
    # 3. Make button yellow like they want
    content = content.replace(old_str_3, new_str_3)
    
    if content != orig:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

cnt = 0
for f in html_files:
    if ".antigravityignore" in f or "fix_modal.py" in f: continue
    if process_file(f):
        cnt += 1

print(f"Updated {cnt} files.")
