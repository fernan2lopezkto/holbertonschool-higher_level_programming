#!/usr/bin/node
// Write a script.

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error)
  } else {
    if (response.statusCode === 200) {
      const data = JSON.parse(body).results;
      let count = 0;
      for (const each of data) {
        for (const chars of each.characters) {
          if (chars.endsWith('/18/')) {
            ++count;
          }
        }
      }
      console.log(count);
    }
  }
});
