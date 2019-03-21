$('div.mobile-button').click(function(e) {
    e.preventDefault();
    $('nav.menu').toggleClass('active');
});

$('.dropdown').click(function(e) {
    $('.dropdown').not(this).removeClass('active');    
    $(this).toggleClass('active');
});
