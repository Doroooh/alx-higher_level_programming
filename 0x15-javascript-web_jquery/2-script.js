// This JavaScript script will update header element text color 
// to red (#FF0000) when the user clicks #red_header:

$(document).ready(function() {
    $('#red_header').click(function() {
        $('header').css('color', '#FF0000');
    });
});
