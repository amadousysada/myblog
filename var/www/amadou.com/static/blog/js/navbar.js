$(function(){
  $('#navbarSupportedContent ul li:last-child a').click(function(){
    $('#navbarSupportedContent form').toggleClass('visible');
    $('#navbarSupportedContent ul li:last-child a').toggleClass('visible');
  });
});