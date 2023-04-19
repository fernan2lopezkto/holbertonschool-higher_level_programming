#!/usr/bin/node
// Write a script that computes the number
// of tasks completed by user id.

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) return;
  const page = JSON.parse(body);
  const outlist = {};
  page.forEach(element => {
    if (page.completed) {
      if (outlist[element.userId]) outlist[element.userId] += 1;
      else outlist[element.userId] = 1;
    }
  });
  console.log(outlist);
});
