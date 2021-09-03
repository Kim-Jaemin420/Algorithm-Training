const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().split('\n');

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = +input();
const arr = input()
  .split(' ')
  .map(n => +n);

function findIdx(LIS, num) {
  let sp = 0;
  let ep = LIS.length - 1;

  while (sp <= ep) {
    let md = Math.round((sp + ep) / 2);

    if (LIS[md] < num) sp = md + 1;
    else ep = md - 1;
  }

  return sp;
}

function solution() {
  const LIS = [];

  for (let i = 0; i < N; i++) {
    if (LIS.length === 0 || LIS[N - 1] < arr[i]) LIS.push(arr[i]);
    else {
      const idx = findIdx(LIS, arr[i]);
      LIS[idx] = arr[i];
    }
  }

  return LIS.length;
}

console.log(solution());
