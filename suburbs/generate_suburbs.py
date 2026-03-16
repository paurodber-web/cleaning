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


def parse_texts(texts_path: Path) -> dict:
    data = {}
    current = None
    for raw in texts_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("[") and line.endswith("]"):
            current = line[1:-1].strip()
            data[current] = {}
            continue
        if current is None:
            continue
        if ": " in line:
            key, value = line.split(": ", 1)
            data[current][key.strip()] = value.strip()
    return data


def build_nearby_links(suburb: str, suburbs: list, count: int) -> str:
    if suburb not in suburbs:
        return ""
    idx = suburbs.index(suburb)
    candidates = [s for s in suburbs if s != suburb]
    if not candidates:
        return ""
    # Rotate list so we start after current suburb
    rotated = suburbs[idx + 1 :] + suburbs[:idx]
    rotated = [s for s in rotated if s != suburb]
    picked = rotated[:count]
    links = []
    for name in picked:
        href = f"{slugify(name)}.html"
        links.append(f'<a href="{href}">{html.escape(name)}</a>')
    # Template has a single <li> wrapper around the placeholder.
    return "</li><li>".join(links)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate suburb pages from template and texts.")
    parser.add_argument("--template", default="suburbs/template.html")
    parser.add_argument("--texts", default="suburbs/suburbs_texts.txt")
    parser.add_argument("--list", default="suburbs/suburbs_info")
    parser.add_argument("--out-dir", default="suburbs")
    parser.add_argument("--nearby-count", type=int, default=12)
    args = parser.parse_args()

    template_path = Path(args.template)
    texts_path = Path(args.texts)
    list_path = Path(args.list)
    out_dir = Path(args.out_dir)

    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")
    if not texts_path.exists():
        raise FileNotFoundError(f"Texts not found: {texts_path}")
    if not list_path.exists():
        raise FileNotFoundError(f"Suburb list not found: {list_path}")

    template = template_path.read_text(encoding="utf-8")
    texts = parse_texts(texts_path)
    suburbs = [s.strip() for s in list_path.read_text(encoding="utf-8").splitlines() if s.strip()]

    out_dir.mkdir(parents=True, exist_ok=True)

    placeholders = set(PLACEHOLDER_RE.findall(template))
    required_tokens = {f"[[{p}]]" for p in placeholders if p != "NEARBY_SUBURBS_LINKS"}
    missing_texts = [s for s in suburbs if s not in texts]
    if missing_texts:
        raise ValueError(f"Missing text blocks for suburbs: {', '.join(missing_texts)}")

    for suburb in suburbs:
        content = template
        content = SUBURB_TOKEN_RE.sub(suburb, content)

        # Replace placeholders
        if suburb not in texts:
            raise ValueError(f"Missing text block for suburb: {suburb}")
        missing_tokens = [t for t in required_tokens if t not in texts[suburb]]
        if missing_tokens:
            missing_tokens.sort()
            raise ValueError(f"Missing tokens for {suburb}: {', '.join(missing_tokens)}")

        for ph in placeholders:
            token = f"[[{ph}]]"
            if ph == "NEARBY_SUBURBS_LINKS":
                value = build_nearby_links(suburb, suburbs, args.nearby_count)
            else:
                value = texts[suburb][token]
                value = html.escape(value)
            content = content.replace(token, value)

        out_path = out_dir / f"{slugify(suburb)}.html"
        out_path.write_text(content, encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
