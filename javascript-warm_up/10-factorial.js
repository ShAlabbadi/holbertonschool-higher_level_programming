#!/usr/bin/node
function factorial (n) {
  if (isNaN(n)) return 1;
  n = parseInt(n);
  if (n <= 1) return 1;
  return n * factorial(n - 1);
}

const num = process.argv[2];
console.log(factorial(num));
