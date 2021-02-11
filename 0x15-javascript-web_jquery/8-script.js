/* script that fetches and lists all movies title by using
this URL: `https://swapi-api.hbtn.io/api/films/?format=json`
You can’t use document.querySelector to select the HTML tag
*/

const $ = window.$;
$(document).ready(function () {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  $.get(url, function (data) {
    $.each(data.results, function (index, value) {
      $('<li>' + value.title + '</li>').appendTo('UL#list_movies');
    });
  });
});
