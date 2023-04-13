#!/usr/bin/node
if (process.argv[2]) {
  let stop = process.argv[2] = parseInt(process.argv[2], 10);
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
} else {
  console.log('Missing size');
}
