#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let idx = 0; idx < parseInt(process.argv[2]); idx++) {
    console.log('C is fun');
  }
}
