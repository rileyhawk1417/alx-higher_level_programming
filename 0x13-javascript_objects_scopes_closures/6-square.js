#!/usr/bin/node

const square = require('./5-square.js');

module.exports = class Square extends square {
  charPrint (c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    }
    for (let idx = 0; idx < this.height; idx++) {
      console.log(c.repeat(this.width));
    }
  }
};
