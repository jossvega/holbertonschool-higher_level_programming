/* script that adds the class red to the HTML tag HEADER
to red (#FF0000) when the user clicks on the tag DIV#red_header:
You can’t use document.querySelector
*/
$(document).ready(function () {
    $('div#red_header').click(function () {
      $('header').addClass('red');
    });
  });