const fs = require('fs');
const filePath =
  process.platform === 'linux' ? '/dev/stdin' : '백준알고리즘/input.txt';
const stdin = fs.readFileSync(filePath).toString().split('\n');

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = +input();
const K = +input();
const apples = Array.from(Array(K), () =>
  input()
    .split(' ')
    .map(s => +s)
);
const L = +input();
const directionChanges = {};

for (let index = 0; index < L; index += 1) {
  const [time, direction] = input().split(' ');
  directionChanges[time] = direction;
}

let snakeHead = [1, 1];
const snakeLocation = [snakeHead];
const dx = [0, 1, 0, -1];
const dy = [1, 0, -1, 0];
let directionIndex = 0;
let time = 0;

const rotate = (directionIndex, direction) => {
  if (direction === 'D') {
    directionIndex = (directionIndex + 1) % 4;
  }

  if (direction === 'L') {
    directionIndex = (directionIndex + 3) % 4;
  }

  return directionIndex;
};

while (true) {
  time += 1;

  const newHead = [
    snakeHead[0] + dx[directionIndex],
    snakeHead[1] + dy[directionIndex],
  ];

  if (newHead[0] < 1 || newHead[0] > N || newHead[1] < 1 || newHead[1] > N) {
    break;
  }

  if (
    snakeLocation.some(
      position => position[0] === newHead[0] && position[1] === newHead[1]
    )
  ) {
    break;
  }

  snakeLocation.push(newHead);

  if (directionChanges[time]) {
    directionIndex = rotate(directionIndex, directionChanges[time]);
  }

  const appleIndex = apples.findIndex(
    apple => apple[0] === newHead[0] && apple[1] === newHead[1]
  );

  if (appleIndex !== -1) {
    apples.splice(appleIndex, 1);
  } else {
    snakeLocation.shift();
  }

  snakeHead = newHead;
}

console.log(time);
