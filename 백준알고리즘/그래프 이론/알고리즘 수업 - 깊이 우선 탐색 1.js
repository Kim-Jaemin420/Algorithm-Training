const fs = require('fs');
const filePath =
  process.platform === 'linux' ? '/dev/stdin' : '백준알고리즘/input.txt';
const stdin = fs.readFileSync(filePath).toString().split('\n');

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, M, R] = input()
  .split(' ')
  .map(s => +s);

const graph = Array.from(Array(N + 1), () => []);
const visitedOrder = Array(N + 1).fill(0);
let order = 0;

for (let index = 0; index < M; index += 1) {
  const [u, v] = input()
    .split(' ')
    .map(s => +s);

  graph[u].push(v);
  graph[v].push(u);
}

for (let index = 1; index <= N; index += 1) {
  graph[index].sort((a, b) => a - b);
}

const dfs = start => {
  order += 1;
  visitedOrder[start] = order;

  for (const node of graph[start]) {
    if (!visitedOrder[node]) {
      dfs(node);
    }
  }

  return visitedOrder;
};

console.log(dfs(R).slice(1).join('\n'));
