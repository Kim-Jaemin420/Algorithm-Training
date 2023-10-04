const fs = require('fs');
const filePath =
  process.platform === 'linux' ? '/dev/stdin' : '백준알고리즘/input.txt';
const stdin = fs.readFileSync(filePath).toString().split('\n');

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, K] = input()
  .split(' ')
  .map(s => +s);

const solution = (N, K) => {
  const queue = Array.from(Array(N), (_, index) => index + 1);
  const josephus = [];
  let countRemoveNumber = 0;

  while (queue.length) {
    const headItem = queue.shift();
    countRemoveNumber += 1;

    if (countRemoveNumber % K === 0) {
      josephus.push(headItem);
    } else {
      queue.push(headItem);
    }
  }

  return `<${josephus.join(', ')}>`;
};

console.log(solution(N, K));
