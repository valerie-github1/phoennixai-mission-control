// PhoennixAI Service Worker v1.0
// Enables offline capability and installability

const CACHE_NAME = 'phoennixai-v1';
const STATIC_ASSETS = [
  '/phoennixai-mission-control/',
  '/phoennixai-mission-control/PhoennixAI_InternalOps_MC.html',
  '/phoennixai-mission-control/PhoennixAI_BetaWaitlist_Landing.html',
  '/phoennixai-mission-control/PhoennixAI_BetaWaitlist.html',
  '/phoennixai-mission-control/PhoennixAI_PaymentConfirmation.html',
  '/phoennixai-mission-control/PhoennixAI_NDA_SignHub.html',
  '/phoennixai-mission-control/PhoennixAI_DigitalCard.html',
  '/phoennixai-mission-control/PhoennixAI.jpg',
  '/phoennixai-mission-control/manifest.json'
];

// Install: cache all static assets
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(STATIC_ASSETS).catch(err => {
        console.log('Cache addAll partial failure:', err);
      });
    })
  );
  self.skipWaiting();
});

// Activate: clean old caches
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(
        keys.filter(key => key !== CACHE_NAME)
            .map(key => caches.delete(key))
      )
    )
  );
  self.clients.claim();
});

// Fetch: cache-first for static, network-first for API
self.addEventListener('fetch', event => {
  const url = new URL(event.request.url);
  
  // Network-first for Supabase API calls
  if (url.hostname.includes('supabase.co') || url.hostname.includes('stripe.com')) {
    event.respondWith(
      fetch(event.request).catch(() => 
        caches.match(event.request)
      )
    );
    return;
  }

  // Cache-first for everything else
  event.respondWith(
    caches.match(event.request).then(cached => {
      if (cached) return cached;
      return fetch(event.request).then(response => {
        if (response && response.status === 200 && response.type === 'basic') {
          const clone = response.clone();
          caches.open(CACHE_NAME).then(cache => {
            cache.put(event.request, clone);
          });
        }
        return response;
      }).catch(() => {
        // Offline fallback
        if (event.request.destination === 'document') {
          return caches.match('/phoennixai-mission-control/PhoennixAI_BetaWaitlist_Landing.html');
        }
      });
    })
  );
});
