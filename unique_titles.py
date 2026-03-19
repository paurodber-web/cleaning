import re

def update_suburbs_with_unique_titles(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 75 UNIQUE TITLES FOR EACH CATEGORY (Personalized Redaction)
    
    about_titles = [
        "A Local Team Dedicated to Your Home's Shine", "Providing the Detailed Care Your Home Deserves",
        "Quality Home Cleaning with a Personal Touch", "Meet the Professionals Behind Your Spotless Home",
        "Our Commitment to a Cleaner, Healthier Home", "Expert Care for Your Most Important Space",
        "Reliable Cleaning Professionals You Can Trust", "Passion for Perfection in Every Room",
        "Making Your Living Space Truly Sparkle", "Dedicated to Excellence in Local Home Care",
        "Your Partner for a Pristine and Tidy Residence", "The Standards of Cleanliness You Deserve",
        "Hand-Picked Experts for Your Home Maintenance", "A Mission to Simplify Your Daily Life",
        "Meticulous Attention to Every Single Corner", "Bringing Freshness and Order to Your House",
        "Experienced Hands for Your Domestic Comfort", "The Local Choice for Superior Home Care",
        "Transforming Your Home Into a Sanctuary", "Our Story: Quality Cleaning Since Day One",
        "Built on Trust and Exceptional Results", "Where Local Care Meets Professional Quality",
        "Focused on Delivering an Immaculate Result", "Your Residence in Expert Professional Hands",
        "Crafting a Clean Environment for Your Family", "The Heart and Soul of Local Home Cleaning",
        "Elevating the Standard of Residential Care", "A Team That Cares About Your Comfort",
        "Your Trusted Connection for a Cleaner Home", "Striving for Excellence in Every Visit",
        "A Fresh Approach to Professional Cleaning", "Reliable Domestic Help for Busy People",
        "Upholding the Beauty of Your Living Space", "Expertise You Can See in Every Surface",
        "The People Who Make Your Home Shine", "Dedicated to Your Ultimate Satisfaction",
        "A Meticulous Team for a Meticulous Home", "Your Satisfaction is Our Primary Goal",
        "Clean Homes, Happy Families: Our Mission", "Providing Peace of Mind through Cleanliness",
        "The Professional Touch Your Home Needs", "Local Experts in Residential Upkeep",
        "Consistent Quality You Can Rely On", "We Treat Your Home Like Our Own",
        "The Foundation of a Healthy Living Space", "Devoted to the Art of Proper Cleaning",
        "Integrity and Quality in Every Service", "Your Local Source for a Spotless House",
        "Redefining What a Clean Home Feels Like", "A Passion for Helping You Stay Organized",
        "Thorough Cleaning for Modern Lifestyles", "Professionalism That Shines Through",
        "Your Comfort is Our Top Priority", "The Team Behind the Area's Cleanest Homes",
        "A Refreshing Level of Professionalism", "Carefully Curated Cleaning for Your Home",
        "The Standard-Bearers of Local Cleaning", "Bringing a New Life to Your Interior",
        "Quality You Can Trust, Care You Can Feel", "Your Home's Best Friend for Cleanliness",
        "Excellence in Every Wipe and Scrub", "The Reliable Choice for Home Maintenance",
        "Honesty, Quality, and a Spotless Result", "Focused on the Details That Matter Most",
        "A Clean Home is a Productive Home", "Professional Care for Your Domestic Bliss",
        "Your Guide to a Cleaner Living Environment", "Local Cleaners Who Never Miss a Spot",
        "Top-Tier Cleaning for Local Residents", "A Refreshing Perspective on Housework",
        "Your Local Authority on Home Cleaning", "Dedication You Can See and Feel",
        "The Ultimate Solution for a Tidy Home", "Superior Service for Discerning Homeowners",
        "Quality Cleaning Made Simple and Easy"
    ]

    why_choose_titles = [
        "Why Your Neighbors Prefer Our Service", "Reliable Results for a Stress-Free Home",
        "The Difference is in the Little Details", "What Local Families Love About Our Care",
        "A Consistently Clean Home Without the Hassle", "Why We’re the Top Choice for Local Residents",
        "Peace of Mind with Every Single Visit", "Professionalism and Quality You Can Count On",
        "Our Secret to a Perfectly Maintained Home", "Exceeding Expectations One Clean at a Time",
        "Vetted Professionals for Your Security", "The Most Thorough Cleaning in the Area",
        "Experience the Joy of a Spotless Home", "Tailored Care That Fits Your Exact Needs",
        "A Commitment to Your Health and Safety", "Why We Are the Preferred Cleaning Partner",
        "Consistency is the Key to Our Success", "Going Above and Beyond for Our Clients",
        "The Best Value for Professional Cleaning", "Transparent Pricing and Superior Results",
        "Friendly Staff and Immaculate Outcomes", "Trusted by Hundreds of Local Households",
        "We Take the Burden of Chores Off Your Hands", "Attention to Detail That Set Us Apart",
        "Reliability is Our Core Guarantee", "The Smart Way to Keep Your Home Tidy",
        "Professional Grade Cleaning for Your House", "Your Time is Precious, Let Us Help",
        "Unmatched Quality for Local Homeowners", "Why Our Regular Clients Stay With Us",
        "The Highest Standards in the Industry", "A Bespoke Cleaning Experience for You",
        "Expertise That Makes a Visible Difference", "Safe Products and Meticulous Staff",
        "Personalized Attention for Every Single Room", "Because Your Home Deserves the Best",
        "The Most Reliable Choice for Local Families", "Quality Control You Can Actually Trust",
        "Why We Lead the Local Cleaning Market", "Superior Results Without the Premium Price",
        "Stress-Free Scheduling and Brilliant Cleaning", "Our Track Record of Spotless Homes",
        "The Passionate Choice for Home Care", "Why Our Customers Recommend Us Daily",
        "A More Thorough Approach to Domestic Care", "Integrity in Every Step of the Service",
        "Making Life Easier for Local Residents", "Expect More From Your Cleaning Service",
        "The Ultimate Standard in Home Maintenance", "We Care More About Your Living Space",
        "The Cleanest Choice You'll Ever Make", "Proven Methods for a Sparkling Home",
        "Local Dedication Meets Global Standards", "Why We Are the Gold Standard Locally",
        "A Healthier Home Starts with Our Visit", "Professionalism That Replaces Your Stress",
        "Unlocking the Beauty of Your Home", "Our Reputation for Meticulous Results",
        "Why Precision is Our Middle Name", "The Most Dedicated Team in the Region",
        "Results That Speak Louder Than Words", "Your Comfort is Our Success Metric",
        "Why We Never Cut Corners in Your Home", "Efficiency and Quality in Perfect Balance",
        "The Most Trusted Hands in Local Cleaning", "Unwavering Quality You Can Observe",
        "Why We Treat Every Home Like a Palace", "Reliable Help for Your Modern Lifestyle",
        "The Solution for a Better Home Life", "A History of Happy and Clean Homes",
        "Why Quality is Our Only Option", "Meticulous Care for Every Local Resident",
        "The Standard You Can Always Expect", "Why We Are Simply Better at Cleaning",
        "Consistent Brilliance for Your Property"
    ]

    services_titles = [
        "Cleaning Solutions Tailored to Your Lifestyle", "From Weekly Upkeep to Deep Seasonal Refreshes",
        "Expert Home Care Designed Specifically for You", "Explore Our Most Popular Cleaning Packages",
        "Complete Cleaning Services for Your Home", "Flexible Plans for a Spotless Living Space",
        "Tackling Everything from Dust to Deep Grime", "Professional Care for Every Corner of Your House",
        "Versatile Services to Suit Your Busy Schedule", "Quality Cleaning Options for Every Local Home",
        "Comprehensive Maintenance for a Fresh Home", "The Full Suite of Professional Cleaning",
        "Dedicated Support for Your Domestic Needs", "Reliable Options for Every Type of Property",
        "A Fresh Start for Your Interior Spaces", "Routine Care That Keeps Your Home Perfect",
        "Specialized Cleaning for Discerning Clients", "The Most Thorough Cleaning Selection Available",
        "Your All-in-One Solution for Home Care", "Premium Services for a Healthier Interior",
        "Meticulous Care from Top to Bottom", "Standard, Deep, and Specialized Cleaning",
        "The Perfect Cleaning Plan for Your Needs", "Reliable Maintenance for Every Season",
        "Expert Attention for Your Entire Property", "Professional Results in Every Single Service",
        "Tailored Solutions for Busy Modern Living", "Deep Cleaning That Rejuvenates Your Home",
        "Quality Upkeep for Every Local Residence", "The Ultimate Choice for House Cleaning",
        "Brilliant Results Across All Our Services", "Detailed Care for Your Living Environment",
        "A Wide Range of Options for Your Home", "The Most Reliable Services in the Region",
        "Targeted Cleaning for Your Unique Space", "Making Every Room in Your House Shine",
        "Superior Care for All Residential Types", "The Professional Way to Maintain Your Home",
        "Consistent Results for Every Cleaning Task", "Your Favorite Local Cleaning Specialists",
        "The Services You Need for a Tidy Home", "Customized Cleaning for Your Absolute Comfort",
        "Everything from Basic Tidying to Deep Scrubs", "Professional Maintenance You Can Rely On",
        "The Quality Your Home Deserves Every Time", "Top-Rated Solutions for Domestic Care",
        "Efficient and Thorough Cleaning Programs", "The Best Care for Your Property and Family",
        "Flexible Cleaning Scheduled Around You", "Our Signature Approach to Home Cleaning",
        "Expertise in Every Cleaning Challenge", "Versatile Options for Local Homeowners",
        "The Most Complete Cleaning Experience", "High-Standard Care for Your Interior",
        "Meticulous Services for a Better Lifestyle", "A Comprehensive Strategy for Home Care",
        "Premium Cleaning That Fits Your Budget", "The Reliable Answer to Your Chores",
        "Quality Assurance in Every Single Service", "The Most Popular Choice for Local Homes",
        "Expert Cleaning for Every Surface and Room", "Your Partner for a Consistently Clean Home",
        "Proven Results Across All Cleaning Types", "Dedicated Services for a Spotless House",
        "The Local Experts in Residential Cleaning", "Superior Methods for a Better Clean",
        "Your Roadmap to a Healthier Living Space", "Complete Support for Your Home's Beauty",
        "Professional Plans for Lasting Cleanliness", "The Most Trusted Cleaning Services Locally",
        "Excellence in Maintenance and Deep Care", "Your Best Choice for Domestic Support",
        "A Focus on Quality in Every Service", "Reliable Help for a Sparkling Interior",
        "The Definitive Guide to Your Clean Home"
    ]

    how_works_titles = [
        "Book Your First Professional Shine in Seconds", "Our Simple and Effortless Path to a Cleaner Home",
        "How We Deliver a Spotless House Every Single Time", "Getting Started with Your Local Team is Easy",
        "Three Simple Steps to a Glowing Living Space", "Our Process for Guaranteed Cleaning Results",
        "Ready for a Fresh Start? Here’s How it Works", "Seamless Booking and Superior Cleaning Care",
        "Your Journey to a Perfectly Tidy Home Starts Here", "Effortless Home Care from Start to Finish",
        "How to Secure Your Professional Cleaning Now", "The Easy Way to a Consistently Clean Home",
        "A Straightforward Process for Local Residents", "Getting Your Home Cleaned Has Never Been Easier",
        "Your Quick Guide to Our Professional Service", "From Booking to a Brilliant Result in Moments",
        "Simple Steps for a Significantly Cleaner House", "How We Ensure Your Home Stays Immaculate",
        "Ready for Quality Care? Here is the Process", "The Stress-Free Way to Arrange Your Cleaning",
        "Your Path to Domestic Bliss starts with a Click", "How to Experience Our Meticulous Service",
        "Booking Your Clean: Simple, Fast, and Secure", "The Transparent Way We Care for Your Home",
        "Your Simple Action Plan for a Tidy House", "Getting Your Weekends Back is Very Simple",
        "How to Join Our List of Happy Local Clients", "A Clear Roadmap to Your Sparkling Home",
        "Ready for Perfection? Follow These Easy Steps", "The Modern Way to Manage Your Housework",
        "How We Transform Your Living Space Quickly", "Simple Instructions for Your First Service",
        "Your Easy Guide to Professional Domestic Care", "The Logical Steps to a Much Cleaner Home",
        "Ready to Relax? Let Us Handle the Chores", "How to Get the Most Out of Our Service",
        "A Hassle-Free Process for Every Homeowner", "Your Quick Start to a Healthier Environment",
        "How We Make Your Home Truly Shine Today", "The Practical Steps to a Tidy Living Space",
        "Ready for a Change? Here’s the Booking Path", "How to Coordinate Your Local Cleaning Visit",
        "Simple and Reliable Steps for Your Comfort", "Your Direct Route to a Spotless Interior",
        "How We Manage the Details of Your Cleaning", "Ready for a Brilliant Result? Start Here",
        "The Friendly Way to Get Your Home Scrubbed", "How to Access the Best Cleaning in the Area",
        "Simple and Efficient Booking for Busy People", "Your Personal Guide to Our Cleaning Process",
        "Ready to Enjoy Your Home? Follow These Steps", "How We Ensure a Consistent Clean Every Time",
        "The Easiest Way to Keep Your House Perfect", "How to Schedule Your Professional Cleaning",
        "Your Step-by-Step Guide to a Glowing Home", "Ready for a Fresh House? It’s This Simple",
        "How We Bring Professionalism to Your Door", "The Intuitive Way to Manage Your Cleaning",
        "How to Get Started with Our Dedicated Team", "Simple Actions for a Perfectly Clean Result",
        "Your Convenient Path to a Sparking Home", "How We Deliver Excellence to Your Property",
        "Ready for Meticulous Care? It’s Easy to Start", "How to Transform Your Home Life Today",
        "The Seamless Process for Your Next Cleaning", "Your Reliable Way to a Spotless Interior",
        "Ready for Better Results? Here is the Way", "How to Partner with Us for a Clean Home",
        "The Simplest Method for Home Maintenance", "Your Quick Gateway to a Cleaner Lifestyle",
        "Ready for Consistent Quality? Book Now", "How We Simplify Your Home Maintenance",
        "The Trusted Way to Get Your House Cleaned", "How to Enjoy a Spotless Home Effortlessly",
        "Your Essential Steps for a Better Home Clean"
    ]

    testimonial_titles = [
        "Client Stories from Your Local Neighborhood", "What Your Neighbors Say About the Results",
        "Kind Words from Our Regular Local Clients", "Real Feedback from Happy Local Homeowners",
        "Why Our Community Trusts Our Cleaning Team", "Genuine Reviews from People in Your Area",
        "Success Stories: A Cleaner Home for Local Families", "What Makes Our Customers Keep Coming Back",
        "Honest Experiences from Local Residents Like You", "The Results Speak for Themselves: Client Praise",
        "Voices from the Community: Our Reputation", "Why Local Residents Recommend Our Service",
        "Real Stories of Clean and Happy Homes", "Trusted Feedback from Your Fellow Neighbors",
        "Hear from the People Who Love Our Work", "Your Community's Verdict on Our Quality",
        "Sharing the Joy of a Consistently Clean Home", "Local Praise for Our Professional Cleaners",
        "The Reputation We’ve Built in Your Area", "Real Experiences from Satisfied Homeowners",
        "What to Expect: Feedback from Local Clients", "Kind Testimonials from the Neighborhood",
        "Why We Are the Most Recommended Locally", "Stories of Transformation and Cleanliness",
        "Honest Reviews You Can Actually Trust", "How We’ve Helped Your Local Neighbors",
        "Word of Mouth: Why Our Service is Popular", "Authentic Feedback on Our Meticulous Care",
        "Celebrating Spotless Homes with Our Clients", "Your Local Neighbors Share Their Thoughts",
        "The Trust We've Earned in Your Neighborhood", "Proving Our Quality Through Client Reviews",
        "Real Words from Real People in the Area", "Our Commitment to Quality as Seen by You",
        "The Stories Behind Our Area's Cleanest Homes", "Local Recognition for Exceptional Service",
        "Why Our Regular Clients are So Satisfied", "Direct Feedback from Local Property Owners",
        "A History of Excellence Shared by Clients", "Your Community Speaks: Why They Choose Us",
        "Trusted Reviews for Peace of Mind", "What Makes Us the Local Favorite",
        "Real People, Real Results, Real Feedback", "The Voice of Our Happy Local Customers",
        "Stories of Reliable Care and Clean Homes", "Why Your Peers Recommend Our Cleaners",
        "Testimonials from Your Local Community", "Our Impact on Local Homes: Client Views",
        "The High Standards Our Clients Observe", "Genuine Praise for Our Dedicated Team",
        "How We’ve Earned the Trust of Your Area", "Client Perspectives on Our Professionalism",
        "The Quality Our Neighbors Talk About", "Consistent Praise for Consistent Cleaning",
        "Why We Are the Talk of the Neighborhood", "Real Reviews: The Secret to Our Success",
        "Trusted Stories from Local Bayside Families", "Feedback That Drives Our Excellence",
        "The Reputation of a Perfectly Clean Home", "Kind Reviews from Local Residential Clients",
        "Why Our Service is a Local Success Story", "The Community's Guide to Our Service Quality",
        "Real Experiences Shared by Local Families", "Honest Praise for Our Professional Staff",
        "The Testimonials That Define Our Quality", "Why Our Local Reputation is So Strong",
        "Client Feedback: The Heart of Our Service", "Hear Why Your Neighbors Stay With Us",
        "Authentic Stories of a Sparking Home", "Local Success: Reviews from Your Area",
        "Why Excellence is Noted by Our Clients", "Sharing the Secret to a Cleaner Home",
        "The Most Trusted Reviews in the District", "Your Neighbors' Guide to Our Cleanliness",
        "Real Insights from Local Homeowners"
    ]

    blog_titles = [
        "Expert Advice for a Healthier, Happier Home", "Our Latest Cleaning Tips and Lifestyle Hacks",
        "Pro Guides to Keeping Your Living Space Fresh", "Simple Solutions for a Consistently Tidy House",
        "Professional Insights for Better Home Maintenance", "Smart Tricks to Keep Your Place Looking Great",
        "Our Best Secrets for an Organized Living Space", "Helpful Articles for Busy Local Homeowners",
        "Enhance Your Home with Our Practical Advice", "Stay Informed with Our Local Home Care Blog",
        "Your Essential Guide to a Pristine Interior", "How to Maintain Your Home Between Visits",
        "The Best Cleaning Strategies for Your Family", "Expert Thoughts on Modern Home Maintenance",
        "Living Better in a Clean and Tidy Home", "Practical Ways to Improve Your Home Life",
        "Our Professional Take on Home Cleanliness", "Helpful Tips for Every Room in Your House",
        "The Ultimate Resource for a Clean Environment", "Ways to Keep Your Living Space Sparkling",
        "Our Experts Share Their Best Cleaning Tips", "Innovative Hacks for a Much Taller Home",
        "The Philosophy of a Perfectly Clean Space", "Practical Advice for Local Property Owners",
        "Enhancing Your Lifestyle through Cleanliness", "Your Go-To Source for Home Care Wisdom",
        "Expert Methods for a More Organized Life", "Seasonal Tips for a Truly Refreshed Home",
        "Our Commitment to Sharing Home Care Knowledge", "The Best Ways to Simplify Your Housework",
        "Professional Guidance for a Healthier Home", "Unlock the Secrets of a Meticulous House",
        "Helpful Insights for a Beautiful Interior", "Maintaining Excellence in Your Living Space",
        "Our Collection of Pro Cleaning Secrets", "Your Digital Resource for Home Maintenance",
        "Smart Strategies for a Spotless Residence", "Expert Perspectives on Residential Care",
        "Practical Tricks for a Stress-Free Home", "Our Favorite Ways to Keep Things Tidy",
        "Building a Better Home Environment Today", "Your Path to an Immaculate Living Area",
        "The Science of a Clean and Healthy Home", "Expert-Led Advice for Modern Families",
        "Making the Most of Your Professional Clean", "Our Top Recommendations for Home Care",
        "Staying Tidy: Advice from the Professionals", "The Best Habits for a Cleaner Interior",
        "Essential Reading for Local Homeowners", "Pro Tips for Every Type of Property",
        "How to Enjoy a Consistently Fresh Home", "Our Vision for Better Home Maintenance",
        "The Most Effective Cleaning Tips Shared", "Enhancing the Beauty of Your Interior",
        "Your Handbook for a Properly Clean Home", "Professional Hacks for a Glowing House",
        "Expert Care Tips for Your Valuable Home", "The Practical Guide to Residential Bliss",
        "Our Most Popular Home Care Articles", "How to Maintain a Shine Every Single Day",
        "The Professionals' View on a Tidy Home", "Innovative Ways to Manage Your Space",
        "Your Essential Blog for Home Cleanliness", "Maintaining a Higher Standard at Home",
        "Expert Wisdom for a Sparkling Residence", "Simple Methods for Lasting Cleanliness",
        "Our Best Advice for Your Domestic Comfort", "Pro Insights for a More Tidy Lifestyle",
        "The Keys to a Successfully Maintained Home", "Helpful Content for a Better Home Life",
        "Our Dedication to Local Home Education", "How to Keep Your Interior Looking New",
        "Expert Tips for a Perfectly Clean House", "Your Weekly Source of Cleaning Inspiration",
        "Professional Secrets for a Better Home"
    ]

    faq_titles = [
        "Clear Answers to Your Common Home Care Questions", "Everything You Need to Know Before You Book",
        "Helpful Details for Your Ultimate Peace of Mind", "Common Questions About Our Local Cleaning Service",
        "Quick Answers to Help You Get Started Today", "Understanding Our Services: Your FAQ Guide",
        "Simple Information for a Better Service Experience", "We’re Here to Help: Common Inquiries Answered",
        "Your Top Questions About Professional Cleaning", "Get the Facts About Our Quality Cleaning Care",
        "Informative Guide to Our Domestic Services", "What to Expect: Your Questions Answered",
        "The Essential FAQ for Local Homeowners", "Clear Explanations for Your Satisfaction",
        "Everything You Want to Know About Our Team", "Your Reliable Resource for Service Details",
        "Common Inquiries and Professional Answers", "Providing Clarity on Our Cleaning Process",
        "Get Ready for Your Service: Key Information", "Your Checklist of Common Cleaning Questions",
        "The Practical Info You Need for Your Home", "Transparency in Action: Our Service FAQ",
        "What Our New Clients Usually Ask Us", "Answers That Make Your Life Much Easier",
        "Simple Facts About Our Local Cleaning Care", "Your Guide to a Hassle-Free Experience",
        "Key Details About Our Rates and Services", "Ensuring You Have All the Information Needed",
        "The Direct Path to Understanding Our Work", "Your Questions, Our Professional Answers",
        "Essential Facts for a Better Home Clean", "Everything Simplified: Our Service FAQs",
        "What You Need to Know for a Spotless Home", "Clear Guidance for Our Residential Clients",
        "Your Frequently Asked Questions Resolved", "Direct Answers for Your Domestic Peace",
        "Information You Can Trust for Your Home", "The Complete FAQ for Your Cleaning Needs",
        "Helping You Understand Our Quality Service", "Simple Solutions to Your Common Inquiries",
        "The Information Hub for Our Local Clients", "Professional Answers for Your Home Care",
        "What Makes Our Service Different: FAQ", "Quick Facts for a Smooth Cleaning Service",
        "Your Most Important Questions Handled Here", "Clear and Concise Info for Homeowners",
        "The Knowledge You Need Before We Arrive", "Your Essential FAQ for a Cleaner House",
        "Understanding Excellence: Our Service Guide", "Simple Answers for Complex Cleaning Needs",
        "The Most Common Questions from Neighbors", "Your Go-To List for All Things Cleaning",
        "Clarity and Quality: Our Detailed FAQ", "Facts to Help You Plan Your Next Clean",
        "Everything Explained for Your Convenience", "Your Resource for Reliable Home Care Info",
        "Common Sense Answers for Home Cleaning", "The Definitive FAQ for Local Residences",
        "What Every Client Needs to Know Today", "Simple, Direct, and Helpful FAQ Guide",
        "Your Source for Professional Service Details", "Answering Your Needs for a Clean Home",
        "The Practical FAQ for a Better Interior", "Ensuring You Are Fully Informed Today",
        "All the Answers for Your Domestic Comfort", "Helping You Choose the Best Cleaning Plan",
        "Your Informative Path to a Spotless Home", "The Essential Facts About Local Cleaning",
        "Quick Reference for Your Cleaning Questions", "Everything You Should Know for a Clean Home",
        "Clear Communication: Our Service FAQ", "Your Trustworthy Guide to Home Care Facts",
        "Providing the Answers Local Families Need", "The Most Helpful FAQ for Home Cleaning",
        "Everything You Need for a Sparkling Result"
    ]

    # Process block by block
    blocks = re.split(r'^\[(.*?)\]$', content, flags=re.MULTILINE)
    new_blocks = [blocks[0]] # Leading text
    
    suburb_count = 0
    for i in range(1, len(blocks), 2):
        suburb_name = blocks[i]
        suburb_content = blocks[i+1]
        
        # Use modulo to cycle if there were more than 75 (unlikely but safe)
        idx = suburb_count % 75
        
        # Replace each tag
        suburb_content = re.sub(r'\[\[ABOUT_SECTION_TITLE\]\]: .*', f'[[ABOUT_SECTION_TITLE]]: {about_titles[idx]}', suburb_content)
        suburb_content = re.sub(r'\[\[WHY_CHOOSE_SECTION_TITLE\]\]: .*', f'[[WHY_CHOOSE_SECTION_TITLE]]: {why_choose_titles[idx]}', suburb_content)
        suburb_content = re.sub(r'\[\[SERVICES_SECTION_TITLE\]\]: .*', f'[[SERVICES_SECTION_TITLE]]: {services_titles[idx]}', suburb_content)
        suburb_content = re.sub(r'\[\[HOW_WORKS_TITLE\]\]: .*', f'[[HOW_WORKS_TITLE]]: {how_works_titles[idx]}', suburb_content)
        suburb_content = re.sub(r'\[\[TESTIMONIALS_TITLE\]\]: .*', f'[[TESTIMONIALS_TITLE]]: {testimonial_titles[idx]}', suburb_content)
        suburb_content = re.sub(r'\[\[BLOG_TITLE\]\]: .*', f'[[BLOG_TITLE]]: {blog_titles[idx]}', suburb_content)
        suburb_content = re.sub(r'\[\[FAQ_TITLE\]\]: .*', f'[[FAQ_TITLE]]: {faq_titles[idx]}', suburb_content)
        
        new_blocks.append(suburb_name)
        new_blocks.append(suburb_content)
        suburb_count += 1

    # Reassemble
    final_output = ""
    for i in range(1, len(new_blocks), 2):
        final_output += f"[{new_blocks[i]}]\n{new_blocks[i+1].strip()}\n\n"

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_output.strip())

if __name__ == "__main__":
    update_suburbs_with_unique_titles('suburbs/suburbs_text')
    print("525 unique titles successfully assigned to 75 suburbs.")
