const CACHE_NAME = 'mibu-birthday-message-2026-offline-v5';
const APP_ASSETS = [
  './',
  './index.html',
  './manifest.webmanifest',
  './cover.webp',
  './icon-192.png',
  './icon-512.png',
  './apple-touch-icon.png',
  './messages-part-1.js',
  './messages-part-2.js',
  './messages-part-3.js',
  './messages-part-4.js'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(APP_ASSETS))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(
        keys.filter(key => key !== CACHE_NAME).map(key => caches.delete(key))
      ))
      .then(() => self.clients.claim())
  );
});

async function networkFirst(request) {
  const cache = await caches.open(CACHE_NAME);
  try {
    const response = await fetch(request, { cache: 'no-store' });
    if (response && response.status === 200 && response.type !== 'opaque') {
      await cache.put(request, response.clone());
    }
    return response;
  } catch (error) {
    const cached = await cache.match(request);
    if (cached) return cached;
    if (request.mode === 'navigate') {
      return (await cache.match('./index.html')) || (await cache.match('./'));
    }
    throw error;
  }
}

self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;
  if (new URL(event.request.url).origin !== self.location.origin) return;
  event.respondWith(networkFirst(event.request));
});
