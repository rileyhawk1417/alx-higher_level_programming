#!/usr/bin/node
/* Fetch an API endpoint then return number of times a character appeared */
const req = require('request');
const apiEndpoint = 'https://swapi-api.alx-tools.com/api/films';
let count = 0;

req(`${apiEndpoint}`, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const reply = JSON.parse(body);
    reply.results.forEach((movie) => {
      movie.characters.forEach((character) => {
        if (character.includes('18')) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
