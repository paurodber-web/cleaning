const allPosts = [
    {
        title: "Airbnb Cleaning Service Melbourne: Fast Turnovers, Spotless Results, 5-Star Reviews",
        url: "/blog/airbnb-cleaning-melbourne/",
        img: "assets/img/standard-clean.webp",
        author: "Maid at Home",
        date: "April 15, 2026",
        timestamp: 1776229200000,
        category: "Commercial & Office",
        tags: ["Airbnb Cleaning Melbourne", "Airbnb Cleaner Melbourne", "Turnover Cleaning"]
    },
    {
        title: "Move-In Cleaning Melbourne: Complete Checklist & Why You Should Book Before Moving In",
        url: "/blog/move-in-cleaning-melbourne/",
        img: "assets/img/deep-clean.webp",
        author: "Maid at Home",
        date: "April 15, 2026",
        timestamp: 1776225600000,
        category: "Deep Cleaning",
        tags: ["Move In Cleaning Melbourne", "Pre Move In Cleaning", "New Home Cleaning Checklist"]
    },
    {
        title: "How to Find a Trustworthy House Cleaner in Melbourne: 10 Questions to Ask Before You Book",
        url: "/blog/how-to-find-a-good-cleaner-melbourne/",
        img: "assets/img/meet.webp",
        author: "Maid at Home",
        date: "April 15, 2026",
        timestamp: 1776222000000,
        category: "Health & Safety",
        tags: ["Best House Cleaner Melbourne", "Reliable House Cleaners Melbourne", "Vetted Cleaners Melbourne"]
    },
    {
        title: "Oven Cleaning Melbourne: How Much It Costs & Why DIY Always Fails",
        url: "/blog/oven-cleaning-melbourne/",
        img: "assets/img/end-of-lease-cleaning-banner.webp",
        author: "Maid at Home",
        date: "April 15, 2026",
        timestamp: 1776218400000,
        category: "Deep Cleaning",
        tags: ["Oven Cleaning", "End Of Lease", "Rangehood"]
    },
    {
        title: "Bathroom Cleaning Melbourne: How to Remove Soap Scum, Mould & Limescale Like a Pro",
        url: "/blog/bathroom-cleaning-melbourne/",
        img: "assets/img/deep-clean.webp",
        author: "Maid at Home",
        date: "April 15, 2026",
        timestamp: 1776214800000,
        category: "Deep Cleaning",
        tags: ["Bathroom Cleaning", "Mould Removal", "Limescale"]
    },
    {
        title: "Bond Back Cleaning Melbourne: How to Guarantee Your Full Bond Refund",
        url: "/blog/bond-back-cleaning-melbourne/",
        img: "assets/img/blog/bond-back-cleaning-melbourne.webp",
        author: "Maid at Home",
        date: "April 15, 2026",
        timestamp: 1776211200000,
        category: "Cleaning Tips",
        tags: ["Bond Back Cleaning", "End of Lease", "Melbourne"]
    },
    {
        title: "How Long Does Carpet Cleaning Take in Melbourne?",
        url: "/blog/how-long-does-carpet-cleaning-take-melbourne/",
        img: "assets/img/blog/how-long-does-carpet-cleaning-take-melbourne.webp",
        author: "Maid at Home",
        date: "April 15, 2026",
        timestamp: 1776207600000,
        category: "Deep Cleaning",
        tags: ["Carpet Cleaning", "Steam Cleaning", "Dry Time"]
    },
    {
        title: "End of Lease Cleaning Cost Melbourne: Pricing & Guide 2026",
        url: "/blog/end-of-lease-cleaning-cost-melbourne/",
        img: "assets/img/blog/end-of-lease-cleaning-cost-melbourne.webp",
        author: "Maid at Home",
        date: "April 14, 2026",
        timestamp: 1776121200000,
        category: "Cleaning Tips",
        tags: ["End of Lease", "Melbourne", "Pricing"]
    },
    {
        title: "House Cleaning Tips for Busy Melbourne Families",
        url: "/blog/house-cleaning-tips-melbourne-families/",
        img: "assets/img/blog/family_cleaning_tips.webp",
        author: "Maid At Home",
        date: "January 12, 2026",
        timestamp: 1768172400000,
        category: "DIY cleaning",
        tags: ["House Cleaning", "Melbourne", "Time-saving"]
    },
    {
        title: "The Real Benefits of Green cleaning for Melbourne Homes",
        url: "/blog/green-cleaning-benefits-melbourne/",
        img: "assets/img/blog/green_cleaning_benefits.webp",
        author: "Maid At Home",
        date: "January 26, 2026",
        timestamp: 1769382000000,
        category: "Eco-Friendly cleaning",
        tags: ["Green cleaning", "Non-toxic", "Melbourne homes"]
    },
    {
        title: "The Best Way to Disinfect Your Home in Melbourne (Without Overdoing It)",
        url: "/blog/best-way-to-disinfect-home-melbourne/",
        img: "assets/img/blog/disinfect_home_melbourne.webp",
        author: "Maid At Home",
        date: "February 10, 2026",
        timestamp: 1770678000000,
        category: "Health & Safety",
        tags: ["Disinfectants", "Hygiene", "Home safety"]
    },
    {
        title: "Eco-Friendly cleaning Products That Actually Work in Melbourne Homes",
        url: "/blog/eco-friendly-cleaning-products-that-work/",
        img: "assets/img/blog/eco_products_work.webp",
        author: "Maid At Home",
        date: "February 24, 2026",
        timestamp: 1771887600000,
        category: "Eco-Friendly cleaning",
        tags: ["Eco friendly", "Products", "Stain removal"]
    },
    {
        title: "House Cleaning Schedule: How Often to Clean Each Room",
        url: "/blog/house-cleaning-schedule-melbourne/",
        img: "assets/img/blog/cleaning_schedule.webp",
        author: "Maid At Home",
        date: "March 05, 2026",
        timestamp: 1772665200000,
        category: "Deep Cleaning",
        tags: ["cleaning schedule", "Routine", "Home care"]
    },
    {
        title: "Deep Cleaning Checklist for Melbourne Homes: A Complete Reset Guide",
        url: "/blog/deep-cleaning-checklist-melbourne/",
        img: "assets/img/blog/deep_cleaning_checklist.webp",
        author: "Maid At Home",
        date: "March 09, 2026",
        timestamp: 1773010800000,
        category: "Deep Cleaning",
        tags: ["Deep Cleaning", "Checklist", "Melbourne"]
    },
    {
        title: "How Much Does House Cleaning Cost in Melbourne? (2026 Pricing Guide)",
        url: "/blog/how-much-does-house-cleaning-cost-in-melbourne/",
        img: "assets/img/blog/cleaning_cost_melbourne.webp",
        author: "Maid at Home",
        date: "April 15, 2026",
        timestamp: 1776207600000,
        category: "Cleaning Tips",
        tags: ["House Cleaning", "Pricing", "Melbourne"]
    },
    {
        title: "How to Keep Your Carpets Fresh Between Professional Cleans in Melbourne",
        url: "/blog/carpet-cleaning-tips-melbourne/",
        img: "assets/img/blog/carpet_cleaning_tips.webp",
        author: "Maid At Home",
        date: "March 18, 2026",
        timestamp: 1773788400000,
        category: "DIY cleaning",
        tags: ["Carpet cleaning", "Stains", "Maintenance"]
    },
    {
        title: "Regular House Cleaning Service Melbourne: 7 Reasons to Book a Recurring Cleaner",
        url: "/blog/regular-house-cleaning-service-melbourne/",
        img: "assets/img/blog/regular-house-cleaning-service-melbourne.webp",
        author: "Maid At Home",
        date: "March 20, 2026",
        timestamp: 1773961200000,
        category: "Deep Cleaning",
        tags: ["Weekly cleaning", "Service", "Melbourne"]
    },
];

// Sort posts by date (latest first)
allPosts.sort((a, b) => b.timestamp - a.timestamp);
