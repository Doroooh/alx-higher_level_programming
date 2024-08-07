// This script will add red color to the header on the red-header click

const jQuery = window.$;
jQuery('#color_trigger').on('click', function () {
  jQuery('header').toggleClass('red');
});
