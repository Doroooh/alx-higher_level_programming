//  Fetch the value hello from URL https://hellosalut.stefanbohacek.dev/?lang=fr 
// the value of hello is displayed in the tag DIV#hello 

$(document).ready(function() {
  // translate Hello in French 
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
    console.log(data.hello);
    // Displaying hello
    $('#hello').html(data.hello);
  });
});
