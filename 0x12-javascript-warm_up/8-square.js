#!/usr/bin/node

const limit = process.argv[2];
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let idx = 0; idx < parseInt(limit); idx++) {
    console.log('x'.repeat(parseInt(limit)));
  }
}
