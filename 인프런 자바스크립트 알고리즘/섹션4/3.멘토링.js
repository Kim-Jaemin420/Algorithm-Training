// 내 답 = 못 품ㅠㅠ
function solution(test) {
  let answer = 0;
  const winner = [];

  for (let i = 0; i < test.length; i++) {
    winner.push(test[i][0]);
  }

  for (let i = 1; i < test[0].length; i++) {
    if (!winner.includes(test[test.length - 1][i])) ++answer;
  }

  return answer;
}

const arr = [
  [3, 4, 1, 2],
  [4, 3, 2, 1],
  [3, 1, 4, 2],
];
console.log(solution(arr));

// 강사님 답
function lecture(test) {
  let answer = 0;
  m = test.length;
  n = test[0].length;
  // 학생 1부터 4까지 짝지을 수 있는 모든 경우의 수(4 * 4)
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= n; j++) {
      let cnt = 0;
      for (let k = 0; k < m; k++) {
        let pi = (pj = 0);
        for (let s = 0; s < n; s++) {
          // pi, pj는 i학생의 등수, j 학생의 등수를 의미
          if (test[k][s] === i) pi = s;
          if (test[k][s] === j) pj = s;
        }
        if (pi < pj) cnt++;
      }
      // i가 j보다 큰 경우가 m(테스트의 길이)이라면
      // i는 j보다 항상 등수가 크므로 답++
      if (cnt === m) answer++;
    }
  }
  return answer;
}

// console.log(lecture(arr));

// 답 보고 다시 풀기
function solution2(test) {
  let answer = 0;

  for (let i = 1; i <= test[0].length; i++) {
    for (let j = 1; j <= test[0].length; j++) {
      let cnt = 0;
      for (let k = 0; k < test.length; k++) {
        let pi = 0;
        let pj = 0;
        for (let s = 0; s < test[0].length; s++) {
          if (test[k][s] === i) pi = s;
          if (test[k][s] === j) pj = s;
        }
        if (pi < pj) ++cnt;
      }
      if (cnt === test.length) answer++;
    }
  }

  return answer;
}

console.log(solution2(arr));
