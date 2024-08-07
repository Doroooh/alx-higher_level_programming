// Toggle the class of the <header> tag DIV#toggle_header

$(document).ready(function () {
  $('DIV#toggle_header').click(function () {
    const the_class = ['green', 'red'];
    const new_class = $('header').attr('class');

    // alternate between green and red with for loop
    for (let r = 0; r < classes.length; r++) {
      if (new_class === the_class[r]) {
        $('header').removeClass(the_class[r]);
        $('header').addClass(the_class[(r + 1) % the_class.length]);
        break;
      }
    }
  });
});
