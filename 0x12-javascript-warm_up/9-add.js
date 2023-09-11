#!/usr/bin/node
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    const res = parseInt(a) + parseInt(b);
    console.log(`${res}`);
  }
}

add(process.argv[2], process.argv[3]);
