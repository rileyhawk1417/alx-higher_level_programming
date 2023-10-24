#!/usr/bin/node
/* Fetch an API endpoint then return a star wars film characters order by index */
const req = require('request');
const args = process.argv;
const apiEndpoint = 'https://swapi-api.alx-tools.com/api/films';
let characterList = [];
// A request call within another request call messy but it works
req(`${apiEndpoint}/${args[2]}`, function (err, res, body) {
  if (err) throw err;
  const reply = JSON.parse(body);
  characterList = reply.characters;
  characterIndex(0);
});

function characterIndex (idx) {
  if (idx === characterList.length) {
    return;
  }
  req(characterList[idx], (err, res, body) => {
    if (err) throw err;
    const character = JSON.parse(body);
    console.log(character.name);
    characterIndex(idx + 1);
  });
}
