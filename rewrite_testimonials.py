import re
import random

def rewrite_testimonials(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Human-sounding templates for testimonials (expanded by ~3-4 words)
    # Category 1: General satisfaction and feeling
    templates_1 = [
        "They do a great job with our place every week. It's so nice to find someone who actually cares about the little details.",
        "Best decision we've made for our home lately. Everything looks amazing and smells so fresh every time they come over.",
        "Honestly the most reliable cleaning crew we've ever had by far. Our house has never looked this good and tidy.",
        "Coming home after they've been is easily the highlight of my week. Everything is just so fresh, clean and tidy.",
        "Super happy with the service they provide us. They are always on time and they really do a proper job every visit.",
        "I honestly can't recommend them enough to everyone. They make keeping the whole house clean so much easier for us now.",
        "The team is absolutely lovely and they do such a thorough job. It's a huge weight off my shoulders for sure.",
        "Everything is always spotless and perfect when they finish. It's such a relief to have one less thing to worry about daily.",
    ]
    
    # Category 2: Time-saving and lifestyle
    templates_2 = [
        "Now we can actually enjoy our weekends together instead of spending the whole day scrubbing floors and dusting everything.",
        "It's life changing having this sorted for us. We finally have some real free time to actually relax and unwind together.",
        "They've saved us so much time every single week. I can focus on my work now without worrying about the mess at home.",
        "We can finally go out on Saturdays now instead of cleaning. The house looks fantastic and welcoming every single time.",
        "It's so nice to have our weekends back for ourselves. They do a much better job than I ever could anyway.",
        "Having them come over has been a total game changer for our family. More quality time together and a clean house.",
        "I don't know how we managed before they started. It's so worth it to have the place looking this sharp and clean.",
        "It's just great to have the weekends free again for fun. They really take the stress out of the weekly housework.",
    ]
    
    # Category 3: Specific quality or detail
    templates_3 = [
        "The house smells absolutely amazing after every single visit. They really pay attention to the little things that matter.",
        "Everything truly shines once they are done. They never miss a spot and they're always so careful with our things.",
        "I'm always impressed by how thorough they are every time. Even the tricky corners are left perfectly clean and shiny.",
        "The whole place feels brand new again after they leave. They really go the extra mile to make sure it's done right.",
        "They are so professional and the results are always very consistent. It's exactly what we were looking for in a service.",
        "Our carpets and floors have never looked better than they do now. They really know what they're doing with every surface.",
        "It's great to find people you can trust who also do a brilliant job. The house feels so much better and brighter.",
        "They are super thorough and efficient with their work. The place is always glowing by the time they're finished.",
    ]

    # Names lists for variety
    first_names = ["Sarah", "Mark", "Emma", "Paul", "Chloe", "David", "Mia", "Ben", "Eleanor", "James", "Sophie", "Liam"]
    last_names = ["Thompson", "Davis", "Wilson", "Roberts", "Smith", "Anderson", "Clarke", "Walker", "White", "Taylor", "Martin", "Lewis"]

    def replace_testimonials(match):
        suburb_block = match.group(0)
        
        # Pick 3 random templates for this suburb to ensure variety
        t1 = random.choice(templates_1)
        t2 = random.choice(templates_2)
        t3 = random.choice(templates_3)
        
        # Pick 3 random names
        n1 = f"{random.choice(first_names)} {random.choice(last_names)}"
        n2 = f"{random.choice(first_names)} {random.choice(last_names)}"
        n3 = f"{random.choice(first_names)} {random.choice(last_names)}"
        
        # Replace the tags
        suburb_block = re.sub(r'\[\[TESTIMONIAL_1_TEXT\]\]: .*', f'[[TESTIMONIAL_1_TEXT]]: {t1}', suburb_block)
        suburb_block = re.sub(r'\[\[TESTIMONIAL_2_TEXT\]\]: .*', f'[[TESTIMONIAL_2_TEXT]]: {t2}', suburb_block)
        suburb_block = re.sub(r'\[\[TESTIMONIAL_3_TEXT\]\]: .*', f'[[TESTIMONIAL_3_TEXT]]: {t3}', suburb_block)

        suburb_block = re.sub(r'\[\[TESTIMONIAL_1_NAME\]\]: .*', f'[[TESTIMONIAL_1_NAME]]: {n1}', suburb_block)
        suburb_block = re.sub(r'\[\[TESTIMONIAL_2_NAME\]\]: .*', f'[[TESTIMONIAL_2_NAME]]: {n2}', suburb_block)
        suburb_block = re.sub(r'\[\[TESTIMONIAL_3_NAME\]\]: .*', f'[[TESTIMONIAL_3_NAME]]: {n3}', suburb_block)
        
        return suburb_block

    # Regex to match each suburb block
    new_content = re.sub(r'\[.*?\]\n(?:.*?\n)+?(?=\n\[|$)', replace_testimonials, content, flags=re.MULTILINE)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    rewrite_testimonials('suburbs/suburbs_text')
    print("Testimonials rewritten successfully with expanded text.")
