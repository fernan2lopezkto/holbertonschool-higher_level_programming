#!/usr/bin/node
if (process.argv[2]) {
  process.argv[2] = parseInt(process.argv[2], 10);
  const stop = process.argv[2];
  while (process.argv[2] > 0) {
    let i = 0;
    let eX = '';
    while (i < stop) {
      eX = eX + 'X';
      i = i + 1;
    }
    console.log(eX);
    process.argv[2] = process.argv[2] - 1;
  }
}
console.log('Missing size');
