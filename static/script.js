
document.addEventListener("DOMContentLoaded", function () {

    // Get the prediction form and button
    const form = document.getElementById("predictionForm");
    const button = document.getElementById("predictButton");

    // Show loading animation when predicting
    if (form && button) {
        form.addEventListener("submit", function (event) {

            if (!form.checkValidity()) {
                return;
            }

            button.disabled = true;
            button.innerHTML = `
                <span>Predicting...</span>
                <span class="spinner"></span>
            `;
        });
    }

    // Smoothly scroll to prediction result
    const result = document.querySelector(".result-card");

    if (result) {
        result.scrollIntoView({
            behavior: "smooth",
            block: "center"
        });
    }

    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(function (link) {

        link.addEventListener("click", function (event) {

            const target = document.querySelector(this.getAttribute("href"));

            if (target) {
                event.preventDefault();

                target.scrollIntoView({
                    behavior: "smooth"
                });
            }
        });

    });

});
