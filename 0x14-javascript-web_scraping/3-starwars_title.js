#!/usr/bin/node
/* Fetch an API endpoint then return a star wars film title */
const req = require('request');
const args = process.argv;
const apiEndpoint = 'https://swapi-api.alx-tools.com/api/films';

req(`${apiEndpoint}/${args[2]}`, function (err, res, body) {
  if (err) throw err;
  const reply = JSON.parse(body);
  console.log(reply.title);
});
