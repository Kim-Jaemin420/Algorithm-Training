// 내 답
function solution(need, plan) {
  let answer = 'YES';
  const needArr = need.split('');
  const queue = [];

  for (let i = 0; i < plan.length; i++) {
    if (needArr.includes(plan[i])) queue.push(plan[i]);
  }

  for (let i = 0; i < needArr.length; i++) {
    if (needArr[i] !== queue.shift()) answer = 'NO';
  }
  return answer;
}

let a = 'CBA';
let b = 'CDAGEB';
console.log(solution(a, b));

// 강사님 답
function solution(need, plan) {
  let answer = 'YES';
  let queue = need.split('');
  for (let x of plan) {
    if (queue.includes(x)) {
      if (x !== queue.shift()) return 'NO';
    }
  }
  if (queue.length > 0) return 'NO';
  return answer;
}
