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
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const storedUser = JSON.parse(localStorage.getItem(email));

    if (storedUser && storedUser.password === password) {
        alert('Login successful');
        window.location.href = 'index-loginned.html';
    } else {
        alert('Invalid email or password');
    }
});

document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const email = document.getElementById('registerEmail').value;
    const password = document.getElementById('registerPassword').value;

    if (localStorage.getItem(email)) {
        alert('User already exists');
    } else {
        const user = { email, password };
        localStorage.setItem(email, JSON.stringify(user));
        alert('Registration successful');
        loginLink.click();
    }
});

const logoutButton = document.querySelector('.btnLogout');

if (logoutButton) {
    logoutButton.addEventListener('click', () => {
        window.location.href = 'login.html';
    });
}
