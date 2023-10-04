const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().split('\n');
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = +input();
const graph = Array.from(Array(N + 1), () => Array());
const answer = Array.from(Array(N + 1).fill(0));

for (let i = 0; i < N - 1; i++) {
  const [u, v] = input()
    .split(' ')
    .map(n => +n);

  graph[u].push(v);
  graph[v].push(u);
}

function dfs(x) {
  const stack = [x];
  while (stack.length > 0) {
    const num = stack.pop();

    for (const item of graph[num]) {
      if (answer[item] === 0) {
        answer[item] = num;
        stack.push(item);
      }
    }
  }
}

dfs(1);

for (let i = 2; i < N + 1; i++) {
  console.log(answer[i]);
}
