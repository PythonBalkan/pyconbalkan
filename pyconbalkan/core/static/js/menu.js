$('div.mobile-button').click(function(e) {
    e.preventDefault();
    $('nav.menu').toggleClass('active');
});