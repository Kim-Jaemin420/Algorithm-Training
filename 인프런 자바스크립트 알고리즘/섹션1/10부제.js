// 내 답
function solution(day, arr) {
  let answer = 0;

  for (const days of arr) {
    if (day === days % 10) ++answer;
  }

  return answer;
}

const arr = [25, 23, 11, 47, 53, 17, 33];
console.log(solution(3, arr));

// 강사님 답
// 내 답과 동일
