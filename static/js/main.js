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