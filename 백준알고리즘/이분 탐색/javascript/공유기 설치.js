const fs = require('fs');
const stdin = fs.readFileSync('백준알고리즘/input.txt').toString().split('\n');

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

conditions = input().split(' ');
const N = +conditions[0];
const C = +conditions[1];
