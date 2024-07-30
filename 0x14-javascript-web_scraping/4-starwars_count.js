#!/usr/bin/node

const request = require('request');
const starWarsUri = process.argv[2];
let ttltimes = 0;

request(starWarsUri, function (_err, _res, body) {
  body = JSON.parse(body).results;

  for (let r = 0; r < body.length; ++r) {
    const characters = body[r].characters;

    for (let n = 0; n < characters.length; ++n) {
      const character = characters[n];
      const characterId = character.split('/')[5];

      if (characterId === '18') {
        ttltimes += 1;
      }
    }
  }

  console.log(ttltimes);
});
