// JavaScript to toggle larger view of images on click
const images = document.querySelectorAll('.image-grid > img');
images.forEach(image => {
    image.addEventListener('click', () => {
        image.classList.toggle('expanded');
    });
});