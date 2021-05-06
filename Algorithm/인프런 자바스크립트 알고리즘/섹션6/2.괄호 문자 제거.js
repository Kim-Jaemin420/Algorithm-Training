// 내 답
function solution(s) {
  let answer = '';
  let openN = 0;
  let closeN = 0;
  let closeIndex = 0;
  let pair = 0;

  for (let i = 0; i < s.length; i++) {
    if (s[i] === '(') ++openN;
    if (s[i] === ')') ++closeN;

    if (openN === closeN && openN && closeN) {
      closeIndex = i;
      closeN = 0;
      openN = 0;
      ++pair;
    }
    if (pair === 1 && openN === 1) {
      answer += s.slice(closeIndex + 1, i);
      pair = 0;
    }
  }

  return answer;
}

let str = '(A(BC)D)EF(G(H)(IJ)K)LM(N)';
console.log(solution(str));

// 강사님 답
function solution(s) {
  let answer;
  let stack = [];
  for (let x of s) {
    if (x === ')') {
      // 팝한 요소가 여는 괄호일때까지 팝한다.
      while (stack.pop() !== '(');
      // 닫는 괄호가 아니라면 모두 스택에 push
    } else stack.push(x);
  }
  answer = stack.join('');
  return answer;
}
