/*
=========================================
SocialMind AI
main.js
=========================================
*/

document.addEventListener("DOMContentLoaded", () => {

    console.log("🚀 SocialMind AI Loaded");

    // ------------------------------------
    // Elements
    // ------------------------------------

    const form = document.querySelector("form");
    const searchInput = document.querySelector("input[name='query']");
    const searchButton = document.querySelector("button[type='submit']");

    // ------------------------------------
    // Auto Focus
    // ------------------------------------

    if (searchInput) {
        searchInput.focus();
    }

    // ------------------------------------
    // Form Validation
    // ------------------------------------

    if (form) {

        form.addEventListener("submit", function (event) {

            const query = searchInput.value.trim();

            if (query.length === 0) {

                event.preventDefault();

                alert("Please enter a search query.");

                searchInput.focus();

                return;

            }

            if (query.length < 2) {

                event.preventDefault();

                alert("Search query must contain at least 2 characters.");

                searchInput.focus();

                return;

            }

            // Loading Button

            if (searchButton) {

                searchButton.disabled = true;

                searchButton.innerHTML = `
                    <span class="spinner-border spinner-border-sm"></span>
                    Searching...
                `;

            }

        });

    }

    // ------------------------------------
    // Press Enter Anywhere
    // ------------------------------------

    document.addEventListener("keydown", function (event) {

        if (event.key === "Enter" && searchInput === document.activeElement) {

            form.requestSubmit();

        }

    });

    // ------------------------------------
    // Search Suggestions
    // ------------------------------------

    const suggestions = [

        "AI Internship",

        "Machine Learning",

        "Python Developer",

        "Artificial Intelligence",

        "Deep Learning",

        "Data Science",

        "Software Engineer",

        "Digital Marketing"

    ];

    if (searchInput) {

        searchInput.addEventListener("focus", function () {

            const randomSuggestion = suggestions[
                Math.floor(Math.random() * suggestions.length)
            ];

            searchInput.placeholder = `Try: ${randomSuggestion}`;

        });

        searchInput.addEventListener("blur", function () {

            searchInput.placeholder =
                "Search AI Internship, Machine Learning, Python...";

        });

    }

    // ------------------------------------
    // Scroll Animation
    // ------------------------------------

    const cards = document.querySelectorAll(".card");

    cards.forEach((card, index) => {

        card.style.opacity = "0";

        card.style.transform = "translateY(25px)";

        setTimeout(() => {

            card.style.transition = "all 0.5s ease";

            card.style.opacity = "1";

            card.style.transform = "translateY(0)";

        }, index * 120);

    });

    // ------------------------------------
    // Success Message
    // ------------------------------------

    console.log("✅ UI Ready");

});
/* ==========================================
   Search History
========================================== */

const historyKey = "socialmind_search_history";

// Save search query
if (form) {

    form.addEventListener("submit", function () {

        const query = searchInput.value.trim();

        if (query.length > 1) {

            let history = JSON.parse(localStorage.getItem(historyKey)) || [];

            // Remove duplicate if it exists
            history = history.filter(item => item !== query);

            // Add latest search to the beginning
            history.unshift(query);

            // Keep only last 5 searches
            history = history.slice(0, 5);

            localStorage.setItem(historyKey, JSON.stringify(history));

        }

    });

}
/* ==========================================
   Display Search History
========================================== */

const historyContainer = document.getElementById("search-history");

if (historyContainer) {

    const history =
        JSON.parse(localStorage.getItem(historyKey)) || [];

    history.forEach(query => {

        const button = document.createElement("button");

        button.className =
            "btn btn-outline-light btn-sm m-1";

        button.textContent = query;

        button.onclick = function () {

            searchInput.value = query;

            form.requestSubmit();

        };

        historyContainer.appendChild(button);

    });

}

/* ==========================================
   Navigation Bar Functionality
   ========================================== */

// Handle navbar scroll effect
const navbar = document.querySelector(".custom-navbar");
if (navbar) {
    window.addEventListener("scroll", () => {
        if (window.scrollY > 20) {
            navbar.classList.add("navbar-scrolled");
        } else {
            navbar.classList.remove("navbar-scrolled");
        }
    });
}

// Highlight current active link dynamically
const currentPath = window.location.pathname;
const navLinks = document.querySelectorAll(".custom-navbar .nav-link");
navLinks.forEach(link => {
    const href = link.getAttribute("href");
    if (href === currentPath) {
        link.classList.add("active");
    } else if (currentPath === "/search" && href === "/") {
        // Keep Home highlighted on search results page
        link.classList.add("active");
    }
});

// Custom hamburger toggle handler (enables smooth animation + toggle state)
const navbarToggler = document.querySelector(".custom-toggler");
const navbarCollapse = document.querySelector("#navbarContent");
if (navbarToggler && navbarCollapse) {
    navbarToggler.addEventListener("click", () => {
        const isCollapsed = navbarToggler.classList.contains("collapsed");
        if (isCollapsed) {
            navbarToggler.classList.remove("collapsed");
            navbarToggler.setAttribute("aria-expanded", "true");
            navbarCollapse.classList.add("show");
        } else {
            navbarToggler.classList.add("collapsed");
            navbarToggler.setAttribute("aria-expanded", "false");
            navbarCollapse.classList.remove("show");
        }
    });
}

/* ==========================================
   Technical Interview Guide Interactions
   ========================================== */
document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.getElementById("guide-search-input");
    const pills = document.querySelectorAll(".category-pill-btn");
    const sections = document.querySelectorAll(".category-section-wrapper");
    const zeroState = document.getElementById("zero-results-card");
    const backToTopBtn = document.getElementById("back-to-top");
    const sidebarLinks = document.querySelectorAll(".sidebar-nav-link");

    if (!searchInput && pills.length === 0) {
        // Not on the interview guide page, skip guide logic
        return;
    }

    let activeCategory = "all";

    // 1. Category Pill click handler
    pills.forEach(pill => {
        pill.addEventListener("click", () => {
            const category = pill.getAttribute("data-category");
            
            // Toggle active pill classes
            pills.forEach(p => p.classList.remove("active-pill"));
            pill.classList.add("active-pill");

            // Sync sidebar links active state
            sidebarLinks.forEach(link => {
                if (link.getAttribute("data-section") === category) {
                    link.classList.add("active");
                } else {
                    link.classList.remove("active");
                }
            });

            activeCategory = category;
            applyFilter();
        });
    });

    // 2. Sidebar Navigation click handler
    sidebarLinks.forEach(link => {
        link.addEventListener("click", (e) => {
            const sectionId = link.getAttribute("data-section");
            
            if (sectionId === "all") {
                e.preventDefault();
                window.scrollTo({ top: 0, behavior: "smooth" });
                
                // Trigger 'all' pill click
                const allPill = document.querySelector('.category-pill-btn[data-category="all"]');
                if (allPill) allPill.click();
                return;
            }

            // Sync pills active state
            const targetPill = document.querySelector(`.category-pill-btn[data-category="${sectionId}"]`);
            if (targetPill) {
                pills.forEach(p => p.classList.remove("active-pill"));
                targetPill.classList.add("active-pill");
                activeCategory = sectionId;
            }

            sidebarLinks.forEach(l => l.classList.remove("active"));
            link.classList.add("active");
            
            applyFilter();
        });
    });

    // 3. Live search query handler
    if (searchInput) {
        searchInput.addEventListener("input", () => {
            applyFilter();
        });
    }

    // 4. Combined Filter and Search Function
    function applyFilter() {
        const query = searchInput ? searchInput.value.toLowerCase().trim() : "";
        let visibleOverall = 0;

        sections.forEach(section => {
            const catId = section.getAttribute("data-category");
            const isCategoryMatch = (activeCategory === "all" || activeCategory === catId);
            const sectionCards = section.querySelectorAll(".question-card");
            let visibleInSection = 0;

            sectionCards.forEach(card => {
                const cardText = card.getAttribute("data-question-text") || "";
                const isSearchMatch = query === "" || cardText.includes(query);

                if (isCategoryMatch && isSearchMatch) {
                    card.classList.remove("d-none");
                    visibleInSection++;
                    visibleOverall++;
                } else {
                    card.classList.add("d-none");
                }
            });

            // Toggle category section visibility based on cards match
            if (isCategoryMatch && visibleInSection > 0) {
                section.classList.remove("d-none");
            } else {
                section.classList.add("d-none");
            }
        });

        // Toggle zero state
        if (visibleOverall === 0) {
            zeroState.classList.remove("d-none");
        } else {
            zeroState.classList.add("d-none");
        }
    }

    // 5. Back to Top behavior
    if (backToTopBtn) {
        window.addEventListener("scroll", () => {
            if (window.scrollY > 300) {
                backToTopBtn.style.display = "block";
            } else {
                backToTopBtn.style.display = "none";
            }
        });

        backToTopBtn.addEventListener("click", () => {
            window.scrollTo({ top: 0, behavior: "smooth" });
        });
    }

    // Expand All / Collapse All button handlers
    const expandAllBtn = document.getElementById("btn-expand-all");
    const collapseAllBtn = document.getElementById("btn-collapse-all");

    if (expandAllBtn) {
        expandAllBtn.addEventListener("click", () => {
            const collapses = document.querySelectorAll(".accordion-collapse");
            collapses.forEach(el => {
                const card = el.closest(".question-card");
                if (card && !card.classList.contains("d-none") && !el.classList.contains("show")) {
                    el.classList.add("show");
                    const button = document.querySelector(`[data-bs-target="#${el.id}"]`);
                    if (button) {
                        button.classList.remove("collapsed");
                        button.setAttribute("aria-expanded", "true");
                    }
                }
            });
        });
    }

    if (collapseAllBtn) {
        collapseAllBtn.addEventListener("click", () => {
            const collapses = document.querySelectorAll(".accordion-collapse");
            collapses.forEach(el => {
                if (el.classList.contains("show")) {
                    el.classList.remove("show");
                    const button = document.querySelector(`[data-bs-target="#${el.id}"]`);
                    if (button) {
                        button.classList.add("collapsed");
                        button.setAttribute("aria-expanded", "false");
                    }
                }
            });
        });
    }

    // 6. ScrollSpy implementation to highlight active sidebar item on scroll
    window.addEventListener("scroll", () => {
        if (activeCategory !== "all") return; // Only highlight based on scroll position when "All Topics" is active

        let currentSectionId = "all";
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 120;
            if (window.scrollY >= sectionTop) {
                currentSectionId = section.getAttribute("data-category");
            }
        });

        sidebarLinks.forEach(link => {
            if (link.getAttribute("data-section") === currentSectionId) {
                link.classList.add("active");
            } else {
                link.classList.remove("active");
            }
        });
    });
});