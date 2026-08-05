const fs = require('node:fs');
const path = require('node:path');

const dist = path.join(process.cwd(), 'dist');
if (!fs.existsSync(dist)) throw new Error('[seo] dist/ does not exist. Run the production build first.');

const walk = (dir) => fs.readdirSync(dir, { withFileTypes: true }).flatMap((entry) => {
  const target = path.join(dir, entry.name);
  return entry.isDirectory() ? walk(target) : [target];
});
const htmlFiles = walk(dist).filter((file) => file.endsWith('.html'));
const errors = [];
const warnings = [];
const encodingIssue = /(?:Ã¢|Ãƒ|Ã‚|Ã°Å¸)/;
const malformedPriceDuration = /\$\s*\d+(?:\.\d+)?-hour\b/i;
const titles = new Map();
const descriptions = new Map();
const publicRoutes = new Set(htmlFiles.map((file) => {
  const relative = path.relative(dist, file).replace(/\\/g, '/');
  if (relative === 'index.html') return '/';
  if (relative.endsWith('/index.html')) return `/${relative.slice(0, -'index.html'.length)}`;
  return `/${relative}`;
}));
const basePath = '/maidathome';
const withoutBasePath = (value) => value === basePath ? '/' : (value.startsWith(basePath + '/') ? value.slice(basePath.length) : value);

const text = (html, pattern) => html.match(pattern)?.[1]?.trim();
for (const file of htmlFiles) {
  const html = fs.readFileSync(file, 'utf8');
  const route = path.relative(dist, file).replace(/\\/g, '/');
  const isRedirect = /http-equiv=["']refresh/i.test(html);
  const is404 = route === '404.html';
  const title = text(html, /<title>([\s\S]*?)<\/title>/i);
  const description = text(html, /<meta\s+name=["']description["']\s+content=["']([^"']*)/i);
  const canonical = text(html, /<link\s+rel=["']canonical["']\s+href=["']([^"']*)/i);
  const robots = text(html, /<meta\s+name=["']robots["']\s+content=["']([^"']*)/i);
  const h1Count = (html.match(/<h1\b/gi) || []).length;
  const htmlLang = text(html, /<html\b[^>]*\blang=["']([^"']+)/i);

  if (encodingIssue.test(html)) errors.push(route + ': contains mojibake');
  if (malformedPriceDuration.test(html)) errors.push(route + ': contains a malformed price-duration phrase');

  if (!title) errors.push(`${route}: missing title`);
  if (!description && !isRedirect) errors.push(`${route}: missing meta description`);
  if (!canonical && !isRedirect) errors.push(`${route}: missing canonical`);
  if (canonical && !canonical.startsWith('https://maidathome.com.au/')) errors.push(`${route}: non-production canonical ${canonical}`);
  if (!isRedirect && !is404 && h1Count !== 1) errors.push(`${route}: expected one H1, found ${h1Count}`);
  if (!isRedirect && !htmlLang) errors.push(`${route}: missing html lang`);
  if (!isRedirect && !is404 && !/<main\b/i.test(html)) errors.push(`${route}: missing main landmark`);
  if (route === 'index.html') {
    const homeH1 = text(html, /<h1\b[^>]*>([\s\S]*?)<\/h1>/i)?.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
    if (homeH1 !== 'House cleaning services in Melbourne') errors.push(`${route}: protected homepage H1 changed`);
  }
  if (is404 && !robots?.includes('noindex')) errors.push(`${route}: 404 must be noindex`);
  if (title) {
    if (titles.has(title) && !isRedirect) errors.push(`${route}: duplicate title also used by ${titles.get(title)}`);
    else titles.set(title, route);
    if (!isRedirect && (title.length < 25 || title.length > 65)) warnings.push(`${route}: title length ${title.length}`);
  }
  if (description && !isRedirect && (description.length < 110 || description.length > 165)) warnings.push(`${route}: description length ${description.length}`);
  if (description && !isRedirect) {
    if (descriptions.has(description)) errors.push(`${route}: duplicate description also used by ${descriptions.get(description)}`);
    else descriptions.set(description, route);
  }

  for (const image of html.matchAll(/<img\b[^>]*>/gi)) {
    if (!/\balt=["'][^"']*["']/i.test(image[0])) errors.push(`${route}: image missing alt attribute`);
  }

  for (const block of html.matchAll(/<script[^>]+type=["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi)) {
    try { JSON.parse(block[1]); } catch (error) { errors.push(`${route}: invalid JSON-LD (${error.message})`); }
  }

  for (const link of html.matchAll(/<a\b[^>]*href=["']([^"']+)["']/gi)) {
    const href = link[1];
    if (!href.startsWith('/') || href.startsWith('//')) continue;
    const clean = withoutBasePath(href.split('#')[0].split('?')[0]);
    if (!clean) continue;
    const normalised = clean.endsWith('/') ? clean : `${clean}/`;
    if (!publicRoutes.has(clean) && !publicRoutes.has(normalised) && !publicRoutes.has(`${clean}.html`)) errors.push(`${route}: broken internal link ${href}`);
  }
}

const sourceRoots = ['src', 'public'];
const sourceExtensions = new Set(['.astro', '.md', '.mdx', '.ts', '.js', '.cjs', '.mjs', '.txt']);
for (const root of sourceRoots) {
  const rootPath = path.join(process.cwd(), root);
  if (!fs.existsSync(rootPath)) continue;
  for (const file of walk(rootPath)) {
    if (!sourceExtensions.has(path.extname(file))) continue;
    if (encodingIssue.test(fs.readFileSync(file, 'utf8'))) {
      errors.push(path.relative(process.cwd(), file).replace(/\\/g, '/') + ': contains mojibake');
    }
  }
}

const deepCleanPath = path.join(dist, 'services', 'deep-clean', 'index.html');
if (fs.existsSync(deepCleanPath)) {
  const deepCleanHtml = fs.readFileSync(deepCleanPath, 'utf8');
  const standardComparison = /Choose Standard[\s\S]{0,1800}href=\"(?:\/maidathome)?\/services\/standard-clean\">Explore Standard Clean/.test(deepCleanHtml);
  if (!standardComparison) errors.push('services/deep-clean/index.html: Standard comparison CTA must link to Standard Clean');
}

const sitemapPath = path.join(dist, 'sitemap.xml');
if (!fs.existsSync(sitemapPath)) errors.push('missing sitemap.xml');
else {
  const sitemap = fs.readFileSync(sitemapPath, 'utf8');
  if (sitemap.includes('/booking/')) errors.push('sitemap includes noindex booking page');
  if (sitemap.includes('/areas-we-serve/template/')) errors.push('sitemap includes suburb template');
  if (!sitemap.includes('/services/regular-house-cleaning/')) errors.push('sitemap misses regular house cleaning page');
}
const robotsPath = path.join(dist, 'robots.txt');
if (!fs.existsSync(robotsPath) || !fs.readFileSync(robotsPath, 'utf8').includes('https://maidathome.com.au/sitemap.xml')) errors.push('robots.txt is missing the production sitemap declaration');

if (warnings.length) {
  console.warn('\n[seo] Non-blocking metadata review:');
  warnings.forEach((warning) => console.warn(`- ${warning}`));
}
if (errors.length) {
  console.error('\n[seo] Built-site validation failed:');
  errors.forEach((error) => console.error(`- ${error}`));
  process.exit(1);
}
console.log(`[seo] Built-site validation passed for ${htmlFiles.length} HTML file(s).`);
