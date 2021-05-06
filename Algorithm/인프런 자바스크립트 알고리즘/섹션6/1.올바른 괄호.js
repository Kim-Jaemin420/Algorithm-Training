// 내 답
function solution(s) {
  let answer = 'YES';
  let openN = 0;
  let closeN = 0;

  for (let i = 0; i < s.length; i++) {
    if (s[i] === '(') ++openN;
    if (s[i] === ')') ++closeN;
  }

  if (openN !== closeN) answer = 'NO';

  return answer;
}

let a = '(()(()))(()';
console.log(solution(a));

// 강사님 답
function solution(s) {
  let answer = 'YES';
  let stack = [];
  for (let x of s) {
    if (x === '(') stack.push(x);
    else {
      if (stack.length === 0) return 'NO';
      stack.pop();
    }
  }
  if (stack.length > 0) return 'NO';
  return answer;
}
