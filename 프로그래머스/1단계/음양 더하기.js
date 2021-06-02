// 내 답
function solution(absolutes, signs) {
  let answer = 0;

  for (let i = 0; i < signs.length; i++) {
    if (signs[i]) {
      answer += absolutes[i];
    } else answer += absolutes[i] * -1;
  }
  return answer;
}
