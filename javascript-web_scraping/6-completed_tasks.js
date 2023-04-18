#!/usr/bin/node
// Write a script that computes the number
// of tasks completed by user id.

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const page = JSON.parse(body);
      const outputs = {}
      for (const each of page) {
        if (page.completed === true) {
          outputs[page.userId] = 
        }
      }
    }
  });