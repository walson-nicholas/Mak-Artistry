if ($(window).width() > 600){
    var SwiperWrapper = $(".swiper-wrapper");
    SwiperWrapper.toggleClass("swiper-wrapper");
    var SwiperSlides = $(".swiper-slide");
    SwiperSlides.toggleClass("swiper-slide");
}

if ($(window).width() < 600){
    console.log('i can see swiper script')
    var swiper = new Swiper(".swiper", {
        slidesPerView: "1",
        spaceBetween: 10,
        loop: true,
    });
}