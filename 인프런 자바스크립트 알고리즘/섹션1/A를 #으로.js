// 내 답
function solution(s) {
  const answer = s.replace(/A/g, '#');

  return answer;
}

const str = 'BANANA';
console.log(solution(str));

// 강사님 답
function lecture(s) {
  let answer = '';
  for (let x of s) {
    if (x == 'A') answer += '#';
    else answer += x;
  }
  return answer;
}

console.log(lecture(str));
