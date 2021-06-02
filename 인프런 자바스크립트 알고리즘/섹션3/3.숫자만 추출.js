function solution(str) {
  let answer = '';

  for (let i = 0; i < str.length; i++) {
    if (!Number.isNaN(+str[i])) answer += str[i];
  }

  return parseInt(answer);
}

const str = 'g0en2T0s8eSoft';
console.log(solution(str));

// 강사님 답
function solution(str) {
  let answer = '';
  for (let x of str) {
    if (!isNaN(x)) answer += x;
  }
  return parseInt(answer);
}

let str = 'g0en2T0s8eSoft';
console.log(solution(str));
