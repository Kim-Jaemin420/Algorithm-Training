// 내 답
function solution(n) {
  let answer;

  if (!n % 12) answer = Math.floor(n / 12);
  else answer = Math.floor(n / 12) + 1;

  return answer;
}

console.log(solution(178));

// 강사님 답
function lecture(n) {
  const answer = Math.ceil(n / 12);

  return answer;
}

console.log(lecture(178));
