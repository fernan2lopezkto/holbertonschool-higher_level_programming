#!/usr/bin/node
if (process.argv[2]) {
  process.argv[2] = parseInt(process.argv[2], 10);
  while (process.argv[2] > 0) {
    let i = 0
    let eX = ''
    for (i < process.argv[2]) {
      eX = eX + 'X';
      console.log(ex);
      i ++;
    }
  }
} else {
  console.log('Missing size');
}
