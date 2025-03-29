// FILE_NAME
function setFileName(fileName) {
    document.getElementById('file-version').textContent = fileName;
}
setFileName("Circus V8.exe");
// SLiDER
const slider = document.querySelector('.slider');
const slides = document.querySelectorAll('.slide');
const dots = document.querySelectorAll('.dot');
const prevButton = document.querySelector('.slider-prev');
const nextButton = document.querySelector('.slider-next');

let currentSlide = 0;

function showSlide(index) {
    if(index < 0 || index >= slides.length){
        return;
    }
    slider.style.transform = `translateX(-${index * 600}px)`;
    dots.forEach(dot => dot.classList.remove('active'));
    dots[index].classList.add('active');
    currentSlide = index;
}

dots.forEach((dot, index) => {
    dot.addEventListener('click', () => {
        showSlide(index);
    });
});

prevButton.addEventListener('click', () => {
  showSlide(currentSlide - 1);
});

nextButton.addEventListener('click', () => {
  showSlide(currentSlide + 1);
});
// DOWNLOAD
const downloadButton = document.getElementById('button');

downloadButton.addEventListener('click', function() {
    const filename = this.getAttribute('data-filename');
    triggerDownload(filename);
});

function triggerDownload(filename) {
    const link = document.createElement('a');
    link.href = filename;
    link.download = filename;
     document.body.appendChild(link);
    link.click();
   document.body.removeChild(link);
}



// PARALLAX
const parallaxWrapper = document.querySelector('.parallax-wrapper');
const parallaxBg = window.getComputedStyle(parallaxWrapper, '::before');
let startY = parallaxBg.getPropertyValue('transform').split('(')[1].split(')')[0].split(',')[5] || 0;

window.addEventListener('scroll', () => {
   const scrollY = window.scrollY;
   const newY = parseFloat(startY) + scrollY * 0.5; // 0.5 - скорость движения, можно менять
   parallaxWrapper.style.setProperty('--bg-translateY', `${newY}px`); // записываем в переменную
   parallaxWrapper.style.setProperty('--scroll-y', `${scrollY}px`)

  //  Удаляем стили псевдоэлемента, при этом он по-прежнему существует и будет изменен в css
   parallaxWrapper.removeAttribute('style');

   parallaxWrapper.classList.add('scrolling')
});