import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const imagePath = z.union([z.url(), z.string().regex(/^\/assets\//)]);

const blog = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/blog' }),
  schema: z.object({
    title: z.string().min(1),
    description: z.string().min(1),
    intro: z.string().min(80),
    takeaway: z.string().min(80),
    publishedAt: z.coerce.date(),
    updatedAt: z.coerce.date().optional(),
    category: z.enum(['home-care', 'cleaning-guides', 'moving', 'local-living']),
    categoryLabel: z.string().min(1),
    image: imagePath,
    imageAlt: z.string().min(1),
    imageWidth: z.number().int().positive().default(1200),
    imageHeight: z.number().int().positive().default(800),
    readingTime: z.string().min(1),
    author: z.string().min(2).default('Maid At Home'),
    reviewedBy: z.string().min(2).default('Maid At Home editorial team'),
    featured: z.boolean().default(false),
    draft: z.boolean().default(false),
  }),
});

const suburbs = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/suburbs' }),
  schema: z.object({
    suburb: z.string().min(2),
    postcode: z.string().regex(/^\d{4}$/),
    region: z.enum(['inner', 'north', 'east', 'west', 'south']),
    regionLabel: z.string().min(2),
    title: z.string().min(30).max(60),
    description: z.string().min(120).max(160),
    heroIntro: z.string().min(120),
    summary: z.string().min(80),
    localSectionTitle: z.string().min(20),
    servicesIntro: z.string().min(120),
    prioritiesIntro: z.string().min(100).max(520),
    recurringIntro: z.string().min(120),
    recurringRecommendation: z.string().min(80),
    carpetTitle: z.string().min(20).max(80),
    carpetIntro: z.string().min(100).max(520),
    carpetImage: imagePath,
    carpetImageAlt: z.string().min(10).max(125),
    whyImage: imagePath,
    whyImageAlt: z.string().min(10).max(125),
    whyIntro: z.string().min(100).max(520),
    nearbyIntro: z.string().min(80).max(1400),
    faqIntro: z.string().min(80),
    ctaIntro: z.string().min(80).max(400),
    image: imagePath,
    imageAlt: z.string().min(10).max(125),
    imageWidth: z.number().int().positive().default(1600),
    imageHeight: z.number().int().positive().default(1067),
    ctaImage: imagePath,
    ctaImageAlt: z.string().min(10).max(125),
    localHighlights: z.array(z.object({
      title: z.string().min(2),
      text: z.string().min(50),
    })).min(3).max(5),
    homeTypes: z.array(z.string().min(3)).min(2).max(6),
    accessNotes: z.array(z.string().min(10)).min(2).max(6),
    services: z.array(z.enum([
      'standard-clean',
      'deep-clean',
      'end-of-lease-clean',
      'move-in-clean',
      'hourly-clean',
    ])).min(3).max(6),
    nearbySuburbs: z.array(z.object({
      name: z.string().min(2),
      slug: z.string().regex(/^[a-z0-9]+(?:-[a-z0-9]+)*$/),
    })).length(10),
    faqs: z.array(z.object({
      question: z.string().min(20),
      answer: z.string().min(80),
    })).min(5).max(8),
    publishedAt: z.coerce.date(),
    updatedAt: z.coerce.date().optional(),
    seoReview: z.object({
      reviewed: z.boolean().default(false),
      uniqueContentEstimate: z.number().min(70).max(100),
      localFactsCheckedAt: z.coerce.date(),
    }),
    draft: z.boolean().default(true),
  }),
});

export const collections = { blog, suburbs };
