#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    while (i < this.height) {
      let j = 0;
      let ast = '';
      while (j < this.width) {
        ast = ast + 'X';
        j++;
      }
      console.log(ast);
      i++;
    }
  }
}
module.exports = Rectangle;
