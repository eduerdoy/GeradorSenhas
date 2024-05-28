document.getElementById('password-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const length = document.getElementById('length').value;

    fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `length=${length}`
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('password').textContent = data.password;
    })
    .catch(error => console.error('Error:', error));
});