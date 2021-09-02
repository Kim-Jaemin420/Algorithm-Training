const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().split('\n');

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = +input();
const K = +input();

function count(num) {
  let sum = 0;

  for (let i = 1; i <= N; i++) {
    sum += Math.min(N, parseInt(num / i));
  }
  return sum;
}

function solution() {
  let sp = 1;
  let ep = N * N;

  while (sp <= ep) {
    let md = Math.round((sp + ep) / 2);

    let cnt = count(md);

    if (cnt < K) sp = md + 1;
    else ep = md - 1;
  }

  return sp;
}

console.log(solution());
