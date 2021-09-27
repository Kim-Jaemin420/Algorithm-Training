const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().split('\n');
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const T = +input();
const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

for (let i = 0; i < T; i++) {
  const [M, N, K] = input()
    .split(' ')
    .map(n => +n);
  const graph = Array.from(Array(N), () => Array(M).fill(0));

  for (let i = 0; i < K; i++) {
    const [u, v] = input()
      .split(' ')
      .map(n => +n);
    graph[v][u] = 1;
  }

  function dfs(x, y) {
    graph[x][y] = 0;

    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];

      if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;

      if (graph[nx][ny] === 1) dfs(nx, ny);
    }
  }

  let cnt = 0;
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (graph[i][j] === 1) {
        cnt++;
        dfs(i, j);
      }
    }
  }

  console.log(cnt);
}
