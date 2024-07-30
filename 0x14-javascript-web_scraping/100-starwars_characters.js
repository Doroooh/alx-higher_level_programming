#!/usr/bin/node

const request = require('request');
const starWarsUri = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(starWarsUri, function (_err, _res, body) {
  const characters = JSON.parse(body).characters;

  for (let r = 0; r < characters.length; ++r) {
    request(characters[r], function (_cErr, _cRes, cBody) {
      console.log(JSON.parse(cBody).name);
    });
  }
});
