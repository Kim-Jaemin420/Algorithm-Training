const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().split('\n');
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let w;
let h;

while (w !== 0 && h !== 0) {
  [w, h] = input()
    .split(' ')
    .map(n => +n);
  if (w === 0 && h === 0) break;
  const graph = [];

  for (let i = 0; i < h; i++) {
    graph.push(
      input()
        .split(' ')
        .map(n => +n)
    );
  }
  const dx = [-1, 1, -1, 1, -1, 1, 0, 0];
  const dy = [0, 0, 1, -1, -1, 1, 1, -1];
  let cnt = 0;

  function dfs(x, y) {
    graph[x][y] = 0;

    for (let i = 0; i < 8; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];

      if (nx < 0 || nx >= h || ny < 0 || ny >= w) continue;

      if (graph[nx][ny] === 1) dfs(nx, ny);
    }
  }

  for (let i = 0; i < h; i++) {
    for (let j = 0; j < w; j++) {
      if (graph[i][j] === 1) {
        cnt++;
        dfs(i, j);
      }
    }
  }

  console.log(cnt);
}
