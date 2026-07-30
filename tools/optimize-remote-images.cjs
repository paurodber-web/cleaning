const fs = require('fs');
const path = require('path');

const dist = path.resolve(__dirname, '..', 'dist');
const walk = (directory) => fs.readdirSync(directory, { withFileTypes: true }).flatMap((entry) => (
  entry.isDirectory() ? walk(path.join(directory, entry.name)) : [path.join(directory, entry.name)]
));
const encodeAttribute = (value) => value.replace(/&/g, '&amp;').replace(/"/g, '&quot;');
const responsiveImage = (tag) => {
  if (!tag.includes('images.unsplash.com/') || /\bsrcset=/.test(tag)) return tag;
  const source = tag.match(/\bsrc=(['"])(.*?)\1/);
  if (!source) return tag;
  const width = Math.max(320, Number(tag.match(/\bwidth=(['"])(\d+)\1/)?.[2]) || 1200);
  const candidates = [...new Set([320, 480, 640, 768, 960, 1200, width])]
    .filter((candidate) => candidate <= width)
    .sort((a, b) => a - b);
  const urlFor = (candidate) => {
    const url = new URL(source[2].replace(/&amp;/g, '&'));
    url.searchParams.set('auto', 'format');
    url.searchParams.set('fit', 'crop');
    url.searchParams.set('fm', 'webp');
    url.searchParams.set('q', '60');
    url.searchParams.set('w', String(candidate));
    return encodeAttribute(url.toString());
  };
  const srcset = candidates.map((candidate) => `${urlFor(candidate)} ${candidate}w`).join(', ');
  const fallback = urlFor(width);
  return tag.replace(source[0], `src=${source[1]}${fallback}${source[1]} srcset=${source[1]}${srcset}${source[1]} sizes=${source[1]}(max-width: 820px) calc(100vw - 30px), 40vw${source[1]}`);
};

let optimized = 0;
for (const file of walk(dist).filter((entry) => entry.endsWith('.html'))) {
  const html = fs.readFileSync(file, 'utf8');
  const next = html.replace(/<img\b[^>]*>/gi, responsiveImage);
  if (next !== html) {
    fs.writeFileSync(file, next);
    optimized += 1;
  }
}
console.log(`[performance] Added responsive remote-image variants in ${optimized} HTML file(s).`);