#!/usr/bin/node

/* Send a request then return the status code */
const req = require('request');
const args = process.argv;
req(args[2], function (error, res, body) {
  if (error) throw error;
  console.log('code: ' + res.statusCode);
});
