#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const patch = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(patch, JSON.parse(body), 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
