/* script that adds a LI element to a list
when the user clicks on the tag DIV#add_item:
You can’t use document.querySelector to select the HTML tag
*/

$(document).ready(function () {
  $('div#add_item').click(function () {
    const item1 = $('<li></li>').text('Item');
    $('ul.my_list').append(item1);
  });
});
