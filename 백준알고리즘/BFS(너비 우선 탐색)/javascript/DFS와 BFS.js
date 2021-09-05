const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().split('\n');

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, M, V] = input()
  .split(' ')
  .map(n => +n);

const graph = new Array(N + 1).fill(0).map(() => new Array(N + 1).fill(0));

for (let i = 0; i < M; i++) {
  const [m1, m2] = input()
    .split(' ')
    .map(n => +n);

  graph[m1][m2] = graph[m2][m1] = 1;
}

const dfs_answer = [];
dfs_visited = new Array(N + 1).fill(0);

function dfs(n) {
  dfs_visited[n] = 1;
  dfs_answer.push(n);

  for (let i = 0; i < N + 1; i++) {
    if (dfs_visited[i] === 0 && graph[n][i] === 1) dfs(i);
  }
}
dfs(V);
console.log(...dfs_answer);

function bfs(v) {
  const visited = [];
  const need_visited = [v];

  while (need_visited.length !== 0) {
    const node = need_visited.shift();

    if (!visited.includes(node)) {
      visited.push(node);

      for (let i = 0; i < N + 1; i++) {
        if (graph[node][i] === 1) need_visited.push(i);
      }
    }
  }
  return visited;
}

console.log(...bfs(V));
