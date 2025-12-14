// Simple ad blocker content script
// Hide elements that might be ads based on common selectors

const selectors = [
  '[class*="ad"]',
  '[id*="ad"]',
  '[class*="banner"]',
  '[id*="banner"]',
  'iframe[src*="doubleclick"]',
  'iframe[src*="googlesyndication"]',
  // Add more selectors for ads and money requests
  '[class*="donate"]',
  '[id*="donate"]',
  '[class*="patreon"]',
  '[id*="patreon"]',
  '[class*="subscribe"]',
  '[id*="subscribe"]',
  '[class*="paywall"]',
  '[id*="paywall"]',
  '[class*="premium"]',
  '[id*="premium"]',
  '[class*="upgrade"]',
  '[id*="upgrade"]',
  'a[href*="donate"]',
  'a[href*="patreon"]',
  'a[href*="subscribe"]',
  // Hide pop-ups or modals that might ask for money
  '.modal[class*="pay"]',
  '.popup[class*="subscribe"]'
];

selectors.forEach(selector => {
  const elements = document.querySelectorAll(selector);
  elements.forEach(el => {
    el.style.display = 'none';
  });
});

// Also, block requests to ad domains using webRequest if possible, but for content script, limited.

// For better blocking, use declarativeNetRequest in manifest, but for simplicity, this hides visible ads.

// To block network requests, need background script and permissions.

