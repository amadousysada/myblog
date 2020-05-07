$(function(){
  $('#navbarSupportedContent ul li:last-child a.nav-link').click(function(){
    $('#navbarSupportedContent form').toggleClass('visible');
    $('#navbarSupportedContent ul li:last-child a.nav-link').toggleClass('visible');
  });

$(document).on('click touchstart', function (a) {
        if ($(a.target).parents().index($('.navbar-nav')) == -1) {
                $('html').removeClass('menu-open');
        }
});
});