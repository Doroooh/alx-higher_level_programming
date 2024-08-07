// Adds <li> element the tag DIV#add_item

$(document).ready(function () {
$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
