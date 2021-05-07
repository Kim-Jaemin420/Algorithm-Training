// 내 답
function solution(s) {
  let answer;
  const stack = [];

  for (let i = 0; i < s.length; i++) {
    let res = 0;
    if (!isNaN(+s[i])) stack.push(+s[i]);
    else {
      if (s[i] === '+') {
        res = stack[stack.length - 1] + stack[stack.length - 2];
        stack.pop();
        stack.pop();
        stack.push(res);
      } else if (s[i] === '-') {
        res = stack[stack.length - 2] - stack[stack.length - 1];
        stack.pop();
        stack.pop();
        stack.push(res);
      } else if (s[i] === '*') {
        res = stack[stack.length - 2] * stack[stack.length - 1];
        stack.pop();
        stack.pop();
        stack.push(res);
      } else {
        res = stack[stack.length - 2] / stack[stack.length - 1];
        stack.pop();
        stack.pop();
        stack.push(res);
      }
    }
  }

  answer = stack[0];
  return answer;
}

let str = '352+*9-';
console.log(solution(str));

// 강사님 답
function solution(s) {
  let answer;
  let stack = [];
  for (let x of s) {
    if (!isNaN(x)) stack.push(Number(x));
    else {
      // 팝한 걸 변수에 담을 생각을 왜 못했을까?
      let rt = stack.pop();
      let lt = stack.pop();
      if (x === '+') stack.push(lt + rt);
      else if (x === '-') stack.push(lt - rt);
      else if (x === '*') stack.push(lt * rt);
      else if (x === '/') stack.push(lt / rt);
    }
  }
  answer = stack[0];
  return answer;
}
