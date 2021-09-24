const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().split('\n');
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

N = +input();
const graph = [];
for (let i = 0; i < N; i++) {
  graph.push(
    input()
      .split(' ')
      .map(n => +n)
  );
}
const maxV = Math.max.apply(
  null,
  graph.map(n => Math.max.apply(Math, n))
);

let visited = Array.from(Array(N), () => Array(N).fill(0));
const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

let answer = 0;

function dfs(x, y, base) {
  visited[x][y] = 1;
  const stack = [[x, y]];

  while (stack.length > 0) {
    const cur = stack.pop();

    for (let i = 0; i < 4; i++) {
      const nx = cur[0] + dx[i];
      const ny = cur[1] + dy[i];

      if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;

      if (graph[nx][ny] > base && visited[nx][ny] === 0) {
        visited[nx][ny] = 1;
        stack.push([nx, ny]);
      }
    }
  }
}

for (let k = 0; k <= maxV; k++) {
  let cnt = 0;
  visited = Array.from(Array(N), () => Array(N).fill(0));
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (graph[i][j] > k && visited[i][j] === 0) {
        cnt++;
        dfs(i, j, k);
      }
    }
  }
  answer = Math.max(cnt, answer);
}
console.log(answer);
