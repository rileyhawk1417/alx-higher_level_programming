#!/usr/bin/node

/* Write to file contents from a given file */
const fs = require('fs');
const path = require('path');
const args = process.argv;
const filePath = path.join(__dirname, args[2]);
fs.writeFile(filePath, args[3], 'utf8', function (err, data) {
  if (err) throw err;
});
