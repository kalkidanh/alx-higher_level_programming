#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    let s = '';
    for (let j = 0; j < parseInt(process.argv[2]); j++) {
      s += 'X';
    }
    console.log(s);
  }
}
