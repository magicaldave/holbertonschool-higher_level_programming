const $ = window.$;
$('#update_header').click(function () {
    $('header').replaceWith('<header>New Header!!!</header>');
});