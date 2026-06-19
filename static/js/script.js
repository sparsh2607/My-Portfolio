// =============================================
//  SPARSH GAHOI — PORTFOLIO JS
// =============================================
 
document.addEventListener('DOMContentLoaded', () => {
 
  // --- NAV SCROLL EFFECT ---
  const nav = document.getElementById('nav');
  if (nav) {
    const onScroll = () => {
      nav.classList.toggle('scrolled', window.scrollY > 50);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }
 
  // --- MOBILE BURGER MENU ---
  const burger = document.getElementById('navBurger');
  const mobileMenu = document.getElementById('mobileMenu');
 
  if (burger && mobileMenu) {
    burger.addEventListener('click', () => {
      mobileMenu.classList.toggle('open');
      burger.classList.toggle('active');
      document.body.style.overflow = mobileMenu.classList.contains('open') ? 'hidden' : '';
    });
 
    // Close on link click
    mobileMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        mobileMenu.classList.remove('open');
        burger.classList.remove('active');
        document.body.style.overflow = '';
      });
    });
  }
 
  // --- SKILL BAR ANIMATION (About page) ---
  const skillFills = document.querySelectorAll('.skill-bar__fill');
  if (skillFills.length > 0) {
    const skillObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('animated');
          skillObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.3 });
 
    skillFills.forEach(fill => skillObserver.observe(fill));
  }
 
  // --- PROJECT CARD ENTRANCE ANIMATION ---
  const cards = document.querySelectorAll('.project-card');
  if (cards.length > 0) {
    // Set initial state via JS (avoids FOUC)
    cards.forEach((card, i) => {
      card.style.opacity = '0';
      card.style.transform = 'translateY(24px)';
      card.style.transition = `opacity 0.5s ease ${i * 0.08}s, transform 0.5s ease ${i * 0.08}s`;
    });
 
    const cardObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
          cardObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });
 
    cards.forEach(card => cardObserver.observe(card));
  }
 
  // --- HERO TEXT ENTRANCE ---
  const heroText = document.querySelector('.hero__text');
  if (heroText) {
    heroText.style.opacity = '0';
    heroText.style.transition = 'opacity 0.8s ease 0.2s';
    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        heroText.style.opacity = '1';
      });
    });
  }
 
});
