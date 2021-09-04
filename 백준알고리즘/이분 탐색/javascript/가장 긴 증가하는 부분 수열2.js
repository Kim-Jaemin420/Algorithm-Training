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

  for (let item of arr) {
    if (LIS.length === 0 || LIS[LIS.length - 1] < item) LIS.push(item);
    else {
      const idx = findIdx(LIS, item);
      LIS[idx] = item;
    }
  }

  return LIS.length;
}

console.log(solution());
