const fs = require('fs');
const filePath =
  process.platform === 'linux' ? '/dev/stdin' : '백준알고리즘/input.txt';
const stdin = fs.readFileSync(filePath).toString().split('\n');

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, M] = input()
  .split(' ')
  .map(s => +s);
const graph = [
  ...Array(N)
    .fill(0)
    .map(() => input().split('')),
];
const visited = Array.from(Array(N), () => Array.from(Array(M), () => false));

function bfs(start, graph) {
  const dx = [0, 1, 0, -1];
  const dy = [1, 0, -1, 0];

  visited[start[0]][start[1]] = true;

  const queue = [start];

  while (queue.length) {
    const [x, y, distance] = queue.shift();

    if (x === N - 1 && y === M - 1) {
      return distance;
    }

    for (let index = 0; index < 4; index += 1) {
      const nx = x + dx[index];
      const ny = y + dy[index];

      if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;

      if (graph[nx][ny] === '1' && !visited[nx][ny]) {
        visited[nx][ny] = true;
        queue.push([nx, ny, distance + 1]);
      }
    }
  }
}

console.log(bfs([0, 0, 1], graph));
