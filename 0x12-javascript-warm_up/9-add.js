#!/usr/bin/node
function add(a, b) {
  const a = parseInt(process.argv[2]);
  const b = parseInt(process.argv[3]);
  return (a + b);
}
console.log(add(a, b));
