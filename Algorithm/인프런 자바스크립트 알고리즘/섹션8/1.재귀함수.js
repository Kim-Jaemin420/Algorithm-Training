// 내 답
function solution(n) {
  // stack = [D(3), D(2), D(1)]
  function DFS(L) {
    if (L === 0) return;
    else {
      DFS(L - 1);
      console.log(L);
    }
  }

  DFS(n);
}

solution(3);

/////////////////////////////////////////////
// 2회차 풀이
////////////////////////////////////////////
function solution(n) {
  function DFS(L) {
    if (L === 0) return;
    else {
      DFS(L - 1);
      console.log(L);
    }
  }

  DFS(n);
}
