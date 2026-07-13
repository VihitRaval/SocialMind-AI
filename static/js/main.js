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