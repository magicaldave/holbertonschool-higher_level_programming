const $ = window.$;
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$(document).ready(function () {
  $.getJSON(url, function (data) {
    $('#character').append(data.name);
  });
});
