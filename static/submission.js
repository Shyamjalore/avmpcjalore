// Get references to the form, modal, and OK button
const form = document.getElementById("formsubmission");
const modal = document.getElementById("myModal");
const okButton = document.getElementById("okButton");

// Handle form submission
form.addEventListener("submit", function (e) {
    e.preventDefault(); // Prevent the default form submission

    // Show the modal
    modal.style.display = "block";
});

// Handle OK button click
okButton.addEventListener("click", function () {
    // Hide the modal
    modal.style.display = "none";

    // Redirect to index.html (you can change this URL)
    
});
