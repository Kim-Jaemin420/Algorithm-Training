function solution(n) {
  const numToString = n + '';
  let answer = 0;
  for (let i = 0; i < numToString.length; i++) {
    answer += +numToString[i];
  }
  return answer;
}

console.log(solution(123));
