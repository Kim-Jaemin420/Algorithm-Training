const fs = require('fs');
const stdin = fs.readFileSync('백준알고리즘/input.txt').toString().split('\n');

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = +input();
const graph = [];

for (let i = 0; i < N; i++) {
  graph.push([]);
}

for (let i = 0; i < N - 1; i++) {
  const [u, v] = input()
    .split(' ')
    .map(n => +n);

  graph[i + 1].push(u, v);
}

const Q = +input();

for (let i = 0; i < Q; i++) {
  const [px, py, x, y] = input().split(' ');
  console.log(px, py, x, y);
  solution(px, py, x, y);
}

function solution(px, py, x, y) {
  const portals = [px, py];

  let hyunJun = [x];
  let jinWoo = [y];

  while (hyunJun !== jinWoo) {
    if (hyunJun.length >= 10 ** 18 && jinWoo.length >= 10 ** 18) {
      return 'J';
    }

    for (let i = 0; i < graph[hyunJun].length; i++) {
      if (graph[hyunjun][i] === hyunJun[0]) continue;

      if (graph[hyunJun][i] !== hyunJun[0]) {
        hyunJun.shift(graph[hyunJun[i]]);
      }
    }
  }
}
