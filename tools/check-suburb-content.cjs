const fs = require('node:fs');
const path = require('node:path');

const contentDir = path.join(process.cwd(), 'src', 'content', 'suburbs');
const MIN_WORDS = 550;
const MIN_UNIQUE_PERCENT = 75;
const SHINGLE_SIZE = 5;

if (!fs.existsSync(contentDir)) process.exit(0);

const files = fs.readdirSync(contentDir).filter((name) => /\.mdx?$/.test(name));
const pages = files.map((name) => {
  const raw = fs.readFileSync(path.join(contentDir, name), 'utf8');
  const match = raw.match(/^---\s*\r?\n([\s\S]*?)\r?\n---\s*\r?\n([\s\S]*)$/);
  if (!match) throw new Error(`[suburbs] ${name} is missing valid frontmatter.`);
  const [, frontmatter, body] = match;
  const published = /draft:\s*false\b/.test(frontmatter) && /reviewed:\s*true\b/.test(frontmatter);
  const frontmatterCopy = frontmatter
    .split(/\r?\n/)
    .filter((line) => !/^\s*(?:image|imageWidth|imageHeight|ctaImage|publishedAt|updatedAt|localFactsCheckedAt|draft|reviewed|uniqueContentEstimate|region|postcode):/.test(line))
    .map((line) => line.replace(/^\s*(?:-\s+)?[A-Za-z][A-Za-z0-9]*:\s*/, ' '))
    .join(' ');
  const words = `${frontmatterCopy} ${body}`
    .replace(/<[^>]+>/g, ' ')
    .replace(/https?:\/\/\S+/g, ' ')
    .toLowerCase()
    .match(/[a-z0-9]+(?:['’-][a-z0-9]+)*/g) ?? [];
  const shingles = new Set();
  for (let index = 0; index <= words.length - SHINGLE_SIZE; index += 1) {
    shingles.add(words.slice(index, index + SHINGLE_SIZE).join(' '));
  }
  return { name, published, words, shingles };
}).filter((page) => page.published);

const errors = [];
for (const page of pages) {
  if (page.words.length < MIN_WORDS) {
    errors.push(`${page.name}: ${page.words.length} meaningful words across local landing-page fields and FAQs; published suburb pages require at least ${MIN_WORDS}.`);
  }
}

for (let left = 0; left < pages.length; left += 1) {
  for (let right = left + 1; right < pages.length; right += 1) {
    const a = pages[left];
    const b = pages[right];
    const smaller = a.shingles.size <= b.shingles.size ? a : b;
    const larger = smaller === a ? b : a;
    let overlap = 0;
    for (const shingle of smaller.shingles) if (larger.shingles.has(shingle)) overlap += 1;
    const sharedPercent = smaller.shingles.size ? (overlap / smaller.shingles.size) * 100 : 100;
    const uniquePercent = 100 - sharedPercent;
    if (uniquePercent < MIN_UNIQUE_PERCENT) {
      errors.push(`${a.name} and ${b.name}: approximately ${uniquePercent.toFixed(1)}% unique; minimum is ${MIN_UNIQUE_PERCENT}%.`);
    }
  }
}

if (errors.length) {
  console.error('\nSuburb content quality check failed:\n');
  errors.forEach((error) => console.error(`- ${error}`));
  console.error('\nRewrite the suburb-specific fields and FAQs before publishing. Shared template labels do not count as sufficient local value.\n');
  process.exit(1);
}

console.log(`[suburbs] Quality check passed for ${pages.length} published suburb page(s).`);
