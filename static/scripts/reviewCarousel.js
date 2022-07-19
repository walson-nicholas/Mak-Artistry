console.log('i can see review script')
$('.img-review').click(function(){
    const currentImage = $('#lastImage').attr('src');
    const imageToShow = $(this).attr('src');
    $('#lastImage').attr('src', imageToShow);
    $(this).attr('src', currentImage);

    const reviewToHide = $('.reviewWriteUp').last().html();
    console.log(reviewToHide)

    let reviewChildren = $('.reviewImages').children();
    reviewChildren.each((index, img) => {
        if($(img).attr('src') === $(this).attr('src')){

            let reviewToShow = $('.reviewWriteUp')[index];
            console.log(reviewToShow)

            let lastReviewContainer = $('.reviewWriteUp')[$('.reviewWriteUp').length - 1];
            $(lastReviewContainer).empty().append($(reviewToShow).html());

            let clickedReviewContainer = $('.reviewWriteUp')[index];
            $(clickedReviewContainer).empty().append(reviewToHide);
        }
    });
});