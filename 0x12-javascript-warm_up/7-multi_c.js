#!/usr/bin/node
const { argv } = require('process');
const x = Number(argv[2]);
const display = () => {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
};
isNaN(x)
  ? (console.log('Missing number of occurrences'))
  : (display());
