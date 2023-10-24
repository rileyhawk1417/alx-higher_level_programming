#!/usr/bin/node
/* Read the file contents from a given file */
const fs = require('fs');
const { argv } = require('process');
const path = require('path');
const filePath = path.join(__dirname, argv[2]);
fs.readFile(filePath, { encoding: 'utf-8' }, function (err, data) {
  if (!err) {
    console.log(data);
  } else {
    console.log(err);
  }
});
