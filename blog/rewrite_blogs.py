import re

html_template = """<h2>{title}</h2>
<p>{intro}</p>
<article>
        <h3>{h1}</h3>
        <p>{p1}</p>
</article>
<article>
        <h3>{h2}</h3>
        <p>{p2}</p>
</article>
<article>
        <h3>{h3}</h3>
        <p>{p3}</p>
        <ul>
                <li>{li1}</li>
                <li>{li2}</li>
                <li>{li3}</li>
        </ul>
        <p>{p3b}</p>
</article>
<article>
        <h3>{h4}</h3>
        <p>{p4}</p>
</article>
<article>
        <div class="row cs_gap_y_24 cs_mb_24">
                <div class="col-md-6" data-aos="fade-right">
                        <img alt="Blog Details" class="cs_radius_16 w-100" src="../assets/img/post-img6.webp" />
                </div>
                <div class="col-md-6" data-aos="fade-left">
                        <img alt="Blog Details" class="cs_radius_16 w-100" src="../assets/img/post-img5.webp" />
                </div>
        </div>
        <h3>{h5}</h3>
        <p>{p5}</p>
</article>
<article>
        <h3>{h6}</h3>
        <p>{p6}</p>
</article>
<article>
        <h3>{h7}</h3>
        <p>{p7}</p>
</article>
<article>
        <h3>{final_h}</h3>
        <p>{final_p}</p>
</article>
<blockquote>
        {quote}
</blockquote>
<div class="cs_video_block_style_1 cs_center cs_bg_filed cs_radius_16 cs_mb_24" data-aos="zoom-in" data-src="../assets/img/video-bg1.webp">
        <a aria-label="Video link" class="cs_player_btn_style_1 cs_video_open cs_center cs_radius_100 position-relative" href="https://www.youtube.com/embed/oCOq0L2xeag">
                <span class="cs_white_bg cs_blue_dark cs_player_btn_icon cs_center">
                        <i class="fa-solid fa-play"></i>
                </span>
        </a>
</div>
<p>{outro}</p>"""

data = {
    "7-quick-cleaning-hacks.html": {
        "title": "7 Quick Cleaning Hacks for Busy Families",
        "intro": "Keeping a tidy home in Melbourne when you have a packed schedule feels impossible sometimes. You want a fresh space to relax in, but spending your entire weekend scrubbing floors is not the answer. The secret is finding small shortcuts that make a huge difference without taking up much time. With a few smart habits, you can maintain a welcoming house while still enjoying your free time.",
        "h1": "1. The One Minute Rule",
        "p1": "If a task takes less than a minute, just do it immediately. Putting your shoes in the closet or wiping down the bathroom sink right after brushing your teeth prevents clutter from building up. Small actions stop mess from turning into a major chore.",
        "h2": "2. Keep Supplies Close",
        "p2": "You are much more likely to clean if the products are right there. Store a basic multi surface spray and a cloth in every bathroom. When you see a spot, you can wipe it instantly instead of walking to the laundry room and getting distracted along the way.",
        "h3": "3. Focus on High Traffic Areas",
        "p3": "Not every room needs deep attention every day. The hallway, kitchen floor, and main living space gather the most dirt.",
        "li1": "A quick sweep of the kitchen floor takes two minutes.",
        "li2": "Tidying the entryway makes the whole house feel cleaner.",
        "li3": "Fluffing the couch cushions creates an instant sense of order.",
        "p3b": "Prioritize these spots to maintain an overall feeling of cleanliness.",
        "h4": "4. Empty the Dishwasher in the Morning",
        "p4": "Starting the day with an empty dishwasher changes everything. You can put dirty plates straight inside after breakfast and dinner, keeping the sink completely empty. An empty kitchen sink instantly makes the entire kitchen look spotless.",
        "h5": "5. Do a Nightly Ten Minute Tidy",
        "p5": "Set a timer for ten minutes before bed. Have everyone in the family pick up their own items from the living room and wipe down the kitchen counters. Waking up to a clean space sets a positive tone for the entire morning.",
        "h6": "6. Use Doormats Generously",
        "p6": "Stop the dirt before it enters your home. Place quality doormats outside and inside every exterior door. This single addition dramatically cuts down the amount of sweeping and mopping you need to do.",
        "h7": "7. Let Professionals Handle the Rest",
        "p7": "Sometimes the best hack is asking for help. Booking a regular residential cleaning service in Melbourne means all the heavy lifting is done for you. You get to come home to a sparkling house and spend your weekends doing what you actually love.",
        "final_h": "Enjoy Your Clean Space",
        "final_p": "You don't need a perfectly pristine house every single second, just a manageable routine. Try implementing one or two of these habits this week and see how much easier keeping things tidy becomes.",
        "quote": "A clean home is not about perfection. It is about creating a comfortable space where your family can relax without the constant stress of unfinished chores.",
        "outro": "Life is too short to stress over housework. By using these simple strategies, busy families can finally find the balance between a fresh living space and a schedule that actually works for them."
    },
    "benefits-green-cleaning.html": {
        "title": "The Benefits of Green Cleaning Products",
        "intro": "Switching to eco friendly products is one of the best decisions you can make for your household. Traditional chemicals often leave strong smells and residues that linger in the air. By choosing natural alternatives, you create a safer environment for your family and pets while getting the same great results right here in Melbourne.",
        "h1": "1. Better Indoor Air Quality",
        "p1": "Strong artificial fragrances and harsh chemicals can irritate your lungs. Natural products do not release toxic fumes, meaning the air inside your home stays fresh and safe to breathe all year round.",
        "h2": "2. Safe for Kids and Pets",
        "p2": "Children and animals spend a lot of time on the floor. When you use plant based cleaners, you never have to worry about them coming into contact with dangerous chemical residues left behind after mopping.",
        "h3": "3. Kinder to the Environment",
        "p3": "Every time you wash chemicals down the drain, they end up in the local water system. Green products are biodegradable and safe for our waterways.",
        "li1": "They break down naturally without harming wildlife.",
        "li2": "Packaging is often recyclable or made from recycled materials.",
        "li3": "Manufacturing processes have a lower carbon footprint.",
        "p3b": "It is an easy way to reduce your household impact on the planet.",
        "h4": "4. Less Risk of Skin Irritation",
        "p4": "Standard cleaners often require gloves and masks to prevent burns or rashes. Gentle, natural ingredients do the job effectively without putting your skin at risk during your weekly scrubbing session.",
        "h5": "5. They Actually Smell Great",
        "p5": "Instead of an overpowering bleach scent, natural products use essential oils like lemon, lavender, and eucalyptus. Your home will smell like a real garden instead of a hospital room.",
        "h6": "6. Protects Your Furniture",
        "p6": "Harsh chemicals can slowly strip the finish off your wooden tables and ruin expensive stone benchtops. Gentle cleaners protect your investments and keep your surfaces looking new for much longer.",
        "h7": "7. Professional Cleaners Love Them",
        "p7": "Top tier cleaning services in Melbourne are increasingly switching to green solutions. It shows a commitment to quality and customer care, ensuring your home gets a premium clean that respects your health.",
        "final_h": "A Healthier Home Awaits",
        "final_p": "The transition to green cleaning is simple and incredibly rewarding. You will notice the difference in how your house smells and feels almost immediately.",
        "quote": "Choosing natural products is not just a trend. It is a commitment to the long term health of your family and the beautiful environment we share.",
        "outro": "Whether you buy them at the store or hire a service that uses them exclusively, green cleaning products are a smart, effective choice for any modern household."
    },
    "choose-right-disinfectants.html": {
        "title": "How to Choose the Right Disinfectants",
        "intro": "Keeping your home and workplace safe from germs is always a priority. With so many options on the supermarket shelves, figuring out which one actually works can be confusing. The ideal product should eliminate harmful bacteria without being overly toxic for everyday use. Here is a simple guide to picking the best options for your property.",
        "h1": "1. Understand the Difference",
        "p1": "Cleaning and disinfecting are two separate steps. Cleaning removes dirt and grime from a surface, while disinfecting actually kills the microscopic germs. You usually need to clean a surface first before the disinfectant can do its job properly.",
        "h2": "2. Read the Labels Carefully",
        "p2": "Not all products kill the same germs. Look for labels that explicitly state they eliminate viruses and bacteria. A proper product will clearly list what it is effective against and how to use it safely.",
        "h3": "3. Check the Contact Time",
        "p3": "Most people spray and wipe immediately, but that does not kill the germs. Disinfectants need time to sit on the surface to work.",
        "li1": "Some require one minute of wet contact time.",
        "li2": "Others might need up to ten minutes.",
        "li3": "Always leave the surface wet for the recommended time.",
        "p3b": "Following the contact time is the only way to ensure the area is truly sanitized.",
        "h4": "4. Match Product to Surface",
        "p4": "Bleach based items are incredibly strong but will ruin fabrics and delicate stone. Always ensure the product you choose is formulated for the specific material you are cleaning, whether it is glass, wood, or stainless steel.",
        "h5": "5. Prioritize High Touch Areas",
        "p5": "You do not need to disinfect your entire house from top to bottom. Focus your efforts on the things people touch constantly, like door handles, light switches, and TV remotes.",
        "h6": "6. Consider Eco Friendly Alternatives",
        "p6": "If you have a sensitive household, heavy chemicals might cause issues. Look for botanical disinfectants that use ingredients like thymol, which are highly effective against germs but much gentler on your respiratory system.",
        "h7": "7. Hire Experts for Deep Sanitation",
        "p7": "If your home needs a thorough reset, professional cleaners know exactly which products to use. A specialized Melbourne cleaning crew brings commercial grade, safe solutions that leave your space genuinely hygienic.",
        "final_h": "Stay Smart and Safe",
        "final_p": "Selecting the right tools makes all the difference in maintaining a healthy environment. A little bit of knowledge goes a long way in protecting your family.",
        "quote": "Effective sanitization is about working smarter. Choosing the correct product and using it the right way ensures your home remains a safe haven.",
        "outro": "Next time you are at the store, take a moment to read the back of the bottle. Making an informed choice ensures your home stays sparkling and secure."
    },
    "eco-friendly-cleaning-products.html": {
        "title": "Eco-Friendly Cleaning Products Really Work",
        "intro": "There is a common misconception that natural products simply cannot handle tough grime. Many people believe you need heavy chemicals to get a truly spotless kitchen or bathroom. However, the latest eco friendly formulas are incredibly powerful and capable of tackling the hardest messes in your Melbourne home.",
        "h1": "1. The Power of Natural Acids",
        "p1": "Ingredients like white vinegar are natural powerhouses. They effortlessly dissolve hard water stains, soap scum, and mineral deposits. You get a brilliant shine on your bathroom fixtures without inhaling toxic fumes.",
        "h2": "2. Baking Soda for Scrubbing",
        "p2": "When you need a mild abrasive, baking soda is unmatched. It cuts through baked on grease in the oven and lifts stains from countertops. It is completely safe and incredibly effective at neutralizing bad odors at the same time.",
        "h3": "3. Enzymes Eat Grime",
        "p3": "Modern green cleaners often use plant derived enzymes. These microscopic helpers literally digest organic stains and odors.",
        "li1": "They are perfect for pet accidents on carpets.",
        "li2": "They work brilliantly on food spills in the kitchen.",
        "li3": "They continue working even after you finish wiping.",
        "p3b": "Enzyme cleaners provide a deep clean that traditional soaps cannot match.",
        "h4": "4. Essential Oils do More Than Smell Good",
        "p4": "Tea tree, eucalyptus, and lavender oils possess natural antibacterial properties. They help sanitize surfaces while leaving your home smelling like a luxurious spa rather than a laboratory.",
        "h5": "5. Gentle on Your Belongings",
        "p5": "Standard harsh cleaners can degrade the protective coatings on your floors and furniture over time. Green products lift the dirt gently, preserving the life and look of your expensive interior finishes.",
        "h6": "6. Better for Long Term Health",
        "p6": "Using products without synthetic dyes and fragrances means your family is not exposed to daily irritants. This is especially important for households dealing with asthma or sensitive skin conditions.",
        "h7": "7. Trusted by the Pros",
        "p7": "The best cleaning companies in Melbourne rely on eco friendly ranges because they deliver exceptional results safely. When the experts trust natural solutions, you know they are up to the task.",
        "final_h": "Make the Switch Today",
        "final_p": "You do not have to compromise on cleanliness to be kind to the earth. The natural route provides everything you need for a pristine living space.",
        "quote": "Nature provides some of the most effective cleaning agents available. Harnessing them means a brilliant home without the chemical compromise.",
        "outro": "Try swapping out just one or two of your regular sprays for a natural alternative. You will quickly see that green cleaning is not just a buzzword, it is a superior way to care for your home."
    },
    "how-often-clean-home.html": {
        "title": "How Often Should You Clean Your Home?",
        "intro": "Figuring out the right cleaning schedule can feel like a guessing game. Do you need to vacuum every single day, or is once a week enough? Every household in Melbourne is different, but having a general guideline helps prevent the mess from becoming overwhelming. Breaking tasks down by frequency keeps your house looking great without burning you out.",
        "h1": "1. Daily Tidy Ups",
        "p1": "Some things simply cannot wait. Making the bed, doing the dishes, and wiping down the kitchen bench should happen every day. These tiny tasks take minutes but completely change how neat your home feels.",
        "h2": "2. Weekly Essentials",
        "p2": "Once a week, you should tackle the dust and the floors. Vacuuming the carpets, mopping the hard floors, and giving the bathroom a good scrub are weekly musts. This prevents dirt from embedding itself into your surfaces.",
        "h3": "3. The Fortnightly Chores",
        "p3": "Every two weeks is the perfect time to handle tasks that get ignored during a quick clean.",
        "li1": "Changing the bed linens and washing the sheets.",
        "li2": "Wiping down the inside of the microwave.",
        "li3": "Dusting ceiling fans and skirting boards.",
        "p3b": "These biweekly habits keep the hidden dust at bay.",
        "h4": "4. Monthly Deep Dives",
        "p4": "Set aside a few hours a month for a deeper refresh. This is when you should clean the inside of your oven, wipe down the interior windows, and vacuum your upholstered furniture.",
        "h5": "5. Seasonal Deep Cleaning",
        "p5": "Four times a year, your home needs serious attention. Decluttering closets, washing the curtains, and deep cleaning the carpets reset your home for the new season. It is a big job, but entirely worth the effort.",
        "h6": "6. Adjust for Pets and Kids",
        "p6": "If you have a busy house with dogs or small children, you will need to increase the frequency. Floors might need vacuuming every two days, and laundry will certainly pile up much faster.",
        "h7": "7. Bring in Regular Help",
        "p7": "If sticking to a schedule feels impossible, you are not alone. Setting up a fortnightly residential cleaning service takes the pressure off. You get the consistency of a spotless home without having to manage the timetable yourself.",
        "final_h": "Find Your Rhythm",
        "final_p": "The best schedule is the one you can actually stick to. Do not aim for perfection, aim for consistency. A little bit of effort regularly makes a massive difference.",
        "quote": "A home should be lived in, not constantly managed. A smart schedule gives you back your weekends while keeping your space perfectly fresh.",
        "outro": "Assess your current routine and see where you can make small adjustments. A balanced approach ensures your home remains a sanctuary rather than a source of stress."
    },
    "spring-cleaning-checklist.html": {
        "title": "Spring Cleaning Checklist You Can Follow",
        "intro": "When the weather starts to warm up in Melbourne, it is the perfect time to refresh your living space. Spring cleaning is an annual tradition that clears out the winter dust and brings new energy into your home. However, looking at the entire house can be daunting. A structured checklist makes the process highly satisfying and easy to manage.",
        "h1": "1. Start with a Major Declutter",
        "p1": "Before you pick up a single sponge, you need to clear the surfaces. Go through your closets, pantry, and living areas. Donate clothes you no longer wear and throw away expired food. Cleaning is much faster when there is less stuff in the way.",
        "h2": "2. Tackle the Ceilings and Walls",
        "p2": "Look up. Dust the ceiling fans, wipe down the light fixtures, and remove any cobwebs lurking in the corners. Washing the walls gently with a damp cloth removes the subtle layer of grime that builds up over winter.",
        "h3": "3. Revitalize Your Windows",
        "p3": "Clean windows let the beautiful spring sunlight pour in.",
        "li1": "Take down curtains and run them through the wash.",
        "li2": "Wipe the glass inside and out until it is streak free.",
        "li3": "Vacuum the window tracks to remove dead bugs and dust.",
        "p3b": "This single step instantly brightens every room in the house.",
        "h4": "4. Deep Clean the Kitchen",
        "p4": "Empty the fridge completely and scrub the shelves. Pull out the appliances and sweep behind them. Finally, apply a heavy duty degreaser to the oven and rangehood to get them sparkling again.",
        "h5": "5. Refresh the Bathrooms",
        "p5": "Go beyond the usual weekly wipe. Scrub the grout with a specialized brush, descale the showerhead, and wash the bath mats. Throw away any half empty, expired cosmetic bottles hiding in the vanity.",
        "h6": "6. Show the Floors Some Love",
        "p6": "Move the furniture to vacuum the areas that rarely see daylight. Consider hiring a carpet steam cleaner to pull out the deeply embedded dirt. Mop the hard floors with a high quality wood or tile solution.",
        "h7": "7. Consider a Spring Cleaning Service",
        "p7": "If this list looks too big for your weekend, professional help is the best answer. A dedicated deep cleaning team will hit every item on this checklist in a single day, leaving your home immaculate.",
        "final_h": "Breathe Easy",
        "final_p": "Completing a deep spring clean brings an incredible sense of accomplishment. Your house will smell better, look brighter, and feel much more inviting.",
        "quote": "Spring cleaning is not just about removing dirt. It is about clearing the slate and creating a fresh, uplifting environment for the months ahead.",
        "outro": "Grab your supplies, put on your favorite playlist, and take it one room at a time. The final result will remind you why you love your home in the first place."
    }
}

for filename, content in data.items():
    filepath = f"blog/{filename}"
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            file_content = f.read()
        
        new_block = html_template.format(**content)
        pattern = re.compile(r"(<div class=\"cs_post_info\">\s*<div class=\"cs_post_meta.*?>.*?</div>\s*)(<h2>.*?</p>)(?=\s*</div>\s*</div>\s*<div class=\"cs_height_50)", re.DOTALL | re.IGNORECASE)
        
        match = pattern.search(file_content)
        if match:
            new_content = file_content[:match.start(2)] + new_block + file_content[match.end(2):]
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Success: Updated {filename}")
        else:
            print(f"Error: Pattern not found in {filename}")
    except Exception as e:
        print(f"Error processing {filename}: {e}")
