﻿document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    // Add your login logic here
    console.log('Email:', email, 'Password:', password);
});