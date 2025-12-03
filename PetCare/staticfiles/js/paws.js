// Shared paw animation initializer
function createPawsLayer(containerId, count, sizeMin, sizeMax, durationMin, durationMax, delayMax) {
  const container = document.getElementById(containerId);
  if (!container) return;
  for (let i = 0; i < count; i++) {
    const paw = document.createElement('img');
    paw.src = window.PAWS_ICON_SRC || '';
    paw.className = 'paw';
    paw.style.left = Math.random() * 100 + '%';
    const size = Math.random() * (sizeMax - sizeMin) + sizeMin;
    paw.style.width = size + 'px';
    paw.style.height = size + 'px';
    paw.style.animationDuration = (Math.random() * (durationMax - durationMin) + durationMin) + 's';
    paw.style.animationDelay = (Math.random() * delayMax) + 's';
    container.appendChild(paw);
  }
}

function initPawsAuth() {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduceMotion) { return; }
  // Larger sizes for kid-friendly look
  createPawsLayer('pawsBack', 28, 80, 140, 16, 26, 8);
  createPawsLayer('pawsMid', 50, 60, 100, 12, 20, 6);
  createPawsLayer('pawsTop', 70, 44, 72, 9, 16, 5);
}

document.addEventListener('DOMContentLoaded', () => {
  initPawsAuth();
});
