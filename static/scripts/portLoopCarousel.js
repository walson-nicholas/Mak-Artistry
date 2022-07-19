console.log('i can see review script')
$('.itemImage').click(function(){
    const currentImage = $('.item1').attr('src');
    const imageToShow = $(this).attr('src');
    $('.item1').attr('src', imageToShow);
    $(this).attr('src', currentImage);
});