// 내 답 = 못 품ㅠ
function solution(c, stable) {
  let answer;

  return answer;
}

let arr = [1, 2, 8, 4, 9];
console.log(solution(3, arr));

// 강사님 답
function count(stable, dist) {
  let cnt = 1,
    ep = stable[0];
  for (let i = 1; i < stable.length; i++) {
    if (stable[i] - ep >= dist) {
      cnt++;
      ep = stable[i];
    }
  }
  return cnt;
}
function solution(c, stable) {
  let answer;
  stable.sort((a, b) => a - b);
  let lt = 1;
  let rt = stable[stable.length - 1];
  while (lt <= rt) {
    let mid = parseInt((lt + rt) / 2);
    if (count(stable, mid) >= c) {
      answer = mid;
      lt = mid + 1;
    } else rt = mid - 1;
  }
  return answer;
}

/////////////////////////////////////////////
// 2회차 풀이
////////////////////////////////////////////
function count(stable, dist) {
  let cnt = 1;
  // 바로 전 말이 들어가있는 자리
  let endpoint = stable[0];

  for (let i = 0; i < stable.length; i++) {
    if (stable[i] - endpoint >= dist) {
      ++cnt;
      endpoint = stable[i];
    }
  }

  return cnt;
}

function solution(c, stable) {
  let answer;
  stable.sort((a, b) => a - b);

  // lt = 두 말 사이의 최소 거리(거리니까 무조건 1)
  let lt = 1;
  // rt = 두 말 사이의 최대 거리
  let rt = stable[stable.length - 1];

  while (lt <= rt) {
    let mid = parseInt((lt + rt) / 2);
    if (count(stable, mid) >= c) {
      answer = mid;
      lt = mid + 1;
    } else rt = mid - 1;
  }

  return answer;
}

let arr = [1, 2, 8, 4, 9];
console.log(solution(3, arr));
