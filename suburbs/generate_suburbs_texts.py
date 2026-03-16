import argparse
import re
from pathlib import Path
import random
from collections import defaultdict


SUBURB_HEADER_RE = re.compile(r"^\[(.+)\]$")
PLACEHOLDER_RE = re.compile(r"\[\[([A-Z0-9_]+)\]\]")


def slugify(name: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", name.strip().lower())
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug


def load_header(lines):
    header = []
    for line in lines:
        if SUBURB_HEADER_RE.match(line.strip()) and not line.strip().startswith("#"):
            break
        header.append(line)
    return header


def parse_texts(lines):
    data = {}
    current = None
    for raw in lines:
        line = raw.rstrip("\n")
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        m = SUBURB_HEADER_RE.match(stripped)
        if m:
            current = m.group(1).strip()
            data[current] = {}
            continue
        if current is None:
            continue
        if ": " in stripped:
            key, value = stripped.split(": ", 1)
            data[current][key.strip()] = value.strip()
    return data


def _pick(rng, items):
    return rng.choice(items)


def _pick_pair(rng, items):
    return items[rng.randrange(len(items))]


def _shuffle_join(rng, parts):
    parts = [p for p in parts if p]
    rng.shuffle(parts)
    return " ".join(parts)


def _unique_or_bump(rng, used_set, candidate, bumpers):
    if candidate not in used_set:
        used_set.add(candidate)
        return candidate
    # Try bumpers
    for b in bumpers:
        alt = f"{candidate} {b}"
        if alt not in used_set:
            used_set.add(alt)
            return alt
    # Final fallback: add short deterministic suffix
    suffix = f"{rng.randrange(1000, 9999)}"
    alt = f"{candidate} {suffix}"
    used_set.add(alt)
    return alt


def template_texts(suburb: str, used: dict) -> dict:
    rng = random.Random(slugify(suburb))

    adj = _pick_pair(rng, [
        "reliable", "trusted", "professional", "friendly", "local", "experienced", "detail-focused"
    ])
    verb = _pick_pair(rng, [
        "deliver", "provide", "offer", "handle", "take care of", "manage"
    ])
    focus = _pick_pair(rng, [
        "eco-friendly products", "careful attention to detail", "consistent results", "flexible scheduling"
    ])

    meta_title = _pick(rng, [
        f"Professional House Cleaning {suburb} | Maid at Home",
        f"Trusted Home Cleaning {suburb} | Maid at Home",
        f"House Cleaning Services {suburb} | Maid at Home",
        f"Reliable House Cleaners {suburb} | Maid at Home",
    ])

    meta_desc = _shuffle_join(rng, [
        _pick(rng, [
            f"Looking for {adj} house cleaning in {suburb}?",
            f"Need a trusted cleaner in {suburb}?",
            f"Searching for professional home cleaning in {suburb}?",
        ]),
        _pick(rng, [
            f"Maid at Home {verb} premium, eco-friendly cleans with flexible bookings.",
            f"Our team {verb} thorough, eco-friendly home cleaning with flexible scheduling.",
            f"We {verb} consistent, high-quality cleaning with {focus}.",
        ]),
        _pick(rng, [
            f"Book your {suburb} clean today.",
            f"Secure your {suburb} service online in minutes.",
            f"Get your {suburb} home cleaned on your schedule.",
        ]),
    ])

    hero_title = _pick(rng, [
        f"Cleaner {suburb} homes, made easy.",
        f"Fresh {suburb} homes, without the hassle.",
        f"{suburb} homes, clean and comfortable.",
        f"Spotless results for {suburb} homes.",
    ])

    hero_desc = _shuffle_join(rng, [
        _pick(rng, [
            f"We {verb} professional, reliable home cleaning tailored to your routine, so you can enjoy a healthier {suburb} home without the stress of chores.",
            f"Our {adj} cleaning team takes care of the housework so you can enjoy more time and a healthier home in {suburb}.",
            f"We {verb} consistent, high-quality cleaning tailored to your lifestyle, so your {suburb} home stays fresh without the effort.",
        ]),
        _pick(rng, [
            "Expect friendly service, clear communication, and results you can feel.",
            "You get a cleaner home and more time back in your week.",
            "We focus on the details so you can relax at home.",
        ]),
    ])

    about_title = _pick(rng, [
        f"Trusted by {suburb} locals every week",
        f"Preferred by {suburb} families",
        f"Your local {suburb} cleaning team",
    ])

    about_desc = _shuffle_join(rng, [
        _pick(rng, [
            f"We believe a clean living space is the foundation for a peaceful life.",
            f"A tidy home makes daily life easier and more comfortable.",
            f"A clean space helps your home feel calm and welcoming.",
        ]),
        _pick(rng, [
            f"From routine visits to deep scrubs, we {verb} every {suburb} room with expert care.",
            f"We {verb} each room with professional care, from regular upkeep to detailed deep cleans in {suburb}.",
            f"Our team handles every room with care, whether you need maintenance cleaning or a full refresh.",
        ]),
        _pick(rng, [
            "We treat your home with respect and attention to detail.",
            "Expect consistent, thoughtful service on every visit.",
            "You can rely on our team for thorough, careful results.",
        ]),
    ])

    why_title = _pick(rng, [
        f"Why {suburb} chooses Maid at Home",
        f"Why {suburb} residents trust us",
        f"The {suburb} choice for reliable cleaning",
    ])

    why_desc = _shuffle_join(rng, [
        _pick(rng, [
            f"Enjoy a premium standard of home care with plans designed around your needs.",
            f"Get dependable service with flexible options that fit your routine.",
            f"Count on a reliable team that respects your time and space.",
        ]),
        _pick(rng, [
            f"Our {adj} cleaners focus on quality, consistency, and the little details.",
            f"We combine reliable scheduling, careful attention to detail, and friendly service.",
            f"Expect consistent results, clear communication, and a professional team.",
        ]),
        _pick(rng, [
            f"That is why so many {suburb} households trust us week after week.",
            f"That is why {suburb} residents choose Maid at Home.",
            f"That is why we are a preferred choice across {suburb}.",
        ]),
    ])

    services_title = _pick(rng, [
        f"{suburb} Cleaning Services",
        f"Cleaning Services in {suburb}",
        f"Our {suburb} Cleaning Options",
    ])

    services_desc = _shuffle_join(rng, [
        _pick(rng, [
            f"From a quick refresh to a detailed deep clean, we offer the right services to keep every {suburb} home fresh, tidy, and welcoming.",
            f"Whether you need a routine tidy or a full deep clean, our services keep {suburb} homes fresh and comfortable.",
            f"We offer flexible cleaning options that suit busy {suburb} households, from maintenance visits to detailed deep cleans.",
        ]),
        _pick(rng, [
            "Choose the service that matches your schedule and priorities.",
            "Pick a plan that fits your home, your time, and your budget.",
            "Select the level of clean that works best for your household.",
        ]),
    ])

    standard_desc = _pick(rng, [
        f"A dependable maintenance clean that covers kitchens, bathrooms, and living spaces to keep your {suburb} home looking its best.",
        f"A reliable regular clean for the key areas of your {suburb} home, keeping everything tidy and welcoming.",
        f"Routine upkeep for kitchens, bathrooms, and living areas to keep your {suburb} home in great shape.",
    ])

    deep_desc = _pick(rng, [
        f"A thorough top-to-bottom clean that targets built-up grime, dust, and hard-to-reach areas for a true reset in {suburb}.",
        f"A detailed deep clean that tackles the areas regular cleans miss, leaving your {suburb} home refreshed.",
        f"An intensive clean that targets dust, buildup, and hidden corners for a complete {suburb} refresh.",
    ])

    move_desc = _pick(rng, [
        f"A complete move-in or move-out clean that helps you transition smoothly with a spotless {suburb} property.",
        f"End-of-lease or move-in cleaning that leaves your {suburb} property spotless and ready for the next chapter.",
        f"A full property clean for move-in or move-out so everything in your {suburb} home is left pristine.",
    ])

    how_title = _pick(rng, [
        "A simpler way to a clean home",
        "Cleaning made easy",
        "A smooth path to a spotless home",
    ])

    process_title = _pick(rng, [
        f"Our streamlined process makes it easy to book, easy to manage, and easy to enjoy a spotless result in {suburb} without disrupting your schedule.",
        f"We keep the process simple and efficient so you can book quickly, get great results, and move on with your day in {suburb}.",
        f"From booking to finish, we make cleaning straightforward and stress-free with clear communication and dependable service in {suburb}.",
    ])

    testimonials_title = _pick(rng, [
        f"What {suburb} residents say about us",
        f"What {suburb} locals think about us",
        f"How {suburb} residents rate our service",
    ])

    testimonials_desc = _pick(rng, [
        f"Real feedback from {suburb} families who love coming home to a cleaner, healthier space.",
        f"Hear from {suburb} locals who trust our team for consistent, high-quality cleaning.",
        f"Reviews from {suburb} residents who rely on us for a spotless home.",
    ])

    t1 = _pick(rng, [
        f"In {suburb}, it is hard to find a service this consistent. The team is punctual and leaves everything spotless every time.",
        f"The cleaners in {suburb} are always on time and thorough. The house looks fantastic after every visit.",
        f"We tried a few options in {suburb}, but this team is the most reliable and the results are always excellent.",
    ])

    t2 = _pick(rng, [
        f"We booked a deep clean in {suburb} and the results were amazing. They handled every detail and the home felt brand new.",
        f"Our {suburb} deep clean was outstanding. They tackled areas I always miss and the place felt refreshed.",
        f"The deep clean in {suburb} was worth it. The team was professional and the results were impressive.",
    ])

    t3 = _pick(rng, [
        f"Reliable and professional cleaners in {suburb}. Coming home after a service visit is the best feeling.",
        f"We love the service in {suburb}. It is consistent, friendly, and the results are always spotless.",
        f"Great service in {suburb}—professional team, clear communication, and a beautifully clean home every time.",
    ])

    faq_title = _pick(rng, [
        f"{suburb} Cleaning FAQ",
        f"{suburb} Service FAQ",
        f"FAQs for {suburb} Cleaning",
    ])

    faq_desc = _pick(rng, [
        f"Find answers about our {suburb} cleaning services, booking options, and what to expect on the day.",
        f"Common questions about cleaning in {suburb}, scheduling, and what our service includes.",
        f"Everything you need to know about booking a clean in {suburb} and how our service works.",
    ])

    blog_title = _pick(rng, [
        f"{suburb} Cleaning Tips",
        f"{suburb} Home Care Tips",
        f"Local Cleaning Tips for {suburb}",
    ])

    blog_desc = _pick(rng, [
        "Practical advice from our local experts to keep your home looking its best.",
        "Simple tips from our team to help you maintain a fresh, tidy home.",
        "Helpful cleaning advice to keep your home comfortable between visits.",
    ])

    # Enforce uniqueness per field
    bumpers = {
        "meta": ["Book online.", "Eco-friendly service.", "Local, reliable team."],
        "hero": ["Get started today.", "We are ready to help.", "Stress-free cleaning."],
        "about": ["We care for your home.", "Quality you can trust.", "Tailored to your needs."],
        "why": ["Local expertise, every visit.", "Consistent results, always.", "Trusted across the area."],
        "services": ["Pick what fits you.", "Flexible options available.", "Simple, clear choices."],
        "standard": ["Perfect for upkeep.", "Ideal for weekly care.", "Great for busy homes."],
        "deep": ["Ideal for a reset.", "Great for seasonal cleans.", "Perfect for a refresh."],
        "move": ["Move with confidence.", "Leave it spotless.", "Start fresh."],
        "process": ["Fast to book.", "Clear and simple.", "No hassle."],
        "testimonials": ["Loved by locals.", "Top-rated nearby.", "Highly recommended."],
        "faq": ["Get quick answers.", "Clear details included.", "Helpful guidance."],
        "blog": ["Fresh tips inside.", "Read the latest.", "Helpful ideas."],
    }

    meta_title = _unique_or_bump(rng, used["META_TITLE"], meta_title, bumpers["meta"])
    meta_desc = _unique_or_bump(rng, used["META_DESCRIPTION"], meta_desc, bumpers["meta"])
    hero_title = _unique_or_bump(rng, used["HERO_TITLE"], hero_title, bumpers["hero"])
    hero_desc = _unique_or_bump(rng, used["HERO_DESCRIPTION"], hero_desc, bumpers["hero"])
    about_title = _unique_or_bump(rng, used["ABOUT_SECTION_TITLE"], about_title, bumpers["about"])
    about_desc = _unique_or_bump(rng, used["ABOUT_DESC"], about_desc, bumpers["about"])
    why_title = _unique_or_bump(rng, used["WHY_CHOOSE_SECTION_TITLE"], why_title, bumpers["why"])
    why_desc = _unique_or_bump(rng, used["WHY_CHOOSE_US_DESC"], why_desc, bumpers["why"])
    services_title = _unique_or_bump(rng, used["SERVICES_SECTION_TITLE"], services_title, bumpers["services"])
    services_desc = _unique_or_bump(rng, used["SERVICES_DESC"], services_desc, bumpers["services"])
    standard_desc = _unique_or_bump(rng, used["STANDARD_CLEAN_DESCRIPTION"], standard_desc, bumpers["standard"])
    deep_desc = _unique_or_bump(rng, used["DEEP_CLEAN_DESCRIPTION"], deep_desc, bumpers["deep"])
    move_desc = _unique_or_bump(rng, used["MOVE_CLEAN_DESCRIPTION"], move_desc, bumpers["move"])
    how_title = _unique_or_bump(rng, used["HOW_WORKS_TITLE"], how_title, bumpers["process"])
    process_title = _unique_or_bump(rng, used["PROCESS_SECTION_TITLE"], process_title, bumpers["process"])
    testimonials_title = _unique_or_bump(rng, used["TESTIMONIALS_TITLE"], testimonials_title, bumpers["testimonials"])
    testimonials_desc = _unique_or_bump(rng, used["TESTIMONIALS_DESC"], testimonials_desc, bumpers["testimonials"])
    t1 = _unique_or_bump(rng, used["TESTIMONIAL_1_TEXT"], t1, bumpers["testimonials"])
    t2 = _unique_or_bump(rng, used["TESTIMONIAL_2_TEXT"], t2, bumpers["testimonials"])
    t3 = _unique_or_bump(rng, used["TESTIMONIAL_3_TEXT"], t3, bumpers["testimonials"])
    faq_title = _unique_or_bump(rng, used["FAQ_TITLE"], faq_title, bumpers["faq"])
    faq_desc = _unique_or_bump(rng, used["FAQ_DESC"], faq_desc, bumpers["faq"])
    blog_title = _unique_or_bump(rng, used["BLOG_TITLE"], blog_title, bumpers["blog"])
    blog_desc = _unique_or_bump(rng, used["BLOG_DESC"], blog_desc, bumpers["blog"])

    return {
        "[[META_TITLE]]": meta_title,
        "[[META_DESCRIPTION]]": meta_desc,
        "[[HERO_TITLE]]": hero_title,
        "[[HERO_DESCRIPTION]]": hero_desc,
        "[[ABOUT_SECTION_TITLE]]": about_title,
        "[[ABOUT_DESC]]": about_desc,
        "[[WHY_CHOOSE_SECTION_TITLE]]": why_title,
        "[[WHY_CHOOSE_US_DESC]]": why_desc,
        "[[SERVICES_SECTION_TITLE]]": services_title,
        "[[SERVICES_DESC]]": services_desc,
        "[[STANDARD_CLEAN_DESCRIPTION]]": standard_desc,
        "[[DEEP_CLEAN_DESCRIPTION]]": deep_desc,
        "[[MOVE_CLEAN_DESCRIPTION]]": move_desc,
        "[[HOW_WORKS_TITLE]]": how_title,
        "[[PROCESS_SECTION_TITLE]]": process_title,
        "[[TESTIMONIALS_TITLE]]": testimonials_title,
        "[[TESTIMONIALS_DESC]]": testimonials_desc,
        "[[TESTIMONIAL_1_TEXT]]": t1,
        "[[TESTIMONIAL_2_TEXT]]": t2,
        "[[TESTIMONIAL_3_TEXT]]": t3,
        "[[FAQ_TITLE]]": faq_title,
        "[[FAQ_DESC]]": faq_desc,
        "[[BLOG_TITLE]]": blog_title,
        "[[BLOG_DESC]]": blog_desc,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Fill missing suburb texts based on index.html messaging.")
    parser.add_argument("--texts", default="suburbs/suburbs_texts.txt")
    parser.add_argument("--list", default="suburbs/suburbs_info")
    parser.add_argument("--template", default="suburbs/template.html")
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--overwrite-testimonials", action="store_true")
    parser.add_argument("--overwrite-all", action="store_true")
    args = parser.parse_args()

    texts_path = Path(args.texts)
    list_path = Path(args.list)
    template_path = Path(args.template)

    if not texts_path.exists():
        raise FileNotFoundError(f"Texts not found: {texts_path}")
    if not list_path.exists():
        raise FileNotFoundError(f"Suburb list not found: {list_path}")
    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")

    lines = texts_path.read_text(encoding="utf-8").splitlines()
    header = load_header(lines)
    existing = parse_texts(lines)

    suburbs = [s.strip() for s in list_path.read_text(encoding="utf-8").splitlines() if s.strip()]
    placeholders = set(PLACEHOLDER_RE.findall(template_path.read_text(encoding="utf-8")))
    placeholder_tokens = {f"[[{p}]]" for p in placeholders}

    output_lines = header[:]
    if output_lines and output_lines[-1].strip() != "":
        output_lines.append("")

    used = defaultdict(set)

    for suburb in suburbs:
        output_lines.append(f"[{suburb}]")
        base = template_texts(suburb, used)
        merged = {}
        if suburb in existing:
            merged.update(existing[suburb])
        # Fill missing keys with base template
        for token in sorted(placeholder_tokens):
            force_testimonials = args.overwrite_testimonials and token in {
                "[[TESTIMONIALS_TITLE]]",
                "[[TESTIMONIALS_DESC]]",
                "[[TESTIMONIAL_1_TEXT]]",
                "[[TESTIMONIAL_2_TEXT]]",
                "[[TESTIMONIAL_3_TEXT]]",
            }
            if token in merged and not force_testimonials and not args.overwrite_all:
                value = merged[token]
            else:
                value = base.get(token, "")
            output_lines.append(f"{token}: {value}")
        output_lines.append("")

    content = "\n".join(output_lines).rstrip() + "\n"

    if args.write:
        texts_path.write_text(content, encoding="utf-8")
    else:
        print(content)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
