#!/usr/bin/node
import { argv } from 'node:process';

argv.forEach((val, idx) => {
  if (idx >= 2) {
    console.log(`${val}`);
  }
  if (idx === 1) {
    console.log('No argument');
  }
});
