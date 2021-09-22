const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().split('\n');

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

N = +input();
const graph = [];
const visited = new Array(N).fill([]).map(() => new Array(N).fill(0));

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

const answer = [];
var cnt = 0;

for (let i = 0; i < N; i++) {
  const a = input()
    .split('')
    .map(n => +n);

  graph.push(a);
}

function dfs(x, y) {
  cnt++;
  visited[x][y] = 1;

  for (let i = 0; i < 4; i++) {
    const nx = x + dx[i];
    const ny = y + dy[i];

    if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;

    if (graph[nx][ny] === 1 && visited[nx][ny] === 0) dfs(nx, ny);
  }
}

for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    if (graph[i][j] === 1 && visited[i][j] === 0) {
      cnt = 0;
      dfs(i, j);
      answer.push(cnt);
    }
  }
}

answer.sort((a, b) => a - b);
console.log(answer.length);
for (let i = 0; i < answer.length; i++) {
  console.log(answer[i]);
}
