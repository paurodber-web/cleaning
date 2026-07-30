const fs = require('fs');
const path = require('path');

const dist = path.resolve(__dirname, '..', 'dist');
const walk = (directory) => fs.readdirSync(directory, { withFileTypes: true }).flatMap((entry) => (
  entry.isDirectory() ? walk(path.join(directory, entry.name)) : [path.join(directory, entry.name)]
));

const failures = [];
for (const file of walk(dist).filter((entry) => entry.endsWith('.html'))) {
  const html = fs.readFileSync(file, 'utf8');
  const relative = path.relative(dist, file);

  if (html.includes('font-display:optional')) failures.push(`${relative}: uses optional font rendering`);
  if (/<link[^>]+rel="preload"[^>]+(?:dm-sans-latin-ext|plus-jakarta-sans-latin-ext)\.woff2/i.test(html)) {
    failures.push(`${relative}: preloads unused extended font subsets`);
  }

  for (const image of html.match(/<img[^>]*images\.unsplash\.com[^>]*>/g) ?? []) {
    if (!image.includes('srcset=') || !image.includes('fm=webp')) {
      failures.push(`${relative}: remote image is missing responsive WebP variants`);
    }
  }
}

if (failures.length) {
  console.error('[performance] Contract failed:\n' + failures.map((failure) => `- ${failure}`).join('\n'));
  process.exit(1);
}

console.log('[performance] Built-site performance contract passed.');