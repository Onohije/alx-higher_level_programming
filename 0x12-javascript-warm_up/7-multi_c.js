#!/usr/bin/node
const count = parseInt(process.argv[2]);
let j;
if (!count) {
  console.log('Missing number of occurrences');
}
for (j = 0; j < count; j++) {
  console.log('C is fun');
}
