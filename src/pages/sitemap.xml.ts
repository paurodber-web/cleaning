import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

const staticPages = [
  '/', '/about-us/', '/areas-we-serve/', '/blog/', '/contact/', '/faqs/', '/pricing/', '/services/',
  '/services/standard-clean/', '/services/regular-house-cleaning/', '/services/deep-clean/', '/services/end-of-lease-clean/',
  '/services/move-in-clean/', '/services/hourly-clean/', '/services/carpet-clean/', '/services/oven-clean/',
];

const escapeXml = (value: string) => value.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

export const GET: APIRoute = async ({ site }) => {
  const origin = site ?? new URL('https://maidathome.com.au');
  const now = new Date();
  const posts = await getCollection('blog', ({ data }) => !data.draft && data.publishedAt <= now);
  const suburbs = await getCollection('suburbs', ({ id, data }) => id !== '_suburb-template' && !data.draft && data.seoReview.reviewed);
  const urls = [
    ...staticPages.map((path) => ({ path, modified: undefined as Date | undefined })),
    ...posts.map(({ id, data }) => ({ path: `/blog/${id}/`, modified: data.updatedAt ?? data.publishedAt })),
    ...suburbs.map(({ id, data }) => ({ path: `/areas-we-serve/${id}/`, modified: data.updatedAt ?? data.publishedAt })),
  ];
  const body = urls.map(({ path, modified }) => `<url><loc>${escapeXml(new URL(path, origin).toString())}</loc>${modified ? `<lastmod>${modified.toISOString().slice(0, 10)}</lastmod>` : ''}</url>`).join('');
  return new Response(`<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${body}</urlset>`, { headers: { 'Content-Type': 'application/xml; charset=utf-8' } });
};
