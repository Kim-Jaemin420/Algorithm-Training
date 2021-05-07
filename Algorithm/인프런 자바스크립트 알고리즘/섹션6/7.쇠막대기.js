function solution(s) {
  let answer = 0;

  return answer;
}

let a = '()(((()())(())()))(())';
console.log(solution(a));

/*
문제 풀이 설명 :
입력에서 여는 괄호라면 차례대로 스택에 push한다. 만약 닫는 괄호를 만나면,
레이저를 의미하는 것인지 막대기의 끝을 의미하는 것인지는,
닫는 괄호 바로 앞을 살펴본다. 만약, 여는 괄호라면 레이저고 닫는 괄호라면
막대 끝을 의미하게 된다.
닫는 괄호 바로 앞을 살펴봤는데 여는 괄호라면 스택에서 여는 괄호를 하나 pop해야 한다.

스택에 남아 있는 여는 괄호들은 막대들을 의미한다.
*/
// 강사님 답
function solution(s) {
  let answer = 0;
  let stack = [];
  for (let i = 0; i < s.length; i++) {
    if (s[i] === '(') stack.push('(');
    else {
      stack.pop();
      if (s[i - 1] === '(') answer += stack.length;
      else answer++;
      //stack.pop(); 이 위치에 하면 레이저까지 카운팅한다.
    }
  }
  return answer;
}
