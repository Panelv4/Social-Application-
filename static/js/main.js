/* Hariom Physio Care — front-end behaviour */
(function () {
  "use strict";

  /* ---------- sticky navbar shadow ---------- */
  var navbar = document.getElementById("navbar");
  function onScroll() {
    if (!navbar) return;
    navbar.classList.toggle("scrolled", window.scrollY > 8);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------- mobile nav ---------- */
  var toggle = document.getElementById("navToggle");
  if (toggle && navbar) {
    toggle.addEventListener("click", function () {
      var open = navbar.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.querySelectorAll(".nav-links a").forEach(function (link) {
      link.addEventListener("click", function () {
        navbar.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  /* ---------- scroll reveal ---------- */
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealEls.length) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12 }
    );
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("visible"); });
  }

  /* ---------- testimonial slider ---------- */
  var slider = document.getElementById("tSlider");
  if (slider) {
    var slides = slider.querySelectorAll(".t-slide");
    var dotsWrap = document.getElementById("tDots");
    var index = 0;
    var timer = null;

    slides.forEach(function (_, i) {
      var dot = document.createElement("button");
      dot.className = "t-dot" + (i === 0 ? " active" : "");
      dot.setAttribute("aria-label", "Show testimonial " + (i + 1));
      dot.addEventListener("click", function () { show(i); restart(); });
      dotsWrap.appendChild(dot);
    });
    var dots = dotsWrap.querySelectorAll(".t-dot");

    function show(i) {
      index = (i + slides.length) % slides.length;
      slides.forEach(function (s, k) { s.classList.toggle("active", k === index); });
      dots.forEach(function (d, k) { d.classList.toggle("active", k === index); });
    }
    function restart() {
      if (timer) clearInterval(timer);
      timer = setInterval(function () { show(index + 1); }, 6500);
    }
    document.getElementById("tNext").addEventListener("click", function () { show(index + 1); restart(); });
    document.getElementById("tPrev").addEventListener("click", function () { show(index - 1); restart(); });
    restart();
  }

  /* ---------- appointment date min guard ---------- */
  var dateInput = document.getElementById("date");
  if (dateInput && !dateInput.min) {
    dateInput.min = new Date().toISOString().split("T")[0];
  }

  /* ---------- flash auto dismiss ---------- */
  document.querySelectorAll(".flash").forEach(function (el) {
    setTimeout(function () {
      el.style.transition = "opacity .5s, transform .5s";
      el.style.opacity = "0";
      el.style.transform = "translateY(-8px)";
      setTimeout(function () { el.remove(); }, 520);
    }, 6000);
  });
})();
