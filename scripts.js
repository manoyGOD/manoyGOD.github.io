let currentBox = null;

function showBox(day) {
    const container = document.querySelector('.box-container');

    if (currentBox) {
        currentBox.style.top = '-600px';
        setTimeout(() => {
            if (currentBox && currentBox.parentNode === container) {
                container.removeChild(currentBox);
            }
        }, 1500);
    }

    const box = document.createElement('div');
    box.className = 'box';

    let borderColor, backgroundColor;
    switch(day) {
        case 'Monday':
            borderColor = 'purple';
            backgroundColor = 'rgba(128, 0, 128, 0.1)';
            break;
        case 'Tuesday':
            borderColor = 'pink';
            backgroundColor = 'rgba(255, 192, 203, 0.1)';
            break;
        case 'Wednesday':
            borderColor = 'blue';
            backgroundColor = 'rgba(0, 0, 255, 0.1)';
            break;
        case 'Thursday':
            borderColor = 'green';
            backgroundColor = 'rgba(0, 128, 0, 0.1)';
            break;
        case 'Friday':
            borderColor = 'yellow';
            backgroundColor = 'rgba(255, 255, 0, 0.1)';
            break;
        case 'Saturday':
            borderColor = 'orange';
            backgroundColor = 'rgba(255, 165, 0, 0.1)';
            break;
        case 'Sunday':
            borderColor = 'red';
            backgroundColor = 'rgba(255, 0, 0, 0.1)';
            break;
    }

    box.style.borderColor = borderColor;
    box.style.backgroundColor = backgroundColor;

    container.appendChild(box);

    setTimeout(() => {
        box.style.top = '300px';
    }, 100);

    setTimeout(() => {
        currentBox = box;
    }, 1600);
}