const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().split('\n');
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = +input();
const graph = [];
for (let i = 0; i < N; i++) {
  graph.push(input().split(''));
}
let visited = Array.from(Array(N), () => Array(N).fill(0));

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

function dfs(x, y) {
  visited[x][y] = 1;

  for (let i = 0; i < 4; i++) {
    const nx = x + dx[i];
    const ny = y + dy[i];

    if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;

    if (graph[nx][ny] === graph[x][y] && visited[nx][ny] === 0) {
      dfs(nx, ny);
    }
  }
}

let cnt = 0;
for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    if (visited[i][j] === 0) {
      cnt++;
      dfs(i, j);
    }
  }
}

for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    if (graph[i][j] === 'G') graph[i][j] = 'R';
  }
}

visited = Array.from(Array(N), () => Array(N).fill(0));
let dcnt = 0;
for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    if (visited[i][j] === 0) {
      dcnt++;
      dfs(i, j);
    }
  }
}

console.log(cnt, dcnt);
