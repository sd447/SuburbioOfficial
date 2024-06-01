let currentIndex = 0;
let intervalId;

const images = document.querySelectorAll('.carousel-img');
const indicators = document.querySelectorAll('.indicator');

function showImage(index) {
  if (index < 0 || index >= images.length) return;

  images[currentIndex].classList.remove('active');
  indicators[currentIndex].classList.remove('active');
  images[index].classList.add('active');
  indicators[index].classList.add('active');
  currentIndex = index;
}

function startCarousel() {
  intervalId = setInterval(() => {
    const nextIndex = (currentIndex + 1) % images.length;
    showImage(nextIndex);
  }, 3000);
}

function pauseCarousel() {
  clearInterval(intervalId);
}

startCarousel(); // Inicia o carrossel quando a página é carregada