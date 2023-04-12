#!/usr/bin/node
const frases = 'C is fun';
if (process.argv[2]) {
  process.argv[2] = parseInt(process.argv[2], 10);
    while (process.argv[2] > 0) {
    console.log(frases);
    process.argv[2] = process.argv[2] - 1;
  }
} else {
  console.log('Missing number of occurrences');
}
