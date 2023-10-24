#!/usr/bin/node
/* Fetch an API endpoint then return a star wars film characters */
const req = require('request');
const args = process.argv;
const apiEndpoint = 'https://swapi-api.alx-tools.com/api/films';
// A request call within another request call messy but it works
req(`${apiEndpoint}/${args[2]}`, function (err, res, body) {
  if (err) throw err;
  const reply = JSON.parse(body);
  reply.characters.forEach((character) => {
    req(character, function (error, response, resBody) {
      if (error) throw error;
      else {
        const answer = JSON.parse(resBody);
        console.log(answer.name);
      }
    });
  });
});
