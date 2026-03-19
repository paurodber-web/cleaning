import argparse
import html
import re
from pathlib import Path

PLACEHOLDER_RE = re.compile(r"\[\[([A-Z0-9_]+)\]\]")
SUBURB_TOKEN_RE = re.compile(r"\{\{suburb\}\}", re.IGNORECASE)

def slugify(name: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", name.strip().lower())
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug

def fix_sentence_case(text: str, suburb_name: str) -> str:
    """
    Lowercase everything except:
    1. The very first letter of the string.
    2. Any letter following a period, exclamation, or question mark (sentence start).
    3. The suburb name itself (case-insensitive match replaced with original casing).
    """
    if not text:
        return text
    
    # Lowercase everything first
    text = text.lower()
    
    # 1. Capitalize first letter of the whole string
    text = text[0].upper() + text[1:]
    
    # 2. Capitalize after sentence-ending punctuation (., !, ?)
    # Matches punctuation followed by optional whitespace
    def capitalize_match(m):
        return m.group(1) + m.group(2).upper()
    
    text = re.sub(r'([.!?]\s+)([a-z])', capitalize_match, text)
    
    # 3. Restore Suburb Name casing (e.g. "abbotsford" -> "Abbotsford")
    # Handle multi-word suburbs like "East Melbourne"
    # We use a case-insensitive regex to find the lowercase version and replace it with the original
    text = re.sub(re.escape(suburb_name), suburb_name, text, flags=re.IGNORECASE)
    
    return text

def parse_texts(texts_path: Path) -> dict:
    data = {}
    content = texts_path.read_text(encoding="utf-8")
    
    blocks = re.split(r'^\[(.*?)\]$', content, flags=re.MULTILINE)
    for i in range(1, len(blocks), 2):
        suburb_name = blocks[i].strip()
        suburb_content = blocks[i+1].strip()
        data[suburb_name] = {}
        tags = re.findall(r'^\[\[([A-Z0-9_]+)\]\]: (.*)$', suburb_content, flags=re.MULTILINE)
        for tag_name, tag_value in tags:
            data[suburb_name][f"[[{tag_name}]]"] = tag_value.strip()
    return data

def build_nearby_links(suburb: str, suburbs: list, count: int) -> str:
    if suburb not in suburbs:
        return ""
    idx = suburbs.index(suburb)
    rotated = suburbs[idx + 1 :] + suburbs[:idx]
    picked = rotated[:count]
    links = []
    for name in picked:
        href = f"house-cleaning-{slugify(name)}.html"
        links.append(f'<a href="{href}">{html.escape(name)}</a>')
    return "</li><li>".join(links)

def main() -> int:
    parser = argparse.ArgumentParser(description="Generate suburb pages with sentence casing.")
    parser.add_argument("--template", default="suburbs/template.html")
    parser.add_argument("--texts", default="suburbs/suburbs_text")
    parser.add_argument("--list", default="suburbs/suburbs_info")
    parser.add_argument("--out-dir", default="suburbs")
    parser.add_argument("--nearby-count", type=int, default=12)
    args = parser.parse_args()

    template_path = Path(args.template)
    texts_path = Path(args.texts)
    # Re-generate info if missing
    if not Path(args.list).exists():
        content = texts_path.read_text(encoding='utf-8')
        suburbs_names = re.findall(r'^\[(.*?)\]$', content, flags=re.MULTILINE)
        Path(args.list).write_text('\n'.join(suburbs_names), encoding='utf-8')

    list_path = Path(args.list)
    out_dir = Path(args.out_dir)

    template = template_path.read_text(encoding="utf-8")
    texts = parse_texts(texts_path)
    suburbs = [s.strip() for s in list_path.read_text(encoding="utf-8").splitlines() if s.strip()]

    placeholders = set(PLACEHOLDER_RE.findall(template))
    
    for suburb in suburbs:
        content = template
        content = content.replace("{{suburb}}", suburb)

        for ph in placeholders:
            token = f"[[{ph}]]"
            if ph == "NEARBY_SUBURBS_LINKS":
                value = build_nearby_links(suburb, suburbs, args.nearby_count)
            else:
                if token in texts.get(suburb, {}):
                    raw_value = texts[suburb][token]
                    # Apply sentence casing logic
                    processed_value = fix_sentence_case(raw_value, suburb)
                    
                    # If it's HERO_TITLE, remove the "in Suburb" part if it exists
                    if ph == "HERO_TITLE":
                        # Match " in " followed by suburb name (case-insensitive) at the end of the string
                        suburb_pattern = re.compile(rf"\s+in\s+{re.escape(suburb)}", re.IGNORECASE)
                        processed_value = suburb_pattern.sub("", processed_value).strip()
                    
                    value = html.escape(processed_value)
                else:
                    value = token
            content = content.replace(token, value)

        filename = f"house-cleaning-{slugify(suburb)}.html"
        out_path = out_dir / filename
        out_path.write_text(content, encoding="utf-8")

    print(f"Generated {len(suburbs)} files with corrected casing.")
    return 0

if __name__ == "__main__":
    main()
