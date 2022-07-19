if ($(window).width() < 600){
    console.log('i can see Clients script')
    var slideIndex2 = 1;
    var myTimer2;

    showSlides2(slideIndex2);

    // NEXT AND PREVIOUS CONTROL
    function plusSlides2(n){
        clearInterval(myTimer2);
        if (n < 0){
            showSlides2(slideIndex2 -= 1);
        } else {
            showSlides2(slideIndex2 += 1);
        }

        if (n === -1){
            myTimer2 = setInterval(function(){plusSlides2(n + 2)}, 2500);
        } else {
            myTimer2 = setInterval(function(){plusSlides2(n + 1)}, 2500);
        }
    }

    //Controls the current slide and resets interval if needed
    function currentSlide2(n){
        clearInterval(myTimer2);
        myTimer2 = setInterval(function(){plusSlides2(n + 1)}, 2500);
        showSlides2(slideIndex2 = n);
    }

    function showSlides2(n){
        var i;
        var slides = $(".clientSlide");
        var dots = $(".dot");
        console.log(slides)
        if (n > slides.length) {slideIndex2 = 1}
        if (n < 1) {slideIndex2 = slides.length}

        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }

        for (i = 0; i < dots.length; i++) {
            dots[i].className = dots[i].className.replace(" active", "");
        }

        slides[slideIndex2-1].style.display = "flex";
        dots[slideIndex2-1].className += " active";
    }
}