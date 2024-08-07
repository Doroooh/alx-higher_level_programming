// Add red color, tag DIV#red_header

$(document).ready(function () {
  $('DIV#red_header').click(function () {
    $('header').addClass('red');
  });
});
