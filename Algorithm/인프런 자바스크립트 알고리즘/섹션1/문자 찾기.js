// 내 답
function solution(s, t) {
  let answer = 0;
  for (const x of s) {
    if (x === t) ++answer;
  }
  return answer;
}

const str = 'COMPUTERPROGRAMMING';
console.log(solution(str, 'R'));

// 강사님 답
// 동일
