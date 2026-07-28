import { createHash, randomBytes } from 'node:crypto';
import { createServer } from 'node:http';
import { mkdir, readFile, writeFile } from 'node:fs/promises';
import { homedir } from 'node:os';
import { join } from 'node:path';
import { spawn } from 'node:child_process';
import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { z } from 'zod';

const CLIENT_ID = '324514751210-ojktpvmgo4s9fs3i4hsh8hf74e5cu1ih.apps.googleusercontent.com';
const SCOPE = 'https://www.googleapis.com/auth/business.manage';
const tokenDirectory = join(process.env.LOCALAPPDATA || join(homedir(), '.local', 'share'), 'MaidAtHome', 'gbp-mcp');
const tokenPath = join(tokenDirectory, 'oauth-token.json');
const clientSecretPath = process.env.GBP_OAUTH_CLIENT_PATH || join(tokenDirectory, 'client-secret.json');

const text = (value) => ({ content: [{ type: 'text', text: typeof value === 'string' ? value : JSON.stringify(value, null, 2) }] });
const codeChallenge = (verifier) => createHash('sha256').update(verifier).digest('base64url');

async function readToken() {
  try { return JSON.parse(await readFile(tokenPath, 'utf8')); } catch { return null; }
}

async function saveToken(token) {
  await mkdir(tokenDirectory, { recursive: true });
  await writeFile(tokenPath, JSON.stringify(token), { encoding: 'utf8', mode: 0o600 });
}

async function readClientSecret() {
  if (process.env.GBP_CLIENT_SECRET) return process.env.GBP_CLIENT_SECRET;
  try {
    const value = JSON.parse(await readFile(clientSecretPath, 'utf8'));
    return value.client_secret || value.installed?.client_secret || value.web?.client_secret || '';
  } catch { return ''; }
}

function openBrowser(url) {
  const child = process.platform === 'win32'
    ? spawn('rundll32.exe', ['url.dll,FileProtocolHandler', url], { detached: true, stdio: 'ignore' })
    : spawn(process.platform === 'darwin' ? 'open' : 'xdg-open', [url], { detached: true, stdio: 'ignore' });
  child.unref();
}

async function authenticate() {
  const verifier = randomBytes(48).toString('base64url');
  const listener = createServer();
  await new Promise((resolve) => listener.listen(0, '127.0.0.1', resolve));
  const { port } = listener.address();
  const redirectUri = `http://127.0.0.1:${port}/oauth2callback`;
  const state = randomBytes(24).toString('base64url');
  const url = new URL('https://accounts.google.com/o/oauth2/v2/auth');
  url.search = new URLSearchParams({ client_id: CLIENT_ID, redirect_uri: redirectUri, response_type: 'code', scope: SCOPE, access_type: 'offline', prompt: 'consent', state, code_challenge: codeChallenge(verifier), code_challenge_method: 'S256' }).toString();
  openBrowser(url.toString());
  const code = await new Promise((resolve, reject) => {
    const timeout = setTimeout(() => reject(new Error('OAuth authorisation timed out after five minutes.')), 300000);
    listener.on('request', (request, response) => {
      const callback = new URL(request.url, redirectUri);
      if (callback.pathname !== '/oauth2callback') { response.writeHead(404).end(); return; }
      if (callback.searchParams.get('state') !== state || callback.searchParams.get('error')) {
        response.writeHead(400, { 'content-type': 'text/html' }).end('<h1>Authorization was cancelled or invalid.</h1>');
        clearTimeout(timeout); reject(new Error('OAuth authorisation was cancelled or state validation failed.')); return;
      }
      response.writeHead(200, { 'content-type': 'text/html' }).end('<h1>Maid At Home connected.</h1><p>You can close this tab and return to Codex.</p>');
      clearTimeout(timeout); resolve(callback.searchParams.get('code'));
    });
  }).finally(() => listener.close());
  const clientSecret = await readClientSecret();
  if (!clientSecret) throw new Error('Missing OAuth client secret. Save it at .');
  const response = await fetch('https://oauth2.googleapis.com/token', { method: 'POST', headers: { 'content-type': 'application/x-www-form-urlencoded' }, body: new URLSearchParams({ client_id: CLIENT_ID, client_secret: clientSecret, code, code_verifier: verifier, redirect_uri: redirectUri, grant_type: 'authorization_code' }) });
  const token = await response.json();
  if (!response.ok) throw new Error(`OAuth token exchange failed: ${token.error_description || token.error || response.status}`);
  await saveToken({ ...token, expires_at: Date.now() + Number(token.expires_in || 3600) * 1000 });
}

async function accessToken() {
  let token = await readToken();
  if (!token) throw new Error('Not connected. Run gbp_authenticate and approve access in the browser.');
  if (token.expires_at > Date.now() + 60000) return token.access_token;
  const clientSecret = await readClientSecret();
  if (!clientSecret) throw new Error('Missing OAuth client secret. Save it at .');
  const response = await fetch('https://oauth2.googleapis.com/token', { method: 'POST', headers: { 'content-type': 'application/x-www-form-urlencoded' }, body: new URLSearchParams({ client_id: CLIENT_ID, client_secret: clientSecret, refresh_token: token.refresh_token, grant_type: 'refresh_token' }) });
  const refreshed = await response.json();
  if (!response.ok) throw new Error(`OAuth refresh failed: ${refreshed.error_description || refreshed.error || response.status}`);
  token = { ...token, ...refreshed, expires_at: Date.now() + Number(refreshed.expires_in || 3600) * 1000 };
  await saveToken(token);
  return token.access_token;
}

async function request(url, options = {}) {
  const response = await fetch(url, { ...options, headers: { authorization: `Bearer ${await accessToken()}`, accept: 'application/json', ...(options.headers || {}) } });
  const body = await response.json().catch(() => ({}));
  if (!response.ok) throw new Error(`${response.status}: ${body.error?.message || JSON.stringify(body)}`);
  return body;
}

const server = new McpServer({ name: 'maid-at-home-google-business-profile', version: '1.0.0' });
server.registerTool('gbp_authenticate', { description: 'Connect the local MCP to the Maid At Home Google Business Profile. Opens a browser for one-time OAuth consent.', inputSchema: {} }, async () => { await authenticate(); return text('Google Business Profile connected successfully.'); });
server.registerTool('gbp_list_accounts', { description: 'List Business Profile accounts available to the authorised Google user.', inputSchema: {} }, async () => text(await request('https://mybusinessaccountmanagement.googleapis.com/v1/accounts')));
server.registerTool('gbp_list_locations', { description: 'List locations in a Business Profile account. accountName uses the accounts/123 format.', inputSchema: { accountName: z.string().min(1), pageSize: z.number().int().min(1).max(100).optional() } }, async ({ accountName, pageSize = 100 }) => text(await request(`https://mybusinessbusinessinformation.googleapis.com/v1/${accountName}/locations?readMask=name,title,storefrontAddress,phoneNumbers,websiteUri,regularHours,serviceArea&pageSize=${pageSize}`)));
server.registerTool('gbp_get_location', { description: 'Read the selected Google Business Profile location.', inputSchema: { locationName: z.string().min(1), readMask: z.string().default('name,title,storefrontAddress,phoneNumbers,websiteUri,regularHours,specialHours,serviceArea,categories,profile,metadata') } }, async ({ locationName, readMask }) => text(await request(`https://mybusinessbusinessinformation.googleapis.com/v1/${locationName}?readMask=${encodeURIComponent(readMask)}`)));
server.registerTool('gbp_list_reviews', { description: 'List customer reviews for a Business Profile location. Read-only.', inputSchema: { accountName: z.string().min(1), locationName: z.string().min(1), pageSize: z.number().int().min(1).max(50).optional() } }, async ({ accountName, locationName, pageSize = 50 }) => text(await request(`https://mybusiness.googleapis.com/v4/${accountName}/${locationName}/reviews?pageSize=${pageSize}`)));
server.registerTool('gbp_update_location', { description: 'Update business information. Use only after the user has explicitly approved the exact update.', inputSchema: { locationName: z.string().min(1), updateMask: z.string().min(1), location: z.record(z.unknown()), confirmation: z.literal('I_CONFIRM_THIS_UPDATE') } }, async ({ locationName, updateMask, location }) => text(await request(`https://mybusinessbusinessinformation.googleapis.com/v1/${locationName}?updateMask=${encodeURIComponent(updateMask)}`, { method: 'PATCH', headers: { 'content-type': 'application/json' }, body: JSON.stringify(location) })));

await server.connect(new StdioServerTransport());
