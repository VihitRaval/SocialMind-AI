/*
=========================================
SocialMind AI
main.js
=========================================
*/

document.addEventListener("DOMContentLoaded", function () {

    console.log("✅ SocialMind AI Loaded Successfully");

    // Search Form
    const form = document.querySelector("form");

    if (form) {

        form.addEventListener("submit", function () {

            const button = document.querySelector("button[type='submit']");

            if (button) {

                button.disabled = true;

                button.innerHTML = `
                    <span class="spinner-border spinner-border-sm"></span>
                    Searching...
                `;

            }

        });

    }

    // Auto Focus Search Box
    const searchInput = document.querySelector("input[name='query']");

    if (searchInput) {
        searchInput.focus();
    }

});