function solution(n) {
  let answer = '';

  return answer;
}

console.log(solution(1));

// 강사님 답
function solution(n) {
  let answer = '';
  function DFS(v) {
    if (v > 7) return;
    else {
      answer += v + ' ';
      DFS(v * 2);
      DFS(v * 2 + 1);
    }
  }
  DFS(n);
  return answer;
}

console.log(solution(1));
