function solution(n) {
  let answer = 0;

  for (let i = 1; i < n; i++) {
    answer += i * n + n;
  }
}
console.log(solution(3));
