function solution(num) {
  let count = 0;
  let param = num;
  while (param > 1) {
    if (count === 500) return -1;
    if (param % 2) {
      param = 3 * param + 1;
    } else {
      param = param / 2;
    }
    ++count;
  }
  return count;
}

console.log(solution(6)); // 8
console.log(solution(16)); // 8
console.log(solution(626331)); // 8
