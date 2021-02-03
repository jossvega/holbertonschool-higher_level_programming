#!/usr/bin/node
/* script that prints a square */

let x = 0;
const size = Number(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  while (x < size) {
    x++;
    let row = '';
    for (let c = 0; c < size; c++) row += 'X';
    console.log(row);
  }
}
