const { spawnSync } = require('node:child_process');
const fs = require('node:fs');
const path = require('node:path');

const base = '/maidathome';
const command = process.argv[2] ?? 'build';
const args = process.argv.slice(3);
const npx = process.platform === 'win32' ? 'npx.cmd' : 'npx';
const astroCommand = command === 'preview' ? ['astro', 'preview', ...args] : ['astro', 'build'];

const result = spawnSync(npx, astroCommand, {
  stdio: 'inherit',
  env: { ...process.env, ASTRO_BASE: base, PUBLIC_DEPLOY_TARGET: 'github-pages' },
  shell: process.platform === 'win32',
});
if (result.status !== 0) process.exit(result.status ?? 1);
if (command !== 'build') process.exit(0);

const dist = path.join(process.cwd(), 'dist');
const files = [];
const walk = (directory) => {
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    const target = path.join(directory, entry.name);
    if (entry.isDirectory()) walk(target);
    else if (entry.name.endsWith('.html') || entry.name.endsWith('.css')) files.push(target);
  }
};
walk(dist);

const prefix = (url) => url === base || url.startsWith(base + '/') ? url : base + url;
for (const file of files) {
  let contents = fs.readFileSync(file, 'utf8');
  contents = contents.replace(/\b(href|src|action)=(['"])(\/(?!\/)[^'"]*)\2/gi, (_match, attribute, quote, url) => `${attribute}=${quote}${prefix(url)}${quote}`);
  contents = contents.replace(/url\((['"]?)(\/(?!\/)[^'")]+)\1\)/gi, (_match, quote, url) => `url(${quote}${prefix(url)}${quote})`);
  contents = contents.replace(/\/_astro\//g, base + '/_astro/');
  contents = contents.replace(new RegExp(base + base + '/_astro/', 'g'), base + '/_astro/');
  contents = contents.replace(/(\.href\s*=\s*['"])(\/(?!\/))/g, (_match, start, slash) => start + prefix(slash));
  fs.writeFileSync(file, contents);
}

const rootReferences = files.flatMap((file) => {
  const contents = fs.readFileSync(file, 'utf8');
  return [...contents.matchAll(/\b(?:href|src|action)=(['"])\/(?!\/|maidathome(?:\/|$))/gi)].map(() => path.relative(dist, file));
});
if (rootReferences.length) {
  throw new Error(`GitHub Pages build still contains root-relative resources: ${[...new Set(rootReferences)].join(', ')}`);
}
console.log(`[pages] Prefixed root-relative resources with ${base} in ${files.length} file(s).`);