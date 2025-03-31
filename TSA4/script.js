document.addEventListener('DOMContentLoaded', () => {
    const menuItems = document.querySelectorAll('.menu-item');
    const popupMenu = document.getElementById('popup-menu');
    const mainMenuBtn = document.getElementById('main-menu-btn');
    const popupTitle = document.querySelector('.popup-title');
    const popupAddress = document.querySelector('.popup-address');
    const popupCategory = document.querySelector('.popup-category');
    const popupDescription = document.querySelector('.popup-description');
    const popupImage = document.getElementById('popup-image');

    // Data for each menu item
    const menuData = {
        'Gabel Loffel': {
            address: 'Lorem Ipsum Street, 123',
            category: 'German Cuisine',
            time: '10:00 AM - 10:00 PM',
            price: '$$$',
            description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
            image: './images/mash.jpg' // Corrected path
        },
        'Gary Gari': {
            address: 'Dolor Sit Avenue, 456',
            category: 'Japanese Cuisine',
            time: '11:00 AM - 9:00 PM',
            price: '$$',
            description: 'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            image: './images/corn_steak.jfif' // Corrected path
        },
        'IL Piatto': {
            address: 'Consectetur Road, 789',
            category: 'Italian Cuisine',
            time: '12:00 PM - 11:00 PM',
            price: '$$$',
            description: 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
            image: './images/fish.png' // Corrected path
        },
        'Pierre Platters': {
            address: 'Adipiscing Blvd, 101',
            category: 'French Cuisine',
            time: '9:00 AM - 8:00 PM',
            price: '$$$$',
            description: 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            image: './images/steak_lobster.jfif' // Corrected path
        }
    };

    // Show pop-up menu
    menuItems.forEach(item => {
        item.addEventListener('click', () => {
            const title = item.querySelector('.menu-title').textContent;
            const data = menuData[title];

            // Populate pop-up with data
            popupTitle.textContent = title;
            popupAddress.innerHTML = `<strong>Address:</strong> ${data.address}`;
            popupCategory.innerHTML = `<strong>Category:</strong> ${data.category}<br><strong>Time:</strong> ${data.time}<br><strong>Price:</strong> ${data.price}`;
            popupDescription.textContent = data.description;
            popupImage.src = data.image;

            // Show the pop-up
            popupMenu.style.display = 'flex';
        });
    });

    // Close pop-up menu using the Main Menu button
    mainMenuBtn.addEventListener('click', () => {
        popupMenu.style.display = 'none';
    });
});