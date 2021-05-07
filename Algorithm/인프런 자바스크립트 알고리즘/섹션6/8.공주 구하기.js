// 내 답(못풀었으나 생각은 맞음)
function solution(n, k) {
  let answer;
  const nArr = Array.from({ length: n }, (_, i) => i + 1);

  const stack = [];

  while (nArr.length !== 1) {
    let idx = 0;
    for (idx = 0; idx < k; idx++) {
      if (idx === k - 1) {
        stack.push(nArr[idx]);
        for (let j = 0; j < k; j++) {
          nArr.push(nArr[j]);
        }
        nArr.splice(0, k - 1);
        nArr.splice(idx, 1);
      }
      console.log(stack);
    }
  }

  return answer;
}

console.log(solution(8, 3));

// 강사님 답
function solution(n, k) {
  let answer;
  let queue = Array.from({ length: n }, (v, i) => i + 1);
  while (queue.length) {
    for (let i = 1; i < k; i++) queue.push(queue.shift());
    queue.shift();
    if (queue.length === 1) answer = queue.shift();
  }
  return answer;
}
