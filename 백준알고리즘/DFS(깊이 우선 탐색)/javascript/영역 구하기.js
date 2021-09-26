const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().split('\n');
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [M, N, K] = input()
  .split(' ')
  .map(n => +n);
const graph = Array.from(Array(M), () => Array(N).fill(0));
const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];
const answer = [];

for (let i = 0; i < K; i++) {
  const [m1, m2, k1, k2] = input()
    .split(' ')
    .map(n => +n);

  for (let i = m2; i < k2; i++) {
    for (let j = m1; j < k1; j++) {
      graph[i][j] = -1;
    }
  }
}

function dfs(x, y) {
  const stack = [[x, y]];
  while (stack.length > 0) {
    const cur = stack.pop();

    graph[cur[0]][cur[1]] = 1;
    cnt++;

    for (let i = 0; i < 4; i++) {
      const nx = cur[0] + dx[i];
      const ny = cur[1] + dy[i];

      if (nx < 0 || nx >= M || ny < 0 || ny >= N) continue;

      if (graph[nx][ny] === 0) {
        graph[nx][ny] = 1;
        stack.push([nx, ny]);
      }
    }
  }
}

let cnt = 0;
for (let i = 0; i < M; i++) {
  for (let j = 0; j < N; j++) {
    if (graph[i][j] === 0) {
      cnt = 0;
      dfs(i, j);
      answer.push(cnt);
    }
  }
}
answer.sort((a, b) => a - b);
console.log(answer.length);
console.log(...answer);
