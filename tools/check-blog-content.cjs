const fs = require('node:fs');
const path = require('node:path');
const blogDir = path.join(process.cwd(), 'src', 'content', 'blog');
const files = fs.readdirSync(blogDir).filter((file) => file.endsWith('.md'));
const errors = [];
for (const file of files) {
  const source = fs.readFileSync(path.join(blogDir, file), 'utf8');
  const frontmatter = source.match(/^---\s*([\s\S]*?)\s*---/);
  const body = frontmatter ? source.slice(frontmatter[0].length) : '';
  const intro = frontmatter?.[1].match(/^intro:\s*"(.+)"$/m)?.[1] ?? '';
  const takeaway = frontmatter?.[1].match(/^takeaway:\s*"(.+)"$/m)?.[1] ?? '';
  const headings = [...body.matchAll(/^##\s+(.+)$/gm)];
  const internalLinks = [...source.matchAll(/\]\(\/(?!areas-we-serve\/[^)]+)([^)]+)\)/g)];
  if (intro.length < 80) errors.push(`${file}: intro must give a direct answer of at least 80 characters`);
  if (takeaway.length < 80) errors.push(`${file}: takeaway must summarise the answer in at least 80 characters`);
  if (headings.length < 3) errors.push(`${file}: needs at least three H2 headings for the visible table of contents`);
  if (internalLinks.length < 3) errors.push(`${file}: needs at least three relevant internal links`);
}
if (errors.length) {
  console.error(`\n[blog] Content validation failed:\n- ${errors.join('\n- ')}`);
  process.exit(1);
}
console.log(`[blog] Content validation passed for ${files.length} article(s).`);