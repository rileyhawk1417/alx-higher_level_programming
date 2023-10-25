#!/usr/bin/node
/* Fetch an API endpoint then return number of times a character appeared */
const req = require('request');
let args = process.argv;
let count = 0;

req(args[2], function (err, res, body) {
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
