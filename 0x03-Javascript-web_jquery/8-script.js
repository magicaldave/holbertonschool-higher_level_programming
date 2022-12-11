const $ = window.$;
const swapi = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.getJSON(swapi, function (data) {
    $.each(data.results, function(index, film) {
        $('UL#list_movies').append(`<li>${this.title}</li>`);
    });
});
