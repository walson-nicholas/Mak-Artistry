if ($(window).width() > 600){

    $(".clients").hover(function(){
        $("#swiper-button-next").css("display", "flex");
        $("#swiper-button-prev").css("display", "flex");
        }, function(){
            $("#swiper-button-next").css("display", "none");
            $("#swiper-button-prev").css("display", "none");
    });


    var swiper = new Swiper(".swiper", {
        slidesPerView: "5",
        spaceBetween: 10,
        loop: true,
        pagination:{
            el: ".swiper-pagination",
            clickable: true,
        },
        navigation:{
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },
    });
}

if ($(window).width() < 600){
    var swiper = new Swiper(".swiper", {
        slidesPerView: "1",
        spaceBetween: 10,
        loop: true,
        pagination:{
            el: ".swiper-pagination",
            clickable: true,
        },
    });
}