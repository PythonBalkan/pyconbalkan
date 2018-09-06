$('div.mobile-button').click(function(e) {
    e.preventDefault();
    $('nav.menu').toggleClass('active');
});

$('.menu__list__about').click(function(e) {
    $('.dropdown-menu').toggleClass('dropdown-menu--active');
    $('.menu__list__about').toggleClass('menu__list__about--active');
});