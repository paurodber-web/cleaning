const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({
    headless: "new"
  });
  const page = await browser.newPage();
  
  // Set viewport to a mobile dimensions (e.g. iPhone SE)
  await page.setViewport({ width: 375, height: 667, isMobile: true });
  
  // Navigate to local index.html
  await page.goto('file:///C:/Users/Pau%20Rodriguez/Antigravity/Trading/Templates/maid_at_home_download_2/index.html', { waitUntil: 'networkidle2' });
  
  // Screenshot
  await page.screenshot({ path: 'mobile_screenshot.webp' });
  
  // Set viewport to tablet (e.g. iPad Mini)
  await page.setViewport({ width: 768, height: 1024, isMobile: true });
  await page.screenshot({ path: 'tablet_screenshot.webp' });

  await browser.close();
})();
