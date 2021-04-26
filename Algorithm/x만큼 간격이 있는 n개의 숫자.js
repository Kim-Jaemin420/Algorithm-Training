function solution(x, n) {
  const answer = [];
  for (let i = 1; i <= n; i++) {
    answer.push(x + x);
  }
  return answer;
}

console.log(solution(2, 5));
console.log(solution(4, 3));
console.log(solution(-4, 2));

// 다른사람의 풀이
function solution(x, n) {
  return Array(n).fill(x).map((v, i) => (i + 1) * v)
}