#!/usr/bin/node

let j;

for (j = 0; process.argv[j]; j++) {
  continue;
}

console.log(j === 2 ? 'No argument' : process.argv[2]);
