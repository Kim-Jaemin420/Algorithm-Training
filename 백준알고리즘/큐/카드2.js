const fs = require('fs');
const filePath =
  process.platform === 'linux' ? '/dev/stdin' : '백준알고리즘/input.txt';
const stdin = fs.readFileSync(filePath).toString().split('\n');

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = +input();

class Queue {
  constructor() {
    this.queue = [];
    this.front = 0;
    this.rear = 0;
  }

  push(value) {
    this.queue[this.rear++] = value;
    return value;
  }

  pop() {
    if (this.front === this.rear) return null;

    const value = this.queue[this.front];
    delete this.queue[this.front];

    this.front += 1;

    return value;
  }

  peek() {
    return this.queue[this.front] || null;
  }

  size() {
    return this.rear - this.front;
  }
}

const solution = N => {
  const queue = new Queue();

  for (let index = 0; index < N; index += 1) {
    queue.push(index + 1);
  }

  while (queue.size() > 1) {
    queue.pop();

    queue.push(queue.pop());
  }

  return queue.peek();
};

console.log(solution(N));
