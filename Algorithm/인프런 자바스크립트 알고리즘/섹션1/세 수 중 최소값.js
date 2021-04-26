// 내 답
function solution(a, b, c) {
  let answer;
  if (a > b && b > c) answer = c;
  else if (a > b && b < c) answer = b;
  else if (a < b && a > c) answer = c;
  else answer = a;

  return answer;
}

// 강사님 답
function lecture(a, b, c) {
  let answer;
  if (a < b) answer = a;
  else answer = b;

  if (c < answer) answer = c;

  return answer;
}

console.log(solution(6, 5, 11));
console.log(lecture(6, 5, 11));
