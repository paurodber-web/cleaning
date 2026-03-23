const allPosts = [
    {
        title: "House Cleaning Tips for Busy Melbourne Families",
        url: "blog/house-cleaning-tips-melbourne-families",
        img: "assets/img/blog/family_cleaning_tips.webp",
        author: "Maid At Home",
        date: "January 12, 2026",
        timestamp: 1768176000000,
        category: "DIY Cleaning",
        tags: ["House cleaning", "Melbourne", "Time-saving"]
    },
    {
        title: "The Real Benefits of Green Cleaning for Melbourne Homes",
        url: "blog/green-cleaning-benefits-melbourne",
        img: "assets/img/blog/green_cleaning_benefits.webp",
        author: "Maid At Home",
        date: "January 26, 2026",
        timestamp: 1769385600000,
        category: "Eco-Friendly Cleaning",
        tags: ["Green cleaning", "Non-toxic", "Melbourne homes"]
    },
    {
        title: "The Best Way to Disinfect Your Home in Melbourne (Without Overdoing It)",
        url: "blog/best-way-to-disinfect-home-melbourne",
        img: "assets/img/blog/disinfect_home_melbourne.webp",
        author: "Maid At Home",
        date: "February 10, 2026",
        timestamp: 1770681600000,
        category: "Health & Safety",
        tags: ["Disinfectants", "Hygiene", "Home safety"]
    },
    {
        title: "Eco-Friendly Cleaning Products That Actually Work in Melbourne Homes",
        url: "blog/eco-friendly-cleaning-products-that-work",
        img: "assets/img/blog/eco_products_work.webp",
        author: "Maid At Home",
        date: "February 24, 2026",
        timestamp: 1771891200000,
        category: "Eco-Friendly Cleaning",
        tags: ["Eco friendly", "Products", "Stain removal"]
    },
    {
        title: "House Cleaning Schedule: How Often to Clean Each Room",
        url: "blog/house-cleaning-schedule-melbourne",
        img: "assets/img/blog/cleaning_schedule.webp",
        author: "Maid At Home",
        date: "March 09, 2026",
        timestamp: 1773014400000,
        category: "Deep Cleaning",
        tags: ["Cleaning schedule", "Routine", "Home care"]
    },
    {
        title: "Deep Cleaning Checklist for Melbourne Homes: A Complete Reset Guide",
        url: "blog/deep-cleaning-checklist-melbourne",
        img: "assets/img/blog/deep_cleaning_checklist.webp",
        author: "Maid At Home",
        date: "March 22, 2026",
        timestamp: 1774137600000,
        category: "Deep Cleaning",
        tags: ["Deep clean", "Checklist", "Melbourne"]
    },
    {
        title: "End of Lease Cleaning Melbourne: Bond Back Guide",
        url: "blog/end-of-lease-cleaning-melbourne-bond-back",
        img: "assets/img/blog/end_of_lease_cleans.webp",
        author: "Maid At Home",
        date: "April 06, 2026",
        timestamp: 1775433600000,
        category: "Deep Cleaning",
        tags: ["End of lease", "Bond back", "Moving"]
    },
    {
        title: "House Cleaning Cost in Melbourne: A Practical Pricing Guide",
        url: "blog/house-cleaning-cost-melbourne",
        img: "assets/img/blog/cleaning_cost_melbourne.webp",
        author: "Maid At Home",
        date: "April 20, 2026",
        timestamp: 1776643200000,
        category: "Commercial & Office",
        tags: ["House cleaning cost", "Pricing", "Melbourne"]
    },
    {
        title: "How to Keep Your Carpets Fresh Between Professional Cleans in Melbourne",
        url: "blog/carpet-cleaning-tips-melbourne",
        img: "assets/img/blog/carpet_cleaning_tips.webp",
        author: "Maid At Home",
        date: "May 05, 2026",
        timestamp: 1777939200000,
        category: "DIY Cleaning",
        tags: ["Carpet cleaning", "Stains", "Maintenance"]
    },
    {
        title: "Weekly Cleaning Service in Melbourne: What’s Included",
        url: "blog/weekly-cleaning-service-melbourne",
        img: "assets/img/blog/weekly_cleaning_melbourne.webp",
        author: "Maid At Home",
        date: "May 18, 2026",
        timestamp: 1779062400000,
        category: "Deep Cleaning",
        tags: ["Weekly cleaning", "Service", "Melbourne"]
    },
];

// Sort posts by date (latest first)
allPosts.sort((a, b) => b.timestamp - a.timestamp);
