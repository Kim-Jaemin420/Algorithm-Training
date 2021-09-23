const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().split('\n');
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = +input();
const C = +input();

const graph = Array.from(Array(N + 1), () => Array());
const visited = Array.from(Array(N + 1), () => 0);
const answer = [];

for (let i = 0; i < C; i++) {
  const [u, v] = input()
    .split(' ')
    .map(n => +n);

  graph[u].push(v);
  graph[v].push(u);
}

function dfs(node) {
  visited[node] = 1;
  answer.push(node);

  for (const item of graph[node]) {
    if (visited[item] === 0) dfs(item);
  }
}

dfs(1);
console.log(answer.length - 1);
