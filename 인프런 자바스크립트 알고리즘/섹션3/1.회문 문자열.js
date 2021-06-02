// 내 답
function solution(s) {
  let answer = 'YES';
  const argToLower = s.toLowerCase();
  let reverseStr = '';

  for (let i = argToLower.length - 1; i >= 0; i--) {
    reverseStr += argToLower[i];
  }

  if (argToLower !== reverseStr) answer = 'NO';

  return answer;
}

const str = 'goooG';
console.log(solution(str));

// 강사님 답
function solution(s) {
  let answer = 'YES';
  s = s.toLowerCase();
  let len = s.length;
  for (let i = 0; i < Math.floor(len / 2); i++) {
    if (s[i] != s[len - i - 1]) return 'NO';
  }
  return answer;
}

let str = 'goooG';
console.log(solution(str));
// 아 절반만 돌면 되는구나..?
