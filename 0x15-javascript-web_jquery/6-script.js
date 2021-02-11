/*
script that updates the text of the HTML tag HEADER to
“New Header!!!” when the user clicks on DIV#update_header
You can’t use document.querySelector to select the HTML tag
*/

const $ = window.$;
$(function () {
  $('div#update_header').click(function () {
    $('header').text('New Header!!!');
  });
});
