const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const btnPopup = document.querySelector('.btnLogin-popup');
const iconClose = document.querySelector('.icon-close');

registerLink.addEventListener('click', () => {
    wrapper.classList.add('active');
});

loginLink.addEventListener('click', () => {
    wrapper.classList.remove('active');
});

btnPopup.addEventListener('click', () => {
    wrapper.classList.add('active-popup');
});

iconClose.addEventListener('click', () => {
    wrapper.classList.remove('active-popup');
});

document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    if (username === 'admin@gmail.com' && password === 'password') {
        alert('Login successful');
        window.location.href = 'index.html';
    } else {
        alert('Invalid username or password');
    }
});

const logoutButton = document.querySelector('.btnLogout');

logoutButton.addEventListener('click', () => {
    window.location.href = 'login.html';
});


