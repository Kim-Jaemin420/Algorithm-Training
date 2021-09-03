const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().split('\n');

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = +input();
const A = input()
  .split(' ')
  .map(n => +n);

const LIS = [];
const LIS_index = [];

function binary_search(arr, n) {
  let sp = 0;
  let ep = arr.length - 1;

  while (sp <= ep) {
    const md = Math.round((sp + ep) / 2);

    if (arr[md] > n) ep = md - 1;
    else sp = md + 1;
  }

  return sp;
}

function solution() {
  for (const num of A) {
    if (LIS.length === 0 || LIS[N - 1] < num) {
      LIS.push(num);
      LIS_index.push([LIS.length - 1, num]);
    } else {
      const res = binary_search(LIS, num);
      LIS[res] = num;
      LIS_index.push([res, num]);
    }
  }
}

solution();

const answer = [];
let idx = LIS.length - 1;

for (let i = LIS_index.length - 1; i >= 0; i--) {
  if (idx === LIS_index[i][0]) {
    answer.push(LIS_index[i][1]);
    idx -= 1;
  }
}

console.log(answer.length);
console.log(...answer.reverse());
