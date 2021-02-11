/* script that fetches and replaces the `name`
of this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
You can’t use document.querySelector to select the HTML tag */

const $ = window.$;
$(document).ready(function () {
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  $.get(url, function (data) {
    const name = data.name;
    $('DIV#character').text(name);
  });
});
