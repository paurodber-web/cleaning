const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const read = (relative) => fs.readFileSync(path.join(root, relative), 'utf8');
const failures = [];
const expect = (condition, message) => { if (!condition) failures.push(message); };

const policy = read('src/data/service-policy.ts');
expect(policy.includes('everydayHours: 48'), 'central policy must define a 48-hour everyday-service window');
expect(policy.includes('endOfLeaseDays: 7'), 'central policy must define a 7-day End of Lease window');

const pages = ['src/pages/index.astro', 'src/pages/about-us.astro', 'src/pages/faqs.astro', 'src/pages/booking.astro', 'src/pages/services/standard-clean.astro', 'src/pages/services/deep-clean.astro'];
for (const page of pages) {
  const contents = read(page);
  expect(!/contact us within 24 hours|within 24 hours so we|within 24 hours if an included|24-hour service follow-up|24-hour support|24-hour care promise/i.test(contents), `${page} retains a 24-hour service-care claim`);
}

const home = read('src/pages/index.astro');
expect(/<a class="service-mini" href="\/services\/regular-house-cleaning">[\s\S]{0,1000}<h3>Regular clean<\/h3>/.test(home), 'Regular clean card must link to /services/regular-house-cleaning');
expect(/href="\/services\/regular-house-cleaning">Explore regular cleaning plans/.test(home), 'Regular cleaning CTA must link to /services/regular-house-cleaning');
expect(/href="\/booking">Book your clean/.test(home), 'Home final CTA must link to /booking');

const standard = read('src/pages/services/standard-clean.astro');
expect(!standard.includes('/services/#deep'), 'Standard Clean must not link to the services hub deep anchor');
expect(/href="\/services\/deep-clean">Explore Deep Clean/.test(standard), 'Standard Clean must link to /services/deep-clean');

const about = read('src/pages/about-us.astro');
expect(/href="\/booking">Book your clean/.test(about), 'About final CTA must link to /booking');

if (failures.length) {
  console.error('[service-policy] Contract failed:\n' + failures.map((failure) => `- ${failure}`).join('\n'));
  process.exit(1);
}

console.log('[service-policy] Central policy and conversion-link contract passed.');
