//  Fetch and list movie titles in URL https://swapi-api.alx-tools.com/api/films/?format=json

$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, status) {
  let j = 0;
  // using the while loop
  while (j < data.count) {
    $('UL#list_movies').append('<li>' + data.results[j].title + '</li>');
    j++;
  }
});
