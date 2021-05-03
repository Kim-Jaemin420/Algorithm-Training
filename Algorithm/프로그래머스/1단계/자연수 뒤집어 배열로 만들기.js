function solution(n) {
  const answer = ((n + '').split('')).sort((a, b) => b - a);
  return answer.map(str => +str);
}
console.log(solution(12345));
