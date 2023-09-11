#!/usr/bin/node

const argValue = process.argv.length;
if (argValue === 3) {
  console.log('Argument found');
} else if (argValue > 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
