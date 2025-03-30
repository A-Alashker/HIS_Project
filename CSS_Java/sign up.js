document.getElementById('signupForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const firstName = document.getElementById('firstName').value;
    const lastName = document.getElementById('lastName').value;
    const email = document.getElementById('email').value;
    const contactNumber = document.getElementById('contactNumber').value;
    const role = document.querySelector('input[name="role"]:checked').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    if (password !== confirmPassword) {
        alert('Passwords do not match');
        return;
    }

    // Add your sign-up logic here
    console.log('First Name:', firstName, 'Last Name:', lastName, 'Email:', email, 'Contact Number:', contactNumber, 'Role:', role, 'Password:', password);
});