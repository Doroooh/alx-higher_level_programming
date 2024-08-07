// Update header element text color with #FF0000, red, tag DIV#red_header

$(document).ready(function() {
    $('DIV#red_header').click(function() {
        $('DIV#red_header').css({ color: '#FF0000' });
    });
});
