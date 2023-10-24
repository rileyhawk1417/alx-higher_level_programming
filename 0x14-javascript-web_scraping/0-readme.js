#!/usr/bin/node
/* Read the file contents from a given file */
const fs = require('fs');
const args = process.argv;
fs.readFile(args[2], { encoding: 'utf-8' }, function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
