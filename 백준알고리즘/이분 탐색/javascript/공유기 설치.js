const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().split('\n');

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const conditions = input().split(' ');
const N = +conditions[0];
const C = +conditions[1];
const houseList = [];

for (let i = 0; i < N; i++) {
  houseList.push(+input());
}

houseList.sort((a, b) => a - b);

function count(n) {
  let sum = 1;
  let num = houseList[0];
  for (let i = 1; i < N; i++) {
    if (houseList[i] - num >= n) {
      ++sum;
      num = houseList[i];
    }
  }

  return sum;
}

function solution() {
  let sp = 1;
  let ep = houseList[N - 1] - houseList[0];

  while (sp <= ep) {
    let md = Math.round((sp + ep) / 2);

    let cnt = count(md);
    if (cnt < C) ep = md - 1;
    else sp = md + 1;
  }

  return ep;
}

console.log(solution());
