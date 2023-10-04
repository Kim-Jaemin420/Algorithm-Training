const fs = require('fs');
const stdin = fs.readFileSync('백준알고리즘/input.txt').toString().split('\n');

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const T = +input();

for (let i = 0; i < T; i++) {
  const [N, M] = input()
    .split(' ')
    .map(n => +n);

  solution(N, M);
}

function solution(N, M) {
  console.log(N, M);
  let count = 0;
  const graph = [[]];
  const visited = [];

  for (let i = 0; i < N; i++) {
    graph.push([]);
  }

  for (let i = 0; i < M; i++) {
    const [u, v] = input()
      .split(' ')
      .map(n => +n);

    graph[u].push(v);
    graph[v].push(u);
  }

  for (let i = 1; i < M; i++) {
    let current = i;
    visited.push(i);

    function dfs(current, visited) {
      for (let i = 0; i < graph[current].length; i++) {
        if (!visited.includes(graph[current][i])) {
          current = graph[current][i];

          dfs(current, visited);
        }
      }
    }

    dfs(current, visited);
  }
}

function dfs(i, visited) {}
