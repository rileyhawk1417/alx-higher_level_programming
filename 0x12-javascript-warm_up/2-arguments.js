#!/usr/bin/node

import { argv } from 'node:process';

const argValue = argv.length;
if (argValue === 3) {
  console.log('Argument found');
} else if (argValue > 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
