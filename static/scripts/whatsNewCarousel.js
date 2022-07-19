console.log('i can see whatsNew script')
var slideIndex1 = 1;
var myTimer1;

showSlides1(slideIndex1);
myTimer1 = setInterval(function(){plusSlides1(1)}, 5000);

// NEXT AND PREVIOUS CONTROL
function plusSlides1(n){
    clearInterval(myTimer1);
    if (n < 0){
        showSlides1(slideIndex1 -= 1);
    } else {
        showSlides1(slideIndex1 += 1);
    }

    if (n === -1){
        myTimer1 = setInterval(function(){plusSlides1(n + 2)}, 5000);
    } else {
        myTimer1 = setInterval(function(){plusSlides1(n + 1)}, 5000);
    }
}

//Controls the current slide and resets interval if needed
function currentSlide1(n){
    clearInterval(myTimer1);
    myTimer1 = setInterval(function(){plusSlides1(n + 1)}, 5000);
    showSlides1(slideIndex1 = n);
}

function showSlides1(n){
    var i;
    var slides = $(".whatsNewSlide");
    if (n > slides.length) {slideIndex1 = 1}
    if (n < 1) {slideIndex1 = slides.length}

    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }

    slides[slideIndex1-1].style.display = "flex";
}