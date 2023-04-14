#!/usr/bin/node
const Squaretul = require('./5-square');

class Square extends Squaretul {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      let i = 0;
      while (i < this.height) {
        let j = 0;
        let ast = '';
        while (j < this.width) {
          ast = ast + 'C';
          j++;
        }
        console.log(ast);
        i++;
      }
    }
  }
}

module.exports = Square;
