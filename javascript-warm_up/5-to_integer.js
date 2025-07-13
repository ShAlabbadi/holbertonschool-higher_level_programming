#!/usr/bin/node
const num = process.argv[2];

if (isNaN(num) || num === '' || num === null) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(num, 10)}`);
}
