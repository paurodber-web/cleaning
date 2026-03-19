import re
import random

def rewrite_titles_with_ai_quality(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Curated, high-conversion, human-centric titles written by me
    title_pool = {
        'ABOUT_SECTION_TITLE': [
            "A Local Team Dedicated to Your Home's Shine",
            "Providing the Detailed Care Your Home Deserves",
            "Quality Home Cleaning with a Personal Touch",
            "Meet the Professionals Behind Your Spotless Home",
            "Our Commitment to a Cleaner, Healthier Home",
            "Expert Care for Your Most Important Space",
            "Reliable Cleaning Professionals You Can Trust",
            "Passion for Perfection in Every Room",
            "Making Your Living Space Truly Sparkle",
            "Dedicated to Excellence in Local Home Care"
        ],
        'WHY_CHOOSE_SECTION_TITLE': [
            "Why Your Neighbors Prefer Our Service",
            "Reliable Results for a Stress-Free Home",
            "The Difference is in the Little Details",
            "What Local Families Love About Our Care",
            "A Consistently Clean Home Without the Hassle",
            "Why We’re the Top Choice for Local Residents",
            "Peace of Mind with Every Single Visit",
            "Professionalism and Quality You Can Count On",
            "Our Secret to a Perfectly Maintained Home",
            "Exceeding Expectations One Clean at a Time"
        ],
        'SERVICES_SECTION_TITLE': [
            "Cleaning Solutions Tailored to Your Lifestyle",
            "From Weekly Upkeep to Deep Seasonal Refreshes",
            "Expert Home Care Designed Specifically for You",
            "Explore Our Most Popular Cleaning Packages",
            "Complete Cleaning Services for Your Home",
            "Flexible Plans for a Spotless Living Space",
            "Tackling Everything from Dust to Deep Grime",
            "Professional Care for Every Corner of Your House",
            "Versatile Services to Suit Your Busy Schedule",
            "Quality Cleaning Options for Every Local Home"
        ],
        'HOW_WORKS_TITLE': [
            "Book Your First Professional Shine in Seconds",
            "Our Simple and Effortless Path to a Cleaner Home",
            "How We Deliver a Spotless House Every Single Time",
            "Getting Started with Your Local Team is Easy",
            "Three Simple Steps to a Glowing Living Space",
            "Our Process for Guaranteed Cleaning Results",
            "Ready for a Fresh Start? Here’s How it Works",
            "Seamless Booking and Superior Cleaning Care",
            "Your Journey to a Perfectly Tidy Home Starts Here",
            "Effortless Home Care from Start to Finish"
        ],
        'TESTIMONIALS_TITLE': [
            "Client Stories from Your Local Neighborhood",
            "What Your Neighbors Say About the Results",
            "Kind Words from Our Regular Local Clients",
            "Real Feedback from Happy Local Homeowners",
            "Why Our Community Trusts Our Cleaning Team",
            "Genuine Reviews from People in Your Area",
            "Success Stories: A Cleaner Home for Local Families",
            "What Makes Our Customers Keep Coming Back",
            "Honest Experiences from Local Residents Like You",
            "The Results Speak for Themselves: Client Praise"
        ],
        'BLOG_TITLE': [
            "Expert Advice for a Healthier, Happier Home",
            "Our Latest Cleaning Tips and Lifestyle Hacks",
            "Pro Guides to Keeping Your Living Space Fresh",
            "Simple Solutions for a Consistently Tidy House",
            "Professional Insights for Better Home Maintenance",
            "Smart Tricks to Keep Your Place Looking Great",
            "Our Best Secrets for an Organized Living Space",
            "Helpful Articles for Busy Local Homeowners",
            "Enhance Your Home with Our Practical Advice",
            "Stay Informed with Our Local Home Care Blog"
        ],
        'FAQ_TITLE': [
            "Clear Answers to Your Common Home Care Questions",
            "Everything You Need to Know Before You Book",
            "Helpful Details for Your Ultimate Peace of Mind",
            "Common Questions About Our Local Cleaning Service",
            "Quick Answers to Help You Get Started Today",
            "Understanding Our Services: Your FAQ Guide",
            "Simple Information for a Better Service Experience",
            "We’re Here to Help: Common Inquiries Answered",
            "Your Top Questions About Professional Cleaning",
            "Get the Facts About Our Quality Cleaning Care"
        ]
    }

    def replace_with_variety(match):
        suburb_block = match.group(0)
        
        for tag, variations in title_pool.items():
            # Pick a unique variation for each tag in this block
            selected_title = random.choice(variations)
            suburb_block = re.sub(rf'\[\[{tag}\]\]: .*', f'[[{tag}]]: {selected_title}', suburb_block)
        
        return suburb_block

    # Use multiline regex to process block by block
    new_content = re.sub(r'\[.*?\]\n(?:.*?\n)+?(?=\n\[|$)', replace_with_variety, content, flags=re.MULTILINE)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    rewrite_titles_with_ai_quality('suburbs/suburbs_text')
    print("All section titles updated with high-quality, human-centric redaction.")
