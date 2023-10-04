const fs = require('fs');
const stdin = fs.readFileSync('백준알고리즘/input.txt').toString().split('\n');

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = +input();

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
    if (this.head === this.tail) {
      return -1;
    }

    const value = this.queue[this.head];
    this.head += 1;

    return value;
  }

  size() {
    return this.tail - this.head;
  }

  empty() {
    const queueLength = this.tail - this.head;

    return queueLength ? 0 : 1;
  }

  front() {
    return this.queue[this.head] || -1;
  }

  back() {
    return this.queue[this.tail - 1] || -1;
  }
}

const queue = new Queue();
const answer = [];

for (let index = 0; index < N; index++) {
  const command = input().split(' ');

  switch (command[0]) {
    case 'push':
      queue.push(+command[1]);
      break;
    case 'pop':
      answer.push(queue.pop());
      break;
    case 'size':
      answer.push(queue.size());
      break;
    case 'empty':
      answer.push(queue.empty());
      break;
    case 'front':
      answer.push(queue.front());
      break;
    case 'back':
      answer.push(queue.back());
      break;
  }
}

console.log(answer.join('\n'));
