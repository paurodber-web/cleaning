import { defineConfig } from 'astro/config';

export default defineConfig(({ command }) => ({
  site: 'https://maidathome.com.au',
  // Production is served from the canonical domain root. ASTRO_BASE remains
  // available only for isolated previews (for example, a GitHub Pages demo).
  base: command === 'dev' || command === 'serve' ? '/' : (process.env.ASTRO_BASE ?? '/'),
  build: {
    format: 'directory',
  },
  redirects: {
    '/blog/regular-vs-deep-cleaning': '/blog/standard-vs-deep-cleaning',
    '/blog/airbnb-cleaning-melbourne': '/blog/airbnb-cleaning-service-melbourne',
    '/blog/house-cleaning-schedule-melbourne': '/blog/realistic-house-cleaning-routine',
    '/blog/house-cleaning-tips-melbourne-families': '/blog/realistic-house-cleaning-routine',
    '/blog/regular-house-cleaning-service-melbourne': '/services/regular-house-cleaning',
  },
  image: {
    domains: ['images.unsplash.com', 'maidathome.com.au'],
    layout: 'full-width',
    responsiveStyles: true,
  },
}));
