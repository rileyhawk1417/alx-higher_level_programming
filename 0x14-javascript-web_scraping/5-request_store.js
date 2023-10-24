#!/usr/bin/node
/* Get a request then pipe the stream to file */
const req = require('request');
const fs = require('fs');
const args = process.argv;

req.get(args[2]).pipe(fs.createWriteStream(args[3], { encoding: 'utf-8' }));
