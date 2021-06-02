// 내 답
function solution(s) {
  let answer = '';

  for (const x of s) {
    if (x === x.toLowerCase()) answer += x.toUpperCase();
    else answer += x;
  }
  return answer;
}

const str = 'ItisTimeToStudy';
console.log(solution(str));

// 강사님 답
