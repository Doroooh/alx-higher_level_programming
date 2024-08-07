// Update with DIV#update_header on <header> element 

$(document).ready(function () {
  $('DIV#update_header').click(function () {
    $('header').html('New Header!!!');
  });
});
