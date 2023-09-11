#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const count = Number(process.argv[2]);
  let j = 0;
  while (j < count) {
    console.log('X'.repeat(count));
    j++;
  }
}
