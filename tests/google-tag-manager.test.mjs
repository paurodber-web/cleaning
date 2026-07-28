import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import test from 'node:test';

const layout = readFileSync(new URL('../src/layouts/SiteLayout.astro', import.meta.url), 'utf8');

test('loads the configured Google Tag Manager container once', () => {
  assert.match(layout, /const gtmId = 'GTM-W9TCF2NW';/);
  assert.match(layout, /https:\/\/www\.googletagmanager\.com\/gtm\.js\?id=/);
  assert.match(layout, /https:\/\/www\.googletagmanager\.com\/ns\.html\?id=/);
  assert.doesNotMatch(layout, /googletagmanager\.com\/gtag\/js/);
});
