#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let idx = 0; idx < this.height; idx++) {
      console.log('x'.repeat(this.width));
    }
  }
};
