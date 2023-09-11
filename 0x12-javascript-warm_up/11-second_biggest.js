#!/usr/bin/node
import { argv } from 'node:process';

function secondBiggest (array, len) {
  if (len <= 3) {
    return ('0');
  }

  array.sort();
  for (let idx = len - 2; idx >= 0; idx--) {
    if (array[idx] !== array[len - 1]) {
      return (array[idx]);
    }
  }
}

const arrLen = argv.length;
console.log(secondBiggest(argv, arrLen));
