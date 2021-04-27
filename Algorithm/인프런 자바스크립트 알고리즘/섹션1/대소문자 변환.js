// 내 답
function solution(s) {
  let answer = '';

  for (let i = 0; i < s.length; i++) {
    if (s[i] === s[i].toUpperCase()) answer += s[i].toLowerCase();
    else answer += s[i].toUpperCase();
  }

  return answer;
}

console.log(solution('StuDY'));

// 강사님 답 === 내 답
