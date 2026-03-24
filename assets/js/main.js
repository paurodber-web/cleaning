(function ($) {
  "use strict";

  /*
  |--------------------------------------------------------------------------
  | Template Name: Maid at Home
  | Author: Maid at Home
  | Version: 1.0.0
  |--------------------------------------------------------------------------
  |--------------------------------------------------------------------------
  | TABLE OF CONTENTS:
  |--------------------------------------------------------------------------
  |
  | 01. Preloader
  | 02. Mobile Menu
  | 03. Sticky Header
  | 04. Dynamic Background
  | 05. Slick Slider
  | 06. Modal Video
  | 07. Scroll Up
  | 08. Accordian
  | 09. Review
  | 10. Counter Animation
  | 11. Smooth Page Scroll
  | 12. Steps Animation
  | 13. Dynamic contact form
  | 14. AOS Animation
  |
  */

  /*--------------------------------------------------------------
    Scripts initialization
  --------------------------------------------------------------*/
  $.exists = function (selector) {
    return $(selector).length > 0;
  };

  $(window).on("load", function () {
    // preloader();
  });
  // Use a single rAF-throttled scroll handler to avoid forced reflows.
  let lastScrollY = 0;
  let isTicking = false;
  const onScroll = () => {
    lastScrollY = window.scrollY || window.pageYOffset || 0;
    if (!isTicking) {
      window.requestAnimationFrame(() => {
        stickyHeader(lastScrollY);
        showScrollUp(lastScrollY);
        isTicking = false;
      });
      isTicking = true;
    }
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  $(window).on("resize", function () {
    $(".cs_site_header").removeClass("active");
    $(".cs_menu_toggle")
      .removeClass("active")
      .siblings(".cs_nav_list_wrap")
      .removeClass("active");
  });

  $(function () {
    mainNav();
    stickyHeader();
    dynamicBackground();
    slickInit();
    modalVideo();
    scrollUp();
    accordian();
    review();
    counterInit();
    smoothScroll();
    footerSuburbsAccordion();
    aosInit();
    $(".tom_select").each(function () {
      new TomSelect(this, {
        create: false,
        onDropdownOpen: function (dropdown) {
          dropdown.classList.add("active");
        },
        onDropdownClose: function (dropdown) {
          dropdown.classList.remove("active");
        },
      });
    });
    if ($.exists(".cs_getting_year")) {
      const date = new Date();
      $(".cs_getting_year").text(date.getFullYear());
    }
  });

  /*=============================================================
    01. Preloader
  ===============================================================*/
  function preloader() {
    $(".cs_preloader_in").fadeOut();
    $(".cs_preloader").delay(150).fadeOut("slow");
  }

  /*=============================================================
    02. Mobile Menu
  ===============================================================*/
  function mainNav() {
    $(".cs_nav").append('<span class="cs_menu_toggle"><span></span></span>');
    $(".menu-item-has-children").append(
      '<span class="cs_menu_dropdown_toggle"><span></span></span>'
    );
    $(".cs_menu_toggle").on("click", function () {
      $(this)
        .toggleClass("active")
        .siblings(".cs_nav_list_wrap")
        .toggleClass("active");
      $(".cs_site_header").toggleClass("active");
    });
    $(".cs_menu_dropdown_toggle").on("click", function () {
      $(this).toggleClass("active").siblings("ul").slideToggle();
      $(this).parent().toggleClass("active");
    });
  }

  /*=============================================================
    03. Sticky Header
  ===============================================================*/
  function stickyHeader(scrollY) {
    var scroll = typeof scrollY === "number" ? scrollY : window.scrollY || 0;
    if (scroll >= 10) {
      $(".cs_sticky_header").addClass("cs_sticky_active");
    } else {
      $(".cs_sticky_header").removeClass("cs_sticky_active");
    }
  }
  /*=============================================================
    04. Dynamic Background
  ===============================================================*/
  function dynamicBackground() {
    $("[data-src]").each(function () {
      var src = $(this).attr("data-src");
      $(this).css({
        "background-image": "url(" + src + ")",
      });
    });
  }
  /*=============================================================
   05. Slick Slider
  ===============================================================*/
  function slickInit() {
    if ($.exists(".cs_slider")) {
      $(".cs_slider").each(function () {
        // Slick Variable
        var $ts = $(this).find(".cs_slider_container");
        var $slickActive = $(this).find(".cs_slider_wrapper");
        // Auto Play
        var autoPlayVar = parseInt($ts.attr("data-autoplay"), 10);
        // Auto Play Time Out
        var autoplaySpdVar = 3000;
        if (autoPlayVar > 1) {
          autoplaySpdVar = autoPlayVar;
          autoPlayVar = 1;
        }
        // Slide Change Speed
        var speedVar = parseInt($ts.attr("data-speed"), 10);
        // Slider Loop
        var loopVar = Boolean(parseInt($ts.attr("data-loop"), 10));
        // Slider Center
        var centerVar = Boolean(parseInt($ts.attr("data-center"), 10));
        // Variable Width
        var variableWidthVar = Boolean(
          parseInt($ts.attr("data-variable-width"), 10)
        );
        // Pagination
        var paginaiton = $(this)
          .find(".cs_pagination")
          .hasClass("cs_pagination");
        // Slide Per View
        var slidesPerView = $ts.attr("data-slides-per-view");
        if (slidesPerView == 1) {
          slidesPerView = 1;
        }
        if (slidesPerView == "responsive") {
          var slidesPerView = parseInt($ts.attr("data-add-slides"), 10) || 1;
          var lgPoint = parseInt($ts.attr("data-lg-slides"), 10) || 1;
          var mdPoint = parseInt($ts.attr("data-md-slides"), 10) || 1;
          var smPoint = parseInt($ts.attr("data-sm-slides"), 10) || 1;
          var xsPoing = parseInt($ts.attr("data-xs-slides"), 10) || 1;
        }
        // Fade Slider
        var fadeVar = parseInt($($ts).attr("data-fade-slide"));
        fadeVar === 1 ? (fadeVar = true) : (fadeVar = false);

        // Slick Active Code
        $slickActive.slick({
          autoplay: autoPlayVar,
          dots: paginaiton,
          centerPadding: "28%",
          speed: speedVar,
          infinite: loopVar,
          autoplaySpeed: autoplaySpdVar,
          centerMode: centerVar,
          fade: fadeVar,
          prevArrow: $(this).find(".cs_left_arrow"),
          nextArrow: $(this).find(".cs_right_arrow"),
          appendDots: $(this).find(".cs_pagination"),
          slidesToShow: slidesPerView,
          variableWidth: variableWidthVar,
          swipeToSlide: true,
          responsive: [
            {
              breakpoint: 1600,
              settings: {
                slidesToShow: lgPoint,
              },
            },
            {
              breakpoint: 1200,
              settings: {
                slidesToShow: mdPoint,
              },
            },
            {
              breakpoint: 992,
              settings: {
                slidesToShow: smPoint,
              },
            },
            {
              breakpoint: 768,
              settings: {
                slidesToShow: xsPoing,
                slidesToScroll: xsPoing,
              },
            },
          ],
        });
      });
    }
  }
  /*=============================================================
    06. Modal Video
  ===============================================================*/
  function modalVideo() {
    if ($.exists(".cs_video_open")) {
      $("body").append(`
        <div class="cs_video_popup">
          <div class="cs_video_popup-overlay"></div>
          <div class="cs_video_popup-content">
            <div class="cs_video_popup-layer"></div>
            <div class="cs_video_popup_container">
              <div class="cs_video_popup-align">
                <div class="embed-responsive embed-responsive-16by9">
                  <iframe class="embed-responsive-item" src="about:blank"></iframe>
                </div>
              </div>
              <div class="cs_video_popup_close"></div>
            </div>
          </div>
        </div>
      `);
      $(document).on("click", ".cs_video_open", function (e) {
        e.preventDefault();
        var video = $(this).attr("href");

        $(".cs_video_popup_container iframe").attr("src", `${video}`);

        $(".cs_video_popup").addClass("active");
        $("html").addClass("overflow-hidden");
      });
      $(".cs_video_popup_close, .cs_video_popup-layer").on(
        "click",
        function (e) {
          $(".cs_video_popup").removeClass("active");
          $("html").removeClass("overflow-hidden");
          $(".cs_video_popup_container iframe").attr("src", "about:blank");
          e.preventDefault();
        }
      );
    }
  }

  /*=============================================================
    07. Scroll Up
  ===============================================================*/
  function scrollUp() {
    $(".cs_scrollup").on("click", function (e) {
      e.preventDefault();
      $("html,body").animate(
        {
          scrollTop: 0,
        },
        0
      );
    });
  }
  /* For Scroll Up */
  function showScrollUp(scrollY) {
    let scroll = typeof scrollY === "number" ? scrollY : window.scrollY || 0;
    if (scroll >= 350) {
      $(".cs_scrollup").addClass("active");
    } else {
      $(".cs_scrollup").removeClass("active");
    }
  }
  /*=============================================================
    08. Accordian
  ===============================================================*/
  function accordian() {
    $(".cs_accordian").children(".cs_accordian_body").hide();
    $(".cs_accordian.active").children(".cs_accordian_body").show();
    $(".cs_accordian_head").on("click", function () {
      $(this)
        .siblings()
        .slideDown(250)
        .parent(".cs_accordian")
        .siblings()
        .children(".cs_accordian_body")
        .slideUp(250);

      /* Accordian Active Class */
      $(this).parents(".cs_accordian").addClass("active");
      $(this).parent(".cs_accordian").siblings().removeClass("active");
    });
  }

  /*=============================================================
    09. Review
  ===============================================================*/
  function review() {
    $(".cs_rating").each(function () {
      var review = $(this).data("rating");
      var reviewVal = review * 20 + "%";
      $(this).find(".cs_rating_percentage").css("width", reviewVal);
    });
  }

  /*===========================================================
    10. Counter Animation
  =============================================================*/
  function counterInit() {
    if (!$.exists(".odometer")) return;

    if ("IntersectionObserver" in window) {
      const observer = new IntersectionObserver(
        (entries, obs) => {
          entries.forEach((entry) => {
            if (!entry.isIntersecting) return;
            const el = entry.target;
            $(el).html($(el).data("count-to"));
            obs.unobserve(el);
          });
        },
        { root: null, threshold: 0.4 }
      );

      $(".odometer").each(function () {
        observer.observe(this);
      });
      return;
    }

    // Fallback for very old browsers
    const checkCounters = () => {
      const scrollPos = window.scrollY || window.pageYOffset || 0;
      const winHeight = window.innerHeight || $(window).height();
      const scrollPosition = Math.round(scrollPos + winHeight / 1.2);
      $(".odometer").each(function () {
        var elemOffset = $(this).offset().top;
        if (elemOffset < scrollPosition) {
          $(this).html($(this).data("count-to"));
        }
      });
    };
    window.addEventListener("scroll", checkCounters, { passive: true });
    checkCounters();
  }

  /*===========================================================
    11. Smooth Page Scroll
  =============================================================*/
  function smoothScroll() {
    if (typeof Lenis !== "undefined") {
      const lenis = new Lenis({
        duration: 1.2,
        smooth: true,
        easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      });

      function raf(time) {
        lenis.raf(time);
        requestAnimationFrame(raf);
      }

      requestAnimationFrame(raf);

      // Fix for Bootstrap Modals: Focus the modal body to enable keyboard scrolling
      // and stop Lenis to prevent background scroll and layout shifts
      $('.modal').on('show.bs.modal', function () {
        lenis.stop();
      });
      $('.modal').on('shown.bs.modal', function () {
        $(this).find('.modal-body').focus();
      });
      $('.modal').on('hidden.bs.modal', function () {
        lenis.start();
      });

      // Also for custom video popup
      $(document).on("click", ".cs_video_open", function () {
        lenis.stop();
      });
      $(document).on("click", ".cs_video_popup_close, .cs_video_popup-layer", function () {
        lenis.start();
      });
    }
  }
  /*===========================================================
    12. Steps Animation
  =============================================================*/
  let tabInterval;
  let currentIndex = 0;

  const $tabs = $(".cs_iconbox_wrapper_style_2 .cs_iconbox_style_2");
  const $tabContents = $(".cs_step_thumbnail");
  const intervalTime = 5000;

  if ($tabs.length > 0 && $tabContents.length > 0) {
    function activateTab(index) {
      $tabs.eq(index).addClass("active").siblings().removeClass("active");
      
      // Prevent layout jump by making sure the container maintains its height during transition
      const $wrapper = $(".cs_steps_thumbnails_wrapper");
      const currentHeight = $wrapper.height();
      $wrapper.css('min-height', currentHeight + 'px');

      $tabContents.eq(index).stop().fadeIn(800, function() {
          // Once animation is done, we can safely remove the min-height constraint
          $wrapper.css('min-height', '');
      }).siblings().stop().hide();
    }

    function startAutoplay() {
      stopAutoplay();
      tabInterval = setInterval(function () {
        currentIndex = (currentIndex + 1) % $tabs.length;
        activateTab(currentIndex);
      }, intervalTime);
    }

    function stopAutoplay() {
      if (tabInterval) clearInterval(tabInterval);
    }

    $tabs.on("click", function (e) {
      e.preventDefault();
      stopAutoplay();
      currentIndex = $(this).index();
      activateTab(currentIndex);
      startAutoplay();
    });

    // Init
    $tabContents.hide();
    activateTab(currentIndex);
    startAutoplay();
  }
  /*==============================================================
    13. Dynamic contact form
    ===============================================================*/
  if ($.exists("#cs_form")) {
    const form = document.getElementById("cs_form");
    const result = document.getElementById("cs_result");

    form.addEventListener("submit", function (e) {
      const formData = new FormData(form);
      e.preventDefault();
      var object = {};
      formData.forEach((value, key) => {
        object[key] = value;
      });
      var json = JSON.stringify(object);
      result.innerHTML = "Please wait...";

      fetch("https://formspree.io/f/xgoldvgo", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
        body: json,
      })
        .then(async (response) => {
          if (response.ok) {
            result.innerHTML = "Form successfully submitted";
          } else {
            let json = await response.json();
            if (Object.hasOwn(json, 'errors')) {
              result.innerHTML = json.errors.map(error => error.message).join(", ");
            } else {
              result.innerHTML = "Oops! There was a problem submitting your form";
            }
          }
        })
        .catch((error) => {
          console.log(error);
          result.innerHTML = "Something went wrong!";
        })
        .then(function () {
          form.reset();
          setTimeout(() => {
            result.style.display = "none";
          }, 5000);
        });
    });
  }
  /*=============================================================
    14. AOS Animation
  ===============================================================*/
  function aosInit() {
    AOS.init({
      offset: 100,
      duration: 800,
      easing: "ease-in-out",
      once: true,
      mirror: false,
    });
  }

  /*=============================================================
    15. Footer Suburbs Accordion
  ===============================================================*/
  function footerSuburbsAccordion() {
    $(".cs_footer_suburbs_toggle").on("click", function () {
      $(this).toggleClass("active");
      $(".cs_footer_suburbs_content").slideToggle(300);
    });
  }
})(jQuery); // End of use strict

function copyCode(elementId, msgId, btnElement) {
  const codeText = document.getElementById(elementId).innerText;
  navigator.clipboard.writeText(codeText).then(() => {
    // Show Success Message
    const msg = document.getElementById(msgId);
    msg.style.setProperty('display', 'block', 'important');
    msg.classList.remove('show');
    void msg.offsetWidth; // Trigger reflow
    msg.classList.add('show');
    
    // Hide after animation ends
    setTimeout(() => {
        msg.style.setProperty('display', 'none', 'important');
        msg.classList.remove('show');
    }, 2500);

    // Add click animation to button
    btnElement.classList.add('clicked');
    setTimeout(() => {
      btnElement.classList.remove('clicked');
    }, 150);
  }).catch(err => {
    console.error('Failed to copy text: ', err);
  });
}

// =====================================================================
// FIX: Prevent Bootstrap from shifting the page when modals open.
// Bootstrap injects padding-right as an INLINE STYLE on <body> to
// compensate for the hidden scrollbar. Inline styles override CSS.
// We use a MutationObserver to immediately reset it back to 0 each
// time Bootstrap adds it, completely eliminating the page shift.
// =====================================================================
(function preventBootstrapScrollbarShift() {
  const fixPadding = () => {
    if (document.body.style.paddingRight) {
      document.body.style.paddingRight = '0px';
    }
    // Also fix any fixed/sticky elements Bootstrap may have adjusted
    document.querySelectorAll('.cs_site_header, .modal, [data-bs-padding-right]').forEach(el => {
      if (el.style.paddingRight) {
        el.style.paddingRight = '0px';
      }
    });
  };

  // Watch the body's style attribute for changes Bootstrap makes
  const observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
      if (mutation.attributeName === 'style') {
        fixPadding();
      }
    });
  });

  document.addEventListener('DOMContentLoaded', () => {
    observer.observe(document.body, {
      attributes: true,
      attributeFilter: ['style']
    });
  });
  
  // Also listen to Bootstrap modal events as a backup
  document.addEventListener('show.bs.modal', () => {
    requestAnimationFrame(fixPadding);
    setTimeout(fixPadding, 50);
  });
})();

// =====================================================================
// NEWSLETTER FOOTER FORM: shared submit handler for all site footers.
// Sends email to the same Google Apps Script endpoint used on home.
// =====================================================================
(function handleNewsletterForms() {
  const NEWSLETTER_ENDPOINT =
    "https://script.google.com/macros/s/AKfycbx-B1He7qGzZGq8HMQ2-ZsvfBU4dHyCaFBiQlowZCp_dmJd4xEFv03SSNg9smKfxOmi/exec";

  document.addEventListener("DOMContentLoaded", () => {
    const forms = document.querySelectorAll(".cs_newsletter_form");
    if (!forms.length) return;

    forms.forEach((form) => {
      if (form.dataset.newsletterBound === "true") return;
      form.dataset.newsletterBound = "true";

      form.setAttribute("action", NEWSLETTER_ENDPOINT);
      form.setAttribute("method", "POST");

      const submitButton = form.querySelector('button[type="submit"]');
      if (!submitButton) return;

      submitButton.dataset.originalText = submitButton.textContent.trim();

      form.addEventListener("submit", (e) => {
        e.preventDefault();

        const originalText = submitButton.dataset.originalText || "Send";
        submitButton.textContent = "Sending...";
        submitButton.disabled = true;

        const formData = new FormData(form);

        fetch(form.action, {
          method: "POST",
          body: formData,
          mode: "no-cors",
        })
          .then(() => {
            submitButton.textContent = "Subscribed";
            form.reset();
            setTimeout(() => {
              submitButton.textContent = originalText;
              submitButton.disabled = false;
            }, 5000);
          })
          .catch((error) => {
            console.error("Newsletter submission failed:", error);
            submitButton.textContent = "Error";
            setTimeout(() => {
              submitButton.textContent = originalText;
              submitButton.disabled = false;
            }, 3000);
          });
      });
    });
  });
})();
// =====================================================================
// AUTOMATIC DISCOUT POPUP: Triggered by scroll, only once per user.
// Uses localStorage for persistence across browser restarts.
// =====================================================================
(function handleAutomaticDiscountModal() {
  const SCROLL_THRESHOLD = 1000; // Trigger after 1000px scroll
  const STORAGE_KEY = 'cs_discount_modal_shown';
  const MODAL_ID = 'popup-discount-final';

  const showModal = () => {
    if (localStorage.getItem(STORAGE_KEY)) return;

    const modalElement = document.getElementById(MODAL_ID);
    if (!modalElement) return;

    const modalInstance = bootstrap.Modal.getOrCreateInstance(modalElement);
    modalInstance.show();
    localStorage.setItem(STORAGE_KEY, 'true');
  };

  const onScroll = () => {
    if (window.scrollY > SCROLL_THRESHOLD) {
      showModal();
      window.removeEventListener('scroll', onScroll);
    }
  };

  if (!localStorage.getItem(STORAGE_KEY)) {
    window.addEventListener('scroll', onScroll, { passive: true });
  }
})();
