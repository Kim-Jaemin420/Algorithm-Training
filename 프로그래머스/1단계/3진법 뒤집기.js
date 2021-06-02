function solution(n) {
  let quotient = n;
  let remainder = '';
  let answer = 0;
  while (quotient > 0) {
    remainder = (quotient % 3) + remainder;
    quotient = Math.floor(quotient / 3);
  }
  console.log(remainder);

  for (let i = 0; i < remainder.length; i++) {
    answer += (3 ** i) * remainder[i];
  }
  return answer;
}
console.log(solution(125));


// 다른 사람의 풀이
// n.toString(3)과 parseInt를 사용해서 간단하게 해결했다...