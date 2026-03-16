const allPosts = [
    {
        title: "Time saving house cleaning tips for busy Melbourne families",
        url: "blog/7-quick-cleaning-hacks.html",
        img: "https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?auto=format&fit=crop&w=1200&q=80",
        author: "Maid At Home",
        date: "July 10, 2025",
        timestamp: 1752141600000,
        category: "DIY Cleaning",
        tags: ["Hacks", "Families", "Routine"]
    },
    {
        title: "Why switching to natural cleaning products is better for your home",
        url: "blog/benefits-green-cleaning.html",
        img: "https://images.unsplash.com/photo-1610555356070-d1fb3d81a8b1?auto=format&fit=crop&w=1200&q=80",
        author: "Maid At Home",
        date: "April 05, 2025",
        timestamp: 1743811200000,
        category: "Eco-Friendly Cleaning",
        tags: ["Eco-friendly", "Health", "Products"]
    },
    {
        title: "A guide to selecting the best disinfectants for a healthy house",
        url: "blog/choose-right-disinfectants.html",
        img: "https://images.unsplash.com/photo-1584622781564-1d987f7333c1?auto=format&fit=crop&w=1200&q=80",
        author: "Maid At Home",
        date: "May 14, 2025",
        timestamp: 1747180800000,
        category: "Health & Safety",
        tags: ["Disinfectants", "Health", "Tips"]
    },
    {
        title: "Do plant based cleaning solutions actually work on tough stains?",
        url: "blog/eco-friendly-cleaning-products.html",
        img: "https://images.unsplash.com/photo-1610555356070-d1fb3d81a8b1?auto=format&fit=crop&w=1200&q=80",
        author: "Maid At Home",
        date: "June 22, 2025",
        timestamp: 1750550400000,
        category: "Eco-Friendly Cleaning",
        tags: ["Eco-friendly", "Detergents", "Tips"]
    },
    {
        title: "The ideal house cleaning schedule to keep your space spotless",
        url: "blog/how-often-clean-home.html",
        img: "https://images.unsplash.com/photo-1493809842364-78817add7ffb?auto=format&fit=crop&w=1200&q=80",
        author: "Maid At Home",
        date: "February 12, 2025",
        timestamp: 1739318400000,
        category: "Deep Cleaning",
        tags: ["Routine", "Hygiene", "Home Care"]
    },
    {
        title: "The ultimate deep cleaning checklist to refresh your property",
        url: "blog/spring-cleaning-checklist.html",
        img: "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=1200&q=80",
        author: "Maid At Home",
        date: "March 20, 2025",
        timestamp: 1742428800000,
        category: "DIY Cleaning",
        tags: ["Spring", "Checklist", "Organization"]
    },
    {
        title: "Everything you need to know about end of lease cleaning in Melbourne",
        url: "blog/end-of-lease-cleaning-melbourne.html",
        img: "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=1200&q=80",
        author: "Maid At Home",
        date: "August 01, 2025",
        timestamp: 1754006400000,
        category: "Deep Cleaning",
        tags: ["End of Lease", "Moving", "Bond Back"]
    },
    {
        title: "How much does a house cleaner cost in Melbourne this year?",
        url: "blog/hiring-a-cleaner-cost.html",
        img: "https://images.unsplash.com/photo-1522771731478-44fb10e99312?auto=format&fit=crop&w=1200&q=80",
        author: "Maid At Home",
        date: "August 15, 2025",
        timestamp: 1755216000000,
        category: "Commercial & Office",
        tags: ["Cost", "Pricing", "Guide"]
    },
    {
        title: "How to maintain your carpets between professional steam cleans",
        url: "blog/carpet-cleaning-tips.html",
        img: "https://images.unsplash.com/photo-1527515637462-cff94eecc1ac?auto=format&fit=crop&w=1200&q=80",
        author: "Maid At Home",
        date: "September 02, 2025",
        timestamp: 1756771200000,
        category: "DIY Cleaning",
        tags: ["Carpet", "Stains", "Maintenance"]
    },
    {
        title: "What to look for in a registered NDIS house cleaning provider",
        url: "blog/ndis-cleaning-services.html",
        img: "https://images.unsplash.com/photo-1585421514738-01798e348b17?auto=format&fit=crop&w=1200&q=80",
        author: "Maid At Home",
        date: "September 20, 2025",
        timestamp: 1758326400000,
        category: "Health & Safety",
        tags: ["NDIS", "Support", "Reliability"]
    }
];

// Sort posts by date (latest first)
allPosts.sort((a, b) => b.timestamp - a.timestamp);
