#!/usr/bin/node
// Write a script.

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    for ()
    (JSON.parse(body).);
  }
});
