import re
import random

def rewrite_testimonials(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Human-sounding templates for testimonials
    # Category 1: General satisfaction and feeling
    templates_1 = [
        "They do a great job with our place. It's so nice to find someone who actually cares about the details.",
        "Best decision we've made for our home. Everything looks amazing every time they come over.",
        "Honestly the most reliable cleaning crew we've ever had. Our house has never looked this good.",
        "Coming home after they've been is the highlight of my week. Everything is just so fresh and tidy.",
        "Super happy with the service. They are always on time and they really do a proper job every visit.",
        "I can't recommend them enough. They make keeping the house clean so much easier for us.",
        "The team is lovely and they do such a thorough job. It's a weight off my shoulders for sure.",
        "Everything is always spotless when they finish. It's such a relief to have one less thing to worry about.",
    ]
    
    # Category 2: Time-saving and lifestyle
    templates_2 = [
        "Now we can actually enjoy our weekends instead of spending the whole day scrubbing floors.",
        "It's life changing having this sorted. We finally have some free time to actually relax together.",
        "They've saved us so much time. I can focus on work now without worrying about the mess at home.",
        "We can finally go out on Saturdays instead of cleaning. The house looks fantastic every single time.",
        "It's so nice to have our weekends back. They do a much better job than I ever could anyway.",
        "Having them come over has been a game changer for our family. More quality time and a clean house.",
        "I don't know how we managed before. It's so worth it to have the place looking this sharp.",
        "It's just great to have the weekends free again. They really take the stress out of the housework.",
    ]
    
    # Category 3: Specific quality or detail
    templates_3 = [
        "The house smells amazing after every visit. They really pay attention to the little things.",
        "Everything truly shines. They never miss a spot and they're always so careful with our things.",
        "I'm always impressed by how thorough they are. Even the tricky corners are perfectly clean.",
        "The whole place feels brand new again. They really go the extra mile to make sure it's right.",
        "They are so professional and the results are always consistent. It's exactly what we were looking for.",
        "Our carpets and floors have never looked better. They really know what they're doing.",
        "It's great to find people you can trust who also do a brilliant job. The house feels so much better.",
        "They are super thorough and efficient. The place is always glowing by the time they're done.",
    ]

    def replace_testimonials(match):
        suburb_block = match.group(0)
        
        # Pick 3 random templates for this suburb to ensure variety
        t1 = random.choice(templates_1)
        t2 = random.choice(templates_2)
        t3 = random.choice(templates_3)
        
        # Replace the tags
        suburb_block = re.sub(r'\[\[TESTIMONIAL_1_TEXT\]\]: .*', f'[[TESTIMONIAL_1_TEXT]]: {t1}', suburb_block)
        suburb_block = re.sub(r'\[\[TESTIMONIAL_2_TEXT\]\]: .*', f'[[TESTIMONIAL_2_TEXT]]: {t2}', suburb_block)
        suburb_block = re.sub(r'\[\[TESTIMONIAL_3_TEXT\]\]: .*', f'[[TESTIMONIAL_3_TEXT]]: {t3}', suburb_block)
        
        return suburb_block

    # Regex to match each suburb block
    new_content = re.sub(r'\[.*?\]\n(?:.*?\n)+?(?=\n\[|$)', replace_testimonials, content, flags=re.MULTILINE)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    rewrite_testimonials('suburbs/suburbs_text')
    print("Testimonials rewritten successfully.")
