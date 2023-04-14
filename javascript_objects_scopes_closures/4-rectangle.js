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

  rotate () {
    const aux = this.width;
    this.width = this.height;
    this.height = aux;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
