document.getElementById("contact-form").addEventListener("submit", function(e) {
    e.preventDefault();
    alert("Thank you for reaching out! We'll get back to you soon.");
});

document.getElementById("contact-form").addEventListener("submit", function(e) {
    e.preventDefault();
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const message = document.getElementById("message").value;

    // Assuming you have a server running on the same Replit project
    fetch('/api/submit-request', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, email, message })
    })
    .then(response => {
        if (response.ok) {
            alert("Thank you for reaching out! We'll get back to you soon.");
        } else {
            alert("Something went wrong, please try again later.");
        }
    })
    .catch(error => {
        alert("Something went wrong, please try again later.");
    });

