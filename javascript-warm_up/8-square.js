#!/usr/bin/node
const frases = 'X';
if (process.argv[2]) {
  process.argv[2] = parseInt(process.argv[2], 10);
  while (process.argv[2] > 0) {
    for (var i = 0; i < process.argv[2]; i ++) {
      console.log(frases);
      process.argv[2] = process.argv[2] - 1;
    }
  }
} else {
  console.log('Missing size');
}
