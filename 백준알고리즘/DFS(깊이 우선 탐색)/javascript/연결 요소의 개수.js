const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().split('\n');
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, M] = input()
  .split(' ')
  .map(n => +n);
const graph = Array.from(Array(N + 1), () => Array());
const visited = Array.from(Array(N + 1), () => 0);

for (let i = 0; i < M; i++) {
  const [u, v] = input()
    .split(' ')
    .map(n => +n);

  graph[u].push(v);
  graph[v].push(u);
}

function dfs(node) {
  visited[node] = 1;

  for (const item of graph[node]) {
    if (visited[item] === 0) dfs(item);
  }
}

let cnt = 0;
for (let i = 1; i <= N; i++) {
  if (visited[i] === 0) {
    cnt++;
    dfs(i);
  }
}

console.log(cnt);
