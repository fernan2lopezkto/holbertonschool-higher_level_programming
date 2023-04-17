#!/usr/bin/node
// Write a script that display the status code of a GET request.

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  console.log('code:', response && response.statusCode);
});
