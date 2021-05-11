// 내 답
function solution(times) {
  let answer = Number.MIN_SAFE_INTEGER;

  for (let i = 0; i < times.length - 1; i++) {
    let cnt = 1;
    for (let j = i + 1; j < times.length; j++) {
      if (times[i][0] <= times[j][0] && times[j][0] > times[i][1]) {
        ++cnt;
      }
    }
    if (answer < cnt) answer = cnt;
  }

  return answer;
}

let arr = [
  [14, 18],
  [12, 15],
  [15, 20],
  [20, 30],
  [5, 14],
];
console.log(solution(arr));

// 강사님 답
function solution(times) {
  let answer = Number.MIN_SAFE_INTEGER;
  let T_line = [];
  for (let x of times) {
    T_line.push([x[0], 's']);
    T_line.push([x[1], 'e']);
  }
  T_line.sort((a, b) => {
    if (a[0] === b[0]) return a[1].charCodeAt() - b[1].charCodeAt();
    else return a[0] - b[0];
  });
  let cnt = 0;
  for (let x of T_line) {
    if (x[1] === 's') cnt++;
    else cnt--;
    answer = Math.max(answer, cnt);
  }
  return answer;
}
