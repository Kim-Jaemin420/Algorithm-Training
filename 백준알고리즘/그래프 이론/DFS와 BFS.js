const fs = require('fs');
const filePath =
  process.platform === 'linux' ? '/dev/stdin' : '백준알고리즘/input.txt';
const stdin = fs.readFileSync(filePath).toString().split('\n');

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, M, V] = input()
  .split(' ')
  .map(s => +s);

const dfs = (start, graph, visited) => {
  const result = [];

  result.push(start);
  visited[start] = true;

  for (const node of graph[start]) {
    if (!visited[node]) {
      result.push(...dfs(node, graph, visited));
    }
  }

  return result;
};

const bfs = (start, graph, visited) => {
  const result = [];
  const queue = [start];

  visited[start] = true;
  result.push(start);

  while (queue.length) {
    const node = queue.shift();

    for (const nextNode of graph[node]) {
      if (!visited[nextNode]) {
        visited[nextNode] = true;
        result.push(nextNode);
        queue.push(nextNode);
      }
    }
  }

  return result;
};

const solution = (N, M, V) => {
  const graph = Array.from(Array(N + 1), () => []);

  for (let index = 0; index < M; index += 1) {
    const [vertex1, vertex2] = input()
      .split(' ')
      .map(s => +s);

    graph[vertex1].push(vertex2);
    graph[vertex2].push(vertex1);
  }

  for (let index = 1; index <= N; index += 1) {
    graph[index].sort((a, b) => a - b);
  }

  console.log(dfs(V, graph, Array(N + 1).fill(false)).join(' '));
  console.log(bfs(V, graph, Array(N + 1).fill(false)).join(' '));
};

solution(N, M, V);
