const fs = require('fs');
const filePath =
  process.platform === 'linux' ? '/dev/stdin' : '백준알고리즘/input.txt';
const stdin = fs.readFileSync(filePath).toString().split('\n');

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

class Queue {
  constructor() {
    this.queue = [];
    this.head = 0;
    this.tail = 0;
  }

  push(value) {
    this.queue[this.tail++] = value;
    return value;
  }

  pop() {
    if (this.head === this.tail) return -1;
    return this.queue[this.head++];
  }

  size() {
    return this.tail - this.head;
  }

  empty() {
    return this.tail === this.head ? 1 : 0;
  }

  front() {
    return this.queue[this.head] || -1;
  }

  back() {
    return this.queue[this.tail - 1] || -1;
  }
}

const N = +input();
const queue = new Queue();

const solution = command => {
  const result = [];

  switch (command[0]) {
    case 'push':
      queue.push(command[1]);
      break;
    case 'pop':
      result.push(queue.pop());
      // result += queue.pop() + '\n';
      break;
    case 'size':
      result.push(queue.size());
      // result += queue.size() + '\n';
      break;
    case 'empty':
      result.push(queue.empty());
      // result += queue.empty() + '\n';
      break;
    case 'front':
      result.push(queue.front());
      // result += queue.front() + '\n';
      break;
    case 'back':
      result.push(queue.back());
      // result += queue.back() + '\n';
      break;
  }
  console.log(result);
  return result.join('\n');
};

for (let index = 0; index < N; index += 1) {
  const command = input().split(' ');

  console.log(solution(command));
}
